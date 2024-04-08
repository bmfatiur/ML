x=input("X: ")
y=input("Y: ")
try:
    z=int(x)/int(y)
except TypeError as e:
    # print("type of exception:",type(e).__name__)
    print("Type Error occured")
    z=None

except ZeroDivisionError as e:
    print("Division by zero error")
    z=None

print("Division:",z)