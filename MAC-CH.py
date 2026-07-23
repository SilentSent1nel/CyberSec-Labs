#!/usr/bin/env python

import subprocess

print("Actieve interfaces:")
subprocess.call("ip -o link show up | awk -F': ' '{print $2}'", shell=True)

print("\n")

interface = input("Interface: ")
Nieuwe_MAC = input("Nieuwe MAC adres: ")
print("\n")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", Nieuwe_MAC])
subprocess.call(["ifconfig", interface, "up"])

print(f"[+] MAC adres veranderen voor: interface {interface} naar {Nieuwe_MAC} - :")
subprocess.call(["ifconfig", interface])