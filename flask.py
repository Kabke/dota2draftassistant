# A very simple Flask Hello World app for you to get started with...
from flask import Flask
import heroTool

app = Flask(__name__)

@app.route('/')
def landingPage():
    return'''
    <html>
            <body>
                <p>Thanks for using the Dota2 drafting sherpa.</p>
                <p>I will tell you all the most-winning heroes for your given playstyle.
                <p></p>
                <p></p>
                <p></p>
                <p>Choose your playstyle from the following: Carry, Support, Disabler, Pusher, Initiator, Jungler, Durable, Escape, Nuker,  Melee, & Ranged.</p>
                <form>
                    <p><input name="desiredPlaystyle" /></p>
                    <p><input type="submit" value="Be blessed by the sherpa" /></p>
                </form>
            </body>
        </html>
    '''