file = open('nginx_logs.txt', 'r', encoding='utf-8') 

for i in file:
  remote_addr = i.split()[0]
  request_type = i.split()[5][1:]
  requested_resource = i.split()[6]
  
  print(tuple([remote_addr, request_type, requested_resource]))
  

