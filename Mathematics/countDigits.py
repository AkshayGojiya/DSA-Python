def countDigs(n):
    count = 0
    while n!= 0:
        n = n // 10
        count += 1
    return count

if __name__ == '__main__':
    n = int(input("Enter the number to count the digits : "))

    a = countDigs(n)
    print("Number of digits in the given number :", a)

    