
def print_name():
    print("Harshit")

print_name()

def print_name(a):
    print(f'Hello ,{a}')

print_name("Harshit")

print_name("Ankit")

def multi_arg(*arg):
    print(arg)

multi_arg(1,2,3)

def add(a,b,c):
    return a+b+c

add(1,3,1)

def student(**info):
    for key, value in info.items():
        print(key,":", value)
        
