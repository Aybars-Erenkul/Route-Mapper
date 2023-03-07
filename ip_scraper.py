from scapy.all import DNS, DNSQR, IP, sr1, UDP
import requests
import bs4
import dns_seeker
import csv

def ip_gatherer(target="default.com"):
    with open("extras.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URI", "IP"])
    if not (target.startswith('http://') or target.startswith('https://')):
        target = 'https://' + target
    print(target)
    res = requests.get(target)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #print(soup)
    results = soup.find_all(href=True)
    urls = list(results)
    #print(urls[0])
    #asd = input('askjfh')
    #test = str(urls[0]).split("=" and '"')
    #print(test)
    #asd = input("skdjfh")
    for url in urls:
        #print(dir(url))
        #print(url)
        #asd = input("skdjfh")
        test = str(url).split('=' and '"')
        #print(test)
        for i in range(len(test)):
            if test[i] == ' href=' or test[i] == '<a href=' or test[i] == '<link href=':
                if '#' not in test[i+1] and target not in test[i+1] and 'linkedin' not in test[i+1] and 'facebook' not in test[i+1] and 'instagram' not in test[i+1] and 'youtube' not in test[i+1] and 'github' not in test[i+1] and 'twitter' not in test[i+1]:
                    test[i+1] = test[i+1].replace('//', '')
                    test[i+1] = test[i+1].replace('http://','')
                    test[i+1] = test[i+1].replace('https://','')
                    test[i+1] = test[i+1].replace('http:','')
                    test[i+1] = test[i+1].replace('https:','')

                    final = test[i+1].split("/")[0]

                    
                    if '.' in final:
                        print(final)
                        got_ips = dns_seeker.seek_dns(final)
                        if got_ips != None:
                            print(got_ips)
                            print("----------------------------------")
                            with open("extras.csv", "a") as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow([final, got_ips])
                            #return got_ips
        #print(test[1])


if __name__ == "__main__":
    ip_gatherer()
