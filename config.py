__author__ = 'diego.freire'

# Configurações de Email
user_name = 'seu_email@gmail.com'
user_pass = 'sua_senha'
attach_dir = 'c:/tmp'
imap_url = 'imap.gmail.com'
imap_port = 993

#Configurações da Base de Dados
db_host = ''
db_name = ''
db_user = ''
db_password = ''
connection_string = "Driver={{FreeTDS}};Server={};Database={};UID={};PWD={};".format(db_host, db_name, db_user,
                                                                                     db_password)