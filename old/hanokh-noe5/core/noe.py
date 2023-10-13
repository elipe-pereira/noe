#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import time
from config.Config import Config
from backup import Backup
from mount import Mount
from services import Services
from log import Log
from mail import Mail
from help import Help


def main():
    main_file_exec_path = os.path.realpath(sys.argv[0])
    working_dir = os.path.dirname(main_file_exec_path)
    config_file = working_dir + "/config/noe/noe.conf"

    config = Config(config_file)
    help = Help()
    backup = Backup()

    sections = config.get_sections_config()
    argument = ""

    try:
        argument = sys.argv[1]

    except:
        print(help.get_help())
        sys.exit(0)

    if (argument == "--list-routines"):
        for section in sections:
            if section == "DEFAULT":
                continue

            print (" - " + section)

    elif (argument == "--help"):
        print(help.get_help())

    elif (argument == "--backup-all"):
        for section in sections:
            if section == 'DEFAULT':
                continue

            backup.exec_backup(section)

    elif (argument in sections):
        backup.exec_backup(argument)

    else:
        print(help.get_help())

if __name__ == '__main__':
    main()