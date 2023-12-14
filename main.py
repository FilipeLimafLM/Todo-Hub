from flask import Flask, render_template, request, redirect, flash, url_for
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "palavra-secreta123"

todos = [
    {
        'id': 0,
        'name':'Escreva uma tarefa',
        'checked': False,
    },
    {
        'id': 0,
        'name':'Escreva uma tarefa',
        'checked': True,
    }
]

@app.route("/", methods=["GET", "POST"])
def homepage():
    if(request.method == "POST"):
        todo_name =request.form["todo_name"]
        cur_id = random.randint(1, 1000)
        todos.append({
            'id': cur_id,
            'name': todo_name,
            'checked': False
        }),
        return redirect(url_for("homepage"))
    return render_template("home.html",items=todos)

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked']
            break
    return redirect(url_for("homepage"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global todos
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
    return redirect(url_for("homepage"))
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("nome")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "admin":
            flash("Login bem-sucedido!", "success")
            return redirect("/")
        else:
             flash("Usuário ou senha incorretos", "error")

    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)