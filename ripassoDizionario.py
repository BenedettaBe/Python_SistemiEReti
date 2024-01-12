dizionario = {"a" : "albero", "b" : "brutto", "c" : "casa"}#elenco indicizzato dalle chiavi
lista=["albero", "brutto", "casa"]#elenco indicizzato per indice

#aggiungo elemento al dizionario
dizionario["d"] = "dado"
#sovrascrivo un elemento -> a una chiave un solo elemento
dizionario["a"] = "alto"

#for che stampa la chiave
for chiave in dizionario:
    print(chiave)

#for che stampa il contenuto
for chiave in dizionario:
    print(dizionario[chiave])

#cerco se è presente un indice
if "a" in dizionario:
    print("a è presente nel dizionario")

print(dizionario["b"])
print(lista[1])