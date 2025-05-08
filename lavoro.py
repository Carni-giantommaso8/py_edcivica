listaras=['uccisi', 'frode', 'contro', 'risse', 'minaccia']
listaras2=['terminata', 'anticipato', 'chance', 'accusa', 'scoperto']
listasos=["incredibile", "denuncia", "svelato", "disastro", "terribile"]
listasos2=["bomba","shock","allarme", "mai visto prima","vergogna", ]
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
    for i in listaras2:  
        if i in n:
            ras += 2  
    for i in listasos2:
        if i in n:
            sos += 2

    if sos > ras: 
        print("è una fake news")
    elif sos < ras: 
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