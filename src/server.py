
import socket
import requests

HOST = '127.0.0.1'  
ACCESS_TOKEN = 'dd1fdad235274ef7b54ebe454c910a6c'
PROJECT_ID = "gdgtest-c33ac"

PORT = 1999     
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Launching server...")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = requests.post('https://api.dialogflow.com/v1/query',
                json = {
                    "context":["web-search"],
                    "lang": "en",
                    "query": str(data),
                    "sessionId": "12345",
                    "timezone": "America/New_York",
                    "v":"20150910"
                },
            headers={"Authorization":"Bearer " + ACCESS_TOKEN, "Content-Type":"application/json" })
            print(response.json())
            if response.json()["result"]["fulfillment"]["messages"][0]["speech"] == "":
                conn.sendall(str.encode("No Response"))
            conn.sendall( str.encode(str(response.json()["result"]["fulfillment"]["messages"][0]["speech"])))