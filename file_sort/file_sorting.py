import os
import shutil


class FileHandler:

    def file_sort(self, path):

        list_ = os.listdir(path)
        for file_ in list_:
            name, ext = os.path.splitext(file_)

            ext = ext[1:]

            if ext == '':
                continue

            elif os.path.exists(path + '/' + ext):
                shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

            else:
                os.makedirs(path + '/' + ext)
                shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
