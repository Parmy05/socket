import socket

HOST = "127.0.0.1"  # Indirizzo del server
PORT = 22017      # Porta usata dal server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
  sock_service.connect((HOST, PORT))
  x = input("dati: (0 uscita)")
  sock_service.sendall(x.encode()) # invio direttamente in formato byte
  data = sock_service.recv(1024) # il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sola volla

#a questo punto la socket è stata chiusa automaticamente
print('Received', data.decode())