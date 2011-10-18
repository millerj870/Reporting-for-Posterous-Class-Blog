"""
this script pull a list of authors from a 'comments' report and the creates an 'authorlist' of unique authors
"""
import sys
import string

###  DEFINTIONS  --------------------------------------------------------

def authors(list):
	"""
	This function takes a list of posterous post or comment information and creates a list of authors for each of the entries in the original list..
	It returns a list of author entries, one for each row in the original list.
	"""
	authors=[]
	for line in list:
		authors.append(line[0])
	return authors

def authorlist(list):
	"""
	This function takes a list of posterous post or comment information and creates a list of unique authors.
	It returns a list of author names.
	"""
	authors=[]
	for line in list:
		authors.append(line[0])
	authorlist=[]
	[authorlist.append(x) for x in authors if x not in authorlist]
	return authorlist

def relist(list):
	"""
	Take report fron pyposterous and convert it into a list of four items:  author, datetime, title, and url.
	"""
	newlist=[]
	for line in list:
		itemlist=[]
		com1=string.find(line,',')
		itemlist.append(line[0:com1])
		com2=string.find(line,',',com1+1,len(line))
		itemlist.append(line[com1+2:com2])
		com3=string.find(line,',',len(line)-23,len(line))
		itemlist.append(line[com2+2:com3])
		itemlist.append(line[com3+2:len(line)-1])
		newlist.append(itemlist)
	return newlist

def findcontrib(list, author):
	"""
	This function finds the indexes in a list of authors at which a search value occurs in its first entry.
	The function returns a list of indices
	"""
	i = -1
	stuff=[]
	try:
		while 1:
			i = list.index(author, i+1)  # <--- need to check this
			stuff.append(i)	
	except ValueError:
			pass
	return stuff

def getpostinfo(list, locs):
	"""
	function gives intry in a contribution list at lcoations locs
	"""
	info = []
	for v in locs:
		info.append(list[int(v)])
	return info

def info(list, auth):
	"""
	function gives information contributed to list by author auth
	"""
	loc = findcontrib(authors(list), auth)
	return getpostinfo(list, loc)

def postsin2011(list):
	"""
	Finds the subset of a post or comment list that were posted in 2011
	"""
	newlist=[]
	i=-1
	indexes=[]
	for x in list:
		newlist.append(int(x[1][0:4]))
	try:
		while 1:
			i=newlist.index(2011,i+1)
			indexes.append(i)
	except ValueError:
		pass
	info=[]
	for v in indexes:
		info.append(list[int(v)])
	return info

def postsin2010(list):
	"""
	Finds the subset of a post or comment list that were posted in 2011
	"""
	newlist=[]
	i=-1
	indexes=[]
	for x in list:
		newlist.append(int(x[1][0:4]))
	try:
		while 1:
			i=newlist.index(2010,i+1)
			indexes.append(i)
	except ValueError:
		pass
	info=[]
	for v in indexes:
		info.append(list[int(v)])
	return info


dict = {'postID':'Lastname, Firstname'
}


#  ----------------------------------------------------------------------------------------------------
# THE SCRIPT   ----------------------------------------------------------------------------------------
#  ----------------------------------------------------------------------------------------------------
                                                           
#let user choose the posts report to be used
#  postfile, postlist
#let user choose the comments report to be used
#  commentfile, commentlist

try:
	postfilename = sys.argv[1]; commentfilename = sys.argv[2]
except:
	print "Usage:", sys.argv[0], "postfilename commentfilename"; sys.exit(1)

postfile = open(postfilename, 'r')
postlist = postfile.readlines() # make a list of lines
postlist = postsin2011(relist(postlist))
commentfile = open(commentfilename, 'r')
commentlist = commentfile.readlines() # make a list of lines
commentlist = postsin2011(relist(commentlist))

# CREATE a list of authors to be used for the reports ----------------------------
# (if a student only comments, they do not deserve credit for the assignment)

allauthors = authorlist(postlist) # list of unique authors; for 'while' list later
orderedauthors=sorted(allauthors)
print orderedauthors
postauthors = authors(postlist) # list of authorships, order reflecting porder of postlist
commentauthors = authors(commentlist) # list of authorships, order reflecting order of commentlist

# gather input from user for the report ----------------------------
#
# week of the semester
# number of posts per week
# 

weekno = int( input('Which week of the semester are we in? (Give a number.)   '))
postrate = int( input('According to the syllabus, how many posts per week should a studen have?   '))

postcount = len(postlist)
commentcount = len(commentlist)
authorcount = len(allauthors)
postave = postcount/authorcount
commentave = commentcount/authorcount

# CREATE data for each author  ----------------------------

## EXAMPLE:  for allauthors[0]

postinfo = info(postlist, allauthors[0])
commentinfo = info(commentlist, allauthors[0])

print allauthors[0]
print 'Number of posts:  ', len(postinfo)
print 'Number of ocmments:  ', len(commentinfo)

print 'Posts:'
for x in postinfo:
	print x[1],'&',x[2],'&',x[3],'\\\\'

print 'Comments:'
for x in commentinfo:
	print x[1],'&',x[2],'&',x[3],'\\\\'


latexfile = open('tmp.tex','w')

latexfile.write("""
	\documentclass[10pt]{article}
	\pagestyle{empty}
	\usepackage{float}
	\usepackage{hyperref}
	\\thispagestyle{empty}
	\setlength{\\topmargin}{-.6in}
	\setlength{\\textheight}{9.5in}
	\setlength{\\textwidth}{7in}
	\setlength{\oddsidemargin}{-.5in}	
	\setlength{\evensidemargin}{-.5in}	
	\setlength{\parskip}{.125in}
	\setlength{\parindent}{0in}
	\\renewcommand{\\baselinestretch}{1}
	\\newcommand{\sectionline}{
	  \\nointerlineskip \\vspace{\\baselineskip}
	  \hspace{\\fill}\\rule{0.75\linewidth}{1pt}\hspace{\\fill}
	  \par\\nointerlineskip \\vspace{\\baselineskip}
	}
	\\begin{document}

	\\begin{center}
	\Large
	Blog Participation Report \\\\
	Integrative Freshman Seminar \\\\
	\\normalsize
	\medskip
	
	\\today
	\end{center}


    Recall the assignment parameters for our section of IDSM 140 are as follows:
	\\begin{quote}
	In order to help students understand the interrelatedness of science and mathematics and their roles in society, 
	each week students will be required to share an interesting science/math news item they find in the popular press. 
	Students will post links to their articles to the class Wiki three days before class. Each week, each student will then 
	choose the three articles (from those submitted by others in the class) that they find most interesting and write a 
	paragraph summary for each article which will be used as a springboard for class discussion. Students must contribute at 
	least 10 unique articles during the semester.
	\end{quote}
	This means that each student should have 10 posts and 30 comments by the end of the semester.

	It is the week number %i, 
	%% variable for number of weeks that have passed
	so according to the syllabus each student should have about %i 
	%% number of posts that the student has submitted
	contributions to the course blog.  So far, there have been a total of %i 
	%% total number of post submitted to the blog
	posts to the blog that have a total of %i
	%% total number of comments submitted to the blog
	comments.  On average, each student has posted %s 
	%% average number of stories submitted, per student
	stories and made %s
	%% average number of comments submitted, per student
	comments to the blog.

""" % (weekno, postrate*weekno, postcount, commentcount, postave, commentave))

latexfile.close()

latexfile = open('tmp.tex','a')

for x in allauthors:
	postinfo = info(postlist, x)
	commentinfo = info(commentlist, x)
	latexfile.write("""
		\sectionline
		\\textbf{%s} (%i posts, %i comments) \\newline

		\\begin{table}[H]
		\\begin{tabular}{lll}
		Post Title & Post Date & Post URL \\\\ \hline 

		""" % (x,len(postinfo), len(commentinfo)))

# the above live should be replaced with 	
# """ % (dict[x],len(postinfo), len(commentinfo)))
# if the user wants to replace an author's postID with 
# their name using a dictionary that's started on
# about line 120, above

	for y in postinfo:
		latexfile.write("""
			%s & %s & \url{%s} \\\\
			""" % (y[1][0:10],y[2][0:min(len(y[2]),60)],y[3]))		

	latexfile.write("""\end{tabular}
		\end{table}

		\\begin{table}[H]
		\\begin{tabular}{lll}
		Comment  & Comment  & Comment  \\\\ 
		 Title &  Date &  URL \\\\ \hline
		""")
	for y in commentinfo:
		latexfile.write("""
		%s & %s & \url{%s} \\\\
		""" % (y[1][0:10],y[2][0:min(len(y[2]),60)],y[3]))		

	latexfile.write("""\end{tabular}
		\end{table}""")


latexfile.write("""\end{document}"""
)