from cryptography.fernet import Fernet
from logs import logger


class EncryptionKeys:

    def generate_key(self):
        key = Fernet.generate_key()
        logger.info("###### key for the encryption generated ######")
        return key

    def write_key(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        logger.info("###### key loaded ######")
        return key


class FileEncryption(EncryptionKeys):

    def encrypt_file(self, key, original_file, encrypted_file):
        f = Fernet(key)
        logger.warn("###### opening original file  ######")
        with open(original_file, 'rb') as file:
            original = file.read()
        encrypted = f.encrypt(original)
        logger.info("###### file encrypted ######")
        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)
        logger.info("###### Encrypted file saved  ######")

    def decrypt_file(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)
        logger.info("###### opening encrypted file ######")
        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        logger.info("###### File decrypted ######")
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
        logger.info("###### Decrypted file saved ######")
