#!/usr/bin/python
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
print current_dir

import cherrypy
from cherrypy import tools


class Root(object):
	def __init__( self ):
		self.watchfolder = []
		self.pageSkeleton = open( os.path.join( current_dir, "html", "skeleton.html" ), "r" ) #.read()
		self.pageHeader   = open( os.path.join( current_dir, "html", "header.html" ),   "r" ) #.read()
		self.pageMenu     = open( os.path.join( current_dir, "html", "menu.html" ),     "r" ) #.read()

	@cherrypy.expose
	def index( self ):
		htmlFile  = self.pageSkeleton

		#htmlFile.replace( "%HEADER%", self.pageHeader )
		#htmlFile.replace( "%MENU%", self.pageMenu )

		return htmlFile;

#cherrypy.quickstart( Root(), '/', 'prod.conf' )
