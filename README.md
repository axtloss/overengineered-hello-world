<p align="center">
  <img src="https://github.com/axtloss/overengenieered-hello-world/blob/main/logo.png?raw=true" alt="Logo" width="150" height="150">
</p>

## overengineered -hello-world
a stupidly overengineered way to print out "Hello world" in python


# How does it work?
___Well___

- First we read the string "Hello World!" from helloworld.png
- then we decode that to utf-8
- after that we get a list of all the printable carachters in python as an array
- we split the "Hello World!" from the image earlier into an array, seperated by each carachter: ["H","e","l","l","o"," ","W,"o","r","l","d","!"]
- then each letter in the array gets the index of the corresponding carachter in the array of all printable carachters, the new array looks like that now:  
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
- We convert this back into Letters, using the same printable carachter index as before, also in an array:
["H","e","l","l","o"," ","W,"o","r","l","d","!"]
- then this array is read into a string
- this string gets printed using the "echo" util from bash with os.system
