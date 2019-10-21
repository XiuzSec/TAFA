def acc_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Konfirmasi", "Lihat selengkapnya", 0, "com")
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()

def rej_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Hapus Permintaan", "Lihat selengkapnya", 0, "com")
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()
	
def unadd_all_friend():
	acc = str(input('\n   [?] type "yes" to confirm: '))
	if acc != "yes":
		print("\n   [+] Operation Canceled")
		enter()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/outgoing/", "Batalkan Permintaan", "Lihat selengkapnya", 0, "com")
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()