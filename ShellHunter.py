import requests
import csv
import sys
import threading
import queue
from datetime import datetime


class colors:
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    end = '\033[0m'


sh = [line.strip()
      for line in open('shell_names.txt', 'r') if line.strip() != '']


def banner():
    print(colors.green + "Coded By ENG Yazeed")
    print(colors.green + " Shell Hunter v1.0")
    print(colors.green + "  github.com/crypticq")
    print(colors.green + " sa.linkedin.com/in/yazeed-alzhrani-23453b169")

    B = r'''
    
    
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬜
    ⬜⬛⬛⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛
    ⬜⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬜⬜⬛⬛⬛⬛⬜⬛⬛⬛
    ⬜⬜⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬜⬛⬛⬜
    ⬛⬛⬛⬜⬛⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜
    ⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜
    ⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    
    '''
    print(colors.red + B + colors.end)


def Shell_search(url, shell_path):
    try:
        r = requests.get(url+"/"+shell_path)
        if r.status_code == 200:
            print(colors.green + "[+] Shell Found: " + colors.end + shell_path)
            results = [{
                "Shell Path": shell_path,
                "URL": url+"/"+shell_path,
                "Status Code": r.status_code,
            }]

            with open("shell_path.csv", "a") as f:
                writer = csv.DictWriter(f, fieldnames=results[0].keys())
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerows(results)

        else:
            print(colors.red + "[-] Shell Not Found: " + colors.end + r.url)
    except Exception as e:
        pass


def main():
    startTime = datetime.now()
    banner()
    if len(sys.argv) != 2:
        print("Usage: python3 shell_hunter.py target")
        print("Example: python3 shell_hunter.py https://www.example.com")
        sys.exit(1)
    url = sys.argv[1]

    if not url.startswith("http") or not url.startswith("https"):
        url = "http://" + url

    def worker():
        while True:
            item = q.get()
            Shell_search(url, item)
            q.task_done()

    q = queue.Queue()

    for i in range(20):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    for item in sh:
        q.put(item)

    q.join()

    def finsih_banner():
        b = r"""
        
        
        zeeeeee-
                    z$$$$$$"
                   d$$$$$$"
                  d$$$$$P
                 d$$$$$P
                $$$$$$"
              .$$$$$$"
             .$$$$$$"
            4$$$$$$$$$$$$$"
           z$$$$$$$$$$$$$"
           """""""3$$$$$"
                 z$$$$P
                d$$$$"
              .$$$$$"
             z$$$$$"
            z$$$$P
           d$$$$$$$$$$"
          *******$$$"
               .$$$"
              .$$"
             4$P"
            z$"
           zP
          z"
         /    Gilo94'
        ^

        """

        print(colors.red + b + colors.end)
        print(colors.green + "[+] Scan Finished in: " +
              colors.end + str(datetime.now() - startTime))

    finsih_banner()


if __name__ == "__main__":
    main()
