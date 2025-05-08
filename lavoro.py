listaras=['terminata', 'chance', 'uccisi', 'radar', 'frode', 'contro', 'rabbia', 'risse', 'anticipato', 'minaccia']

listasos=["bomba", "vergogna", "allarme", "incredibile", "shock", "denuncia", "svelato", "disastro", "mai visto prima", "terribile"]

def titolo():

    ras = 0   
    sos = 0   

    n=input("scrivi un titolo : ")

    for i in listaras:  
        if i in n:
            ras += 1  
    for i in listasos:
        if i in n:
            sos += 1 

    if sos > ras: 
        print("è una fake news")
    elif sos<ras: 
        print("Non è una fake news")    
    else: 
        print("Non si sa")

def menu(): 
        print(f"inserisci 1 per scrivere il titolo da controllare")
        print(f"inserisci 0 per fermare il programma")

while True: 
        menu()
        scelta = int(input("cosa vuoi fare ?: "))
        if scelta == 1:
            titolo()
        elif scelta == 0:
            break