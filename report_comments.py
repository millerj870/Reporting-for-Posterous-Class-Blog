# This work is copyright 2011, Jason Miller. All rights reserved except as permitted under the Creative Commons Attribution-NonCommercial
# 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/ or send a letter to Creative
# Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA. #

"""
This report returns the following information about posts made to spectrawiki.posterous.com:
	name of comment author
	datetime of comment
"""

import datetime
import pyposterous
from pyposterous import Cursor

api = pyposterous.API(username='[username]', password='[password]')

d=datetime.datetime.today().strftime("%y%B%d-%H%M")
filename = 'report-comments-' + str(d) +'.txt' 
log=open(filename,'w')

for post in Cursor(method=api.read_posts, start_page=1, parameters={'hostname':'[name]'}):
	try:
		for comment in post.comments:
			print >> log, "%s, %s, %s, %s" % (comment.author, comment.date, post.title, post.url)
	except AttributeError:
		pass # No comments
	except UnicodeEncodeError:
		pass