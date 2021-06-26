def set_input():
    size = int(input())
    ks = []
    ns = []
    for _ in range(size):
        k = int(input())
        n = int(input())
        ks.append(k)
        ns.append(n)

    return ks,ns

def main():
    ks,ns = set_input()
    result = 0
    for k, n in zip(ks,ns):
        result = [x for x in range(1,n+1)]
        for _ in range(k):
            for j in range(1,n):
                result[j] += result[j-1]
        print(result[-1])

if __name__ == '__main__':
    main()

