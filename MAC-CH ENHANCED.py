#!/usr/bin/env python

import subprocess
import optparse
from colorama import Fore, Back, Style

def argumenten_ophalen():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface waarvan de MAC-Adres wordt gewijzigd")
    parser.add_option("-m", "--mac-adres", dest="Nieuwe_MAC", help="Dit wordt de nieuwe MAC-Adres dat gebuikt gaat worden")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Voer een interface in, gebruik -h of --help voor meer info")
    elif not options.Nieuwe_MAC:
        parser.error("[-] Voer een nieuwe MAC adres in, gebruik -h of --help voor meer info")
    return options

    print("Actieve interfaces:")
    subprocess.call("ip -o link show up | awk -F': ' '{print $2}'", shell=True)


def mac_wijzigen(interface, Nieuwe_MAC):
    print("\n")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", Nieuwe_MAC])
    subprocess.call(["ifconfig", interface, "up"])

    print(f"{Fore.LIGHTWHITE_EX} [+] MAC adres veranderen voor: interface {Fore.LIGHTRED_EX}{interface}{Style.RESET_ALL} {Fore.LIGHTWHITE_EX} naar: {Fore.LIGHTYELLOW_EX}{Nieuwe_MAC}{Style.RESET_ALL}")
    print(Fore.LIGHTGREEN_EX)
    subprocess.call(["ifconfig", interface])



options = argumenten_ophalen()
mac_wijzigen(options.interface, options.Nieuwe_MAC)