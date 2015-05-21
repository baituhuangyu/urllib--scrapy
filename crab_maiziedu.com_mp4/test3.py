import re,urllib,os,codecs,sys

from mp4models import *

##mp4RootPath = raw_input('Enter mp4RootPath receive:')
  
for lessonNum in range(1, 5500):
##    lessonNum = 2    
    aurl = generateUrlList(lessonNum)
    mp4RootPath = r'C:\Users\hy\Desktop\test\006'

    state = copyMaizieduMp4(aurl, mp4RootPath)
    if not state:
        continue
    print 'lesson' + str(lessonNum) + 'ok'
print 'copy maiziedu lessons ok'
