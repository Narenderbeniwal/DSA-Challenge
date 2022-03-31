from logs import logger
from process_handler import sort_file


def main():
    logger.info(" #### main function called #### ")
    try:
        while True:
            todo = input("Wanted to sort your unorganised directory !! type 'Y' to sort and type 'END' end")
            if todo == "Y":
                sort_file()
            elif todo == "END":
                break
            else:
                print("please type 'Y' or 'END' as per above instruction ")
    except Exception as e:
        logger.error(f" #### some error occur in main function due to {e} ####")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

