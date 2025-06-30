from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extrair informações do formulário
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Inserir no banco de dados
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            name, month, day
        )

        # Redirecionar para a página inicial
        return redirect("/")
    else:
        # Buscar todos os aniversários no banco de dados
        birthdays = db.execute("SELECT * FROM birthdays")

        # Renderizar a página com os aniversários
        return render_template("index.html", birthdays=birthdays)

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")
