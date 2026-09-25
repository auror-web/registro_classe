from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
# La secret_key serve per firmare la sessione (il "braccialetto" dell'utente)
app.secret_key = "una_frase_qualsiasi_a_caso"

def connetti_al_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",  # ⚠️ Inserisci qui la tua password MySQL
        database="registro_classe"
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connessione = connetti_al_database()
        cursore = connessione.cursor()
        
        # Cerchiamo l'utente nel database
        cursore.execute(
            "SELECT * FROM utente WHERE username = %s AND password = %s",
            (username, password)
        )
        utente_trovato = cursore.fetchone()
        connessione.close()

        if utente_trovato is None:
            # Se non troviamo l'utente, ricarichiamo la pagina con il messaggio d'errore
            return render_template("login.html", errore="Credenziali errate")
        else:
            # Se lo troviamo, salviamo il login in sessione
            session["loggato"] = True
            return redirect(url_for("elenco"))
    else:
        return render_template("login.html", errore=None)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)