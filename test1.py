
import re,urllib
#URL
aurl = r"http://www.maiziedu.com"
print aurl
#download page
page = urllib.urlopen(aurl)
print page
#<type '_sre.SRE_Pattern'>
htmlsrc = page.read()
type(htmlsrc)
#string

reg = r'<meta name="description" content="(.+?)">'
#string

#reg = r'<title>(.+?)</title>'

#reg = r'<meta name="keywords" content="(.+?)">'

searchConditionRe = re.compile(reg)
#Pattern
#search strings
searchResultList = re.findall(searchConditionRe,htmlsrc)
#

#get
searchResultString = searchResultList[0]
#list
print searchResultString
#decode/encode type
