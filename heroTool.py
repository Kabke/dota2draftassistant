import styleData
from selenium import webdriver

playStyles = ['carry', 'disabler', 'durable', 'escape', 'initiator', 'jungler', 'melee', 'nuker', 'pusher', 'ranged', 'support']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

def draftSherpa(chosenStyle):
    try:
        browser.get("https://www.dotabuff.com/heroes/winning?date=week")
        heroRanking = browser.find_elements_by_class_name("link-type-hero")
        heroWinrates = browser.find_elements_by_class_name("sorted")

        compatibleHeroes = styleData.styleData[chosenStyle.capitalize()]

        #Iterate through the best heroes, and see if they match anything on the compatible hero list. Find 20 matches.
        exceptionalHeroes = 0
        resultsText = str("<p></p>This week's top 20 " + chosenStyle.capitalize() + " heroes.<p></p>")
        for x in range(0,119):
            if exceptionalHeroes == 20:
                return(resultsText)
            hero = heroRanking[x].text
            rate = heroWinrates[x + 1].text
            if hero.upper() in compatibleHeroes:
                resultsText = resultsText + (hero.ljust(25, "-") + ": " + rate.center(8)) + "<p></p>"
                exceptionalHeroes = exceptionalHeroes + 1

    finally:
        browser.quit()