from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for registered users (for demo purposes)
registered_users = []

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        event = request.form.get("event")

        if not name or not email or not event:
            return render_template("register.html", error="All fields are required!")

        # Save registration
        registered_users.append({"name": name, "email": email, "event": event})

        return redirect(url_for("success", name=name))

    return render_template("register.html")

@app.route("/success/<name>")
def success(name):
    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)