def main():
    x = int(input("What number would you like to go up to: "))
    z = [0] * (x -1) 
    for i in range(x):
        z[i-1] = i + 1
        
    while (len(z) > 0):
        pn = z[0]
        print(pn)
        z.remove(pn)
        
        for i in z:
            if (i % pn == 0):
                z.remove(i)
main()
