def main():
    s = str(input())
    a = s.split()
    for i in range(len(a)):
        x = a[i]
        a[i] = x.capitalize()
    n = a[0]
    for i in range(1,len(a)):
        n += a[i]
    print(n)
main()
