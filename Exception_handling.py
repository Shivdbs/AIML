try:
    x=int(input("enter x: "))
    ans=10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

else:
    print(f"answer is {ans}")

finally:
    print("End of the program")
    