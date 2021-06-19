'''
# 분수문제
# 대각선 와리가리
# 
1 / 2 3 / 4 5 6 / 7 8 9 10 / 11 12 13 14 15
1 2 3 4 5 6 7 8 9 ....
#내려간다 / 올라간다 = 홀짝
걍 수열을 트리로 보여준거
'''
def set_input():
    number = int(input())
    return number

def main():
    number = set_input()
    x = 1
    y = 1
    step = 1
    while number > step:
        number -= step
        step += 1

        if step % 2:
            x = step - number + 1
            y = number
        else:
            x = number
            y = step - number + 1
    
    print(f"{x}/{y}")

if __name__ == '__main__':
    main()