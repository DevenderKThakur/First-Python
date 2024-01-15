def pattern1(n):
    for row in range (n):
        for col in range (n):
            print ("*",end="")
        print ("\r")

# pattern1(4)

def pattern2(n):
    for row in range(1,n+1):
        for col in range (1,row+1):
            print ("*",end="")
        print ("\r")

# pattern2(4)
        
def pattern3(n):
    for row in range(n):
        for col in range (n-row):
            print ("*",end="")
        print ("\r")

# pattern3(5)

def pattern4(n):
    for row in range(n):
        for col in range (0,row+1):
            print (col+1,end="")
        print("\r")

# pattern4(5)
        
def pattern5(n):
    for row in range(2*n):
        totalColinRow = 2 * n - row if row >= n else row 
        for col in range (totalColinRow):
            print ("*",end="")
        print("\r")

# pattern5(5)
        
def pattern28(n):
    for row in range (2*n):
        totalColinRow = 2 * n - row if row > n else row 
        totalSpace = n - totalColinRow
        for space in range (totalSpace):
            print (end=" ")
        for col in range (totalColinRow):
            print("*",end="")
        print("\r")

pattern28(5)

