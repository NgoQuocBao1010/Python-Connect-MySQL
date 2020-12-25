-- BANG CONG TRINH

-- Them Cong trinh
DELIMITER //
create procedure insertIntoCgtrinh(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
	Begin
		insert into  cgtrinh values (stt , tenCtr, dchi, tthanh, kphi , tenchu, tenthau, nbatdau); 
	End //
DELIMITER ;


-- Update Cong Trinh
DELIMITER //
create procedure updateCgtrinh(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
	Begin
		update cgtrinh set ten_ctr=tenCtr,diachi_ctr=dchi,tinh_thanh=tthanh,kinh_phi=kphi,ten_chu=tenchu,ten_thau=tenthau,ngay_bd=nbatdau where stt_ctr=stt;
	End //
DELIMITER ;


-- Xoa Cong Trinh
DELIMITER //
create procedure xoaCgtrinh(stt int)
	Begin
		delete from cgtrinh where stt_ctr=stt;
    End//
DELIMITER ;