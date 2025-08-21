s = "Python"
print(len(s))  

s = "HELLO"
print(s.lower())   

s = "hello"
print(s.upper())  

s = "python programming"
print(s.title())   

s = "python"
print(s.capitalize())  

s = "   hello   "
print(s.strip())  

s = "I love Java"
print(s.replace("Java", "Python"))   

s = "apple,banana,cherry"
print(s.split(","))   # ['apple', 'banana', 'cherry']

words = ["Python", "is", "fun"]
print(" ".join(words))   

s = "hello world"
print(s.find("world"))   

s = "banana"
print(s.count("a"))   

s = "banana"
print(s.count("a"))   

s = "Python Programming"
print(s.startswith("Py"))   
print(s.endswith("ing"))    

s1 = "123"
s2 = "Python"
s3 = "Python123"

print(s1.isdigit())   
print(s2.isalpha())   
print(s3.isalnum())   

s = "PyThOn"
print(s.swapcase())   

s = "42"
print(s.zfill(5))   

s = "Python"
print(s.center(10, "*"))   

s = "Hi"
print(s.ljust(6, "-"))  

s = "Hi"
print(s.rjust(6, "-"))  

s = "I love Python"
print(s.partition("love"))   

s = "apple banana apple"
print(s.rpartition("apple"))   

s = "Hello\nWorld\nPython"
print(s.splitlines())   

s = "Name\tAge\tCity"
print(s.expandtabs(8))

s = "Python"
print(s.encode())   

print("Python".isascii())  
print("Py❤".isascii())      

print("Python Programming".istitle())  
print("python programming".istitle())   

print("name".isidentifier())    
print("123abc".isidentifier())  

s1 = "PYTHON"
s2 = "ß"
print(s1.casefold())   
print(s2.casefold())   

name = "Ameesha"
age = 21
print("My name is {} and I am {} years old".format(name, age))

data = {"name": "ameesha", "age": 20}
print("My name is {name}, age {age}".format_map(data))

txt = "hello"
trans = txt.maketrans("h", "j")
print(txt.translate(trans))   








