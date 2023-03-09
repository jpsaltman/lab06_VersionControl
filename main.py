
# Joshua Park
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


# Sofia Lammers

def decode(decoded):
    decoded_pwd = ''
    input_list = list(decoded)
    for i in range(0, len(input_list)):
        input_list[i] = int(input_list[i])
        if input_list[i] > 2:
            input_list[i] -= 3
        else:
            input_list[i] += 7
    for i in range(0, len(input_list)):
        decoded_pwd += str(input_list[i])
    return decoded_pwd

def main():
    while True:
        print("1. Encode password\n2. Decode password\n3. Exit")
        choice = int(input("Enter an option: "))
        if choice == 1:
            raw_pwd = input("Enter an 8-digit password to be encoded: ")
            encoded_pwd = encode(raw_pwd)
            print("Password encoded and stored.")
        elif choice == 2:
            decoded_pwd = decode(encoded_pwd)
	    print(f"The encoded password is {encoded_pwd}, and the original password is {raw_pwd}.")
        elif choice == 3:
            exit()
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()
