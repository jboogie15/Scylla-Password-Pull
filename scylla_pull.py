import requests
import sys
import argparse

proxy = {"http:": "http://127.0.0.1:4444"}
		
p = argparse.ArgumentParser(description="Querying scylla.sh database.")

p.add_argument("-u", "--username", help= "Username to be queried.")
p.add_argument("-e", "--email", help = "Email to be queried.")
p.add_argument("-n", "--name", help = "Name to be queried. If first & last name is to be used, use quotes.")
p.add_argument("-l", "--list", help = "List with multiple dataset to be checked. Need additional parameter to identify if list consists of emails, usernames, names. Ex: -e list, -u list, -n list")
p.add_argument("-c", "--count", help = "How many results are returned. Default is 100", default='100')

args = p.parse_args()

username = args.username
email    = args.email
name 	 = args.name
in_list  = args.list
count 	 = args.count 

query = "'q': "

if not args.list:
	if args.username:
		print("[+] Getting results for the username %s..." % username)
		user = 'username:' + str(username)
		payload = {'q': user, 'size': count, 'start': '0'}
	elif args.email:
		print("[+] Getting results for the email %s..." % email)
		e = 'email:' + str(email)
		payload = {'q': e, 'size': count, 'start': '0'}
	elif args.name:
		print("[+] Getting results for the name %s..." % name)
		n = 'name:' + str(name)
		payload = {'q': n, 'size': count, 'start': '0'}
	r = requests.get('https://scylla.sh/search', proxies=proxy, params=payload)
	print("[+] Here are the results from scylla.sh:\n")
	print(r.text)
else:
	print("[+] Making requests to scylla.sh reading %s..." % in_list)
	f = open(in_list, "r")
	for x in f:
		print("[+] Results for %s\n" % x)
		if args.username == 'list':
			user = 'username:' + x
			payload = {'q': user, 'size': count, 'start': '0'}
			r = requests.get('https://scylla.sh/search', params=payload)
			print(r.text)
			print("\n")
		elif args.email == 'list':
			e = 'email:' + x
			payload = {'q': e, 'size': count, 'start': '0'}
			r = requests.get('https://scylla.sh/search', params=payload)
			print(r.text)
			print("\n")
		elif args.name == 'list':
			n = 'name:' + x
			payload = {'q': n, 'size': count, 'start': '0'}
			r = requests.get('https://scylla.sh/search', params=payload)
			print(r.text)
			print("\n")
