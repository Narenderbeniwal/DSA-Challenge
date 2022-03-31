from file_sorting import FileHandler
from logs import logger

file = FileHandler()

def sort_file():
    try:

        path = input("please enter the directory path  you wanted to sort ")
        logger.info(f"##### the path of directory to be sorted {path} #####")

        file.file_sort(path)
        logger.info("#### file sorted !! ####")

    except Exception as e:
        logger.error(f" #### some error occur due to {e} ####")
