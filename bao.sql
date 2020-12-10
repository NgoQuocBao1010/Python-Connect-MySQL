create database project character set utf8mb4;
use project;


CREATE TABLE CGTRINH (
	STT_CTR int NOT NULL ,
	TEN_CTR varchar(50)  NULL ,
	DIACHI_CTR varchar(50)  NULL ,
	TINH_THANH varchar (50)  NULL ,
	KINH_PHI int NULL ,
	TEN_CHU varchar (50)  NULL ,
	TEN_THAU varchar (50)  NULL ,
	NGAY_BD date NULL 
);


CREATE TABLE  CHUNHAN (
	TEN_CHU varchar (50)  NOT NULL ,
	DCHI_CHU varchar (50)  NULL 
) ;


CREATE TABLE  CHUTHAU (
	TEN_THAU varchar (20)  NOT NULL ,
	TEL char (7)  NULL ,
	DCHI_THAU varchar (20)  NULL 
) ;


CREATE TABLE  CONGNHAN (
	HOTEN_CN varchar (50)  NOT NULL ,
	NAMS_CN int NULL ,
	NAM_VAO_N int NULL ,
	CH_MON varchar (50)  NULL 
) ;


CREATE TABLE  KTRUCSU (
	HOTEN_KTS varchar (50)  NOT NULL ,
	NAMS_KTS int NULL ,
	PHAI char (2)  NULL ,
	NOI_TN varchar (50)  NULL ,
	DCHI_LL_KTS varchar (30)  NULL 
) ;


CREATE TABLE  THAMGIA (
	HOTEN_CN varchar (50)  NOT NULL ,
	STT_CTR int NOT NULL ,
	NGAY_TGIA date NULL ,
	SO_NGAY int NULL 
) ;


CREATE TABLE  THIETKE (
	HOTEN_KTS varchar (50)  NOT NULL ,
	STT_CTR int NOT NULL ,
	THU_LAO int NULL 
) ;


ALTER TABLE  CGTRINH ADD 
	CONSTRAINT PK_CGTRINH PRIMARY KEY  	(STT_CTR)  ; 


ALTER TABLE  CHUNHAN ADD 
	CONSTRAINT PK_CHUNHAN PRIMARY KEY  (	TEN_CHU	)  ; 


ALTER TABLE  CHUTHAU ADD 
	CONSTRAINT PK_CHUTHAU PRIMARY KEY  (	TEN_THAU	)  ; 


ALTER TABLE  CONGNHAN ADD 
	CONSTRAINT PK_CONGNHAN PRIMARY KEY  (	HOTEN_CN	)  ; 


ALTER TABLE  KTRUCSU ADD 
	CONSTRAINT PK_KTRUCSU PRIMARY KEY  	(	HOTEN_KTS	)  ; 


ALTER TABLE  THAMGIA ADD 
	CONSTRAINT PK_THAMGIA PRIMARY KEY  	(	HOTEN_CN,	STT_CTR	)  ; 


ALTER TABLE  THIETKE ADD 
	CONSTRAINT PK_THIETKE PRIMARY KEY  	(	HOTEN_KTS,	STT_CTR	)  ; 


ALTER TABLE  CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUNHAN FOREIGN KEY 	(	TEN_CHU	) REFERENCES  CHUNHAN (	TEN_CHU	);

ALTER TABLE  CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUTHAU FOREIGN KEY 
	(	TEN_THAU	) REFERENCES  CHUTHAU (	TEN_THAU	);


ALTER TABLE  THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CGTRINH FOREIGN KEY 
	(		STT_CTR	) REFERENCES  CGTRINH (		STT_CTR	);

ALTER TABLE  THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CONGNHAN FOREIGN KEY 
	(		HOTEN_CN	) REFERENCES  CONGNHAN (		HOTEN_CN	);


ALTER TABLE  THIETKE ADD 
	CONSTRAINT FK_THIETKE_CGTRINH FOREIGN KEY 	(STT_CTR) REFERENCES  CGTRINH (	STT_CTR	);

ALTER TABLE  THIETKE ADD 
	CONSTRAINT FK_THIETKE_KTRUCSU FOREIGN KEY 
	(	HOTEN_KTS	) REFERENCES  KTRUCSU (	HOTEN_KTS );


insert into  chunhan values ('so thuong mai du lich', '54 xo viet nghe tinh');
insert into  chunhan values ('so van hoa thong tin', '101 hai ba trung');
insert into  chunhan values ('so giao duc','29 duong 3/2');
insert into  chunhan values ('dai hoc can tho','56 duong 30/4');
insert into  chunhan values ('cty bitis','29 phan dinh phung');
insert into  chunhan values ('nguyen thanh ha','45 de tham');
insert into  chunhan values ('phan thanh liem','48/6 huynh thuc khan');


insert into  chuthau values ('cty xd so 6','567456','5 phan chu trinh');
insert into  chuthau values ('phong dich vu so xd','206481','2 le van sy');
insert into  chuthau values ('le van son','028374','12 tran nhan ton');
insert into  chuthau values ('tran khai hoan','658432','20 nguyen thai hoc');

insert into  congnhan values ('nguyen thi suu', 45 , 60, 'ho');
insert into  congnhan values ('vi chi a', 66  , 87, 'han');
insert into  congnhan values ('le manh quoc', 56, 71, 'moc');
insert into  congnhan values ('vo van chin', 40 , 52, 'son');
insert into  congnhan values ('le quyet thang', 54, 74,'son');
insert into  congnhan values ('nguyen hong van', 50, 70,'dien');
insert into  congnhan values ('dang van son', 48, 65,'dien');


insert into  ktrucsu values ('le thanh tung',   1956          ,'1','tp hcm','25 duong 3/2 tp bien hoa');
insert into  ktrucsu values ('le kim dung',   1952          ,'0','ha noi','18/5 phan van tri tp can tho');
insert into  ktrucsu values ('nguyen anh thu',   1970          ,'0','new york usa','khu i dhct tp can tho');
insert into  ktrucsu values ('nguyen song do quyen',   1970          ,'0','tp hcm','73 tran hung dao tp hcm');
insert into  ktrucsu values ('truong minh thai',   1950          ,'1','paris france','12/2/5 tran phu tp hanoi');

insert into  cgtrinh values 
( 1       ,'khach san quoc te','5 nguyen an ninh','can tho',450 ,'so thuong mai du lich','cty xd so 6', '1994-12-13'); 
insert into  cgtrinh values 
( 2       ,'cong vien thieu nhi','100 nguyen thai hoc','can tho',   200         ,'so van hoa thong tin','cty xd so 6','1994-05-08'); 
insert into  cgtrinh values 
( 3       ,'hoi cho nong nghiep','bai cat','vinh long',   1000        ,'so thuong mai du lich','phong dich vu so xd','1994-06-10'); 
insert into  cgtrinh values 
( 4       ,'truong mg mang non','48 cm thang 8','can tho',   30          ,'so giao duc','le van son','1994-06-10'); 
insert into  cgtrinh values 
( 5       ,'khoa trong trot dhct','khu ii dhct','can tho',   3000        ,'dai hoc can tho','le van son','1994-06-10'); 
insert into  cgtrinh values 
( 6       ,'van phong bitis','25 phan dinh phung','ha noi',   40          ,'cty bitis','le van son','1994-10-05'); 
insert into  cgtrinh values 
( 7       ,'nha rieng 1','124/5 nguyen trai','tp hcm',   65          ,'nguyen thanh ha','phong dich vu so xd','1994-11-15'); 
insert into  cgtrinh values 
( 8       ,'nha rieng 2','76 chau van liem','ha noi',   100         ,'phan thanh liem','tran khai hoan','1994-09-06'); 

insert into  thamgia values ('nguyen thi suu',   2       ,'1994-05-08',   20          );
insert into  thamgia values ('nguyen thi suu',   4       ,'1994-09-07',   20          );
insert into  thamgia values ('nguyen thi suu',   1       ,'1994-12-15',   5           );
insert into  thamgia values ('le manh quoc',   1       ,'1994-12-18',   6           );
insert into  thamgia values ('vo van chin',   2       ,'1994-05-10',   10          );
insert into  thamgia values ('le quyet thang',   2       ,'1994-05-12',   5           );
insert into  thamgia values ('nguyen hong van',   1       ,'1994-12-16',   7           );
insert into  thamgia values ('nguyen hong van',   4       ,'1994-09-14',   7           );
insert into  thamgia values ('dang van son',   3       ,'1994-06-10',   18          );
insert into  thamgia values ('vo van chin',   3       ,'1994-06-10',   10          );



insert into  thietke values ('le thanh tung',   1       ,    25          );
insert into  thietke values ('le kim dung',   5       ,    30          );
insert into  thietke values ('truong minh thai',   8       ,    18          );
insert into  thietke values ('le kim dung',   6       ,    40          );
insert into  thietke values ('nguyen anh thu',   3       ,    12          );
insert into  thietke values ('le thanh tung',   7       ,    10          );
insert into  thietke values ('nguyen song do quyen',   2       ,    6           );
insert into  thietke values ('truong minh thai',   6       ,    27          );
insert into  thietke values ('le kim dung',   4       ,    20          );
insert into  thietke values ('truong minh thai',   1       ,    12          );





call getKTSbyCtrinh(6, t);

SET @v1 := (select max(stt_ctr) from cgtrinh) ;
SELECT @v1;

DELIMITER //
create procedure insertIntoCgtrinh(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
	Begin
		insert into  cgtrinh values (stt , tenCtr, dchi, tthanh, kphi , tenchu, tenthau, nbatdau); 
	End //
DELIMITER ;

call insertIntoCgtrinh(9 ,'nha rieng 2','76 chau van liem' ,'ha noi', 100, 'phan thanh liem', 'tran khai hoan', '1994-09-06');


DELIMITER //
create procedure insertIntoChuthau(tenthau varchar(50), tel char(7), dchi varchar(50))
	Begin
		insert into  chuthau values (tenthau, tel, dchi); 
	End //
DELIMITER ;
call insertIntoChuthau('cty TNHH NCHM', '1212', 'cau Hung Loi');


DELIMITER //
create procedure insertIntoChunhan(tenthau varchar(50), dchi varchar(50))
	Begin
		insert into chunhan values (tenthau, dchi); 
	End //
DELIMITER ;
call insertIntoChunhan('NCHM', 'cau Hung Loi');


DELIMITER //
create procedure insertIntoCongnhan(tencn varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
	Begin
		insert into congnhan values (tencn, nsinh, nvaonghe, cmon); 
	End //
DELIMITER ;
call insertIntoCongnhan('NCHM', 2000, 2012, 'java');


DELIMITER //
create procedure insertIntoKtrucsu(tenKts varchar(50), nskts int, phai int, noitn varchar(50), dchi varchar(50))
	Begin
		insert into ktrucsu values (tenkts, nskts, phai, noitn, dchi); 
	End //
DELIMITER ;
call insertIntoKtrucsu('NCHM', 2000, 1, 'new york', 'cau hung loi');







