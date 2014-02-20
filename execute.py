# -*- coding: iso-8859-1 -*-

#import database query script

import models

Gene = models.Gene(%s)


#import cgi programs

import cgi
import cgitb

cgitb.enable()


form = cgi.FieldStorage()
#write out the data that is to be output back to the webpage.

print "content-type: text/html" #html stuff is following
print
print "<html><head> <title> Your results </title></head>"
print "<body><h1> Results</h1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
    print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

print "<table>"

print "</body></html>"
