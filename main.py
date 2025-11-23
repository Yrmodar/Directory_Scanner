import requests
import sys
from tqdm import tqdm


def check_url():
    if sys.argv[1]=="-h":            
        print(Yellow + "USAGE: python main.py <url>" + Reset)
        sys.exit()
    else:
        url=sys.argv[1]
        return url

Green="\x1b[32m"
Red="\x1b[31m"
Yellow="\x1b[33m"
Reset="\x1b[0m"
 
print("""                                                                                                                           
████▄  ▄▄ ▄▄▄▄     ▄▄▄▄  ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄  ▄▄ ▄▄▄▄▄ ▄▄▄▄  
██  ██ ██ ██▄█▄   ███▄▄ ██▀▀▀ ██▀██ ███▄██ ███▄██ ██▄▄  ██▄█▄ 
████▀  ██ ██ ██   ▄▄██▀ ▀████ ██▀██ ██ ▀██ ██ ▀██ ██▄▄▄ ██ ██ 
                                                                                                                     
       """)

url=check_url()

found_dir=0
with open("list.txt","r") as file:
   lines=file.readlines()

   for dir in tqdm(lines, desc="Scanning url",total=len(lines)):
        new_url=url + dir.strip()
        try:
            respond=requests.get(new_url)
            if 200<=respond.status_code<300:
                found_dir+=1
                tqdm.write(Green + new_url + Reset)
            else:
                tqdm.write(Red + new_url + Reset)
        except requests.exceptions.RequestException as e:
            print("\nError fetching website")
            break

print(Yellow + str(found_dir) + " url found" + Reset)
