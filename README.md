sublime-poster
==============

A Sublime 2 Plugin to do HTTP requests.  Modeled after Poster Add-on for Firefox.  Syntax is JSON.

Sample Syntax:
{
	"localhost_post" : {
		"url":"http://localhost/dump.php?foo=bar",
		"header":{
			"X-Auth-Username": "username",
			"X-Auth-Password": "password"
		},
		"data":{
			"field_1": "value_1",
			"field_2": "val2"
		},
		"method":"post"
	}
}
