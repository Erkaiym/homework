#1 необходимо извлечь IP-адреса посетителей.
(\d+\.\d+\.\d+\.\d+)

#2 необходимо извлечь время запроса.
(\d+\/\w+\/\d+:\d+:\d+:\d+.\+\d+)


#3 нужно извлечь IP-адрес, дату и время запроса, HTTP-метод “GET” только из GET-запросов.
(\d+\.\d+\.\d+\.\d+.+\d+\/\w+\/\d+:\d+:\d+:\d+.\+\d+.+"GET\s\/\w+\/\s\w+\/\d\.\d")