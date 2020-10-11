from colorama import Fore, init, Style
import threading, requests, ctypes, os

class eBay:
    def __init__(self):
        self.session = requests.Session()
        self.session.trust_env = False
        self.sent = 0
        self.errors = 0
    
    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW('eBay View Bot | Sent: {0} | Errors: {1}'.format(self.sent, self.errors))

    def view(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'X-Forwarded-For': '3.4.5.6'
        }
        try:
            self.session.get(self.url, headers = headers)
            self.sent += 1
        except:
            self.errors += 1
        self.title()
    
    def main(self):
        os.system('cls'); ctypes.windll.kernel32.SetConsoleTitleW('eBay View Bot')
        self.url = str(input('\n {0}> {1}{2}URL: '.format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.threads = int(input('\n {0}> {1}{2}Threads: '.format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        def my_function():
            self.view()
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target = my_function).start()

eBay().main()