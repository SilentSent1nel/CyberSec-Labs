#!/usr/bin/env python

import subprocess
import optparse

def mac_wijzigen(interface, Nieuwe_MAC):
    print("\n")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", Nieuwe_MAC])
    subprocess.call(["ifconfig", interface, "up"])

    print(f"[+] MAC adres veranderen voor: interface {interface} naar {Nieuwe_MAC} - :")
    subprocess.call(["ifconfig", interface])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface waarvan de MAC-Adres wordt gewijzigd")
parser.add_option("-m", "--mac-adres", dest="Nieuwe_MAC", help="Dit wordt de nieuwe MAC-Adres dat gebuikt gaat worden")

(options, arguments) = parser.parse_args()

print("Actieve interfaces:")
subprocess.call("ip -o link show up | awk -F': ' '{print $2}'", shell=True)

mac_wijzigen(options.interface, options.Nieuwe_MAC)