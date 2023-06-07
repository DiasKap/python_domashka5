def power(nummer,grad):
    if grad ==0:
        return 1
    elif grad % 2 ==0:
        return power(nummer,grad//2)**2
    else:
        return nummer*power(nummer,grad-1)

nummer = int(input("Enter number: "))
grad = int(input("Enter degree: "))
print(f"Degree {grad} of number {nummer} is {power(nummer,grad)}")