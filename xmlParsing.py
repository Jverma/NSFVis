# -*- coding: utf-8 -*-
# Parsing a corpus of XML files and saving the information as a JSON document. 


import sys
import json
import os
import xml.etree.ElementTree as ET




class Parser:
	"""
	Parsing an XML file. 
	"""
	def __init__(self, input_file):
		"""
		Arguments :
			An XML file. 
		"""
		self.tree = ET.parse(input_file)

	def jsonInfo(self):
		"""
		Converting the contents of the XML file into a JSON document. 

		Returns:
			A JSON document of the form {attribute:[values], ..}
		"""
		tree = self.tree
		root = tree.getroot()
		contents = {}
		for child in root:
			for t in child.iter():
				if (t.tag in contents):
					key1 = str(t.tag) + "1"
					contents[key1] = [t.text]
					for x in t:
						alpha = {x.tag : x.text}
						contents[key1].append(alpha)

				else:
					contents[t.tag] = [t.text]
					for x in t:
						alpha = {x.tag : x.text}
						contents[t.tag].append(alpha)

		return json.dumps(contents)			




directory = sys.argv[1]

corpus = os.listdir(directory)



for f in corpus:
	f = os.path.join(directory,f)
	with open(f) as document:
		info = document
		out = Parser(info)
		jsonData = out.jsonInfo()
		print jsonData 










