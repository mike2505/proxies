import requests
import os

def import_proxies5():
    #Get proxies
    print("Getting socks5 proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt'
    socks = requests.get(url)
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")

def import_proxies4():
    #Get proxies
    print("Getting socks4 proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt'
    socks = requests.get(url)
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")

def import_proxies3():
    #Get proxies
    print("Getting HTTP proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt'
    socks = requests.get(url) 
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")

def import_proxies5_anon():
    #Get proxies
    print("Getting anon socks5 proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt'
    socks = requests.get(url)
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")

def import_proxies4_anon():
    #Get proxies
    print("Getting anon socks4 proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt'
    socks = requests.get(url)
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")

def import_proxies3_anon():
    #Get proxies
    print("Getting anon HTTP proxies")
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt'
    socks = requests.get(url)
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    else:
        pass
    proxies_file = open('./proxies.txt', 'wb')
    proxies_file.write(socks.content)
    proxies_file.close()
    print("Done")


if __name__ == '__main__':
    sck = int(input("Socks5, Socks4 or HTTP? (1/2/3): "))
    if sck == 1: 
        tmp = int(input("Anonymous or no? (1/2): "))
        if tmp == 1: import_proxies5_anon()
        else: import_proxies5()
    elif sck == 2:
        tmp = int(input("Anonymous or no? (1/2): "))
        if tmp == 1: import_proxies4_anon()
        else: import_proxies4()
    elif sck == 3:
        tmp = int(input("Anonymous or no? (1/2): "))
        if tmp == 1: import_proxies3_anon()
        else: import_proxies3()
    else: print("Enter 1, 2 or 3")
