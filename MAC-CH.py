#!/usr/bin/env python

import subprocess

print("Actieve interfaces:")
subprocess.call("ip -o link show up | awk -F': ' '{print $2}'", shell=True)

print("\n")

interface = input("Interface: ")
Nieuwe_MAC = input("Nieuwe MAC adres: ")
Oude_MAC = subprocess.check_output(f"ip link show {interface} | awk '/link\\/ether/ {{print $2}}'", shell=True).decode().strip()


subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {Nieuwe_MAC}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

subprocess.call(f"ifconfig {interface}", shell=True)
print(f"[+] MAC adres veranderen voor: interface {interface} van {Oude_MAC} naar {Nieuwe_MAC}")