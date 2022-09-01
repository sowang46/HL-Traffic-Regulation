from scapy.all import sendp, sniff, IP, ICMP, ls, conf

def main():
    conf.route.delt(host="192.168.1.19", dev="tr0")

    while True:
        capt = sniff(iface="enp0s1", filter="src host 192.168.1.19", count=1)
        capt[0].src = "1e:57:dc:e3:82:64"
        capt[0].dst = "c8:d7:4a:4e:47:50"   # dummy
        sendp(capt[0], iface="tr0")

if __name__=="__main__":
    main()