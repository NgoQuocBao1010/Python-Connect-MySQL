from mysqlConnection import ConnectionToMySQl
from datetime import datetime

class Congtrinh:
	table = 'cgtrinh'
	tableName = 'Công Trình'
	pk = 'stt_ctr'
	imptField = 'ten_ctr'
	colData = {
		1 : {
			'width': 50,
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

	sqlSyntax =  {
			'stt_ctr': 'STT',
			'ten_ctr': 'Tên Công Trình',
			'diachi_ctr': 'Địa Chỉ',
			'tinh_thanh': 'Tỉnh Thành',
			'kinh_phi': 'Kinh Phí',
			'ten_chu': 'Tên Chủ',
			'ten_thau': 'Tên Thầu',
			'ngay_bd': 'Ngày Bắt Đầu',
	}

	@classmethod
	def createAnObj(cls, condition=()):
		x = ConnectionToMySQl()
		rs = x.getObject(cls.table, condition)
		obj = dict(zip(list(cls.sqlSyntax.values()), rs))
		return obj

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Tên Công Trình', 'Địa Chỉ', 
					'Tỉnh Thành', 'Kinh Phí', 
					'Ngày Bắt Đầu'
					],
			'forgeinKey': {
				'Tên Chủ': Chunhan, 
				'Tên Thầu': Chuthau,
			},
			'manyToMany': {
				'Công Nhân': Congnhan,
				'Kiến Trúc Sư': Ktrucsu
			}
		}

	@classmethod
	def saveToDatabase(cls, values, edit=False):
		conn 		= ConnectionToMySQl()
		idCtr 		= max(conn.getQueryset('select stt_ctr from cgtrinh'))[0] + 1 if not edit else values.get('STT')
		tenctr 		= values.get('Tên Công Trình')
		dchi   		= values.get('Địa Chỉ')
		tthanh   	= values.get('Tỉnh Thành')
		kphi   		= values.get('Kinh Phí')
		ngaybd   	= values.get('Ngày Bắt Đầu')
		tenChu 		= values.get('Tên Chủ')
		tenThau 	= values.get('Tên Thầu')

		try:
			kphi = int(kphi)
			ngaybd = datetime.strptime(ngaybd, '%Y-%m-%d').date()

		except Exception as e:
			raise Exception('Wrong Format or Data Type in Field kinhphi or ngaybatdau')

		
		args = (idCtr, tenctr, dchi, tthanh, kphi, tenChu, tenThau, ngaybd)

		if edit:
			print(args)
			conn.cursor.callproc('updateCgtrinh', args)
		else:
			conn.cursor.callproc('insertIntoCgtrinh', args)

		conn.connection.commit()

		return True

	@classmethod
	def deleteFromDb(cls, values):
		for syn, field in cls.sqlSyntax.items():
			if syn == cls.pk:
				data = values.get(field)
				print("Du lieu xoa: ", data)

				try:
					args = (data, )
					conn 		= ConnectionToMySQl()
					conn.cursor.callproc('xoaCgtrinh', args)
					conn.connection.commit()
				except Exception as e:
					print(str(e))

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


	def __str__(self):
		return self.tenctr


class Chuthau:
	table = 'chuthau'
	tableName = 'Nhà Thầu'
	pk = 'ten_thau'
	imptField = 'ten_thau'
	sqlSyntax =  {
			'ten_thau': 'Tên Thầu',
			'tel': 'SDT',
			'dchi_thau': 'Địa Chỉ',
	}
	colData = {}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Tên Thầu', 'Địa Chỉ', 'SDT'],
			'forgeinKey': {
			}
	}

	# method to save data to database whether if the data is new or edited
	@classmethod
	def saveToDatabase(cls, values, edit=False):

		tenThau 	= values.get('Tên Thầu')
		dchi   		= values.get('Địa Chỉ')
		sdt 		= values.get('SDT')
		
		if not sdt.isdigit():
			raise Exception('Wrong Format or Data Type in Field Số điện thoại')

		conn = ConnectionToMySQl()
		args = (tenThau, sdt, dchi)

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateChuthau', args)

		else:
			conn.cursor.callproc('insertIntoChuthau', args)
		conn.connection.commit()


		return True

	@classmethod
	def deleteFromDb(cls, values):
		for syn, field in cls.sqlSyntax.items():
			if syn == cls.pk:
				data = values.get(field)
				print("Du lieu xoa: ", data)

				try:
					args = (data, )
					conn 		= ConnectionToMySQl()
					conn.cursor.callproc('xoaChuThau', args)
					conn.connection.commit()
				except Exception as e:
					print(str(e))

	def __init__(self, tenthau, tel, diachi):
		self.tenthau = tenthau
		self.tel = tel
		self.diachi = diachi


class Chunhan:
	table = 'chunhan'
	tableName = 'Chủ Nhà'
	pk = 'ten_chu'
	imptField = 'ten_chu'
	colData = {}
	sqlSyntax =  {
			'ten_chu': 'Tên Chủ',
			'dchi_chu': 'Địa Chỉ',
	}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Tên Chủ', 'Địa Chỉ'],
			'forgeinKey': {
			}
	}

	@classmethod
	def saveToDatabase(cls, values, edit=False):
		tenThau 	= values.get('Tên Chủ')
		dchi   		= values.get('Địa Chỉ')

		
		args = (tenThau, dchi)
		conn = ConnectionToMySQl()

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateChunhan', args)

		else:
			conn.cursor.callproc('insertIntoChunhan', args)

		conn.connection.commit()

		return True

	@classmethod
	def deleteFromDb(cls, values):
		for syn, field in cls.sqlSyntax.items():
			if syn == cls.pk:
				data = values.get(field)
				print("Du lieu xoa ", data)

				try:
					args = (data, )
					conn 		= ConnectionToMySQl()
					conn.cursor.callproc('xoaChuNhan', args)
					conn.connection.commit()
				except Exception as e:
					print(str(e))
	
	def __init__(self, tenchu, diachi):
		self.tenchu = tenchu
		self.diachi = diachi


class Congnhan:
	table = 'congnhan'
	tableName = 'Công Nhân'
	imptField = pk = 'hoten_cn'
	colData = {}
	sqlSyntax =  {
			'hoten_cn': 'Họ và tên',
			'nams_cn': 'Năm sinh',
			'nam_vao_n': 'Năm vào nghề',
			'ch_mon': 'Chuyên môn'
	}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Họ và tên', 'Năm sinh', 'Năm vào nghề', 'Chuyên môn'],
			'forgeinKey': {
			}
	}

	@classmethod
	def saveToDatabase(cls, values, edit=False):
		tenCn 		= values.get('Họ và tên')
		namsinhcn   = values.get('Năm sinh')
		namvaonghe  = values.get('Năm vào nghề')
		chuyenmon   = values.get('Chuyên môn')

		if not namsinhcn.isdigit() or not namvaonghe.isdigit():
			raise Exception('Wrong Format or Data Type in Field Năm sinh hoặc Năm vào nghề')

		if namsinhcn > namvaonghe:
			raise Exception('Năm sinh không lớn hơn Năm vào nghề')

		conn = ConnectionToMySQl()
		args = (tenCn, namsinhcn, namvaonghe, chuyenmon)

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateCongnhan', args)

		else:
			conn.cursor.callproc('insertIntoCongnhan', args)

		conn.connection.commit()

		return True

	@classmethod
	def deleteFromDb(cls, values):
		for syn, field in cls.sqlSyntax.items():
			if syn == cls.pk:
				data = values.get(field)
				print("Du lieu xoa ", data)

				try:
					args = (data, )
					conn 		= ConnectionToMySQl()
					conn.cursor.callproc('xoaCongNhan', args)
					conn.connection.commit()
				except Exception as e:
					print(str(e))

	def __init__(self, hotencn, namsinhcn, namvaonghe, chuyenmon):
		self.hotencn = hotencn
		self.namsinhcn = namsinhcn
		self.namvaonghe = namvaonghe
		self.chuyenmon = chuyenmon

	def __str__(self):
		return self.hotencn


class Ktrucsu:
	table =  'ktrucsu'
	tableName = 'Kiến Trúc Sư'
	imptField = pk='hoten_kts'
	colData = {}
	sqlSyntax =  {
			'hoten_kts': 'Họ và tên',
			'nams_kts': 'Năm sinh',
			'phai': 'Phái',
			'noi_tn': 'Nơi tốt nghiệp',
			'dchi_ll_kts': 'Địa chỉ'
	}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Họ và tên', 'Năm sinh', 'Phái', 'Nơi tốt nghiệp', 'Địa chỉ'],
			'forgeinKey': {
			}
	}

	@classmethod
	def saveToDatabase(cls, values, edit=False):
		args = ()

		tenkts 		= values.get('Họ và tên')
		namsinhkts  = values.get('Năm sinh')
		phai		= values.get('Phái')
		noitn   	= values.get('Nơi tốt nghiệp')
		dchi 		= values.get('Địa chỉ')

		if not phai.isdigit():
			raise Exception('Wrong Format or Data Type in Field Năm sinh')
		
		conn = ConnectionToMySQl()
		args = (tenkts, namsinhkts, phai, noitn, dchi)

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateKtrucsu', args)

		else:
			conn.cursor.callproc('insertIntoKtrucsu', args)
		conn.connection.commit()

		return True

	@classmethod
	def deleteFromDb(cls, values):
		for syn, field in cls.sqlSyntax.items():
			if syn == cls.pk:
				data = values.get(field)
				print("Du lieu xoa ", data)

				try:
					args = (data, )
					conn 		= ConnectionToMySQl()
					conn.cursor.callproc('xoaKtrucsu', args)
					conn.connection.commit()
				except Exception as e:
					print(str(e))

		

	def __init__(self, hotenkts, namsinhkts, phai, noitn, diachi_ll_kts):
		self.hotenkts = hotenkts
		self.namsinhkts = namsinhkts
		self.phai = phai
		self.noitn = noitn
		self.diachi_ll_kts = diachi_ll_kts

	def __str__(self):
		return self.hotenkts


class Thamgia:
	table =  'thamgia'
	tableName = 'Tham Gia'

	colData = {}
	sqlSyntax =  {
			'hoten_cn': 'Họ và tên',
			'stt_ctr': 'STT',
			'ngay_tgia': 'Ngày tham gia',
			'so_ngay': 'Số ngày',
	}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Họ và tên', 'Tên Công Trình', 'Ngày tham gia', 'Số ngày'],
		}

	def __init__(self, hotenCn, sttctr, ngayTG, soNgay):
		self.hoten_cn = hotenCn
		self.stt_ctr = sttctr
		self.ngay_tgia = ngayTG
		self.so_ngay = soNgay

class Thietke:
	table =  'thietke'
	tableName = 'Thiết Kế'

	colData = {}
	sqlSyntax =  {
			'hoten_cn': 'Họ và tên',
			'stt_ctr': 'STT',
			'thu_lao': 'Thù Lao',
	}

	@classmethod
	def formsField(cls):
		return {
			'arribute': ['Họ và tên', 'Tên Công Trình', 'Thù Lao'],
		}

	@classmethod
	def saveToDatabase(cls, values, edit=False):
		args = ()

		tenkts 		= values.get('Họ và tên')
		namsinhkts  = values.get('Năm sinh')
		phai		= values.get('Phái')
		noitn   	= values.get('Nơi tốt nghiệp')
		dchi 		= values.get('Địa chỉ')

		if not phai.isdigit():
			raise Exception('Wrong Format or Data Type in Field Năm sinh')
		
		conn = ConnectionToMySQl()
		args = (tenkts, namsinhkts, phai, noitn, dchi)

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateKtrucsu', args)

		else:
			conn.cursor.callproc('insertIntoKtrucsu', args)
		conn.connection.commit()

		return True

	def __init__(self, tenkts, sttctr, thu_lao):
		self.tenkts = tenkts
		self.stt_ctr = sttctr
		self.thulao = thu_lao

# Congtrinh.createAnObj()
# print(Congtrinh.createAnObj())
