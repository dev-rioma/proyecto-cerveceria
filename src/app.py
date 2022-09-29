from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        correo= request.form["userName"]
        clave= request.form["clave"]
        
        print(f"Correo: {correo}  \nclave: {clave}")
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/empleado")
def render_empleado():
    return render_template("employer.html", user_name="Jorge Acevedo")

@app.route("/admin")
def render_admin():
    return render_template("Administrador.html")

@app.route("/superadmin")
def render_superAdmin():
    return render_template("SuperAdmin.html")
if __name__ == "__main__":
    app.run(debug=True)
    


