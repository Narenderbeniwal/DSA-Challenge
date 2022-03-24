from file_compression import FileCompression
from logs import logger

filecmp = FileCompression()


def compress():
    try:
        fDir = input("Enter the file directory")
        fName = input("Enter file  you want to compress with extension(ex:- .png,.mp4 etc :")
        logger.info(f"###### File to be compressed  {fName}  #######")

        new_File = input("Enter the name of new File :")

        filecmp.compress(fDir, fName, new_File)
        logger.info(f"###### File Compressed ! and saved with name - {new_File} #######")
    except Exception as e:
        logger.error(f"###### compression fails due to {e} #######")

def decompress():
    try:
        fDir = input("Enter the file directory")
        fName = input("Enter file  you want to decompress :")
        logger.info(f"###### File to be decompressed  {fName}  #######")

        new_File = input("Enter the name of new File :")

        filecmp.decompress(fDir, fName, new_File)
        logger.info(f"###### File DeCompressed ! and saved with name - {new_File} #######")
    except Exception as e:
        logger.error(f"###### decompression fails due to {e} #######")
