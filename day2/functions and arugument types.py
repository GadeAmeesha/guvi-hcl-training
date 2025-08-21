def fun_name():
    print("Hello World")


def intro(name, age):
    print("My name is", name, "and age is", age)

intro("Ameesha", 21)   # My name is Ameesha and age is 21


def intro(name, age=18):
    print("My name is", name, "and age is", age)

intro("Sree")      # My name is Sree and age is 18
intro("Ameesha", 21)  # My name is Ameesha and age is 21


def intro(name, age):
    print("My name is", name, "and age is", age)

intro(age=22, name="Ameesha")  # order change chesina panikivastundi


def fun(*names):
    for n in names:
        print("Hi", n)

fun("Abi", "Darshan", "Mugin")  
# Hi Abi, Hi Darshan, Hi Mugin


def fun(**data):
    print(data)
    print(type(data))

fun(name="Sree", age=22)
# {'name': 'Sree', 'age': 22}
# <class 'dict'>

def fun():
    x = 10   # local variable
    print("Inside function:", x)

fun()
# print(x)   # Error! x is not defined outside


name = "SIC"   # global variable

def fun_name():
    global name
    name = "AK"   # override chestundi
    print("Hi this is", name)

fun_name()
print("Outside:", name)
# Output:
# Hi this is AK
# Outside: AK


def fun_name(name):
    print("Hi this is", name)

lst = ["abi", "darshan", "mugin"]

for i in lst:
    fun_name(i)

# Output:
# Hi this is abi
# Hi this is darshan
# Hi this is mugin
