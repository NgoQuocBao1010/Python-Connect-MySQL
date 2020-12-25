-- Bang Kien Truc Su

-- Them kts
DELIMITER //
create procedure insertIntoKtrucsu(tenKts varchar(50), nskts int, phai int, noitn varchar(50), dchi varchar(50))
	Begin
		insert into ktrucsu values (tenkts, nskts, phai, noitn, dchi); 
	End //
DELIMITER ;

-- Update kts
DELIMITER //
create procedure updateKtrucsu(tenKtscu varchar(50),tenKtsmoi varchar(50), nskts int, phai int, noitn varchar(50), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update ktrucsu set HOTEN_KTS = tenKtsmoi, NAMS_KTS = nskts, PHAI = phai, NOI_TN = noitn, DCHI_LL_KTS = dchi where hoten_kts = tenKtscu; 
        update thietke set HOTEN_KTS = tenKtsmoi where HOTEN_KTS = tenKtscu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;

-- Xoa kts
DELIMITER //
create procedure xoaKtrucsu(tenKts varchar(50))
	Begin
		delete from ktrucsu where hoten_kts=tenKts;
    End//
DELIMITER ;