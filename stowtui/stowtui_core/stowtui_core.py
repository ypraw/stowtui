#!/usr/bin/env python
# encoding: utf-8
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
            name for name in workdir(path_to_dir) if not name.startswith('.')
            and pth.isdir(pth.join(path_to_dir, name))
        ]

        return get_only_directory

    @staticmethod
    def stowExecuteCreate(dirs_name: List[str] = [],
                          path_dir: str = None,
                          path_dotfiles: str = None):
        """Static Method for executing stow function create
        Args:
            dirs_name (List[str]): List of dotfiles directories
            path_dir ([type]): path to target DIR, ex, $HOME
            path_dotfiles: Path of dotfiles config, ex ~/mydotfiles/

        Returns:
            [type]: [Executing stow on shell]
        """
        status: Tuple[bool, str] = (bool, str)
        try:
            for keyName in dirs_name:
                # if keyName[0] == 'neofetch':
                targetExecute = "cd {} && stow -R -t {} {}".format(
                    path_dotfiles, path_dir, keyName)
                subprocess.run([targetExecute],
                               shell=True,
                               stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL)
            status = (True, 'Successfully restored')
        except Exception as e:
            # pass
            status = (True, 'Errors Detected')
        return status

    @staticmethod
    def stowExecuteDelete(dirs_name: List[str] = [],
                          path_dir: str = None,
                          path_dotfiles: str = None):
        """Static Method for executing stow function delete
        Args:
            dirs_name (List[str]): List of dotfiles directories
            path_dir ([type]): path to target DIR, ex, $HOME
            path_dotfiles: Path of dotfiles config, ex ~/mydotfiles/
        Returns:
            [type]: [Executing stow on shell]
        """

        status: Tuple[bool, str] = (bool, str)
        try:
            for keyName in dirs_name:
                # if keyName[0] == 'neofetch':
                targetExecute = "cd {} && stow -D -t {} {}".format(
                    path_dotfiles, path_dir, keyName)
                subprocess.run([targetExecute],
                               shell=True,
                               stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL)
            status = (True, 'Successfully Deleted')
        except Exception as e:
            # pass
            status = (True, 'Errors Detected')
        return status


if __name__ == '__main__':
    path_DIR = '/home/ypraw/Programming/linux/configDotfiles'
    testing = StowtuiCore()
    TestingDir = testing.getAllDir(path_DIR)
    print(TestingDir)
