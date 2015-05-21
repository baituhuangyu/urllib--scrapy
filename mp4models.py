import re,urllib,os,codecs,sys


#get html src and translate html src to string
def getHtml(aurl):
    page = urllib.urlopen(aurl)
    htmlsrc = page.read()
    return htmlsrc

#find mp4 file from the resouce code
def getMp4Url(html):
    reg = r'file: "(.+?\.mp4)"'
    mp4re = re.compile(reg)
    mp4listUrlList = re.findall(mp4re,html)
    if mp4listUrlList:
        mp4listUrl = mp4listUrlList[0]
        return mp4listUrl
    else:
        return False

#get content father name from the resouce code
def getContentFather(html):
    reg = r'<li><a href="/course/\d+/">(.+)</a></li>'
    contentre = re.compile(reg)
    contentNameFatherList = re.findall(contentre,html)
    if contentNameFatherList:
        fatherContentNameSrc = contentNameFatherList[0]
        fatherContentName = fatherContentNameSrc
        return fatherContentName
    else:
        return ""
###do with windows creat folder char error
##    fuckWindowsFolderNameChar = '\\'
###    fuckWindowsFolderName = re.compile(fuckWindowsFolderNameChar)
##    fuckWindowsFolderNameIndex = fatherContentNameSrc.index(fuckWindowsFolderNameChar)
##    if fuckWindowsFolderNameIndex >= 0:
##        fatherContentNameSrc[fuckWindowsFolderNameIndex] = ' '
    

#get content sun name from the resouce code
def getContentSun(html):
    reg = r'<li class="active">(.+)</li>'
    contentre = re.compile(reg)
    contentNameSunGroup = re.search(contentre,html)
    contentNameSunWithHtmlLable = contentNameSunGroup.group(0)#the first search result is right
    contentNameSunList = re.findall(contentre,contentNameSunWithHtmlLable)
    sunContentNameSrc = contentNameSunList[0]
    #do with windows creat folder char error
    fuckWindowsFolderNameChar = '\\'
    
    #fuckWindowsFolderName = re.compile(fuckWindowsFolderNameChar)
    fuckCharIsExist = sunContentNameSrc.find(fuckWindowsFolderNameChar)
    if fuckCharIsExist >= 0:
        fuckWindowsFolderNameIndex = sunContentNameSrc.index(fuckWindowsFolderNameChar)
        sunContentName = sunContentNameSrc[0:fuckWindowsFolderNameIndex] + " " + sunContentNameSrc[fuckWindowsFolderNameIndex+1 :]
        return sunContentName
    else:
        sunContentName = sunContentNameSrc   
        return sunContentName

#get content mp4 file name from the resouce code
def getMp4FileName(html):
    reg = r'<a href="/lesson/\d+/"  class="active" lesson_id=\d+>(.+)</a>'
    contentre = re.compile(reg)
    Mp4FileNameListSrc = re.findall(contentre,html)
    #List type to string
    mp4FileNamesrc = Mp4FileNameListSrc[0]
    #delete ".&nbsp;" to normal mp4 file name
    reg2 = r'(\d+).&nbsp;'    
    contentre2 = re.compile(reg2)
    list2 = re.findall(reg2,mp4FileNamesrc)
    str2 = list2[0]
    reg3 = r'.&nbsp;(.+)'    
    contentre3 = re.compile(reg3)     
    list3 = re.findall(reg3,mp4FileNamesrc)
    str3 = list3[0]
    #join them
    mp4FileName = str2 + " . " + str3
    return mp4FileName

def generateUrlList(lessonNum):
    str1 = "http://www.maiziedu.com/lesson/"
    str2 = str1 + str(lessonNum) + "/"
    return str2

#setMp4RootPath
def generateLocalMp4FatherContentPathName(mp4RootPath, fatherContentName):
#    mp4RootPath = "C:\\Users\\hy\\Desktop\\test\\001"
    localFatherContentPath = mp4RootPath + "\\" + fatherContentName
    return localFatherContentPath
def generateLocalMp4SunContentPathName(localFatherContentPath, sunContentName):
    localSunContentPath = localFatherContentPath + "\\" + sunContentName
    return localSunContentPath
def generateLocalMp4TxtFileName(localSunContentPath, mp4FileName):
    mp4FileName_mp4_txtPath = localSunContentPath + "\\" + mp4FileName + r".txt"
    return mp4FileName_mp4_txtPath

##judge ContentFather and ContentSunPath exit,if not creat it
def prepareSaveMp4InfoFolder(localFatherContentPath, localSunContentPath):
    if not os.path.exists(localFatherContentPath.decode('utf-8')):
        os.mkdir(localFatherContentPath.decode('utf-8'))
    if not os.path.exists(localSunContentPath.decode('utf-8')):
        os.mkdir(localSunContentPath.decode('utf-8'))
##    #create txt file to save mp4 file url
##    if not os.path.exists(mp4FileName_mp4_txt.decode('utf-8')):
##        os.mknod(mp4FileName_mp4_txt.decode('utf-8'))

#writeMp4InfoIntoTxt
def writeMp4InfoIntoTxt(mp4FileName_mp4_txtPath, mp4listUrl, mp4FileName):
    f=open(mp4FileName_mp4_txtPath.decode('utf-8'),'a')
    f.write('%s%s%s%s%s' % (mp4FileName, os.linesep, mp4listUrl, os.linesep, os.linesep))
    f.close()

#writeMp4InfoIntoTxt2
def writeMp4InfoIntoTxt2(localSunContentPath, mp4listUrl, mp4FileName):
    testnamePath = localSunContentPath + "\\" + r'test.txt'
    f=open(testnamePath.decode('utf-8'),'a')
    f.write('%s%s%s%s%s' % (mp4FileName, os.linesep, mp4listUrl, os.linesep, os.linesep))
    f.close()

#writeMp4InfoIntoTxt2
def writeFatherErrorInfoIntoTxt(aurl):
    f=open(r"C:\Users\hy\Desktop\test\003\FNE.txt",'a')
    f.write('%s%s%s' % (aurl, os.linesep, os.linesep))
    f.close()
    

##copyMaizieduMp4
def copyMaizieduMp4(aurl, mp4RootPath):
    #get a html
    html = getHtml(aurl)
    #print "html ok"
    #get a url of a mp4 file from website
    mp4listUrl = getMp4Url(html)
    if mp4listUrl == False:
        return False
    else:
        #print "mp4listUrl ok"
        #get content father name from the resouce code
        fatherContentName = getContentFather(html)
        if fatherContentName == False:
            writeFatherErrorInfoIntoTxt(aurl)
        else:
            #print "fatherContentName ok"
            #get content sun name from the resouce code
            sunContentName = getContentSun(html)
            #print "sunContentName ok"
            #get content mp4 file name from the resouce code
            mp4FileName = getMp4FileName(html)
            #print "mp4FileName ok"
            #generate Mp4 Path Name
            localFatherContentPath = generateLocalMp4FatherContentPathName(mp4RootPath, fatherContentName)
            localSunContentPath = generateLocalMp4SunContentPathName(localFatherContentPath, sunContentName)
            mp4FileName_mp4_txtPath = generateLocalMp4TxtFileName(localSunContentPath, mp4FileName)
            
            ##judge ContentFather and ContentSunPath exit,if not creat it
            prepareSaveMp4InfoFolder(localFatherContentPath, localSunContentPath)
            #print "prepareSaveMp4InfoFolder ok"
        ##    #writeMp4InfoIntoTxt
        ##    writeMp4InfoIntoTxt(mp4FileName_mp4_txtPath, mp4listUrl, mp4FileName)
            
            #writeMp4InfoIntoTxt2
            writeMp4InfoIntoTxt2(localSunContentPath, mp4listUrl, mp4FileName)
            #print "writeMp4InfoIntoTxt2 ok"

            return True
