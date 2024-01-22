from socket import *

def connectionScan(targetHost, targetPort):
    try:
        connectionskt = socket(AF_INET, SOCK_STREAM)
        connectionskt.connect((targetHost, targetPort))
        print("[+]%d/tcp open"% targetPort)
        connectionskt.close()
    except:
        print("[-]%d/tcp closed"% targetPort)


if __name__ == '__main__':
    connectionScan("172.217.31.174", 22)