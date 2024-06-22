from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search_page():
    if request.method == "POST":
        user_msg = request.form.get('search_query', '').lower()
        if not user_msg:
            return render_template('search.html', results=None)

        response = MessagingResponse()
        q = user_msg + " site:google.com"
        result = [url for url in search(q, num_results=3)]

        return render_template('search.html', results=result)

    return render_template('search.html', results=None)

@app.route("/result")
def result_page():
    url = request.args.get('url')
    return render_template('result.html', url=url)

if __name__ == "__main__":
    app.run(debug=True)
