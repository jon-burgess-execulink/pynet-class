#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
import re

cisco_cfg = CiscoConfParse("cisco-config-assignment1.txt")

crypto_cfg = cisco_cfg.find_objects(r"^crypto map")


print "All Crypto Maps:\n"

for i in crypto_cfg:
    print i.text
    for j in i.children:
        print j.text


print "\n\nCrypto maps using PFS Group 2:\n"
group2 = cisco_cfg.find_objects_w_child(r"^crypto map", r"pfs group2")
for i in group2:
    print i.text
    for j in i.children:
        print j.text
    
    
print "\n\nCrypto maps not using AES:\n"
not_aes = cisco_cfg.find_objects_wo_child(r"^crypto map", r"AES-SHA")
for i in not_aes:
    for j in i.children:
        if 'transform' in j.text:
            print i.text
            print j.text

