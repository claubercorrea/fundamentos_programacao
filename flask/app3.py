from flask import Flask
# pagina de maneira dinamica
app3 = Flask(__name__)


@app3.route("/hello/")
@app3.route('/hello/<nome>')
def hello (nome =""):  # sourcery skip: use-fstring-for-formatting
    return "<h1> hello {}<h1>".format(nome)
    # ----------------------------------- para int---------------------------------------------
@app3.route('/blog/')
@app3.route('/blog/<int:postID>')
def blog(postID =-1):  # sourcery skip: assign-if-exp, use-fstring-for-formatting
    if(postID >=0):
        return "blog info {}".format(postID)
    else:
        return"blog todo"
    # ----------------------------------- para float---------------------------------------------

@app3.route('/blog/<float:postID>')
def blog2(postID =-1):  # sourcery skip: assign-if-exp, use-fstring-for-formatting
    if(postID >=0):
        return "blog info {}".format(postID)
    else:
        return"blog float todo"
    

if __name__=="__main__":
    app3.run(debug=True)    