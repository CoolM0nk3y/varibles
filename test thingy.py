def main():
    while True:
        base = input('Please input the base (B:inary, D:ecimal, S:top)\n')
        if base in {'B', 'b'}:
            convert = lambda b: str(int(b, 2))
        elif base in {'D', 'd'}:
            convert = lambda d: bin(int(d))[2:]
        elif base in {'S', 's'}:
            break
        else:
            print('Your input is not a valid base')
            continue
        number = input('Please input a number\n')
        try:
            print(convert(number))
        except ValueError:
            print('Your input is not a valid number')

if __name__ == '__main__':
    main()
