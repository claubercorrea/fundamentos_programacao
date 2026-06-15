from flask import Flask, request    

app5 = Flask(__name__, static_folder='public')

# Correções: rota começa com '/', 'methods' em inglês e 'POST' em maiúsculo
@app5.route('/add', methods=["POST"])
def add():
     # Aqui você pode processar os dados enviados pelo formulário
     return "OKK"

if __name__ == '__main__':
     app5.run(debug=True)
     