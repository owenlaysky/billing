from json import dump, load
from os import system
from time import sleep

fileUser = 'user.json'
fileContact = 'member.json'
user = {}
member = {}



def loadData():
	global user, member

	with open(fileUser) as f:
		user = load(f)

	with open(fileContact) as f:
		member = load(f)

	return True



def saveData():
	global user, member

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileContact, 'w') as f:
		dump(member, f)

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
		Password = input('Enter Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Login Pass')
		return True



def print_menu():
	print('Shabalabala Warnet')
	print('[1] Lihat daftar Member')
	print('[2] Tambah Member')
	print('[3] Blacklist Member')
	print('[4] Update Saldo')
	print('[q] Keluar Aplikasi')



def print_member():
	if len(member) > 0:
		for info in member:
			print(f'Nama \t: {info}\t Saldo \t: {member[info]}')
	else:
		print('Member kosong bro.')



def add_member():
	print('Add new member\n')

	nama = input('Nama \t:')
	saldo = input('Saldo \t:')

	member[nama] = saldo
	saveData()
	print('Saving Data ...')
	sleep(1)
	print('Data Saved.')




def remove_member():
	print('Blacklist member\n')

	nama = input('Nama \t:')

	if nama in member:
		del member[nama]
		saveData()
		print('Proses dulu coy ...')
		sleep(1)
		print('Udah di Blacklist.')
	else:
		print(f'{nama} tidak terdaftar di member')



def tambah_saldo():
	print('Tambah saldo\n')

	nama = input('Nama member \t:')
	saldo = input('Jumlah saldo baru \t:')

	member[nama] = saldo
	saveData()
	print('Saving Data ...')
	sleep(1)
	print('Data Saved.')	

