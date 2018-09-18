#A programmer's way to access news
#Use this scrapper to get headlines of popular news websites in just 
#one click without the need of navigating through websites
#or opening several tabs
#The news headlines get displayed in the console
#Current Topics scarpped: front-page, entertainment-media, world
#Websites scrapped: bbc, foxnews, ndtv, buzzfeed
#Usage: <topic> where topic = top, media, world


import requests, sys, bs4


bbcurl = "https://www.bbc.com/news/"
foxnewsurl = "https://www.foxnews.com/"
ndtvurl = "https://www.ndtv.com/"
buzzurl = "https://www.buzzfeed.com/"


if len(sys.argv) > 1:
    #Get the news topic
    topic = sys.argv[1]
    if topic == "top":
        
        #foxnews
        print("front page news: \n\n")
        foxpg = requests.get(foxnewsurl)
        foxbs = bs4.BeautifulSoup(foxpg.text, "html.parser")
        foxList = foxbs.select('.title a')
        print("fox news: ")
        for elem in foxList:
            print(elem.getText()+'\n')        
        
        
        print("\n\n\n\n")
        
        
        #ndtv
        print("front page news: \n\n")
        ndtvpgtop =  requests.get(ndtvurl)
        ndtvtoppagebs = bs4.BeautifulSoup(ndtvpgtop.text, "html.parser")
        ndtvtopList = ndtvtoppagebs.select('.item-title')
        print("ndtv news: ")
        for elem in ndtvtopList:
            print(elem.getText()+'\n')        
        
        
    elif topic == "media":
        
        #bbcnews
        print("entertainment-media: \n\n")
        bbcenturl = bbcurl + "entertainment_and_arts"
        bbcent = requests.get(bbcenturl)
        bbcentbs = bs4.BeautifulSoup(bbcent.text, "html.parser")
        bbcentList = bbcentbs.select('.title-link__title-text')
        print("bbc news: ")
        for elem in bbcentList:
            print(elem.getText()+'\n')
        
        print("\n\n\n\n")
        
        
        #buzzfeed
        print("entertainment-media: \n\n")
        buzzenturl = buzzurl + "entertainment"
        buzzent = requests.get(buzzenturl)
        buzzentbs = bs4.BeautifulSoup(buzzent.text, "html.parser")
        buzzentList = buzzentbs.select('.link-gray h2')        
        print("buzzfeed: ")
        for elem in buzzentList:
            print(elem.getText()+'\n')
            
            
            
            
    elif topic == "world":
        


        #bbc
        print("world news: \n\n")
        bbcworldurl = bbcurl + "world"
        bbcpgworld = requests.get(bbcworldurl)
        bbcworldbs = bs4.BeautifulSoup(bbcpgworld.text, "html.parser")
        bbcworldList = bbcworldbs.select('.title-link__title-text')
        print("bbc news: ")
        for elem in bbcworldList:
            print(elem.getText()+'\n')
            
            
        print("\n\n\n\n")
        

        #ndtv
        print("world news: \n\n")
        ndtvworldurl = ndtvurl+"world-news"
        ndtvpgworld =  requests.get(ndtvworldurl)
        ndtvworldpagebs = bs4.BeautifulSoup(ndtvpgworld.text, "html.parser")
        ndtvworldList = ndtvworldpagebs.select('.nstory_header a')
        print("ndtv news: ")
        for elem in ndtvworldList:
            print(elem.getText()+'\n')
        
    else:
        print("topic not supported by scrapper")
        
        
else:
    print("Command: <topic> where topic = top, media, world")
