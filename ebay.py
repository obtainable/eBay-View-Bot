from colorama import Fore, init, Style
import threading, requests, ctypes, os

class eBay:
    def __init__(self):
        self.sent = 0
        self.errors = 0
    
    def update_title(self):
        ctypes.windll.kernel32.SetConsoleTitleW("eBay View Bot | Sent: {0} | Errors: {1}".format(self.sent, self.errors))

    def session(self):
        session = requests.Session()
        session.trust_env = False
        return session
    
    def view_bot(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36", "X-Forwarded-For": "3.4.5.6"}
        try:
            self.session().get(self.url, headers = headers)
            self.sent += 1
        except:
            self.errors += 1
        self.update_title()
    
    def main(self):
        os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW("eBay View Bot")
        self.url = str(input("\n {0}> {1}{2}URL: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        threads = int(input("\n {0}> {1}{2}Threads: ".format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        def thread_starter():
            self.view_bot()
        while True:
            if threading.active_count() <= threads:
                threading.Thread(target = thread_starter).start()

eBay().main()
