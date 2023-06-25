def ASS1():
    f = open("practice.txt", "r")
    c = 0
    p = f.read()
    for K in p.split():
        if K.upper() == "ZERO":
            c = c + 1
    print(c)
    f.close()

def ASS2():
    f = open("practice.txt", "r")
    p = f.read()
    for Line in p.split("\n"):
        c = 0
        for cha in Line:
            if cha.upper() in "AEIOU":
                c = c + 1
        print(c)
    f.close()

def ASS3():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for Line in p.split("\n"):
        if len(Line) > 20:
            print(Line)
            c = c + 1
    print(c)
    f.close()

def ASS4():
    f = open("practice.txt", "r")
    p = f.read()
    L = []
    for w in p.split():
        if len(w) > 3 or w[0].upper() == "A":
            L.append(w)
    print(L)
    f.close()

def ASS5():
    f = open("practice.txt", "r")
    g = open("output.txt", "w")
    p = f.read()
    for Line in p.split("\n"):
        g.write(Line[::-1] + "\n")
    f.close()
    g.close()

def ASS6():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for I in p:
        if I in "+-*/":
            c = c + 1
    print(c)
    f.close()

def ASS7():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for Line in p.split("\n"):
        if Line[0].upper() in "AEIOU" and Line[-2].upper() in "AEIOU":
            c = c + 1
    print(c)
    f.close()

def ASS8():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for Line in p.split("\n"):
        if Line[0].upper() == "I" or Line[0].upper() == "M":
            c = c + 1
    print(c)
    f.close()

def ASS9():
    f = open("practice.txt", "r")
    p = f.read()
    for w in p.split():
        if len(w) < 4:
            print(w)
    f.close()

def ASS10():
    f = open("practice.txt", "r")
    p = f.read()
    L = 0
    W = ""
    for Line in p.split("\n"):
        if len(Line) > L:
            L = len(Line)
            W = Line
    print(W)
    f.close()

def ASS11():
    f = open("practice.txt", "r")
    p = f.read()
    S = 0
    for I in p:
        if I.isdigit():
            S = S + int(I)
    print(S)
    f.close()

def ASS12():
    f = open("practice.txt", "r")
    p = f.read()
    for Line in p.split("\n"):
        if "ke" not in Line.lower():
            print(Line)
    f.close()

def ASS13():
    f = open("practice.txt", "r")
    p = f.read()
    L = []
    for w in p.split():
        if "S" in w.upper():
            L.append(w)
    print(L)
    f.close()

def ASS14():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for Line in p.split("\n"):
        if Line[0].upper() == Line[-2].upper():
                c = c + 1
    print(c)
    f.close()

def ASS15():
    f = open("practice.txt", "r")
    p = f.read()
    for I in p:
        if I == "k":
            print("c")
        elif I == "K":
            print("C")
        else:
            print(I)
    f.close()

def ASS16():
    f = open("practice.txt", "r")
    p = f.readlines()
    for Line in p:
        s = Line.split()
        if s[0].upper() == "IN":
            print(Line)
    f.close()

def ASS17():
    f = open("practice.txt", "r")
    p = f.read()
    c = 0
    for I in p:
        if I.upper() in "AEIOU":
            c = c + 1
    print(c)
    f.close()

import os
def ASS18():
    f = open("output.txt", "r")
    g = open("temp.txt", "w")
    p = f.read()
    for Line in p.split("\n"):
        g.write(Line[::-1] + "\n")
    f.close()
    g.close()
    os.remove("output.txt")
    os.rename("temp.txt", "output.txt")

def ASS19():
    f = open("output.txt", "r")
    g = open("temp.txt", "w")
    for Line in f.readlines():
        if Line[0] != "#":
            g.write(Line)
    f.close()
    g.close()
    os.remove("output.txt")
    os.rename("temp.txt", "output.txt")

def ASS20():
    f = open("output.txt", "r")
    g = open("temp.txt", "w")
    p = f.readlines()
    for Line in p:
        for w in Line.split():
            if len(w) != 3:
                g.write(w + " ")
        g.write("\n")
    f.close()
    g.close()
    os.remove("output.txt")
    os.rename("temp.txt", "output.txt")

def ASS21():
    f = open("output.txt", "r")
    g = open("temp.txt", "w")
    p = f.read()
    for w in p:
        if w.isalnum() == True or w.isspace() == True:
            g.write(w)
    f.close()
    g.close()
    os.remove("output.txt")
    os.rename("temp.txt", "output.txt")

ASS1()
ASS2()
ASS3()
ASS4()
ASS5()
ASS6()
ASS7()
ASS8()
ASS9()
ASS10()
ASS11()
ASS12()
ASS13()
ASS14()
ASS15()
ASS16()
ASS17()
ASS18()
ASS19()
ASS20()
ASS21()
