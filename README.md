sublime-poster
==============

A Sublime 2 Plugin to perform HTTP requests.  Modeled after the Poster Add-on for Firefox.  Syntax is JSON.  When selecting the "Poster: Current File" from the Command Pallete, if the files JSON is readable a menu will appear asking which poster test to execute.  Upon execution, a new window will open with the results of the request.

This plugin is nice because reproducing a request at a later date is easy as the requests can be saved in JSON.

Sample Syntax:
```json
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
```
