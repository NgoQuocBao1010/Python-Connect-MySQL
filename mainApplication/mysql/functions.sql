use project;


-- cong trinh hon 1 ty
DELIMITER $$
CREATE FUNCTION cgtrinhHon1ty(kphiCt int) 
	RETURNS int
DETERMINISTIC
BEGIN
	declare motTy int;
    
    if kphiCt >= 1000 then
		set motTy=True;
	else
		set motTy=False;
	end if;
    
    return (motTy);
END$$
DELIMITER ;



DELIMITER //
create procedure layCgtrinhHon1ty()
	Begin
		
		select ten_ctr
        from cgtrinh
        where cgtrinhHon1ty(kinh_phi)=True;
    End//
DELIMITER ;
-- call layCgtrinhHon1ty();



-- lay so cong trinh nhieu nhat
DELIMITER $$
CREATE FUNCTION soCtr1cgnhanLamnhieuI() 
	RETURNS int
DETERMINISTIC
BEGIN
	declare motTy int;
    
    if kphiCt >= 1000 then
		set motTy=True;
	else
		set motTy=False;
	end if;
    
    return (motTy);
END$$
DELIMITER ;










