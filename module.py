class Core:
	def __init__(self):
		self.id = []
		try:
			self.kuki = eval(open('kuki.txt').read())['kuki']
		except:
			self.kuki = ""
	
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
			
	def mo_url(self, url):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('Cookie', self.kuki), ('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36')]
		return str(br.open(url).read())
	
	def o_url(self, url):
		data = r.get(url, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'Cookie':self.kuki}).text
		return data
	
	def dump_sts(self, url, stri, stri2, limit):
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
		
class Information(Core):
	def get_name_myself(self):
		data = self.mo_url("https://mbasic.facebook.com/me")
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')
	
	def get_name(self, id):
		data = self.mo_url("https://mbasic.facebook.com/profile.php?id="+id)
		return str(parser(data, 'html.parser').find('title')).replace('<title>', '').replace('</title>', '')

class Like(Information):
	def hajar(self, stri):
		for ss in self.id:
			if stri in ss:
				cek = self.mo_url(ss)
				if "Konten Tidak Ditemukan" in cek:
					if not "mbasic_logout_button" in self.o_url("https://mbasic.facebook.com"):
						self.kuki = update_kuki()

class Other(Information):
	def hajar(self, stri):
		for ss in self.id:
			if stri in ss:
				cek = self.o_url(ss)
				if "Konten Tidak Ditemukan" in cek:
					if not "mbasic_logout_button" in self.o_url("https://mbasic.facebook.com"):
						self.kuki = update_kuki()
	