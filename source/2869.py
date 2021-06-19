'''
높이 V
up A
down B
입력 순서 A B V
d(A-B) >= V stop
day = (V-B)//(A-B)
저녁에 내려감
day = (V-B-1)//(A-B)
'''
def set_input():
    A,B,V = map(int, input().split())
    return A,B,V

def main():
    A,B,V = set_input()
    day = (V-B-1)//(A-B)
    print(day+1)

if __name__ == '__main__':
    main()

