#!/usr/bin/python
__author__ = 'Diego Freire'

import email
import imaplib
import os
import config


def read_mensages():
    try:
        mail.select('Inbox')
        # Busca mensagens nao lidas
        (return_code, messages) = mail.search(None, '(UNSEEN)')

        if return_code == 'OK':
            for num in messages[0].split():
                typ, data = mail.fetch(num, '(RFC822)')
                # Salvando anexos
                save_attachments(data[0][1])
                # Imprimindo algumas propriedades do header para testes
                print_properties(data)

        print 'Procurando mensagens...'
    except Exception, e:
        print 'Erro Mensagem: ' + str(e)


def save_attachments(data):
    m = email.message_from_string(data)
    for part in m.walk():
        filename = part.get_filename()
        if filename is not None:
            sv_path = os.path.join(config.attach_dir, filename)
            if not os.path.isfile(sv_path):
                print sv_path
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()


def print_properties(data):
    for response_part in data:
        if isinstance(response_part, tuple):
            original = email.message_from_string(response_part[1])
            print original['From']
            print original['Subject']
            print original['Body']


# Efetua conexao na conta de email.
try:
    mail = imaplib.IMAP4_SSL(config.imap_url, config.imap_port)
    mail.login(config.user_name, config.user_pass)
except Exception, e:
    print 'Erro Login: ' + str(e)

# Inicia procura de mensagens nao lidas.
while True:
    read_mensages()