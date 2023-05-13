import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from main import parseUrl

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        url = request.form["url"]
        response = openai.ChatCompletion.create( 
            model = "gpt-3.5-turbo",
            messages=[{"role": "user", "content": generate_news_prompt(url)}],
            temperature=0.6,
        )
        return redirect(url_for("index", result=response["choices"][0]["message"]["content"]))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_news_prompt(url):
    
    header, text = parseUrl(url)

    prompt = f"""Summarize the following news article titled {header.capitalize()} 
                    in approximately four to five pointer. Also, give credits to {url.capitalize()}
                The detailed article: {text.capitalize()} """

    return prompt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)