from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    upper_name = None
    reversed_name = None
    length = None

    if request.method == "POST":
        name = request.form.get("name")

        upper_name = name.upper()
        reversed_name = name[::-1]
        length = len(name)

    return render_template(
        "index.html",
        upper_name=upper_name,
        reversed_name=reversed_name,
        length=length
    )

if __name__ == "__main__":
    app.run(debug=True)