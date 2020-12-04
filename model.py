

class ChuThau:
	def __init__(self, tenthau, tel, diachi):
		self.tenthau = tenthau
		self.tel = tel
		self.diachi = diachi



c = ChuThau('cty xd so 6', '123', 'so 5 phan chu trinh')
c.diachi = 'To Chau, Hung Phu'
print(c.diachi)