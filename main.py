def encode(raw_pwd):
    encoded_pwd = ''
    input_list = list(raw_pwd)
    for i in range(0, len(input_list)):
        input_list[i] = int(input_list[i])
        if input_list[i] < 7:
            input_list[i] += 3
        else:
            input_list[i] -= 7
    for i in range(0, len(input_list)):
        encoded_pwd += str(input_list[i])
    return encoded_pwd


def main():
    while True:
        print("1. Encode password\n2. Decode password")
        choice = int(input("Enter an option: "))
        if choice == 1:
            raw_pwd = input("Enter an 8-digit password to be encoded: ")
            print(encode(raw_pwd))
        elif choice == 2:
            encoded_pwd = input("Enter an 8-digit password to be decoded: ")
            # decode function call
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()