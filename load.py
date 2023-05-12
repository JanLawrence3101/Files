import threading
import multiprocessing

class LoadBalancer:
    def __init__(self, initial_load):
        self.lock = multiprocessing.Lock() 
        self.load = initial_load

    def pasaload(self, amount):
        with self.lock:
            if amount <= self.load:
                self.load -= amount
                print(f"{amount} pesos pasaloaded. Remaining load: {self.load} pesos.")
            else:
                print("Error: Not enough load to pasaload.")

def threaded_load_balancer(amount):
    lb = LoadBalancer(100)
    t = threading.Thread(target=lb.pasaload, args=(amount,))
    t.start()

def process_load_balancer(amount):
    lb = LoadBalancer(100)
    p = multiprocessing.Process(target=lb.pasaload, args=(amount,))
    p.start()

def main():
    print("Choose a load amount to pasaload:")
    print("1. 20 pesos")
    print("2. 50 pesos")
    print("3. 100 pesos")
    option = input("Enter your choice (1-3): ")

    if option == "1":
        threaded_load_balancer(20)
    elif option == "2":
        process_load_balancer(50)
    elif option == "3":
        threaded_load_balancer(100)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
