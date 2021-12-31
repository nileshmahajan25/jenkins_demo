# Add all elements of list using decorator function

def decor(func):
    def inner(inputNum):
        result = 0
        for val in inputNum:
            result = result + val
        return result

    return inner

@decor
def display(list1):
    print('This is display function!')

list1 = [10, 20, 30]
result = display(list1)

print('Addition of all numbers : ', result)