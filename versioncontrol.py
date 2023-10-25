

def encoder(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        encoded += str(digit)
    return encoded


def decoder(encoded):
    return encoded


def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoded_password = encoded_password
            print(f"The encoded password is {decoded_password}, and the original password is {password}.")
        if option == 3:
            break


if __name__ == "__main__":
    main()
