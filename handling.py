def ASS1(): # Counts the frequency of the word "Zero" in the file
    f = open("practice.txt", "r") # File is opened to perform operations
    c = 0
    p = f.read() # It gives whole content of the file
    for K in p.split(): # It helps to give access to each word
        if K.upper() == "ZERO":
            c = c + 1
    print(c)
    f.close() # File is closed

def ASS2():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for Line in p.split("\n"): # It helps to give access to each line
        c = 0
        for cha in Line: # It helps to give access to each character
            if cha.upper() in "AEIOU":
                c = c + 1
        print(c)
    f.close() # File is closed

def ASS3():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for Line in p.split("\n"): # It helps to give access to each line
        if len(Line) > 20:
            print(Line)
            c = c + 1
    print(c)
    f.close() # File is closed

def ASS4():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    L = []
    for w in p.split(): # It helps to give access to each word
        if len(w) > 3 or w[0].upper() == "A":
            L.append(w)
    print(L)
    f.close() # File is closed

def ASS5():
    f = open("practice.txt", "r") # File is opened to perform operations
    g = open("output.txt", "w") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for Line in p.split("\n"): # It helps to give access to each line
        g.write(Line[::-1] + "\n")
    f.close()
    g.close() # File is closed

def ASS6():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for I in p:
        if I in "+-*/":
            c = c + 1
    print(c)
    f.close() # File is closed

def ASS7():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for Line in p.split("\n"): # It helps to give access to each line
        if Line[0].upper() in "AEIOU" and Line[-2].upper() in "AEIOU":
            c = c + 1
    print(c)
    f.close() # File is closed

def ASS8():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for Line in p.split("\n"): # It helps to give access to each line
        if Line[0].upper() == "I" or Line[0].upper() == "M":
            c = c + 1
    print(c)
    f.close() # File is closed

def ASS9():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for w in p.split(): # It helps to give access to each word
        if len(w) < 4:
            print(w)
    f.close() # File is closed

def ASS10():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    L = 0
    W = ""
    for Line in p.split("\n"): # It helps to give access to each line
        if len(Line) > L:
            L = len(Line)
            W = Line
    print(W)
    f.close() # File is closed

def ASS11():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    S = 0
    for I in p:
        if I.isdigit():
            S = S + int(I)
    print(S)
    f.close() # File is closed

def ASS12():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for Line in p.split("\n"): # It helps to give access to each line
        if "ke" not in Line.lower():
            print(Line)
    f.close() # File is closed

def ASS13():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    L = []
    for w in p.split(): # It helps to give access to each word
        if "S" in w.upper():
            L.append(w)
    print(L)
    f.close() # File is closed

def ASS14():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for Line in p.split("\n"): # It helps to give access to each line
        if Line[0].upper() == Line[-2].upper():
                c = c + 1
    print(c)
    f.close() # File is closed

def ASS15():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for I in p:
        if I == "k":
            print("c")
        elif I == "K":
            print("C")
        else:
            print(I)
    f.close() # File is closed

def ASS16():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.readlines() # Returns a list of all the lines in the file
    for Line in p:
        s = Line.split() # It helps to give access to each word
        if s[0].upper() == "IN":
            print(Line)
    f.close() # File is closed

def ASS17():
    f = open("practice.txt", "r") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    c = 0
    for I in p:
        if I.upper() in "AEIOU":
            c = c + 1
    print(c)
    f.close() # File is closed

import os # Operating System Module
def ASS18():
    f = open("output.txt", "r") # File is opened to perform operations
    g = open("temp.txt", "w") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for Line in p.split("\n"): # It helps to give access to each line
        g.write(Line[::-1] + "\n")
    f.close() # File is closed
    g.close() # File is closed
    os.remove("output.txt") # It removes the file for secondary storage
    os.rename("temp.txt", "output.txt") # It renames a file

def ASS19():
    f = open("output.txt", "r") # File is opened to perform operations
    g = open("temp.txt", "w") # File is opened to perform operations
    for Line in f.readlines(): # Returns a list of all the lines in the file
        if Line[0] != "#":
            g.write(Line)
    f.close() # File is closed
    g.close() # File is closed
    os.remove("output.txt") # It removes the file for secondary storage
    os.rename("temp.txt", "output.txt") # It renames a file

def ASS20():
    f = open("output.txt", "r") # File is opened to perform operations
    g = open("temp.txt", "w") # File is opened to perform operations
    p = f.readlines() # Returns a list of all the lines in the file
    for Line in p:
        for w in Line.split():
            if len(w) != 3:
                g.write(w + " ")
        g.write("\n")
    f.close() # File is closed
    g.close() # File is closed
    os.remove("output.txt") # It removes the file for secondary storage
    os.rename("temp.txt", "output.txt") # It renames a file

def ASS21():
    f = open("output.txt", "r") # File is opened to perform operations
    g = open("temp.txt", "w") # File is opened to perform operations
    p = f.read() # It gives whole content of the file
    for w in p:
        if w.isalnum() == True or w.isspace() == True:
            g.write(w)
    f.close() # File is closed
    g.close() # File is closed
    os.remove("output.txt") # It removes the file for secondary storage
    os.rename("temp.txt", "output.txt") # It renames a file

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
ASS11() # Calling the functions
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
