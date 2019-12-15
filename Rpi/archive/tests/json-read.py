import json 

j = '{"SCretry":false,"SCmusic":null,"SCswitch1":true,"SCswitch2":false,"SCswitch3":false}'

dic = json.loads(j)
for i in dic:
	print i, dic[i]