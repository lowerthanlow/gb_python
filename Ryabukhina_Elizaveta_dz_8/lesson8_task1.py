import re

def email_parse(email_address):
  username = re.search(r'([\w.-]+)@([\w.-]+)', email_address)

  key = ['username', 'domain']
  el = [username.group(1), username.group(2)]

  if re.search('\.',username.group(2)):
    print(dict(zip(key, el)))
  else:
    raise ValueError 


email_parse('someone@geekbrains.ru')
  
  
  