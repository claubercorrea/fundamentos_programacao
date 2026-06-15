# Construcao de URL

from flask import Flask, redirect, url_for

app4 = Flask (__name__)

@app4.route("/admin")
def admin():
    return "<h1>Admin</h1>"

@app4.route("/guest/<name>")
def guest(name):
    
    # o %s indica que a o url sera injetada
    return "<p>Olá guest<b>%s</b></p>" % name

@app4.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest", name=guest))

if __name__ == "__main__":

    app4.run(debug=True)
    
    