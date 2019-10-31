def hapus_msg():
	gas = Other()
	confirm_execute()
	gas.dump_sts_wclass('https://mbasic.facebook.com/messages', True, 'Lihat Pesan Sebelumnya', 0, 'messages/read', href_na=True)
	echo("[+] Total: " + str(len(gas.id)))
	gas.hapus_msg()
	print()
	echo("[+] Done!")
	enter()