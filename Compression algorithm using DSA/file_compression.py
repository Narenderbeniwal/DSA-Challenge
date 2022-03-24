import os
import zlib, sys
from logs import logger


class FileCompression:

    def compress(self, fdir: str, filename_in: str, filename_out: str, ):
        logger.warn("###### opening original file  ######")
        os.chdir(fdir)
        with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as file_out:
            data = fin.read()
            compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
            logger.info(f"##### Original size of file {filename_in}: {sys.getsizeof(data)} #####")
            logger.info(f"##### Compressed size: {sys.getsizeof(compressed_data)} #####")
            file_out.write(compressed_data)

    def decompress(self, fdir: str, compressed_file: str, filename_out: str):
        logger.warn("###### opening original file  ######")
        os.chdir(fdir)
        with open(compressed_file, mode="rb") as fin, open(filename_out, mode="wb") as file_out:
            data = fin.read()
            compressed_data = zlib.decompress(data)
            print(f"##### Compressed size: {sys.getsizeof(data)} #####")

            print(f"##### Decompressed size: {sys.getsizeof(compressed_data)} #####")
            file_out.write(compressed_data)
