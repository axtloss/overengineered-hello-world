#!/usr/bin/python
import os
import mmap

def split_str(s):
    return [ch for ch in s]

def fetch_decrypt():
    with open("helloworld.png", "r+b") as f:
        mm = mmap.mmap(f.fileno(),0)
        mm.seek(mm.find(b"Hello World!",0))
        helloworld=mm.read(12)
        print(helloworld)
        mm.close
        return helloworld.decode("utf-8")

def main():
    helloworld=fetch_decrypt()
    alphabet=[chr(i) for i in range(128)]
    output=split_str(helloworld)
    x=0
    y=0
    string=""
    alphabetnumber=[]
    while y != len(alphabet):
        if alphabet[y] == output[x]:
            alphabetnumber.append(y)
            x=x+1
            #print(alphabetnumber)
            y=0
        else:
            y=y+1
        if x >= len(output):
            break
    print(alphabet)
    print(output)
    x=0
    print(alphabetnumber)
    while x != len(alphabetnumber):
        string=string+alphabet[alphabetnumber[x]]
        x=x+1
    _= "os.system('echo '+string)"
    eval(_)

if __name__ == '__main__':
    main()
