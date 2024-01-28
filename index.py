from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/isprime/<int:n>")
def isprimet(n):
   if n <= 1:
      return "False"
   else:
      for i in range(2, n):
         if (n % i) == 0:
            return jsonify(
               result ={
                  "number": n,
                  "status":"False",
                  "divisor":i

               }
             )
         else:
          return jsonify(
               result ={
                  "number": n,
                  "status":"True",
                  "divisor":i

               }
         )
      



