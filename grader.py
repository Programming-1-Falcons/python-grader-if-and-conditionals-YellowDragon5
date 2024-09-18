while True:
    new = int(input("How many assignments?: "))
    pos = int(input("How many points possible?: "))
    for i in range (0, new):
        got = int(input("How many points did they get?: "))
        grade = (got/pos)*100
        if grade>100:
            print("A - Extra credit!")    
        elif grade>=89:
            print("A")
        elif grade<=88 and grade>=76:
            print("B")
        elif grade <=75 and grade>=61:
            print("C")
        elif grade <=60 and grade >=51:
            print("D")
        elif grade<=50:
            print("F")
