#!/usr/bin/env python3 
import xml.sax 
class bookch(xml.sax.ContentHandler): 
 def __init__(self): 
  self.curtag='' 
  self.title='' 
  self.author='' 
  self.year='' 
  self.price='' 
 def startElement(self,tag,attrs): 
  self.curtag=tag 
 def characters(self,content): 
  if self.curtag=='title': 
   self.title=content 
  if self.curtag=='author': 
   self.author=content 
  if self.curtag=='year': 
   self.year=content 
  if self.curtag=='price': 
   self.price=content 
 def endElement(self,tag): 
  if tag=='title': 
   print('title:',self.title) 
  if tag=='author': 
   print('author:',self.author) 
  if tag=='year': 
   print('year:',self.year) 
  if tag=='price': 
   print('price:',self.price) 
pobj=xml.sax.make_parser() 
pobj.setContentHandler(bookch()) 
pobj.parse('book.xml') 
