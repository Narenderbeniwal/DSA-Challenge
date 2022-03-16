# !pip install cryptography

from encryption import FileEncryption
from logs import logger

ecr = FileEncryption()
mykey = ecr.generate_key()
ecr.write_key(mykey, 'secret.key')

def encryption():
    try:
        fDir = input("Enter the file directory")
        fName = input("Enter file name you want to encrypt :")
        ext = input("Enter the extension : ( For eg :- .mp4, .csv, .txt, .png etc )")
        ch = input("You want to create new File after encryption or not ( y or n ) : ")
        file_Name = fName + ext
        logger.info(f"###### File to be encrypted {file_Name}  #######")

        if (ch == 'y'):
            new_File = input("Enter the name of new File :")
            new_Fname = new_File + ext
        elif (ch == 'n'):
            new_Fname = file_Name



        loaded_key = ecr.key_load('secret.key')
        ecr.encrypt_file(loaded_key, fDir, file_Name, new_Fname)
        logger.info(f"###### File Encrypted ! and saved with name - {new_Fname} #######")
    except Exception as e:
        logger.error(f"###### Encryption fails due to {e} #######")


# If the secret key is not present or filename is incorrect, then Exception will occur
def decryption():
    try:
        fDir = input("Enter the file directory")
        fName = input("Enter name of file you want to decrypt :")
        ext = input("Enter the extension : ( For eg :- .mp4, .csv, .txt, .png etc )")
        ch = input("You want to create new File after decryption or not ( y or n ) : ")
        file_Name = fName + ext
        logger.info(f"###### File to be decrypted -  {file_Name}  #######")

        if (ch == 'y'):
            new_File = input("Enter the name of new File :")
            new_Fname = new_File + ext
        elif (ch == 'n'):
            new_Fname = file_Name


        loaded_key = ecr.key_load('secret.key')
        ecr.decrypt_file(loaded_key, fDir, file_Name, new_Fname)
        logger.info(f"###### File Decrypted ! and saved with name - {new_Fname} #######")

    except Exception as e:
        logger.error(f"###### Decryption fails due to {e} #######")