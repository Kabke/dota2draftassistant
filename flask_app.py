from flask import Flask, request
from heroTool import playStyles, draftSherpa

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        chosenStyle = str(request.form["desiredPlaystyle"])
        chosenStyle = chosenStyle.lower()

        if chosenStyle in playStyles:
            result = draftSherpa(chosenStyle)
            return '''
                <html>
                    <body>
                        <p>Thanks for using the Dota2 draft assistant tool.</p>
                        <p>I will tell you all the most-winning heroes for your given playstyle.
                        <p></p>
                        <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.</p>
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
            return'''
            <html>
                <body>
                    <p>Thanks for using the Dota2 draft assistant tool.</p>
                    <p>I will tell you all the most-winning heroes for your given playstyle.
                    <p></p>
                    <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.</p>
                    <form method="post" action=".">
                        <p><input name="desiredPlaystyle" /></p>
                        <p><input type="submit" value="Show me the meta" /></p>
                    </form>
                    <p>Choose from the playstyles listed above.<p>
                </body>
            </html>
            '''

    return'''
    <html>
        <body>
            <p>Thanks for using the Dota2 draft assistant tool.</p>
            <p>I will tell you all the most-winning heroes for your given playstyle.
            <p></p>
            <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.</p>
            <form method="post" action=".">
                <p><input name="desiredPlaystyle" /></p>
                <p><input type="submit" value="Show me the meta" /></p>
            </form>
        </body>
    </html>
    '''