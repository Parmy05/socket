import socket
import json

# Configurazione del server 
IP='127.0.0.1'
PORTA = 65432
DIM_BUFFER = 1024

#Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    #Binding della socket alla porta specificata
    sock_server.bind((IP, PORTA))

    #Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()

    print(f"Server in ascolto su {IP}:{PORTA}...")

    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            while True: 
                data= sock_client.recv(DIM_BUFFER).decode()
                data = json.loads(data)
                primoNumero = data["primoNumero"]
                operazione = data["operazione"]
                secondoNumero = data["secondoNumero"]
                
                risultato = 0
                if not data:
                    break
                if operazione == "+":
                    risultato = primoNumero + secondoNumero
                elif operazione == "-":
                    risultato = primoNumero - secondoNumero
                elif operazione == "+":
                    risultato = primoNumero * secondoNumero
                elif operazione == "/":
                    if secondoNumero != 0:
                        risultato = primoNumero / secondoNumero
                    else:
                        risultato = "Impossibile"
                elif operazione == "%":
                    risultato = primoNumero % secondoNumero
                elif primoNumero == 0:
                    break

                            #Stampa il messaggio ricevuto e invia una risposta al client 
                print(f"Ricevuto messaggio dal client {sock_service}: {data}")
                sock_service.sendall(str(risultato).encode())
                sock_client.close()
                    