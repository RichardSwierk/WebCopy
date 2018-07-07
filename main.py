#!/usr/bin/python
import requests, os
from pathlib import Path

sources=[]
filePaths=[]
website='http://www.suzannecollinsbooks.com/'
filename=website[website.find('www.')+4:website.find('.com')]

my_dir=Path(filename)
if my_dir.is_dir():
        os.system('rm -r '+filename)
os.system('mkdir '+filename)

def getWebsite(url,path):
        html=requests.get(url)
        f=open(path,'w')
        f.write(html.content)
        f.close()

def getContent(pathToFile):
        with open(pathToFile) as f:
                content=f.readlines()
        f.close()
        #print content
        content=[x.strip() for x in content]
        return content

def add(found,lang):
        found=found[:found.find(lang)+len(lang)]
        found=found[found.rfind(' ')+1:]
        found=found[found.rfind('"')+1:]
        print found
        sources.append(found)

def getFileType(found):
        if '.js' in found:
                add(found,'.js')
        elif '.php' in found:
                add(found,'.php')
        elif '.css' in found:
                add(found,'.css')
        elif '.jpg' in found:
                add(found,'.jpg')
        elif '.gif' in found:
                add(found,'.gif')
        elif '.htm' in found:
                add(found,'.htm')
        elif '.html' in found:
                add(found,'html')

def findSources(content,loopNum):
        for x in range(len(content)):
                line=content[x]
                if "'" in line:
                        line=list(line)
                        num=int(line.index("'"))
                        line[num]='"'
                        "".join(line)
                found=str(line)
                if loopNum==1:
                        if 'href' in found or 'src' in found:
                                getFileType(found)
                else:
                        if '"' in found and 'url' in found:
                                getFileType(found)

def getSources():
        for x in range(len(sources)):
                source=sources[x]
                if 'http' not in source:
                        #print source
                        dir=source
                        file=''
                        if source.find('/')!=source.rfind('/'):
                                for y in range(source.count('/')-1):
                                        file=file+dir[dir.find('/'):dir.find('/', dir.find('/')+1)]
                                        dir=dir[dir.find('/', dir.find('/')+1):]
                                        myDir=Path(filename+file)
                                        if myDir.is_dir():
                                                pass
                                        else:
                                                os.system('mkdir '+filename+file)
                        if '.jpg' in source or '.gif' in source:
                                os.system('wget '+website+source[source.find('/')+1:]+' -P '+filename+source[source.find('/'):])
                                #pass
                        else:
                                getWebsite(website+source[source.find('/')+1:],filename+source[source.find('/'):])
                                #if '.css' not in source:
                                        #filePaths.append(filename+source[source.find('/'):])

getWebsite(website,filename+'/index.html')
findSources(getContent(filename+'/index.html'),1)
getSources()
#sources=[]
#for x in range(len(filePaths)):
#        #print filePaths[x]
#        source=filePaths[x]
#        findSources(getContent(source),2)
