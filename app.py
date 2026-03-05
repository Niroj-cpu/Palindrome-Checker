from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Your palindrome checker logic
def is_palindrome(s):
    tempString = ""

    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            tempString += chr(ord(s[i]) + 32)
        else:
            tempString += chr(ord(s[i]))

    isPal = True
    for i in range(len(tempString)):
        l = len(tempString) - 1
        if tempString[i] != tempString[l - i]:
            isPal = False

    return isPal


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    word = ""

    if request.method == "POST":
        word = request.form["word"]
        result = is_palindrome(word)

    return render_template("index.html", result=result, word=word)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)
