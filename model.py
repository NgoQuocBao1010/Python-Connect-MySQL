from mysqlConnection import ConnectionToMySQl
from datetime import datetime

class Congtrinh:
	tableName = 'cgtrinh'
	pk = 'stt_ctr'
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

	@classmethod
	def createAnObj(cls):
		x = ConnectionToMySQl()
		rs = x.getObject(cls.tableName)
		obj = Congtrinh(*rs)
		return obj

	@classmethod
	def detailsField(cls):
		return {
			'arribute': ['Tên Công Trình', 'Địa Chỉ', 
					'Tỉnh Thành', 'Kinh Phí (triệu đồng)', 
					'Ngày Bắt Đầu'
					],
			'forgeinKey': {
				'Tên Chủ': Chunhan, 
				'Tên Thầu': Chuthau,
			}
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


	def getArchitects(self):
		self.architects = []
		conn = ConnectionToMySQl()
		statement = f'select k.* from ktrucsu k join thietke t on k.hoten_kts=t.hoten_kts where stt_ctr = {self.stt}'
		rs = conn.getQueryset(statement)
		
		for rset in rs:
			arct = Ktrucsu(*rset)
			self.architects.append(arct)

	def getEngineers(self):
		self.engineers = []
		conn = ConnectionToMySQl()
		statement = f'select c.* from congnhan c join thamgia t on c.hoten_cn=t.hoten_cn where stt_ctr={self.stt}'
		rs = conn.getQueryset(statement)
		
		for rset in rs:
			eng = Congnhan(*rset)
			self.engineers.append(eng)

	def saveToDatabase(self, values):
		if self.stt is not None:
			raise Exception("New Data's ID Should Be None, Your Data may exist in Database")

		conn = ConnectionToMySQl()
		idCtr = max(conn.getQueryset('select stt_ctr from cgtrinh'))[0] + 1
		
		self.stt = idCtr

		try:
			self.kinhphi = int(self.kinhphi)
			self.ngaybatdau = datetime.strptime(self.ngaybatdau, '%Y-%m-%d').date()

		except Exception as e:
			raise Exception('Wrong Format or Data Type in Field kinhphi or ngaybatdau')

		
		insertStatement = f"insert into cgtrinh values ({self.stt}, '{self.tenctr}', '{self.diachi}', '{self.tinhthanh}', {self.kinhphi}, '{self.tenchu}', '{self.tenthau}', '{self.ngaybatdau}')"
		print(insertStatement)
		conn.cursor.execute(insertStatement)
		conn.connection.commit()


	def __str__(self):
		return self.tenctr



class Chuthau:
	tableName = 'chuthau'
	pk = 'ten_thau'
	colData = {}
	def __init__(self, tenthau, tel, diachi):
		self.tenthau = tenthau
		self.tel = tel
		self.diachi = diachi


class Chunhan:
	tableName = 'chunhan'
	pk = 'ten_chu'
	colData = {}
	
	def __init__(self, tenchu, diachi):
		self.tenchu = tenchu
		self.diachi = diachi


class Congnhan:
	tableName = 'congnhan'
	pk = 'hoten_cn'
	colData = {}

	def __init__(self, hotencn, namsinhcn, namvaonghe, chuyenmon):
		self.hotencn = hotencn
		self.namsinhcn = namsinhcn
		self.namvaonghe = namvaonghe
		self.chuyenmon = chuyenmon

	def __str__(self):
		return self.hotencn


class Ktrucsu:
	tableName = 'ktrucsu'
	colData = {}
	def __init__(self, hotenkts, namsinhkts, phai, noitn, diachi_ll_kts):
		self.hotenkts = hotenkts
		self.namsinhkts = namsinhkts
		self.phai = phai
		self.noitn = noitn
		self.diachi_ll_kts = diachi_ll_kts

	def __str__(self):
		return self.hotenkts



x = Congtrinh.createAnObj()
# print(x)
# print(type(x.ngaybatdau))

# y = 'xin chao'
# yTime = datetime.strptime(y, '%d-%m-%Y').date()
# print(yTime)

# x = ConnectionToMySQl()
# print(x.getObject('cgtrinh', ('stt_ctr', 3)))

data = (None, 'vincom', 'bai cat', 'vinh long', 5000, 'so thuong mai du lich', 'phong dich vu so xd', '2000-10-06')
# x = Congtrinh(*data).saveToDatabase(data)



