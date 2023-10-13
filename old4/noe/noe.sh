#!/bin/bash
# noe.sh - Script de backup com vários parâmetros para definir o tipo de backup
# que você quer.
# Desenvolvido por: Eli Pereira, Início: 03/10/2017.

data=`date +%d-%m-%Y`

function ajuda(){

	echo "

		full - Faz o backup full do sistema operacional, exceto o que estiver no exclude
		
		incremental - Faz o backup incremental dos arquivos
		
		parcial - Faz backup somente das pastas escolhidas
			
		ajuda - Exibe o menu de ajuda
									
	"	
}

function install(){

	test -d /opt/backup || mkdir /opt/backup
	test -d /etc/noe || mkdir /etc/noe
	test -d /etc/noe/full || mkdir /etc/noe/full
	test -d /etc/noe/incremental || mkdir /etc/noe/incremental
	test -d /etc/noe/parcial || mkdir /etc/noe/parcial
	test -f /etc/noe/full/exclude.full || touch /etc/noe/full/exclude.full
	test -f /etc/noe/incremental/exclude.incremental || touch /etc/noe/incremental/exclude.incremental
	test -f /etc/noe/parcial/exclude.parcial || touch /etc/noe/parcial/exclude.parcial
	test -d /var/log/noe || mkdir /var/log/noe
	test -d /var/log/noe/full || mkdir /var/log/noe/full
	test -d /var/log/noe/incremental || mkdir /var/log/noe/incremental
	test -d /var/log/noe/parcial || mkdir /var/log/noe/parcial
	test -f /var/log/noe/full/erros.log || touch /var/log/noe/full/erros.log
	test -f /var/log/noe/incremental/erros.log || touch /var/log/noe/incremental/erros.log
	test -f /var/log/noe/parcial/erros.log || touch /var/log/noe/parcial/erros.log
	test -f /etc/noe/.noe || touch /etc/noe/.noe

	existe_sys_full=`grep '/sys' /etc/noe/full/exclude.full 2> /dev/null| wc -l`
	existe_dev_full=`grep '/dev' etc/full/exclude.full 2> /dev/null|wc -l`
	existe_proc_full=`grep '/proc' etc/full/exclude.full 2> /dev/null|wc -l`
	existe_sys_incremental=`grep '/sys' /etc/noe/incremental/exclude.incremental 2> /dev/null |wc -l`
	existe_dev_incremental=`grep '/dev' /etc/noe/incremental/exclude.incremental 2> /dev/null |wc -l`
	existe_proc_incremental=`grep '/proc' /etc/noe/incremental/exclude.incremental 2> /dev/null |wc -l`
	existe_sys_parcial=`grep '/sys' /etc/noe/parcial/exclude.parcial 2> /dev/null |wc -l`
	existe_dev_parcial=`grep '/dev' /etc/noe/parcial/exclude.parcial 2> /dev/null |wc -l`
	existe_proc_parcial=`grep '/proc' /etc/noe/parcial/exclude.parcial 2> /dev/null |wc -l`

	if [[ ${existe_sys_full} -eq 0 ]]
	then
	  	echo  "/sys" >> /etc/noe/full/exclude.full;
	fi

	if [[ ${existe_dev_full} -eq 0 ]]
	then
	  echo "/dev" >> /etc/noe/full/exclude.full;
	fi

	if [[ ${existe_proc_full} -eq 0 ]]
	then
	  echo "/proc" >> /etc/noe/full/exclude.full;
	fi

	if [[ ${existe_sys_incremental} -eq 0 ]]
	then
	    echo "/sys" >> /etc/noe/incremental/exclude.incremental
	fi

	if [[ ${existe_dev_incremental} -eq 0 ]]
	then
	    echo "/dev" >> /etc/noe/incremental/exclude.incremental
	fi

	if [[ ${existe_proc_incremental} -eq 0 ]]
	then
	    echo "/proc" >> /etc/noe/incremental/exclude.incremental
	fi

	if [[ ${existe_sys_parcial} -eq 0 ]]
	then
        echo "/sys" >> /etc/noe/parcial/exclude.parcial
	fi

	if [[ ${existe_dev_parcial} -eq 0 ]]
	then
	    echo "/dev" >> /etc/noe/parcial/exclude.parcial
	fi

	if [[ ${existe_proc_parcial} -eq 0 ]]
	then
	    echo "/proc" >> /etc/noe/parcial/exclude.parcial
	fi
}

function full(){

#	testaArquivosBackupFull

	# Efetua o backup full e já cria a base para os backups incrementais com a opção -g

	echo "Iniciando Backup `date`" >> logs/full/messages.log

	tar --exclude-from=etc/full/exclude.full \
	 -jcvf backup/backup-${data}-full.tar.bz2 / -g etc/incremental-list 2>> logs/full/messages.log

	 tar --exclude-from=etc/full/exclude.full \
	 	-jcvf backup/backup-${data}-full.tar.bz2 /

	echo "Finalizando backup `date`" >> logs/full/messages.log

	echo "last_backup_full=${data}" > etc/.noe
}

function incremental(){

	. etc/.noe

	if [[ -f backup/backup-${last_backup_full}-full.tar.bz2 ]]
	then

		echo "Ultimo backup full encontrado ..."

		if [[ -f etc/incremental-list ]]
		then
			echo "Iniciando backup incremental `date`" >> incremental.log
			tar --exclude-from=etc/full/exclude.full -jvcf\
		 		backup/backup-${data}-incremental.tar.bz2 / -g etc/incremental-list
		else
			echo "incremental-list não foi encontrado !!"
			echo "Não foi possível executar o backup !!"
		fi
	else
		echo "Backup full não encontrado !!"
		echo "Não é possível continuar !!"
	fi

}

#function testFilesPartial(){
#
#	test -d backup_parcial || mkdir backup_parcial
#	test -d etc || mkdir etc
#	test -f etc/exclude.parcial || touch etc/exclude.parcial
#	test -f etc/include.parcial || touch etc/include.parcial
#
#	existe_sys=`grep -c "/sys" etc/exclude.parcial`
#	existe_proc=`grep -c "/proc" etc/exclude.parcial`
#	existe_dev=`grep -c /dev etc/exclude.parcial`
#
#	if [ ${existe_sys} -eq 0 ]
#	then
#		echo "/sys" >> exclude.parcial
#	fi
#
#	if [ ${existe_proc} -eq 0 ]
#	then
#		echo "/proc" >> exclude.parcial
#	fi
#
#	if [ ${existe_dev} -eq 0 ]
#	then
#		echo "/dev" >> exclude.parcial
#	fi
#
#	tamanho_include=`cat etc/include.parcial|wc -l`
#
#	if [ ${tamanho_include} -eq 0 ]
#	then
#		echo "Arquivos não foram incluídos no backup parcial!!"
#		echo "Saindo ..."
#		exit 1
#	fi
#}
#
#function partial(){
#
#	testFilesPartial
#
#	tar --exclude-from=etc/exclude-parcial -jcvf \
#	 --files-from=etc/include.parcial 2> etc/erros.log
#
#}
#
#
case "$1" in

	full) full;;
#	incremental) incremental;;
#	partial) partial;;
#	help) help;;
#	*) help;;

esac