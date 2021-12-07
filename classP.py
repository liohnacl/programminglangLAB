# class Dog:

#     def eat():
#         return "Eating..."

#     def bark():
#         return "Barking..."

#     def run():
#         return"Running..."

#     def sleep():
#         return"Sleeping..."


# if __name__ == "__main__":
    
#     dg = Dog
#     action = dg.eat()
#     print (action)

class Dog:

    def eat(**kwargs):
        return "Eating..." + kwargs["name"]

    def bark():
        return "Barking..."

    def run():
        return"Running..."

    def sleep():
        return"Sleeping..."


if __name__ == "__main__":
    
    dg = Dog
    action = dg.eat(name = "Saver")
    print (action)

class Cat:# class name

    def eat(**kwargs): #Functions
        return "Eating..." + kwargs["name"]

    def bark():
        return "Barking..."

    def run():
        return"Running..."

    def sleep():
        return"Sleeping..."


if __name__ == "__main__":
    
    ct = Cat # Class instance
    action2 = ct.eat(name = "Tom") 
    print (action2)