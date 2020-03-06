from flask import Flask, request
from heroTool import playStyles, draftSherpa
#The flask application name is app.
app = Flask(__name__)

#The landingPage function is called when someone lands on the root landing page of the site.
@app.route("/", methods=["GET", "POST"])
def landingPage():
    #Conditional to verify the POST from the webform. Input is accepted as a string, then converted to lowercase.
    if request.method == "POST":
        chosenStyle = str(request.form["desiredPlaystyle"])
        chosenStyle = chosenStyle.lower()

        #The list playStyles was imported from heroTool.py. This conditional verifies that the input from the webform matches a 
        # valid playstyle within the playSyles list. If it finds a match, raw HTML is returned to redraw the webpage with meta hero results at the bottom.
        #If no match is found, then the page is redrawn to alert the user a valid playstyle was not entered.
        if chosenStyle in playStyles:
            #In the file heroTool.py draftSherpa() is the function that performs the webscraping and returns a list of winning, compatible heroes in a the form of raw html.
            #Here we call that function with a valid user-provded playstyle, and store the results in the result variable.
            result = draftSherpa(chosenStyle)
            #This returns a results page.
            return '''
                <html>
                    <body>
                        <p>Thanks for using the Dota2 draft assistant tool.</p>
                        <p>I will tell you all the most-winning heroes for your given playstyle.
                        <p></p>
                        <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Durable, Escape, Nuker,  Melee, & Ranged.</p>
                        <form method="post" action=".">
                            <p><input name="desiredPlaystyle" /></p>
                            <p><input type="submit" value="Show me the meta" /></p>
                        </form>
                        <p></p>
                        <p></p>
                        {result}
                    </body>
                </html>
            '''.format(result=result)
        else:
            #This returns a page informing that an incorrect playstyle was previously entered.
            return'''
            <html>
                <body>
                    <p>Thanks for using the Dota2 draft assistant tool.</p>
                    <p>I will tell you all the most-winning heroes for your given playstyle.
                    <p></p>
                    <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Durable, Escape, Nuker,  Melee, & Ranged.</p>
                    <form method="post" action=".">
                        <p><input name="desiredPlaystyle" /></p>
                        <p><input type="submit" value="Show me the meta" /></p>
                    </form>
                    <p>Choose from the playstyles listed above.<p>
                </body>
            </html>
            '''
    #This is the raw html of the default landing page.
    return'''
    <html>
        <body>
            <p>Thanks for using the Dota2 draft assistant tool.</p>
            <p>I will tell you all the most-winning heroes for your given playstyle.
            <p></p>
            <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Durable, Escape, Nuker,  Melee, & Ranged.</p>
            <form method="post" action=".">
                <p><input name="desiredPlaystyle" /></p>
                <p><input type="submit" value="Show me the meta" /></p>
            </form>
        </body>
    </html>
    '''