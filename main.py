import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while total <= 100:
        num = random.randrange(0, 100)
        numbers.append(num) 
        total = total + num
    
    total = total - num
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
