#!/usr/bin/python
__author__ = "Diego Freire"
import email
import imaplib
import os

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
u_name = 'seu_email@gmail.com'
u_pass = 'sua_senha'
d_dir = 'c:/tmp'

def read_mensages():
    try:
        mail.select('Inbox')

        #Busca mensagens nao lidas
        (return_code, messages) = mail.search(None, '(UNSEEN)')
        
        if return_code == 'OK':
            for num in messages[0].split():
                typ, data = mail.fetch(num, '(RFC822)')

                # Salvando anexos
                m = email.message_from_string(data[0][1])
                for part in m.walk():
                    filename = part.get_filename()
                    if filename is not None:
                        sv_path = os.path.join(d_dir, filename)
                        if not os.path.isfile(sv_path):
                            print sv_path
                            fp = open(sv_path, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()

                # Imprimindo algumas propriedades do header
                for response_part in data:
                    if isinstance(response_part, tuple):
                        original = email.message_from_string(response_part[1])
                        data = response_part.get
                        print original['From']
                        print original['Subject']
                        print original['Body']
        print "Procurando mensagens..."
    except Exception,e:
        print "Erro Mensagem: "+str(e)

# Efetua conexao na conta de email.
try:
    mail.login(u_name, u_pass)
except Exception, e:
    print "Erro Login: "+str(e)

# Inicia procura de mensagens nao lidas.
while True:
    read_mensages()
