#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class Backup(object):
    @staticmethod
    def run(exclude_list_file, folder_dest, filename, folder_backup):
        os.system("tar --exclude-from={0} --exclude={1} --numeric-owner -zcvf {2}/{3}.tar.gz {4}"
                  .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))

