from scapy.all import sendp, sniff, IP, ICMP, conf
import subprocess
import argparse

def main(args):
    conf.route.delt(host="192.168.1.19", dev="tr0")

    # while True:
    #     # Sleep cycle: store received data to 
    #     buffer = [] 
    #     while 
    while True:
        capt = sniff(filter="dst host 192.168.1.19", count=1)
        capt[0].dst = "1e:57:dc:e3:82:64"
        # capt[0].src = "c8:d7:4a:4e:47:50"   # dummy
        # capt[0].src = "52:54:00:5e:11:0a"   # lo
        print(f'MAC SRC: {capt[0].src}, DST: {capt[0].dst}')
        sendp(capt[0])

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Regulate traffic')
    parser.add_argument('--on_duration', type=int, default=20, help='On duration (ms)')
    parser.add_argument('--cycle', type=int, default=40, help='Cycle (ms)')
    args = parser.parse_args()
    assert args.cycle > args.on_duration, "cycle should be larger than on_duration"

    main(args)