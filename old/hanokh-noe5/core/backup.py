#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
from config.Config import Config
from mount import Mount
from services import Services
from log import Log
from mail import Mail


class Backup(object):
    def __init__(self):
        self.log = Log()

    def run(self, exclude_list_file, folder_dest, filename, folder_backup):
        os.system("XZ_OPT='-9' tar --exclude-from={0} --exclude={1} --numeric-owner -Jcvf {2}/{3}.tar.xz {4}"
                  .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))

    def exec_backup(self, section):
        main_file_exec_path = os.path.realpath(sys.argv[0])
        working_dir = os.path.dirname(main_file_exec_path)
        config_file = working_dir + "/config/noe/noe.conf"

        config = Config(config_file)
        # command_exec = Services()

        config.set_all_variables_from_config(section)

        type_backup = config.get_type_config()
        folder_backup = config.get_folder_config()
        folder_dest = config.get_folder_dest_config()
        time_keep = config.get_time_keep()
        remote_share = config.get_remote_share_config()
        host = config.get_host_config()
        port = config.get_port()
        user = config.get_user_config()
        password = config.get_password_config()
        database = config.get_database()
        bucket_name = config.get_bucket_name_config()
        access_key = config.get_access_key_config()
        secret_access_key = config.get_secret_access_key()
        filename = config.get_file_name_config()
        exclude_list_file = config.get_exclude_list_file()

        dests_prohibited = [
            "/", "/bin/", "/dev/", "/home/", "/lib32/", "/libx32/","/media/",
            "/opt/", "/root/", "/sbin/", "/srv/", "/sys/", "/usr/", "/boot/", 
            "/etc/", "/lib/","/lib64/", "/mnt/", "/proc/", "/run/", "/snap/",
            "/tmp/", "/var/", "/var/lib/", "/tmp/", "/usr/bin/", "/usr/games/",
            "/usr/include/", "/usr/lib/", "/usr/lib32/", "/usr/lib64/", "/usr/libexec/",
            "/usr/libx32/", "/usr/local/", "/usr/sbin/", "/usr/share/", "/usr/src/", 
            "/usr/local/bin/", "/usr/local/etc/", "/usr/local/games/", "/usr/local/include",
            "/usr/local/lib/", "/usr/local/main/", "/usr/local/sbin/", "/usr/local/share/",
            "/usr/local/src/"
        ]

        for dests in dests_prohibited:
            if folder_dest == dests or folder_dest in dests:
                print("""
                    folder_dest está em local perigoso, por favor
                    configure outra pasta para ser o destino do
                    backup, porque o noe verifica pastas e arquivos
                    e as apaga se forem mais antigas que time_keep.
                    Isso pode definitivamente quebrar o sistema.
                """)
                sys.exit(0)

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        os.system("tmpreaper --mtime {0} {1}".format(time_keep, folder_dest))

        # enable_stop_services = config.get_enable_stop_services()
        # command_stop = config.get_command_stop().split(',')
        # command_start = config.get_command_start().split(',')

        # if enable_stop_services == "yes":
        #     log.log("Parando serviços")
        #     for command in command_stop:
        #         command_exec.stop_service(command)

        hora_inicio = ""
        hora_fim = ""

        if type_backup == "local":
            self.log.log("Iniciando backup")
            self.log.log("Backup do tipo local")
            self.log.log("Executando cópia e compressão dos arquivos")
            hora_inicio = time.strftime('%H:%M')
            self.run(exclude_list_file, folder_dest, filename, folder_backup)
            hora_fim = time.strftime('%H:%M')
            self.log.log("Fim do backup " + section)

        elif type_backup == "rsync-down":
            self.log.log("Iniciando backup")
            self.log.log("Backup do tipo rsync-down")
            hora_inicio = time.strftime("%H:%M")
            os.system("rsync --exclude-from={5} -av -e 'ssh -p {2}' --progress --compress {0}@{1}:{3} {4}".format(
                    user,
                    host,
                    port,
                    folder_backup,
                    folder_dest,
                    exclude_list_file
                ))
            hora_fim = time.strftime("%H:%M")
            self.log.log("Fim do backup " + section)

        elif type_backup == "ssh-down":
            self.log.log("Iniciando backup")
            self.log.log("Backup do tipo ssh-down")
            hora_inicio = time.strftime("%H:%M")

            folder_to_backup = os.path.basename(folder_backup)

            if folder_to_backup == '':
                folder_to_backup = '.'

            change_dir = os.path.dirname(folder_backup)

            os.system(
                """ssh -p {2} {0}@{1} \
                 'cd {3} && tar \
                  --exclude=/proc --exclude=/sys --exclude=/dev --exclude=./proc --exclude=./sys --exclude=./dev \
                   -Jcvf - {4}' > {5}/{6}.tar.xz"""
                .format(
                    user,
                    host,
                    port,
                    change_dir,
                    folder_to_backup,
                    folder_dest,
                    filename
                ))
            hora_fim = time.strftime("%H:%M")
            self.log.log("Fim do backup " + section)

        # elif type_backup == "samba":
        #     mount = Mount()
        #     log.log("Executando backup do tipo samba")
        #     log.log("Montando compartilhamento")
        #     mount.mountSamba(host, remote_share, folder_dest, user, password)
        #     log.log("Executando cópia e compressão dos arquivos")
        #     self.run(exclude_list_file, folder_dest, filename, folder_backup)
        #     log.log("Fim do backup " + section)
        #     log.log("Desmontando compartilhamento")
        #     mount.umount(folder_dest)

        # elif type_backup == "bucket":
        #     tmp_file = "/tmp/.passwd-s3fs"
        #     log.log("Montando o bucket")
        #     mount.mountBucket(access_key, secret_access_key, tmp_file, bucket_name, folder_dest)
        #     log.log("Executando a cópia e compactação dos arquivos")
        #     self.run(exclude_list_file, folder_dest, filename, folder_backup)
        #     log.log("Demontando bucket")
        #     mount.umount(folder_dest)

        elif type_backup == "mysql":
            self.log.log("Iniciando backup")
            self.log.log("Executando backup do banco de dados mysql")
            hora_inicio = time.strftime('%H:%M')
            os.system("mysqldump -u {0} -p{1} -R {2} -h {3} -P {4} > {5}/{6}.sql".format(
                user,
                password,
                database,
                host,
                port,
                folder_dest,
                filename
            ))
            os.chdir(folder_dest)
            os.system("XZ_OPT='-9' tar -Jcvf {0}/{1}.tar.xz {1}.sql".format(folder_dest, filename))
            os.system("rm {0}/{1}.sql".format(folder_dest, filename))

            hora_fim = time.strftime('%H:%M')
            self.log.log("Backup do " + section + " concluído")

        elif type_backup == "pgsql":
            self.log.log("Iniciando backup")
            self.log.log("Executando backup do banco de dados postgresql")
            hora_inicio = time.strftime('%H:%M')
            os.system("PGPASSWORD='{1}' pg_dump -U {0} -d {2} -h {3} -p {4} > {5}/{6}.sql".format(
                user,
                password,
                database,
                host,
                port,
                folder_dest,
                filename
            ))
            os.chdir(folder_dest)
            os.system("XZ_OPT='-9' tar -Jcvf {0}/{1}.tar.xz {1}.sql".format(folder_dest, filename))
            os.system("rm {0}/{1}.sql".format(folder_dest, filename))

            hora_fim = time.strftime('%H:%M')
            self.log.log("Backup " + section + " concluído")

        else:
            print("Tipo de backup não válido")
            sys.exit(0)

        # if enable_stop_services == "yes":
        #     log.log("Subindo serviços")

        # for command in command_start:
            # command_exec.start_service(command)

        mail = Mail(hora_inicio, hora_fim, section)

        config.set_mail_address('DEFAULT', 'mail_address')
        mail_address = config.get_mail_address()
        server_name = config.get_server_name()

        if mail_address:
            self.log.log("Enviando E-mail")
            mail.send("Backup NOE - {0}".format(server_name), mail_address)