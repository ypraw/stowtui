import subprocess
import time
from os import listdir as workdir
from os import path as pth
from os import system as osSys
from typing import List, Tuple, Sequence


class StowtuiCore:

    @staticmethod
    def getAllDir(path_to_dir: str):
        get_only_directory: List[str] = [
            name for name in workdir(path_to_dir) if
            not name.startswith('.') and pth.isdir(pth.join(path_to_dir, name))
        ]
        it = iter(get_only_directory)
        list_of_tuple: List[Tuple[str, str]] = [(value, value) for value in it]
        return list_of_tuple

    @staticmethod
    def stowExecute(dirsName: List[str], path_DIR):
        for keyName in dirsName:
            # if keyName[0] == 'neofetch':
            targetExecute = "cd {} && stow -R -t ~/ {}".format(
                path_DIR, keyName)
            subprocess.run([targetExecute], shell=True)
        return True


if __name__ == '__main__':
    path_DIR = '/home/ypraw/Programming/linux/configDotfiles'
    testing = StowtuiCore()
    TestingDir = testing.getAllDir(path_DIR)
    print(testing.stowExecute(TestingDir, path_DIR))
