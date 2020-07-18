from time import sleep
def collatz(num):
    while num > 1:
        print(num)
        if num % 2 == 0:
            num = num // 2
            sleep(0.5)
        elif num % 2 == 1:
            num = 3 * num + 1
            sleep(0.5)
    print(1)

def main():
    number = int(input('Enter a Number: '))
    print('Collatz Sequence: ')
    collatz(number)

main()
