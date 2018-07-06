#!/usr/bin/python
import requests, os
from pathlib import Path
sources=[]
website='http://www.suzannecollinsbooks.com/'
filename=website[website.find('www.')+4:website.find('.com')]
my_dir=Path(filename)
if my_dir.is_dir():
        os.system('rm -r '+filename)
os.system('mkdir '+filename)
html=requests.get(website)
f=open(filename+'/index.html','w')
f.write(html.content)
f.close()
with open(filename+'/index.html') as f:
        content=f.readlines()
f.close()
content=[x.strip() for x in content]
#print content
def add(found):
        found=found[found.rfind(' ')+1:]
        sources.append(found[found.rfind('"')+1:])
for x in range(len(content)):
        line=content[x]
        if "'" in line:
                line=list(line)
                num=int(line.index("'"))
                line[num]='"'
                "".join(line)
        found=str(line)
        if '.js' in line:
                found=line[:line.find('.js')+3]
                add(found)
        elif '.php' in line:
                found=line[:line.find('.php')+4]
                add(found)
        elif '.css' in line:
                found=line[:line.find('.css')+4]
                add(found)

for x in range(len(sources)):
        source=sources[x]
        if 'http' not in source:
                print source
                dir=source
                file=''
                if source.find('/')!=source.rfind('/'):
                        for y in range(source.count('/')-1):
                                file=file+dir[dir.find('/'):dir.find('/', dir.find('/')+1)]
                                dir=dir[dir.find('/', dir.find('/')+1):]
                                print file
                                myDir=Path(filename+file)
                                if myDir.is_dir():
                                        pass
                                else:
                                        os.system('mkdir '+filename+file)

#name=source[source.rfind('/')+1:]
#print name
