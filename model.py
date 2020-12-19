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
			'manyToMany': [Congnhan, Ktrucsu],
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
		obj = Congtrinh(*args)

		if edit:
			conn.cursor.callproc('updateCgtrinh', args)
		else:
			conn.cursor.callproc('insertIntoCgtrinh', args)

		conn.connection.commit()

		return obj

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
	
	def getPk(self):
		return self.stt

	def getKienTrucSu(self):
		conn = ConnectionToMySQl()
		args = (self.stt, )
		# args = ('nguyen thi suu', )
		conn.cursor.callproc('getKTSTuCTrinh', args)
		rs = conn.cursor.stored_results()

		for row in rs:
			data = row.fetchall()

		return data

	def getCongNhan(self):
		conn = ConnectionToMySQl()
		args = (self.stt, )
		# args = ('nguyen thi suu', )
		conn.cursor.callproc('getCongNhanTuCTrinh', args)
		rs = conn.cursor.stored_results()

		for row in rs:
			data = row.fetchall()

		return data


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
			},
			'manyToMany': [Congtrinh],
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
		obj = cls(*args)

		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateCongnhan', args)

		else:
			conn.cursor.callproc('insertIntoCongnhan', args)

		conn.connection.commit()

		return obj

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
	
	def getCongTrinh(self):
		conn = ConnectionToMySQl()
		args = (self.hotencn, )
		# args = ('nguyen thi suu', )
		conn.cursor.callproc('getTenCongTrinhTuCongNhan', args)
		rs = conn.cursor.stored_results()

		for row in rs:
			data = row.fetchall()

		return data
	
	def getPk(self):
		return self.hotencn
	
	def __str__(self):
		return self.hotencn


class Ktrucsu:
	table =  'ktrucsu'
	tableName = 'Kiến Trúc Sư'
	imptField = pk ='hoten_kts'
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
			},
			'manyToMany': [Congtrinh],
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
		
		obj = cls(*args)
		if edit:
			oldPk = values.get('oldPk')
			args = (oldPk, *args)
			conn.cursor.callproc('updateKtrucsu', args)

		else:
			conn.cursor.callproc('insertIntoKtrucsu', args)
		conn.connection.commit()

		return obj

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
	

	def getCongTrinh(self):
		conn = ConnectionToMySQl()
		args = (self.hotenkts, )
		# args = ('nguyen thi suu', )
		conn.cursor.callproc('getTenCongTrinhTuKTS', args)
		rs = conn.cursor.stored_results()

		for row in rs:
			data = row.fetchall()

		return data

	def getPk(self):
		return self.hotenkts

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
	
	@classmethod
	def saveToDatabase(cls, values, edit=False):
		try:
			values[2] = datetime.strptime(values[2], '%Y-%m-%d').date()
			values[3] = int(values[3])

		except Exception as e:
			raise Exception('Wrong Format or Data Type in Field Ngày tham gia or Số ngày')

		conn = ConnectionToMySQl()

		if type(values[1]) is not int:
			rs = conn.getQueryset(f"select stt_ctr from cgtrinh where ten_ctr='{values[1]}'")
			values[1] = rs[0][0]

		args = tuple(values)
		if edit:
			conn.cursor.callproc('suaThongTinCongNhanLamViec', args)

		else:
			conn.cursor.callproc('themCongNhanLamViec', args)

		conn.connection.commit()

	@classmethod
	def deleteFromDB(cls, values):
		conn = ConnectionToMySQl()

		if type(values[1]) is not int:
			rs = conn.getQueryset(f"select stt_ctr from cgtrinh where ten_ctr='{values[1]}'")
			values[1] = rs[0][0]

		args = tuple(values)
		conn.cursor.callproc('xoaCongNhanLamViec', args)
		conn.connection.commit()
	

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
		try:
			values[2] = int(values[2])

		except Exception as e:
			raise Exception('Wrong Format or Data Type in Field Thù Lao')

		conn = ConnectionToMySQl()

		if type(values[1]) is not int:
			rs = conn.getQueryset(f"select stt_ctr from cgtrinh where ten_ctr='{values[1]}'")
			values[1] = rs[0][0]

		args = tuple(values)
		if edit:
			conn.cursor.callproc('suaThongTinKTSLamViec', args)

		else:
			conn.cursor.callproc('themKTSLamViec', args)

		conn.connection.commit()

	@classmethod
	def deleteFromDB(cls, values):
		conn = ConnectionToMySQl()

		if type(values[1]) is not int:
			rs = conn.getQueryset(f"select stt_ctr from cgtrinh where ten_ctr='{values[1]}'")
			values[1] = rs[0][0]

		args = tuple(values)
		conn.cursor.callproc('xoaKTSLamViec', args)
		conn.connection.commit()
	
	def __init__(self, tenkts, sttctr, thu_lao):
		self.tenkts = tenkts
		self.stt_ctr = sttctr
		self.thulao = thu_lao

# Congtrinh.createAnObj()
# print(Congtrinh.createAnObj())
