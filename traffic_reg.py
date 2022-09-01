from scapy.all import sendp, sniff, IP, ICMP, conf
import subprocess
import argparse
import time

def main(args):
    # conf.route.delt(host="192.168.60.163", dev="tr0")

    # while True:
    #     # Sleep cycle: store received data to 
    #     buffer = [] 
    #     while 
    while True:
        capt = sniff(iface="tr0", filter="dst host 192.168.60.163", count=1)
        s = time.perf_counter()
        capt[0].dst = "40:a6:b7:41:71:10"
        # capt[0].src = "c8:d7:4a:4e:47:50"   # dummy
        # capt[0].src = "40:a6:b7:41:72:90"   # eth4 on 64
        print(f'MAC SRC: {capt[0].src}, DST: {capt[0].dst}')
        sendp(capt[0], iface="eth4")
        e = time.perf_counter()
        print(f'Time used: {(e-s)*1000}ms')

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Regulate traffic')
    parser.add_argument('--on_duration', type=int, default=20, help='On duration (ms)')
    parser.add_argument('--cycle', type=int, default=40, help='Cycle (ms)')
    args = parser.parse_args()
    assert args.cycle > args.on_duration, "cycle should be larger than on_duration"

    main(args)