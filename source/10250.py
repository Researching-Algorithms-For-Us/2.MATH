'''
층수 계싼
'''
def set_input():
    size = int(input())
    hights = []
    widths = []
    numbers = []
    for _ in range(size):
        hight,width,number = map(int, input().split())
        hights.append(hight)
        widths.append(width)
        numbers.append(number)
        
    return hights,widths,numbers

def main():
    hights,widths,numbers = set_input()
    for height, width, number in zip(hights,widths,numbers):
        floor = number % height
        step = ( number // height )

        if floor > 0:
            step+=1
        else:
            floor = height
        
        result = floor * 100 + step
        print(result) 

if __name__ == '__main__':
    main()

