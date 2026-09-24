# verifica_da_python.py — COPIA E INCOLLA, poi eseguilo!
# Un ultimo controllo: verifica che Python riesca a collegarsi
# al database appena creato, PRIMA di lanciare app.py
import mysql.connector

connessione = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="registro_classe"
)

print("Connessione al database riuscita!")

cursore = connessione.cursor()
cursore.execute("SHOW TABLES")
tabelle = cursore.fetchall()

print("Tabelle trovate:", tabelle)
# Atteso: [('presenza',), ('studente',), ('ute

connessione.close()