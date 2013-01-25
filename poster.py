import sublime, sublime_plugin
import os
import json
import curl
from urlparse import urlparse
import httplib
import urllib
import urllib2

class PosterCommand(sublime_plugin.WindowCommand):

	def read_file_contents(self):
		path = self.window.active_view().file_name()
		with open(path, 'r') as f:
			self.contents = f.read()
		self.json = json.loads(self.contents)

	def prompt_sections(self):
		out = ""
		self.items = []
		for key, value in self.json.iteritems():
			out += "%s\n" % key
			self.items.append([key, value["url"]])
		self.window.show_quick_panel(self.items, self.panel_done, sublime.MONOSPACE_FONT)

	def panel_done(self, picked):
		key = self.items[picked][0]
		data = self.json[key]
		value = None
		# try:
		method = data.get("method") if data.get("method") is not None else "get"
		body = data.get("data")
		body = urllib.urlencode(body) if body else None
		url = data.get("url")
		url_parsed = urlparse(url)
		header = data.get("header")
		header = dict() if not header else header
		path = url_parsed.path
		query = url_parsed.query
		if method.lower() == "get" and body is not None:
			query = body if not query else "%s&%s" % (query, body)
			body = None
		if query:
			path += "?%s" % query
		if method.lower() == "post":
			header = dict(header)
			header["Content-type"] = "application/x-www-form-urlencoded"
		
		full_url = "%s://%s%s" % (url_parsed.scheme, url_parsed.netloc, query)
		# req = urllib2.Request(full_url, data, header)
		# response = urllib2.urlopen(req)
		# contents = response.read()

		if url_parsed.scheme == "http":
			request = httplib.HTTPConnection(url_parsed.netloc)
			request.request(method.upper(), path, body, header)
			response = request.getresponse()
			contents = response.read()
		elif hasattr(httplib, "HTTPSConnection"):
			request = httplib.HTTPSConnection(url_parsed.netloc)
			request.request(method.upper(), path, body, header)
			response = request.getresponse()
			contents = response.read()
			# sublime.status_message("HTTPS currently not supported")
			# return
		else:
			full_url = "%s://%s%s%s" % (url_parsed.scheme, url_parsed.netloc, path, query)
			contents = curl.post(full_url, body, header)

		v = self.window.new_file()
		v.set_name("Poster Results")
		v.set_scratch(True)
		edit = v.begin_edit()
		v.insert(edit, 0, contents)
		v.end_edit(edit)

		# except:
		# 	sublime.status_message("HTTP Request failed!")

	def run(self):
		try:
			self.read_file_contents()
			self.prompt_sections()
		except:
			sublime.status_message("Failed to find anything to post!")