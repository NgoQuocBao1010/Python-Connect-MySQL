-- Bang Tham Gia 


DELIMITER //
create procedure getTenCongTrinhTuCongNhan(hotencn varchar(50))
	Begin
		select ten_ctr 
        from cgtrinh c inner join thamgia tg 
        on c.stt_ctr=tg.stt_ctr
        where tg.hoten_cn=hotencn;
	End //
DELIMITER ;



DELIMITER //
create procedure getCongNhanTuCTrinh(sttctr varchar(50))
	Begin
		select hoten_cn from thamgia
        where stt_ctr=sttctr;
	End //
DELIMITER ;



DELIMITER //
create procedure themCongNhanLamViec(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
	Begin
		insert into thamgia values (hotencn, sttCtr, ngayTg, songay);
	End //
DELIMITER ;



DELIMITER //
create procedure suaThongTinCongNhanLamViec(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
	Begin
		update thamgia set so_ngay=songay, ngay_tgia=ngayTg
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End //
DELIMITER ;



DELIMITER //
create procedure xoaCongNhanLamViec(hotencn varchar(50), sttCtr int)
	Begin
		delete from thamgia 
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End //
DELIMITER ;