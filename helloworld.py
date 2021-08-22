#!/usr/bin/python
import os

def split_str(s):
    return [ch for ch in s]

def main():
    alphabet=[chr(i) for i in range(128)]
    output=split_str("Hello World")
    x=0
    y=0
    string=""
    alphabetnumber=[]
    while y != len(alphabet):
        if alphabet[y] == output[x]:
            alphabetnumber.append(y)
            x=x+1
            print(alphabetnumber)
            y=0
        else:
            y=y+1
        if x >= len(output):
            break
    x=0
    print(alphabetnumber)
    while x != len(alphabetnumber):
        string=string+alphabet[alphabetnumber[x]]
        x=x+1
    _= "os.system('echo '+string)"
    eval(_)

if __name__ == '__main__':
    main()
