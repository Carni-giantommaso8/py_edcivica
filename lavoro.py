
listaras=['terminata', 'chance', 'uccisi', 'radar', 'frode', 'contro', 'rabbia', 'risse', 'anticipato', 'minaccia']
listasos=["bomba", "vergogna", "allarme", "incredibile", "shock", "denuncia", "svelato", "disastro", "mai visto prima", "terribile"]

#abbiamo dichiarato 2 liste da dove prendere le parole che si possono trovre nei titoli che scriviamo in input 
def titolo():

    ras=0   #dichiaro il punteggio rassicurante 
    sos=0   #dichiaro il punteggio sospetto 

    n=input("scrivi un titolo : ")

    for i in listaras:  #definisco i per scorrere la lista rassicurante
        if i in n:
            ras+=1  #se la parola che scorriamo è presente nell'input aggiungiamo 1 al punteggio rassicurante
    for i in listasos:
        if i in n:
            sos+=1 #facciamo lo stesso ma con il valore sospetto

    if sos>ras: #compariamo i 2 punteggi se il val. sospetto è maggiore stampa è una fake news
        print("è una fake news")
    elif sos<ras: #facciamo lo stesso ma in caso il punteggio maggiore sia il valore rassicurante
        print("Non è una fake news")    
    else: #in caso siano uguali 
        print("Non si sa")

def menu(): #mostriamo le azioni che si possono fare tramite il terminale 
        print(f"inserisci 1 per scrivere il titolo da controllare")
        print(f"inserisci 0 per fermare il programma")

while True: #creiamo un ciclo while True e chiediamo che operazione vuoi eseguire 
        menu()
        scelta = int(input("cosa vuoi fare ?: "))
        if scelta == 1:
            titolo()
        elif scelta == 0:
            break