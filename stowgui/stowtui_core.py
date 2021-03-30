"""
---------
Stow TUI Core
---------

StowTUI Core module.

Define Classes for logical step to create symlink using stow packages.

There are two static methods on this class:

* ``getAllDir`` a getter for get list of directories of dotfiles.
* ``stowExecute`` an executer for stow to create symlink use stow it self.

"""

import subprocess
import time
from os import listdir as workdir
from os import path as pth
from os import system as osSys
from typing import List, Tuple, Sequence


class StowtuiCore:

    @staticmethod
    def getAllDir(path_to_dir: str):
        """This is static method for get all list name on target directory

        Args:
            path_to_dir (str): [path to directory location, exp: ~/mydotfiles]

        Returns:
            (List[str]): [list directory name from target directory]
        """
        get_only_directory: List[str] = [
            name for name in workdir(path_to_dir) if
            not name.startswith('.') and pth.isdir(pth.join(path_to_dir, name))
        ]
        # it = iter(get_only_directory)
        # list_of_tuple: List[Tuple[str, str]] = [(value, value) for value in it]
        return get_only_directory

    @staticmethod
    def stowExecute(dirsName: List[str], path_DIR):
        """Static Method for executing stow function

        Args:
            dirsName (List[str]): [description]
            path_DIR ([type]): [description]

        Returns:
            [type]: [Executing stow on shell]
        """
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
    print(TestingDir)
    # print(testing.stowExecute(TestingDir, path_DIR))
