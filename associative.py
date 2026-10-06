def associative():
    print("Associative Law for Addition")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a + (b + c)
    rhs = (a + b) + c

    if rhs == lhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")

    print("\nAssociative Law for Multiplication")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a * (b * c)
    rhs = (a * b) * c

    if lhs == rhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")

    print("\nAssociative Law for Boolean Operations")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a and (b and c)
    rhs = (a and b) and c

    if lhs == rhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


associative()