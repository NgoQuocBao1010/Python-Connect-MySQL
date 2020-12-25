-- BANG CHU THAU

-- Them chu thau
DELIMITER //
create procedure insertIntoChuthau(ten_thau varchar(50), tel char(7), dchi_thau varchar(50))
	Begin
		insert into  chuthau values (ten_thau, tel, dchi_thau); 
	End //
DELIMITER ;


-- Update Chu thau
DELIMITER //
create procedure updateChuthau(tenthaucu varchar(50), tenthaumoi varchar(50), sdt char(7), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chuthau set ten_thau=tenthaumoi, tel=sdt, dchi_thau=dchi where ten_thau=tenthaucu;
        update cgtrinh set ten_thau=tenthaumoi where ten_thau=tenthaucu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;


-- Xoa chu thau 
DELIMITER //
create procedure xoaChuThau(tenthau varchar(50))
	Begin
		delete from chuthau where ten_thau=tenthau;
    End//
DELIMITER ;