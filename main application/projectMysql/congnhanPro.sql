-- Bang Cong Nhan

-- Them cong nhan
DELIMITER //
create procedure insertIntoCongnhan(tencn varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
	Begin
		insert into congnhan values (tencn, nsinh, nvaonghe, cmon); 
	End //
DELIMITER ;

-- Update cong nhan
DELIMITER //
create procedure updateCongnhan(tencncu varchar(50),tencnmoi varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update congnhan set HOTEN_CN = tencnmoi, NAMS_CN = nsinh, NAM_VAO_N = nvaonghe, CH_MON = cmon where HOTEN_CN = tencncu;
        update thamgia set HOTEN_CN = tencnmoi where HOTEN_CN = tencncu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;

-- Xoa cong nhan
DELIMITER //
create procedure xoaCongNhan(tencn varchar(50))
	Begin
		delete from congnhan where hoten_cn=tencn;
    End//
DELIMITER ;