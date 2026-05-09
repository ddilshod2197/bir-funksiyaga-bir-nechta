def dekorator1(func):
    def wrapper():
        print("Dekorator 1 ishlayapti")
        func()
    return wrapper

def dekorator2(func):
    def wrapper():
        print("Dekorator 2 ishlayapti")
        func()
    return wrapper

def dekorator3(func):
    def wrapper():
        print("Dekorator 3 ishlayapti")
        func()
    return wrapper

@dekorator1
@dekorator2
@dekorator3
def funksiya():
    print("Funksiya ishlayapti")

funksiya()
```

Natija:
```
Dekorator 3 ishlayapti
Dekorator 2 ishlayapti
Dekorator 1 ishlayapti
Funksiya ishlayapti
