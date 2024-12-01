from flask import Flask, request, render_template
import pywhatkit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        song = request.form.get("song")
        try:
            pywhatkit.playonyt(song)
            message = f"Lagu '{song}' berhasil diputar di YouTube!"
        except Exception as e:
            message = f"Terjadi error: {e}"
        return render_template("index.html", message=message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
