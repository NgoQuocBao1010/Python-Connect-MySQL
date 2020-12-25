-- Bang Chu Nhan

-- Them chu nhan
DELIMITER //
create procedure insertIntoChunhan(tenthau varchar(50), dchi varchar(50))
	Begin
		insert into chunhan values (tenthau, dchi); 
	End //
DELIMITER ;


-- Update chu nhan
DELIMITER //
create procedure updateChunhan(tenchucu varchar(50),tenchumoi varchar(50), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chunhan set ten_chu=tenchumoi, dchi_chu=dchi where ten_chu=tenchucu; 
        update cgtrinh set ten_chu=tenchumoi where ten_chu=tenchucu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;


-- Xoa chu nhan
DELIMITER //
create procedure xoaChuNhan(tenchu varchar(50))
	Begin
		delete from chunhan where ten_chu=tenchu;
    End//
DELIMITER ;