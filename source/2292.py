'''
# 벌집 문제
# 1 7 19 37 61
   6 12 18 24

# y = a*6 (간격) (시그마 합)
'''
def set_input():
    number = int(input())
    return number

def main():
    number = set_input()
    sig = 1
    step = 0
    while True:
        sig += step*6
        if number < sig + 1:
            break
        step += 1
    print(step+1) 
if __name__ == '__main__':
    main()

