#Get a list a best moview per year as per rotten tomatoes
import sys, os, requests, bs4

rottenurl = "https://www.rottentomatoes.com/top/bestofrt/?year="
if len(sys.argv) > 1:
    url = rottenurl + sys.argv[1]
    
    #Create the folder and text file
    name = sys.argv[1] + '_rating.txt'
    os.makedirs('ROTTEN_TOP_MOVIES', exist_ok = True)
    rottenTextFile = os.path.join('ROTTEN_TOP_MOVIES', name) 
    
    #Get the html page
    rottenlink = requests.get(url)
    rottenbs = bs4.BeautifulSoup(rottenlink.text, 'html.parser')
    
    #Get the list of names of movies of that year in the <a> tag
    rottenTableElemList = rottenbs.select('.table a')
    
    #Open a reference to the file to write to
    rottenTextFileRef = open(rottenTextFile, 'w')
    
    #Write to the file as you loop through the element
    for elem in rottenTableElemList:
        rottenTextFileRef.write(elem.getText())
        
    rottenTextFileRef.close()  
    
else:
    print("please enter year")
    
    
    
    


