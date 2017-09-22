#!/usr/bin/env python
# coding: utf-8
from urllib import urlopen as AbreUrl
from urllib import urlencode as UrlE
from re import search as b
import sys as s

print'''\033[93m
 _    _             _____ 
| |  | |           / ____|
| |__| |  ______  | |     
|  __  | |______| | |     
| |  | |          | |____ 
|_|  |_|           \_____|

	by Anyone-k

Suporte para hash MD5, SHA1 & SHA2 

      Hash Cracker 
		'''




def ServidorOmega():
    U = UrlE({"hash": hash, "decrypt": "Decrypt"})
    A = AbreUrl("http://md5decrypt.net/en/Sha256/", U)
    f = A.read()
    m = b(r'<b>[^<]*</b><br/><br/>', f)
    if m:
        print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", m.group().split('<b>')[1][:-14]
        s.exit()
    else:
        print "\033[1;31m[]==>\033[1;m Sua hash não foi encontrada na nossa data base."
        s.exit()


def ServidorLambda():
    A = AbreUrl(
        "http://md5decrypt.net/Api/api.php?hash=" + hash + "&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728")
    f = A.read()
    if len(f) > 0:
        print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", f
        s.exit()
    else:
        print "\033[1;31m[]==>\033[1;m Sua hash não foi encontrada na nossa data base."
        s.exit()


def ServidorBeta():
    U = UrlE({"auth": "8272hgt", "hash": hash, "string": "", "Submit": "Submit"})
    A = AbreUrl("http://hashcrack.com/index.php", U)
    f = A.read()
    m = b(r'<span class=hervorheb2>[^<]*</span></div></TD>', f)
    if m:
        print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", m.group().split('hervorheb2>')[1][:-18]
        s.exit()
    else:
        ServidorOmega()


hash = raw_input('\033[97m[]==>Digite a sua hash: \033[1;m').lower()
if len(hash) == 32:
    print "\033[1;33m[]==>Tipo de hash\033[1;m  : MD5"
    U = UrlE({"hash": hash, "submit": "Decrypt It!"})
    A = AbreUrl("http://md5decryption.com", U)
    f = A.read()
    m = b(r"Decrypted Text: </b>[^<]*</font>", f)
    if m:
        print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", m.group().split('b>')[1][:-7]
        s.exit()
    else:
        U = UrlE({"md5": hash, "x": "21", "y": "8"})
        A = AbreUrl("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", U)
        f = A.read()
        m = b(r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", f)
        if m:
            print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", m.group().split('span')[2][3:-6]
            s.exit()
        else:
            url = "http://www.nitrxgen.net/md5db/" + hash
            purl = AbreUrl(url).read()
            if len(purl) > 0:
                print "\n\033[1;32m[]==> Hash crackeada:\033[1;m", purl
                s.exit()
            else:
                print "\033[1;31m[]==>\033[1;m Sua hash não foi encontrada na nossa data base."
                s.exit()
if len(hash) == 40:
    print "\033[1;33mTipo de Hash ==>\033[1;m Hash : SHA1"
    ServidorBeta()
if len(hash) == 64:
    print "\033[1;33mTipo de Hash ==>\033[1;m Hash : SHA-256"
    ServidorLambda()
else:
    print "\033[1;31m[]==>\033[1;m Não temos suporte para esse tipo de hash."

# Servidores usados Alpha, Beta, Gamma, Delta, Omega, Lambda

