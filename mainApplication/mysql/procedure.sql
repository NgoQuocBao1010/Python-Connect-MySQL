use project;

-- Bang cong trinh
DELIMITER //
create procedure insertIntoCgtrinh(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
	Begin
		insert into  cgtrinh values (stt , tenCtr, dchi, tthanh, kphi , tenchu, tenthau, nbatdau); 
	End //
DELIMITER ;

-- call insertIntoCgtrinh(9 ,'nha rieng 2','76 chau van liem' ,'ha noi', 100, 'phan thanh liem', 'tran khai hoan', '1994-09-06');


DELIMITER //
create procedure updateCgtrinh(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
	Begin
		update cgtrinh set ten_ctr=tenCtr,diachi_ctr=dchi,tinh_thanh=tthanh,kinh_phi=kphi,ten_chu=tenchu,ten_thau=tenthau,ngay_bd=nbatdau where stt_ctr=stt;
	End //
DELIMITER ;
-- call updateCgtrinh(18 ,'testtest','76 chau van liem' ,'ha noi', 100, 'phan thanh liem', 'tran khai hoan', '1994-09-06');


DELIMITER //
create procedure xoaCgtrinh(stt int)
	Begin
		delete from cgtrinh where stt_ctr=stt;
    End//
DELIMITER ;
-- call xoaCgtrinh(9);


DELIMITER //
create procedure tongKinhPhiCacCongTrinh()
	Begin
		select sum(kinh_phi) from cgtrinh;
    End//
DELIMITER ;
-- call tongKinhPhiCacCongTrinh();





-- Bang chu thau
DELIMITER //
create procedure insertIntoChuthau(tenthau varchar(50), tel char(7), dchi varchar(50))
	Begin
		insert into  chuthau values (tenthau, tel, dchi); 
	End //
DELIMITER ;
-- call insertIntoChuthau('cty TNHH NCHM', '1212', 'cau Hung Loi');

DELIMITER //
create procedure updateChuthau(tenthaucu varchar(50), tenthaumoi varchar(50), sdt char(7), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chuthau set ten_thau=tenthaumoi, tel=sdt, dchi_thau=dchi where ten_thau=tenthaucu;
        update cgtrinh set ten_thau=tenthaumoi where ten_thau=tenthaucu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;
-- update chuthau set ten_thau='xin chao111' where ten_thau='cccccc';
-- call updateChuthau('nchm2', 'nchm3', '123', 'ct');

DELIMITER //
create procedure xoaChuThau(tenthau varchar(50))
	Begin
		delete from chuthau where ten_thau=tenthau;
    End//
DELIMITER ;
-- call xoaChuThau('nchm2');






-- Bang Chu Nhan
DELIMITER //
create procedure insertIntoChunhan(tenthau varchar(50), dchi varchar(50))
	Begin
		insert into chunhan values (tenthau, dchi); 
	End //
DELIMITER ;
-- call insertIntoChunhan('NCHM', 'cau Hung Loi');

DELIMITER //
create procedure updateChunhan(tenchucu varchar(50),tenchumoi varchar(50), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chunhan set ten_chu=tenchumoi, dchi_chu=dchi where ten_chu=tenchucu; 
        update cgtrinh set ten_chu=tenchumoi where ten_chu=tenchucu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;

DELIMITER //
create procedure xoaChuNhan(tenchu varchar(50))
	Begin
		delete from chunhan where ten_chu=tenchu;
    End//
DELIMITER ;
-- call xoaChuNhan('bao bao');






-- Bang Cong Nhan
DELIMITER //
create procedure insertIntoCongnhan(tencn varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
	Begin
		insert into congnhan values (tencn, nsinh, nvaonghe, cmon); 
	End //
DELIMITER ;
-- call insertIntoCongnhan('NCHM', 2000, 2012, 'java');

DELIMITER //
create procedure updateCongnhan(tencncu varchar(50),tencnmoi varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update congnhan set HOTEN_CN = tencnmoi, NAMS_CN = nsinh, NAM_VAO_N = nvaonghe, CH_MON = cmon where HOTEN_CN = tencncu;
        update thamgia set HOTEN_CN = tencnmoi where HOTEN_CN = tencncu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;

DELIMITER //
create procedure xoaCongNhan(tencn varchar(50))
	Begin
		delete from congnhan where hoten_cn=tencn;
    End//
DELIMITER ;
-- call xoaCongNhan('test');







-- Bang KTS
DELIMITER //
create procedure insertIntoKtrucsu(tenKts varchar(50), nskts int, phai varchar(10), noitn varchar(50), dchi varchar(50))
	Begin
		insert into ktrucsu values (tenkts, nskts, phai, noitn, dchi); 
	End //
DELIMITER ;
-- call insertIntoKtrucsu('NCHM', 2000, 1, 'new york', 'cau hung loi');

DELIMITER //
create procedure updateKtrucsu(tenKtscu varchar(50),tenKtsmoi varchar(50), nskts int, phai varchar(10), noitn varchar(50), dchi varchar(50))
	Begin
		set FOREIGN_KEY_CHECKS = 0;
		update ktrucsu set HOTEN_KTS = tenKtsmoi, NAMS_KTS = nskts, PHAI = phai, NOI_TN = noitn, DCHI_LL_KTS = dchi where hoten_kts = tenKtscu; 
        update thietke set HOTEN_KTS = tenKtsmoi where HOTEN_KTS = tenKtscu;
        set FOREIGN_KEY_CHECKS = 1;
	End //
DELIMITER ;


DELIMITER //
create procedure xoaKtrucsu(tenKts varchar(50))
	Begin
		delete from ktrucsu where hoten_kts=tenKts;
    End//
DELIMITER ;
-- call xoaCongNhan('test');




-- Bang Tham gia
DELIMITER //
create procedure getTenCongTrinhTuCongNhan(hotencn varchar(50))
	Begin
		select ten_ctr, ngay_tgia, so_ngay
        from cgtrinh c inner join thamgia tg 
        on c.stt_ctr=tg.stt_ctr
        where tg.hoten_cn=hotencn;
	End //
DELIMITER ;
-- call getTenCongTrinhTuCongNhan('nguyen thi suu');



DELIMITER //
create procedure getCongNhanTuCTrinh(sttctr varchar(50))
	Begin
		select hoten_cn, ngay_tgia, so_ngay from thamgia
        where stt_ctr=sttctr;
	End //
DELIMITER ;
-- call getCongNhanTuCTrinh(10);


DELIMITER //
create procedure themCongNhanLamViec(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
	Begin
		insert into thamgia values (hotencn, sttCtr, ngayTg, songay);
	End //
DELIMITER ;
-- call themCongNhanLamViec('dang van son', 10, '1994-12-18', 12);



DELIMITER //
create procedure suaThongTinCongNhanLamViec(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
	Begin
		update thamgia set so_ngay=songay, ngay_tgia=ngayTg
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End //
DELIMITER ;
-- call suaThongTinCongNhanLamViec('nguyen thi suu', 5, '1994-12-18', 30);



DELIMITER //
create procedure xoaCongNhanLamViec(hotencn varchar(50), sttCtr int)
	Begin
		delete from thamgia 
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End //
DELIMITER ;
-- call xoaCongNhanLamViec('nguyen thi suu', 5);

DELIMITER //
create procedure congNhanLamViecNhieuCongTrinhNhat()
	Begin
		select hoten_cn from thamgia
		group by hoten_cn having count(stt_ctr) = 
			(select max(tg) from 
				(select hoten_cn, count(stt_ctr) tg
				from thamgia
				group by hoten_cn) as T);
	End //
DELIMITER ;
-- call congNhanLamViecNhieuNhat();

DELIMITER //
create procedure congNhanLamViecNhieuNgayNhat()
	Begin
		select hoten_cn, sum(so_ngay) from thamgia
		group by hoten_cn having sum(so_ngay) = 
			(select max(tg) from 
				(select hoten_cn, sum(so_ngay) tg
				from thamgia
				group by hoten_cn) as T);
	End //
DELIMITER ;
-- call congNhanLamViecNhieuNhat();


















-- Bang Thiet Ke
DELIMITER //
create procedure getCongTrinhTuKTS(hotenkts varchar(50))
	Begin
		select ten_ctr, tk.thu_lao
        from cgtrinh c inner join thietke tk
        on c.stt_ctr=tk.stt_ctr
        where tk.hoten_kts=hotenkts;
	End //
DELIMITER ;
-- call getCongTrinhTuKTS('le thanh tung');


DELIMITER //
create procedure getKTSTuCTrinh(sttctr int)
	Begin
		select hoten_kts, thu_lao from thietke
        where stt_ctr = sttctr;
	End //
DELIMITER ;
-- call getKTSTuCTrinh(1);


DELIMITER //
create procedure themKTSLamViec(hotenkts varchar(50), sttCtr int, thulao int)
	Begin
		insert into thietke values (hotenkts, sttCtr, thulao);
	End //
DELIMITER ;
-- call themKTSLamViec('truong minh thai', 7, 30);



DELIMITER //
create procedure suaThongTinKTSLamViec(hotenkts varchar(50), sttCtr int, thulao int)
	Begin
		update thietke set thu_lao=thulao
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End //
DELIMITER ;
-- call suaThongTinKTSLamViec('truong minh thai', 7, 13);



DELIMITER //
create procedure xoaKTSLamViec(hotenkts varchar(50), sttCtr int)
	Begin
		delete from thietke 
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End //
DELIMITER ;
-- call xoaKTSLamViec('truong minh thai', 7); 



DELIMITER //
create procedure ktsLamViecNhieuCtrinhNhat()
	Begin
		select hoten_kts from thietke
		group by hoten_kts having count(stt_ctr) = 
			(select max(tg) from 
				(select hoten_kts, count(stt_ctr) tg
				from thietke
				group by hoten_kts) as T);
	End //
DELIMITER ;





DELIMITER //
create procedure ktsCoThulaoNhieuNhat()
	Begin
		select hoten_kts from thietke
		group by hoten_kts having sum(thu_lao) = 
			(select max(tg) from 
				(select hoten_kts, sum(thu_lao) tg
				from thietke
				group by hoten_kts) as T);
	End //
DELIMITER ;

