# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:00:05 2019

@author: ASSUS
"""



def searchByKeyWord(pageContent,keyword):
    keywordfound=[]
    for kw in keyword:
        if kw.lower() in (str(pageContent)).lower():
            keywordfound.append(kw)
    return keywordfound



def searchByRegex(pageContent,Regex):
    return ""


def isAlink(link):
    suffixe=[".com/",".fr/",".org/",".bj/",".it/",".xyz/",".de/",".co/",".ca/",".be/","http://"]
    for suf in suffixe:
        if suf in link:
            return True


def getWebSiteRoot(link):
    suffixe=[".com/",".fr/",".org/",".bj/",".it/",".xyz/",".de/",".co/",".ca/",".be/"]
    for suf in suffixe:
        if suf in link:
            endRootIndex=link.find(suf)
            return str (link[0:endRootIndex+len(suf)])
    return ""





def recursiveSearch(link,keyword):
    from bs4 import BeautifulSoup
    import urllib  
    visitedLink=[]
    queue=[]
    #keyword=["music","Melo"]      
    #link="http://localhost/witunes/public/"
    queue.append(link)
    for link in queue:   
        try:         
            print(link)
            sock = urllib.request.urlopen(link) 
            htmlSource = sock.read()                            
            sock.close()                                        
            
            soup = BeautifulSoup(htmlSource)
                
            for p in soup.find_all('a'):
                pget=p.get("href")
                if(visitedLink.count(pget)==0):
                    if(("http" in str(pget)) and ("." in str(pget)) and getWebSiteRoot(link) in str(pget) ):# and ("." in str(pget))
                        if(pget not in queue):
                            queue.append(pget)
                    elif len(str(pget))>0:
                        if((str(pget))[0]=="/"):
                            if((str(getWebSiteRoot(link))+(str(pget))[1:] not in queue) and (getWebSiteRoot(link) in str(getWebSiteRoot(link))+(str(pget))[1:])):
                                queue.append(str(getWebSiteRoot(link))+(str(pget))[1:])
            for keyW in searchByKeyWord(htmlSource,keyword):
                print(keyW+" is found on "+link)
        except:
            pass
    

    

if __name__== "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', help='link of website')
    parser.add_argument('-rs', help='Recursive Search mode, pprogram will make reseach on all of page of site')
    parser.add_argument('-kw', help='key-words list (separate by comma without space)')
    args = parser.parse_args()
    
    link=str(args.l)
    rs=str(args.rs)
    kw=str(args.kw)
    keyword=kw.split(",")
    print(keyword)
    if(rs=="1"):
        recursiveSearch(link,keyword)
        
        
                

