from socket import *

def connectionScan(targetHost, targetPort):
    try:
        connectionskt = socket(AF_INET, SOCK_STREAM)
        connectionskt.connect((targetHost, targetPort))
        print("[+]%d/tcp open"% targetPort)
        connectionskt.close()
    except:
        print("[-]%d/tcp closed"% targetPort)

def allPortScan(targetHost):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("[-] Cannot resolve %s"% targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print("\n[+] Scan result of: %s"% targetName[0])
    except:
        print("\n[+] Scan result of: %s"% targetIP)
    setdefaulttimeout(1)
    for targetPort in range(1, 1025):
        print("Scanning Port: %d"% targetPort)
        connectionScan(targetHost, targetPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("[-] Cannot resolve %s"% targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print("\n[+] Scan result of: %s"% targetName[0])
    except:
        print("\n[+] Scan result of: %s"% targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print("Scanning Port: %d"% targetPort)
        connectionScan(targetHost, int(targetPort))


if __name__ == '__main__':
    portScan("google.com", [80, 22])