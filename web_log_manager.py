import json
import sys
import markdown

class WebLogManager:
	"""
	Helps add and manage blog articles
	"""

	def __init__(self, database="entries.json"):
		"""
		Load up the entries database.
		"""
		with open(database) as db:
			self.entries = json.load(db)

	def find_all(name, path):
		"""
		Finds all files matching name in path.
		Lifted from https://stackoverflow.com/a/1724723
		"""
	    result = []
	    for root, dirs, files in os.walk(path):
	        if name in files:
	            result.append(os.path.join(root, name))
	    return result

	def add(self, articleName):
		"""
		Add an article to the list of entries. Recursively searches down to find
		article and adds it.
		"""
		articles = self.find_all()
		if len(articles) > 1:
			print('error: Found more than one matching article: ')


	def make_rss(self):
		"""
		Generates the rss.xml file at the root of the blog.
		"""
		pass

	def make_sitemap(self):
		"""
		Generates the sitemap.xml file at the root of the site.
		"""
		pass

	def make_html(self):
		"""
		Generates the HTML files from the markdown sources.
		"""
		pass

	def compile(self):
		"""
		Generates all blog support files.
		"""
		self.make_rss()
		self.make_sitemap()
		self.make_html()

	def args(self, a):
		"""
		Take in and process command line arguments.
		:param a: sys.argv
		"""
		if len(a) == 0:
			print('add [articleName]	Adds an article to the list of entries.')
			print('compile 				Regenerates all support files.')
		elif a[1] == 'add':
			self.add(a[2])
		elif a[1] == 'compile':
			self.compile()

if __name__ == "__main__":
	b = WebLogManager()
	b.args(sys.argv)
