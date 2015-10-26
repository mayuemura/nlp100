#test_jinja.py
# -*- coding:utf-8 -*-
import cgi
from jinja2 import Environment, FileSystemLoader

#config
_ENCODE = "utf-8"
_HTML_TEMPLATE_FILE = "template.html"

class HTTPtemplate(object):

	def __init__(self, template_file):
		self.encoding 	= "utf-8"
		self.data 		= {}
		self.template_dir = "./"
		self.template_file = template_file

	def set_encode(self, encode):
		self.encode = encode

	def set_template_dir(self, template_dir):
		self.template_dir = template_dir

	def set_data(self, key, value):
		try:
			value = unicode(value, self.encode)
		except:
			value = value

		self.data[key] = value

	def http_output(self):
		env = Environment(loader=FileSystemLoader(self.template_dir, encoding=self.encode))
		tmpl = env.get_template(self.template_file)

		html = tmpl.render(data=self.data).encode(self.encode)

		with open("test_jinja.html", "w") as fo:
			fo.write(html)

def main():
	http_requests = cgi.FieldStorage()

	http = HTTPtemplate(_HTML_TEMPLATE_FILE)
	http.set_encode(_ENCODE)
	http.set_data("charset", _ENCODE)
	http.set_data("request_get", http_requests.getvalue("get", None))
	http.set_data("request_post", http_requests.getvalue("post", None))
	http.http_output()

if __name__ == "__main__":
	main()
