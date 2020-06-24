from json import dump, load
from os import system
from time import sleep

fileUser = 'user.json'
fileContact = 'member.json'

user = {}
contact = {}

def loadData():
	global user, contact

	with open(fileUser) as f:
		user = load(f)

	with open(fileContact) as f:
		contact = load(f)

	return True

def saveData():
	global user, contact

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileContact, 'w') as f:
		dump(contact, f)

	return True

def login():
	counter = 1
	Username = input('Enter Username : ')
	Password = input('Enter Password : ')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination Username and Password is Wrong')
		Username = input('Enter Username : ')
		Password = getpass('Enter Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Login Pass')
		return True

def print_menu():
	print('Shabalabala Warnet')
	print('[1] Lihat daftar member')
	print('[2] Tambah member')
	print('[3] Blacklist member')
	print('[4] Cari nama member')
	print('[q] Keluar aplikasi')

def print_member():
	if len(contact) > 0:
		for info in contact:
			print(f'Nama \t: {info}\t Saldo \t: {contact[info]}')
	else:
		print('Member kosong bro.')

def add_member():
	print('Add new member\n')

	nama = input('Nama \t:')
	phone = input('Saldo \t:')

	contact[nama] = phone
	saveData()
	print('Saving Data ...')
	sleep(1)
	print('Data Saved.')

def remove_member():
	print('Blacklist member\n')

	nama = input('Nama \t:')

	if nama in contact:
		del contact[nama]
		saveData()
		print('Removing Data ...')
		sleep(1)
		print('Data Saved.')
	else:
		print(f'{nama} doesnot exists in contact')

def cari_member():
	print('Cari member :\n')

	nama = input('Name \t:')

	if nama in contact:
		print(f'Name \t: {nama}\t Saldo \t:{contact[nama]}')
	else:
		print(f'{nama} doesnot exists in contact')	

