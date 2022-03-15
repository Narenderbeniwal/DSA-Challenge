from process_handler import encryption, decryption


def main():
    while True:
        todo = input("What to do? Type 'EN' for 'Encryption' and 'DE' for 'Decryption' or 'END' to shut the program")
        if todo == "EN":
            encryption()
        elif todo == "DE":
            decryption()
        elif todo == "END":
            break
        else:
            print("please type 'EN' or 'DE' as per above instruction ")


if __name__ == "__main__":
    main()
