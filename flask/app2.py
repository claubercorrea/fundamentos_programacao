from flask import Flask

app2 =  Flask(__name__)

@app2.route("/")

def index():

    return "Index"

def teste():
    return "<p>Teste 1</P>"
app2.add_url_rule("/teste","teste", teste)

def teste2():
    return '<h1> teste 2</h1>'
app2.add_url_rule("/teste2", "teste2", teste2 ) 
if __name__ == '__main__':
    app2.run(debug = True, port = "3000")