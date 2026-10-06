def distributive():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    print("Distributive law of Multiplication over Addition")
    lhs = a * (b + c)
    rhs = (a * b) + (a * c)
    print("LHS =", lhs)
    print("RHS =", rhs)
    print("Distributive law satisfied" if lhs == rhs else "Distributive law not satisfied")

    print("Distributive law of Addition over Multiplication")
    lhs = a + (b * c)
    rhs = (a + b) * (a + c)
    print("LHS =", lhs)
    print("RHS =", rhs)
    print("Distributive law satisfied" if lhs == rhs else "Distributive law not satisfied")

    print("Distributive law of Boolean AND over OR")
    lhs = a and (b or c)
    rhs = (a and b) or (a and c)
    print("LHS =", lhs)
    print("RHS =", rhs)
    print("Distributive law satisfied" if lhs == rhs else "Distributive law not satisfied")

    print("Distributive law of Boolean OR over AND")
    lhs = a or (b and c)
    rhs = (a or b) and (a or c)
    print("LHS =", lhs)
    print("RHS =", rhs)
    print("Distributive law satisfied" if lhs == rhs else "Distributive law not satisfied")


distributive()