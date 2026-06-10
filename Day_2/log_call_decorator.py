def log_call(func):
    def called(*args,**kwargs):
        func(*args,**kwargs)
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}\n")
    return called

@log_call
def name_age(name,age):
    print(f"Name is {name}\nage is {age}")
    print("-------------------------------")

@log_call
def roll_no(roll):
    print(f"roll_no: {roll}")
    print("-------------------------------")

@log_call
def sum(a,b):
    print(f"sum: {a+b}")
    print("-------------------------------")

name_age("aber",20)
roll_no(2)
sum(1,3)
