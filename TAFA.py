
inp = '   >>> '
def logo(t=False, n=False):
	a = ("""  _________    _________ 
 /_  __/   |  / ____/   |
  / / / /| | / /_  / /| |
 / / / ___ |/ __/ / ___ |
/_/ /_/  |_/_/   /_/  |_| v0.1
                         
""").splitlines()
	for s in a:
		print("\t" + s)
	if t:
		supported = ["\t[*] Supported: Uzang     [*]", "\t[*] Supported: TyoMP     [*]"]
		print("\t[*] Toolkit For Facebook [*]")
		print("\t[*] Author: SalisM3      [*]")
		print(random.choice(supported))
	elif n:
		nama = eval(open('kuki.txt').read())['nama'][:20]
		spasi = (22 - len(nama) - 1) // 2
		spasi = spasi * " "
		print("\t[*] " + spasi + nama + spasi + " [*]")
		
def enter():
	click('\n   [ Press Enter To Back ]')
	home()
	exit()
	
def wrong_id(id,p=False,g=False,f=False,h=False):
	gas = Core()
	if p:
		cek = gas.cek_id(id,p=True)
	elif g:
		cek = gas.cek_id(id,p=True)
	elif f:
		cek = gas.cek_id(id,f=True)
	elif h:
		cek = gas.cek_id(id,h=True)
		
	if cek:
		return True
	else:
		return False
		
##### menu #####
def bom_like_friend():
	id = str(input("   [?] Id Target: "))
	if wrong_id(id,p=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	gas = Like()
	gas.dump_sts("https://mbasic.facebook.com/profile.php?id="+id, "Suka", "Lihat Berita Lain", limit)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("like.php")
	print("   [+] Done!")
	enter()

def bom_like_grup():
	id = str(input("   [?] Id Group: "))
	if wrong_id(id,g=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000:
		limit = 1000
	gas = Like()
	print("   [+] Spamming Like To: " + gas.get_name(id))
	gas.dump_sts("https://mbasic.facebook.com/groups/"+id, "Suka", "Lihat Postingan Lainnya", limit)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("\n   [+] Process")
	gas.hajar("like.php")
	print("   [+] Done!")
	enter()
	
def bom_like_halaman():
	id = str(input("   [?] Username Fanspage: "))
	if wrong_id(id,f=True):
		print("   [+] Invalid Username")
		enter()
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000:
		limit = 1000
	gas = Like()
	gas.dump_sts("https://mbasic.facebook.com/"+id, "Suka", "Tampilkan lainnya", limit)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("like.php")
	print("   [+] Done!")
	enter()

def bom_like_home():
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000:
		limit = 1000
	gas = Like()
	print("   [+] Spamming Like in Home ")
	gas.dump_sts("https://mbasic.facebook.com/", "Suka", "Lihat Berita Lain", limit)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("like.php")
	print("   [+] Done!")
	enter()

def acc_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Other()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Konfirmasi", "Lihat selengkapnya", 0)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("com")
	print("   [+] Done!")

def rej_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Other()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Hapus Permintaan", "Lihat selengkapnya", 0)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("com")
	print("   [+] Done!")
	
def unadd_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Other()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/outgoing/", "Batalkan Permintaan", "Lihat selengkapnya", 0)
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar("com")
	print("   [+] Done!")
	 
	
##### menu #####


##### class #####
class Menu:
	def __init__(self):
		pass
		
	def m1(self):
		print("\n   1). Go To Menu")
		print("   2). Login")
		print("   3). Logout")
		print("   0). Exit")
		pilih = int(input(inp))
		login = Login()
		if pilih == 0:
			print("   [!] Exit: Ok")
		elif pilih == 1:
			if not cek_login():
				print("   [!] Please Login")
				time.sleep(1)
				home()
			else:
				self.m2()
		elif pilih == 2:
			login.in_()
		elif pilih == 3:
			login.out()
		else:
			home()
			
	def m2(self):
		os.system('clear')
		logo(n=True)
		print("\n   1). Like")
		print("   2). Comment")
		print("   3). Group")
		print("   4). Other")
		print("   0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			home()
		elif pilih == 1:
			self.m3()
		elif pilih == 2:
			print("\n   [!] Cooming Soon")
			enter()
		elif pilih == 3:
			print("\n   [!] Cooming Soon")
			enter()
		elif pilih == 4:
			self.m4()
		else:
			self.m2()
	
	def m3(self): # like menu
		os.system('clear')
		logo(n=True)
		print("\n   1). Bom Like Friend Timeline")
		print("   2). Bom Like in Group")
		print("   3). Bom Like in Fanspage")
		print("   4). Bom Like in Home")
		print("   0). Back")
		pilih = int(input(inp))
		if pilih == 1:
			bom_like_friend()
		elif pilih == 2:
			bom_like_grup()
		elif pilih == 3:
			bom_like_halaman()
		elif pilih == 4:
			bom_like_home()
		elif pilih == 0:
			self.m2()
		else:
			self.m3()
	
	def m4(self): # other menu
		os.system('clear')
		logo(n=True)
		print("\n   1). Acc All Friend Requests")
		print("   2). Reject All Friend Requests")
		print("   3). Unadd (not Unfriend)")
		print("   0). Back")
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			acc_all_friend()
		elif pilih == 2:
			rej_all_friend()
		elif pilih == 3:
			unadd_all_friend()
		else:
			self.m4()
		
class Login():
	def __init__(self):
		pass
	
	def in_(self):
		if cek_login():
			print("   [!] You Has Been Login")
			time.sleep(1)
			home()
		else:
			os.system('clear')
			print("   [ Enter Your Facebook Cookies ]\n")
			kuki = str(input("   [?] Your Cookies: "))
			if cek_login(c=True, kuki=kuki):
				open('kuki.txt', 'w').write("{'kuki':'" + kuki + "'}")
				kuki = eval(open('kuki.txt').read())['kuki']
				r.get('https://mbasic.facebook.com/a/mobile/friends/profile_add_friend.php?subjectid=100041106940465&istimeline=1&hf=profile_button&fref=unknown&frefid=0&referrer_uri=https%3A%2F%2Fmbasic.facebook.com%2Fremovefriend.php%3Ffriend_id%3D100041106940465%26removed%26_rdr&gfid=AQDj3Ny5Q2Ax6lVZ', headers={'Cookie':kuki})
				info = Information()
				nama = info.get_name_myself()
				print("   [!] Login Success")
				time.sleep(0.5)
				open('kuki.txt', 'w').write("{'nama':'" + nama + "', 'kuki':'" + kuki + "'}")
				print("   [!] Your Cookies Saves in: kuki.txt")
				time.sleep(1)
				home()
			else:
				print("   [!] Invalid Cookies")
				time.sleep(1)
				home()
	
	def out(self):
		pilih = str(input('\n   [?] type "yes" to confirm: '))
		if pilih == "yes":
			try:
				os.remove('kuki.txt')
				print("   [!] Logout: Ok")
			except:
				print("   [!] Logout: Failed")
			time.sleep(1)
			home()
		else:
			print("   [!] Operation Cancelled")
			time.sleep(1)
			home()
##### class #####

def update_kuki():
	while True:
		kuki = str(input('\n   [!] your proses has been stoped because your\n   cookies expired to continue please update it\n   or type "exit" to exit : '))
		if kuki == "exit":
			raise KeyboardInterrupt
		elif cek_login(c=True, kuki=kuki):
			return kuki
			break
		
def cek_kuki():
	if not cek_login():
		exit("   [!] Kuki Expired")
		
def cek_login(c=False, kuki=""):
	try:
		if not c:
			kuki = eval(open('kuki.txt').read())['kuki']
		cek = r.get('https://mbasic.facebook.com', headers={'cookie':kuki}).text
		if "mbasic_logout_button" in cek:
			return True
		else:
			return False
	except:
		return False			

def home():
	os.system('clear')
	logo(t=True)
	menu = Menu()
	menu.m1()
	
try:
	import random, time, mechanize, os, requests as r
	from bs4 import BeautifulSoup as parser
	from getpass import getpass as click
	exec(open('module.py').read())
	home()
except KeyboardInterrupt:
	print("   [!] Exit: Ok")
except ImportError as e:
	print("[!] " + str(e))
#except Exception as e:
#	print("   [!] " + str(e))