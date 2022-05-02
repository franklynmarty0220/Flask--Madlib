from stories import Story
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbar

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] ="Madlib"

debug = DebugToolbar(app)


@app.route('/root')
def ask_question():

    prompts =Story.prompts
    return render_template('question.html', prompts=prompts)

@app.route('/story')
def story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)
