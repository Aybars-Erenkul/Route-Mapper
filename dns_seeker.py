from scapy.all import DNS, DNSQR, IP, sr1, UDP

def seek_dns(target, finalResult=' '):
    if (target.startswith('http://') or target.startswith('https://')):
        target = target.replace("http://", '')
        target = target.replace("https://", '')
    if target.startswith('www.'):
        target = target.replace("www.", '')
    target = target.split('/')[0]

    try:
        
        #print("now printing", target)

        dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname = target))
        answer = sr1(dns_req, verbose=0)
        result = str(answer[DNS].summary())
        #print(result)
        result = result.split('"')[1::2]
        result = result[0]
        if "b'" in result:
            #print("FOUND 'b in ", result)
            result = result.split("'")[1]
            result = result[:-1]
            deeper = seek_dns(result)
        #print(result)
        else:
            #print("NO 'b in", result)
            finalResult = result
            #print("Returning ",finalResult)
            return finalResult
        return deeper
    except:
        print("Error")
        return
    

if __name__ == "__main__":
    res = seek_dns("")
    print(res)
