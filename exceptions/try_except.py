try:
    number = float(input('enter a number: '))
    inverse = 1 / number
    print(inverse)
except ValueError:
    print('must enter a number')
except ZeroDivisionError:
    print('number must be non-zero')
except:
    print('an error occurred')