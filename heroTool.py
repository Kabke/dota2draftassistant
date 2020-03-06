import styleData
from selenium import webdriver

#This list contains all the valid playStyles the script will be able to categorize heroes within.
playStyles = ['carry', 'disabler', 'durable', 'escape', 'initiator', 'jungler', 'melee', 'nuker', 'pusher', 'ranged', 'support']

#PythonAnywhere is my host, and they requre a headless Chrome browser for web scraping.
#These 4 lines of code will add the appropriate arguments to the chrome webdriver to be compatible for the host.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

#The function that performs the web scraping, and returns a list of winning heroes in valid HTML.
def draftSherpa(chosenStyle):
    #Opens dotabuff's top heroes of the week page
    browser.get("https://www.dotabuff.com/heroes/winning?date=week")
    #Creates a list of heroes with the most successful heroes being first in the list.
    heroRanking = browser.find_elements_by_class_name("link-type-hero")
    #Creates a list of winning percentages, which will later be associated to the appriate hero.
    heroWinrates = browser.find_elements_by_class_name("sorted")
    #styleData.py is essentially one large dictionary to map certain playstyles to certain heroes. This piece of code takes the chosenStyle variable provided by the user and then uses
    #it as a key for the styleData dictionary. As long as the input is valid, a list of all the heroes of a given playstyle are referenced.
    compatibleHeroes = styleData.styleData[chosenStyle.capitalize()]

    #Exceptional heroes are heroes that match the requested playstyle. They are also in the top 20 win-rates for their style.
    exceptionalHeroes = 0
    #resultsText is the header of the "table" that is printed out when returning hero results to the front-end.
    resultsText = str("<p>This week's top 20 " + chosenStyle.capitalize() + " heroes.</p>")
    #Iterate through all heroes until 20 valid matches are found.
    for x in range(0,119):
        #Stop iterations to identify more valid heroes, if 20 heroes are already selected.
        if exceptionalHeroes == 20:
            #Once 20 heroes are selected, return the results as the variable "resultsText"
            return(resultsText)
        #Hero and rate both reference the scraped data. During iterations, hero and rate reference information for the same here.    
        hero = heroRanking[x].text
        rate = heroWinrates[x + 1].text
        #Since all the most-winning heroes will be interated through first, each hero found within compatibleHeroes will be printed to the front-end. Matches are added to the resultsText
        #varible and returned as HTML.
        if hero.upper() in compatibleHeroes:
            resultsText = resultsText + "<p>" + (hero.ljust(25, "-") + ": " + rate.center(8)) + "</p>"
            exceptionalHeroes = exceptionalHeroes + 1