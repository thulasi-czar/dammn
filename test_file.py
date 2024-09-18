name = "thulasi"



import threading

def run():
    for _ in range(10):
        print("th")

threadOne = threading.Thread(target=run)
threadOne.start()#this is new line
