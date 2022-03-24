from process_handler import compress, decompress


def main():
    while True:
        todo = input("What to do? Type 'CM' for 'Compression' and 'DC' for 'Decompress' or 'END' to shut the program")
        if todo == "CM":
            compress()
        elif todo == "DC":
            decompress()
        elif todo == "END":
            break
        else:
            print("please type 'EN' or 'DE' as per above instruction ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
