import socket
import json

HOST='127.0.0.1' # Indirizzo del server
PORT=65432 #Porta usata dal server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service: 
    sock_service.connect((HOST,PORT))
    while True:
        primoNumero = float(input("Insenisci il primo numero: "))
        operazione = input("Inserisci l'operazione(simbolo)")
        secondoNumero = float(input("Inserisci il secondo numero: "))
        if(operazione==0):
            break
        messaggio = {"primoNumero" : primoNumero,
                    "operazione" : operazione,
                    "secondoNumero" : secondoNumero}
        messaggio = json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))

        data = sock_service.recv(1024)
        print("Risultato: ", data.decode())