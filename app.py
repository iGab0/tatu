from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para procesar el formulario
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Simular el almacenamiento (aquí puedes usar una base de datos)
    print(f"Nombre: {name}, Correo: {email}, Mensaje: {message}")
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
