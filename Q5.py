x = int(input("Enter a number of repetitions: "))

def repeat(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper

@repeat
def hello():
    print('Hello')

hello()
