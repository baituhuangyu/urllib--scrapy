import re,urllib,os,codecs,sys

from mp4models import *


def copyMaizieduMp4(aurl, mp4RootPath):
    #get a html
    html = getHtml(aurl)
    
    #get a url of a mp4 file from website
    mp4listUrl = getMp4Url(html)
    
    #get content father name from the resouce code
    fatherContentName = getContentFather(html)
    
    #get content sun name from the resouce code
    sunContentName = getContentSun(html)
    
    #get content mp4 file name from the resouce code
    mp4FileName = getMp4FileName(html)

    #generate Mp4 Path Name
    localFatherContentPath = generateLocalMp4FatherContentPathName(mp4RootPath, fatherContentName)
    localSunContentPath = generateLocalMp4SunContentPathName(localFatherContentPath, sunContentName)
    mp4FileName_mp4_txtPath = generateLocalMp4TxtFileName(localSunContentPath, mp4FileName)
    
    ##judge ContentFather and ContentSunPath exit,if not creat it
    prepareSaveMp4InfoFolder(localFatherContentPath, localSunContentPath)

    #writeMp4InfoIntoTxt
    writeMp4InfoIntoTxt(mp4FileName_mp4_txtPath, mp4listUrl, mp4FileName)  

    
for lessonNum in range(1, 5):
##    lessonNum = 2    
    aurl = generateUrlList(lessonNum)
    mp4RootPath = r'C:\Users\hy\Desktop\test\001'

    copyMaizieduMp4(aurl, mp4RootPath)

    print 'lesson' + str(lessonNum) + 'ok'
