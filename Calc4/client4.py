import socket, sys, random, os, time, threading, multiprocessing,json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15

def genera_richieste(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        start_time_thread = time.time()
        sock_service.connect((SERVER_ADDRESS,SERVER_PORT))
        v = ["+","-","*","/"]
        primoNumero = random.randint(0,10)
        operazione = random.randint(0,3)
        secondoNumero = random.randint(0,10) 
        messaggio = {"primoNumero" : primoNumero,
                    "operazione" : v[operazione],
                    "secondoNumero" : secondoNumero}
        messaggio = json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        end_time_thread = time.time()
        data = sock_service.recv(1024)
        print("risultato = ", data.decode())
        print(f"{threading.current_thread().name} execution time = ", end_time_thread - start_time_thread)
        

if __name__== '__main__':
    start_time = time.time()
    threads = [threading.Thread(target = genera_richieste,args = (SERVER_ADDRESS, SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    
    print("Total threads time =", end_time - start_time)
