def divideBy(a, b):
    return a / b

def callDivide():
    try:
        divideBy(40, 0)
    except ZeroDivisionError as e:
        print(e, "we cannot divide by zero")
        print(e.__class__)
    except Exception as e:
        print(e, "something else went wrong")

def callOpen():
    try:
        # Starter code
        with open('file_does_not_exist.txt', 'r') as file:
            print(file.read())
    except:
        print("file could not be found")