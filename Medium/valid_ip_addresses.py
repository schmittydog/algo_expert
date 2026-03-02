#!/usr/bin/env python3

def gen_strings(str):
    l = len(str)
    for a in range(1, l-2):
        if a > 3: break
        for b in range(a+1, l-1):
            if b - a > 3: break
            for c in range(b+1, l):
                if c - b > 3: break
                if l - c > 3: continue
                yield f'{str[:a]}.{str[a:b]}.{str[b:c]}.{str[c:]}'
                

def validIPAddresses(string):
    valid_ips = []
    for ip in gen_strings(string):
        octets = ip.split('.')
        valid = True
        for octet in octets:
            if len(octet) > 1 and octet[0] == '0':
                valid = False
                break
            octet_int = int(octet)
            if octet_int > 255:
                valid = False
                break
        if valid:
            valid_ips.append(ip)
    return valid_ips
