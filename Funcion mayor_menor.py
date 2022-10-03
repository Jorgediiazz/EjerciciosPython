def mayor_menor(a,b):   
    if(a>b):
        print(a, "es mayor que", b)
    else:
        print(b, "es mayor que ", a)
    
def mayor_menor_3(a,b,c):
    if(a>b):
        if(a>c):
            print(a, "es el mayor")
        if(b>c):
            print(c, "es el menor")
        else:
            print(b, "es el menor")
    if(b>a):
        if(b>c):
            print(b, "es el mayor")
        if(a>c):
            print(c, "es el menor")
        else:
            print(a, "es el menor")
    if(c>a):
        if(c>b):
            print(c, "es el mayor")
        if(a>b):
            print(b, "es el menor")
        else:
            print(a, "es el menor")
    
    


