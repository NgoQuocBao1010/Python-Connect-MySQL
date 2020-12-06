class Congtrinh:
	tableName = 'cgtrinh'

	colData = {
		1 : {
			'width': 80,
			'anchor': 'c'
		},
		2 : {
			'width': 150,
			'anchor': 'c'
		},
		3 : {
			'width': 150,
			'anchor': 'c'
		},
		4 : {
			'width': 150,
			'anchor': 'c'
		},
		5 : {
			'width': 150,
			'anchor': 'c'
		},
		6 : {
			'width': 150,
			'anchor': 'c'
		},
		7 : {
			'width': 120,
			'anchor': 'c'
		},
		8 : {
			'width': 100,
			'anchor': 'c'
		},
	}

	def __init__(self, stt, tenctr, diachi, tinhthanh, kinhphi, tenchu, tenthau, ngaybatdau):
		self.stt = stt
		self.tenctr = tenctr
		self.diachi = diachi
		self.tinhthanh = tinhthanh
		self.kinhphi = kinhphi
		self.tenchu = tenchu
		self.tenthau = tenthau
		self.ngaybatdau = ngaybatdau


class Chuthau:
	tableName = 'chuthau'
	colData = {}
	def __init__(self, tenthau, tel, diachi):
		self.tenthau = tenthau
		self.tel = tel
		self.diachi = diachi


class Chunhan:
	tableName = 'chunhan'
	colData = {}
	def __init__(self, tenchu, diachi):
		self.tenchu = tenchu
		self.diachi = diachi


class Congnhan:
	tableName = 'congnhan'
	colData = {}
	def __init__(self, hotencn, namsinhcn, namvaonghe, chuyenmon):
		self.hoten = hoten
		self.namsinh = namsinh
		self.namvaonghe = namvaonghe
		self.chuyenmon = chuyenmon


class Ktrucsu:
	tableName = 'ktrucsu'
	colData = {}
	def __init__(self, hotenkts, namsinhkts, phai, noitn, diachi):
		self.hotenkts = hotenkts
		self.namsinhkts = namsinhkts
		self.phai = phai
		self.namvaonghe = namvaonghe
		self.chuyenmon = chuyenmon


# print(Congtrinh.tableName)
# x = 5 if 4 % 2 !=0 else 4
# print(x)