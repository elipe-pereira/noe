# Changelog
# Noe
# [unreleased]
## [x.x.x]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Release]
## [0.12.4]
### Added
### Changed
### Deprecated
### Removed
### Fixed
	- Adicionado parâmetro de porta que estava faltando na rotina de backup ssh-down.
### Security

# [Released]
## [0.12.3]
### Added
### Changed
    - Alterado parâmetro do tmpreaper de --ctime para --mtime
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.12.2] - 2022-12-10
### Added
### Changed
    - Pequenos ajustes na lista de exclude da rotina ssh-down.
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.12.1] - 2022-12-10
### Added
### Changed
    - Alterado para que o ssh-down faça backup somente da pasta fim e não da raiz inteira
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.12.0] - 2022-12-10
### Added
    - Adicionado modo de backup ssh-down
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.11.0] - 2022-12-09
### Added
### Changed
    - Alterado compactação dos backups das bases para usar xz em vez de gzip.
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.10.0] - 2022-12-09
### Added
### Changed
    - Alterado algoritimo de backup para o xz(zip) versão linuz com nível -9 de
    compressão
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.9.0] - 2022-12-09
### Added
### Changed
    - Alterado para que os arquivos sejam removidos com base no tempo de criação 
    e não com base no tempo de acesso.
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.8.0] - 2022-09-26
### Added
	- Adicionado para parametro para compressão de dados na conexão, no backup do tipo rsync-down
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.7.0] - 2022-09-22
### Added
	- Adicionado exclude list à rotina rsync. 
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.6.0] - 2022-09-22
### Added
	- Backup de bancos de dados do postgresql
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.5.0] 2022-09-22
### Added
	- Adicionado backup remoto via rsync, somente download e sem compactar arquivos
	- Adicionado parametro no arquivo de configuração de porta que deve ser agora
	inserido para mysql e rsync. Porta ainda não é opcional
### Changed
### Deprecated
### Removed
### Fixed
### Security

# [Released]
## [0.4.0] - 2022-09-18
### Added
### Changed
	- E-mails agora informam hora de início e hora de fim e nome da rotina.
### Deprecated
### Removed
### Fixed
### Security

## [Released]
## [0.3.0] - 2022-09-18
### Added
	- Backup mysql usando mysqldump e usando tar e gzip para compactação
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released]
## [0.2.0] - 2022-09-12
### Added
### Changed
	- Nomes de arquivos terão agora a hora de execução além da data junto no nome do arquivo.
### Deprecated
### Removed
### Fixed
### Security

## [Released]
## [0.1.1] - 2022-09-11
### Added
### Changed
### Deprecated
### Removed
### Fixed
	- Fixado problema onde era feito backup de folder_dest junto com o banco de dados.
### Security

## [Released]
## [0.1.0] - 2022-08-19
### Added
	- Backup local.
### Changed
### Deprecated
### Removed
### Fixed
### Security
