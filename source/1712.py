'''
# A : 1000 : 대여 공장비
# B : 70 :인건비
1 대 : 1070만
10 대 : 1700만
노트북 가격 C
# C : 170
A + x * b < x * c 
A < c x - b x
A / (c-b) < x
'''
def set_input():
    data = list(map(int,input().split()))
    return data

def main():
    data = set_input()
    A = data[0]
    B = data[1]
    C = data[2]
    if C == B:
        y = -1
    else:
        y = A // (C-B)

        if y >= 0:
            y = y +1
        else:
            y = -1

    print(y)

if __name__ == '__main__':
    main()

