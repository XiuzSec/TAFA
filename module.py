class Core:
	def __init__(self):
		self.id = []
		try:
			self.kuki = eval(open('kuki.txt').read())['kuki']
		except:
			self.kuki = ""
	
	def filter(self, str):
		data = filter(lambda x: str in x, self.id)
		return list(data)
	
	def cek_id(self, id, p=False, g=False, f=False, h=False):
		if p:
			url = "https://mbasic.facebook.com/profile.php?id="+id
		elif g:
			url = "https://mbasic.facebook.com/groups/"+id
		elif f:
			url = "https://mbasic.facebook.com/"+id
		elif h:
			url = "https://mbasic.facebook.com/"
		if "Halaman yang diminta tidak bisa ditampilkan sekarang." in self.o_url(url):
			return True
		else:
			return False
	
	#def get_url(self, url, stri):
		#data = parser(self.o_url(url), 'html.parser').find('a', "wow" in string).get('href')
		#return str(data)
			
	def mo_url(self, url):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
		return str(br.open(url).read())
	
	def o_url(self, url):
		data = r.get(url, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'Cookie':self.kuki}).text
		return data
	
	def dump_sts_wclass(self, url, stri, stri2, classna, limit):
		penentu = 0
		angka = 0
		self.url = url
		while penentu == 0:
			a = self.o_url(self.url)
			b = parser(a, 'html.parser')
			for s in b.find_all('a', class_=classna):
				self.id.append("https://mbasic.facebook.com" + s.get('href'))
				angka += 1
				if angka == limit:
					penentu += 1
					break
			next = b.find('a', string=stri2)
			if "None" in str(next):
				break
			else:
				self.url = "https://mbasic.facebook.com" + next.get('href')
				
	def dump_sts(self, url, stri, stri2, limit, kondisi):
		penentu = 0
		angka = 0
		self.url = url
		while penentu == 0:
			a = self.o_url(self.url)
			b = parser(a, 'html.parser')
			for s in b.find_all('a', string=stri):
				self.id.append("https://mbasic.facebook.com" + s.get('href'))
				angka += 1
				if angka == limit:
					penentu += 1
					break
			next = b.find('a', string=stri2)
			if "None" in str(next):
				break
			else:
				self.url = "https://mbasic.facebook.com" + next.get('href')
		self.id = self.filter(kondisi)
		
class Information(Core):
	def get_name_myself(self):
		data = self.mo_url("https://mbasic.facebook.com/me")
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')
	
	def get_name(self, id):
		data = self.mo_url("https://mbasic.facebook.com/profile.php?id="+id)
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')

class Like(Information):
	def hajar(self):
		for ss in self.id:
			cek = self.mo_url(ss)
			if "Konten Tidak Ditemukan" in str(cek):
				if not "mbasic_logout_button" in self.mo_url("https://mbasic.facebook.com"):
					self.kuki = update_kuki()
			elif "Peringatan: Jangan Terlalu Cepat" in str(cek):
				print("\n   [!] Process Stoped, Because Your Account Can't Like")
				enter()
			time.sleep(1)
		self.id.clear()
		
class React(Information):
	def hajar(self, re):
		if re == 1:
			stri = "Super"
		elif re == 2:
			stri = "Haha"
		elif re == 3:
			stri = "Wow"
		elif re == 4:
			stri = "Sedih"
		elif re == 5:
			stri = "Marah"
		for ss in self.id:
			ss = ss.split("&")[2].replace("ft_ent_identifier=", "")
			data = parser(self.mo_url('https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id='+ss), 'html.parser').find_all('a')
			for s in data:
				if stri in str(s):
					cek = self.mo_url("https://mbasic.facebook.com" + s.get('href'))
					if "Konten Tidak Ditemukan" in str(cek):
						if not "mbasic_logout_button" in self.o_url("https://mbasic.facebook.com"):
							self.kuki = update_kuki()
					elif "Peringatan: Jangan Terlalu Cepat" in str(cek):
						print("\n   [!] Process Stoped, Because Your Account Can't Like")
						enter()
					
class Friend(Information):
	def hajar(self):
		for ss in self.id:
			cek = self.o_url(ss)
			if "Konten Tidak Ditemukan" in cek:
				if not "mbasic_logout_button" in self.o_url("https://mbasic.facebook.com"):
					self.kuki = update_kuki()
		self.id.clear()
			
	