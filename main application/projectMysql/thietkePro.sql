-- Bang thiet ke 


DELIMITER //
create procedure getTenCongTrinhTuKTS(hotenkts varchar(50))
	Begin
		select ten_ctr 
        from cgtrinh c inner join thietke tk
        on c.stt_ctr=tk.stt_ctr
        where tk.hoten_kts=hotenkts;
	End //
DELIMITER ;



DELIMITER //
create procedure getKTSTuCTrinh(sttctr int)
	Begin
		select hoten_kts from thietke
        where stt_ctr = sttctr;
	End //
DELIMITER ;



DELIMITER //
create procedure themKTSLamViec(hotenkts varchar(50), sttCtr int, thulao int)
	Begin
		insert into thietke values (hotenkts, sttCtr, thulao);
	End //
DELIMITER ;



DELIMITER //
create procedure suaThongTinKTSLamViec(hotenkts varchar(50), sttCtr int, thulao int)
	Begin
		update thietke set thu_lao=thulao
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End //
DELIMITER ;



DELIMITER //
create procedure xoaKTSLamViec(hotenkts varchar(50), sttCtr int)
	Begin
		delete from thietke 
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End //
DELIMITER ;
