# def add(val1,val2):
#     return val1 + val2

# def sub(val1,val2):
#     return val1 - val2

#*args **kwargs -> *args - arguement and **kwargs - Key arguement

def add2(*args):
    return args[0] + args[1] + args[2]


def sub2(**kwargs):
    val1 = kwargs['val1']
    val2 = kwargs['val2']
    val3 = kwargs['val3']

    return val1 - val2 - val3

if __name__ == "__main__":
    # sum = add2(1,2,3)
    # print("The Sum is: " + str(sum))
    # print (f"The sum is {sum}" )

    diff = sub2(val1 = 1, val2 = 2, val3 = 3)
    print(f"The difference is {diff}")

