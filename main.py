try:
    print(eval(input()))
except NameError:
    print("invalid value")
except SyntaxError:
    print("invalid value")
