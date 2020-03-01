import styleData, heroData
from selenium import webdriver

playStyles = ['carry', 'disabler', 'durable', 'escape', 'initiator', 'jungler', 'melee', 'nuker', 'pusher', 'ranged', 'support']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

def draftSherpa():
    try:
        print("\nThanks for using the Dota 2 draft assistant!\n\nI can help you find the best meta heroes for your playstyle...\n\n")
        browser.get("https://www.dotabuff.com/heroes/winning?date=week")
        heroRanking = browser.find_elements_by_class_name("link-type-hero")
        heroWinrates = browser.find_elements_by_class_name("sorted")

        #Obtain valid playstyle from the user.
        playStyle = input("Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.\n")
        while playStyle.lower() not in playStyles:
            playStyle = input("Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.\n")
        print("\n\n\nThis week's top 20 " + playStyle.capitalize() + " heroes.")
        compatibleHeroes = styleData.styleData[playStyle.capitalize()]

        #Iterate through the best heroes, and see if they match anything on the compatible hero list. Find 20 matches.
        exceptionalHeroes = 0
        for x in range(0,119):
            if exceptionalHeroes == 20:
                break
            hero = heroRanking[x].text
            rate = heroWinrates[x + 1].text
            if hero.upper() in compatibleHeroes:
                print(hero.ljust(25, "-") + ": " + rate.center(8))
                exceptionalHeroes = exceptionalHeroes + 1

    finally:
        browser.quit()
draftSherpa()