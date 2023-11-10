#collezione di coppie chiave: valore
#il dizionario non ha indici, ma si indicizza per chiave(che devono avere un nome univoco)

dizionario = {"nome" : "Mario", "cognome" : "Rossi"}
# lista con stesso significato lista = ["Mario", "Rossi"]
print(dizionario["nome"])

#aggiunge due elementi nuovi
dizionario["data nascita"] = "01/01/1900"
dizionario["età"] = 123

#sovrascrivere l'elemento con chiave "nome"
dizionario["nome"] = "Luca"

print(dizionario)

#ciclo for su dizionario 1 - scorre sulle chiavi
for chiave in dizionario:
    #print(dizionario[chiave])
    print(f"Chiave: {chiave}  valore: {dizionario[chiave]}")

#esempio rubrica-> chiave: numero di telefono, valore: nome
rubrica = {31284 : "Mario Rossi", 4738989258475 : "Alice Verdi",
           4663278 : "Giacomo Gialli"}
print(dizionario)