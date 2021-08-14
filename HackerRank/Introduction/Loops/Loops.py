if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i**2)
    
    #another Solution
    #print(*[number**2 for number in range(n)], sep = "\n")

