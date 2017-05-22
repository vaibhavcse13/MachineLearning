import urllib2
import re

htmlfile = urllib2.openurl("http://www.indiawaterportal.org/")

htmltext = htmlfile.read()
