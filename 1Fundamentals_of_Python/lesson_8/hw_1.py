import re


def email_parse(email):
    if not MAIL:
        raise ValueError(f'wrong email: {email}')
    return dict(zip(['username', 'domain'], MAIL[0]))


e_mail = 'someone_123@geekbrains.ru'
MAIL = re.findall(r'([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', e_mail)
print(email_parse(e_mail))

# Есть ли шанс на существование у такого подхода?
# Не получается выкинуть ошибку в случае некорректного мыла
# А в случае корректной почты выцепляет нормально информацию
# Условие надо какое-то иное...
#
# import re
# def email_parse(mails):
#     if not MAIL:
#         raise ValueError(f'wrong email: {MAIL}')
#     else:
#         print(*map(lambda x: x.groupdict(), MAIL.finditer(mails)), sep='\n')
# MAIL = re.compile(r'(?P<username>([\w_-]+))@(?P<domain>([\w_-][\w_\.-]*\.[\w_-]{2,})$)')
# email_parse('someone_1@geekbrains.ru')