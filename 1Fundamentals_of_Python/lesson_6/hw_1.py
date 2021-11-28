with open('nginx_logs.txt') as f:
    print([(line.split()[0], line.split()[5].replace('"', ''), line.split()[6]) for line in f])
