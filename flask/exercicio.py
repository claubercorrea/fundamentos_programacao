from flask import Flask,request 

exercicio =  Flask (__name__, static_folder="index")

@exercicio.route('/adicionar', methods = ["POST"])
def adcionar():
    return "OKK"
if __name__== '__main__':
    exercicio.run(debug=True)