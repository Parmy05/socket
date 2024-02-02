import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
DIM_BUFFER=1024

def ricevi_comandi(sock_service, addr_client):
    print("connessione",addr_client)
    with sock_service as sock_client:
        while True:
            dati=sock_client.recv(DIM_BUFFER).decode()
            
            if not dati:
                break
            
            dati=json.loads(dati)
            primoNumero = dati['primoNumero']
            operazione = dati['operazione']
            secondoNumero = dati['secondoNumero']
            risultato = 0
            
            if operazione == "+":
                risultato = primoNumero + secondoNumero
            elif operazione == "-":
                    risultato = primoNumero - secondoNumero
            elif operazione == "*":
                    risultato = primoNumero * secondoNumero
            elif operazione == "/":
                if secondoNumero != 0:
                    risultato = primoNumero / secondoNumero
                else:
                    risultato = "Impossibile"
            risultato = str(risultato)
            sock_client.sendall(risultato.encode("UTF-8"))
            print("Il risultato è: ",risultato)
        sock_service.close()


def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_listen:
            sock_listen.bind((indirizzo, porta))
            sock_listen.listen()
            ricevi_connessioni(sock_listen)
    except socket.error as errore:
        print(errore)


if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")