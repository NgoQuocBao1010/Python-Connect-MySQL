create database project character set utf8mb4;
use project;
drop database project;

CREATE TABLE CGTRINH(
	STT_CTR int NOT NULL,
	TEN_CTR varchar(50) NULL,
	DIACHI_CTR varchar(50) NULL,
	TINH_THANH varchar(50) NULL,
	KINH_PHI varchar(50) NULL,
	TEN_CHU varchar(50) NULL,
	TEN_THAU varchar(50) NULL,
	NGAY_BD date NULL 
);


CREATE TABLE CHUNHAN(
	TEN_CHU varchar(50) NOT NULL ,
	DCHI_CHU varchar(50) NULL 
);


CREATE TABLE CHUTHAU(
	TEN_THAU varchar(50) NOT NULL,
	TEL char(7) NULL,
	DCHI_THAU varchar(20) NULL 
);


CREATE TABLE CONGNHAN(
	HOTEN_CN varchar(50) NOT NULL,
	NAMS_CN int NULL,
	NAM_VAO_N int NULL ,
	CH_MON varchar(50) NULL 
);


CREATE TABLE KTRUCSU(
	HOTEN_KTS varchar(50) NOT NULL,
	NAMS_KTS int NULL,
	PHAI char(10) NULL,
	NOI_TN varchar(50)  NULL,
	DCHI_LL_KTS varchar(50) NULL 
);


CREATE TABLE THAMGIA(
	HOTEN_CN varchar(50) NOT NULL ,
	STT_CTR int NOT NULL,
	NGAY_TGIA date NULL,
	SO_NGAY int NULL 
);


CREATE TABLE THIETKE(
	HOTEN_KTS varchar(50) NOT NULL,
	STT_CTR int NOT NULL,
	THU_LAO int NULL 
);

ALTER TABLE CGTRINH ADD 
	CONSTRAINT PK_CGTRINH PRIMARY KEY(STT_CTR); 

ALTER TABLE CHUNHAN ADD 
	CONSTRAINT PK_CHUNHAN PRIMARY KEY(TEN_CHU); 

ALTER TABLE CHUTHAU ADD 
	CONSTRAINT PK_CHUTHAU PRIMARY KEY(TEN_THAU); 

ALTER TABLE CONGNHAN ADD 
	CONSTRAINT PK_CONGNHAN PRIMARY KEY(HOTEN_CN); 

ALTER TABLE KTRUCSU ADD 
	CONSTRAINT PK_KTRUCSU PRIMARY KEY(HOTEN_KTS); 

ALTER TABLE THAMGIA ADD 
	CONSTRAINT PK_THAMGIA PRIMARY KEY(HOTEN_CN,	STT_CTR); 

ALTER TABLE THIETKE ADD 
	CONSTRAINT PK_THIETKE PRIMARY KEY(HOTEN_KTS, STT_CTR); 

ALTER TABLE CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUNHAN FOREIGN KEY (TEN_CHU) REFERENCES CHUNHAN(TEN_CHU);

ALTER TABLE CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUTHAU FOREIGN KEY 
	(TEN_THAU) REFERENCES CHUTHAU (TEN_THAU);

ALTER TABLE THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CGTRINH FOREIGN KEY 
	(STT_CTR) REFERENCES  CGTRINH (STT_CTR);

ALTER TABLE THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CONGNHAN FOREIGN KEY 
	(HOTEN_CN) REFERENCES CONGNHAN(HOTEN_CN);

ALTER TABLE THIETKE ADD 
	CONSTRAINT FK_THIETKE_CGTRINH FOREIGN KEY(STT_CTR) REFERENCES CGTRINH (STT_CTR);

ALTER TABLE THIETKE ADD 
	CONSTRAINT FK_THIETKE_KTRUCSU FOREIGN KEY 
	(HOTEN_KTS) REFERENCES KTRUCSU (HOTEN_KTS);

insert into  chunhan values ('Sở Thương Mại Du Lịch', '54 Xô Viết Nghệ Tĩnh');
insert into  chunhan values ('Sở Văn Hóa Thông Tin', '101 Hai Bà Trưng');
insert into  chunhan values ('Sở Giáo Dục', '29 đường 3/2');
insert into  chunhan values ('Đại Học Cần Thơ', '56 đường 30/4');
insert into  chunhan values ('Công Ty Bitis', '29 Phan Đình Phùng');
insert into  chunhan values ('Nguyễn Thanh Hà', '45 Đề Thám');
insert into  chunhan values ('Phan Thanh Liêm', '48/6 Huỳnh Thúc Kháng');


insert into  chuthau values ('Công ty Xăng Dầu số 6', '567456', '5 Phan Chu Trinh');
insert into  chuthau values ('Phòng Dịch Vụ Sở Xây Dựng', '206481', '2 Lê Văn Sỹ');
insert into  chuthau values ('Lê Văn Sơn', '028374', '12 Trần Nhân Tông');
insert into  chuthau values ('Trần Khải Hoàn', '658432', '20 Nguyễn Thái Học');

insert into  congnhan values ('Nguyễn Thị Sửu', 45, 60, 'hồ');
insert into  congnhan values ('Vĩ Chí A',66, 87, 'hàn');
insert into  congnhan values ('Lê Mạnh Quốc', 56, 71, 'mộc');
insert into  congnhan values ('Võ Văn Chín', 40 , 52, 'sơn');
insert into  congnhan values ('Lê Quyết Thắng', 54, 74, 'sơn');
insert into  congnhan values ('Nguyễn Hồng Vân', 50, 70, 'điện');
insert into  congnhan values ('Đặng Văn Sơn', 48, 65, 'điện');


insert into  ktrucsu values ('Lê Thanh Tùng', 1956, 'Nam', 'TP Hồ Chí Minh', '25 đường 3/2 TP Biên Hòa');
insert into  ktrucsu values ('Lê Kim Dung', 1952, 'Nữ', 'Hà Nội', '18/5 Phan Văn Trị TP Cần Thơ');
insert into  ktrucsu values ('Nguyễn Anh Thư', 1970, 'Nữ', 'New York USA', 'Khu 1 ĐH Cần Thơ');
insert into  ktrucsu values ('Nguyễn Song Đỗ Quyên', 1970, 'Nữ', 'TP Hồ Chí Minh', '73 Trần Hưng Đạo TP Hồ Chí Minh');
insert into  ktrucsu values ('Trương Minh Thái', 1950, 'Nam', 'Paris France', '12/2/5 Trần Phú TP Hà Nội');

insert into cgtrinh values 
(1, 'Khách Sạn Quốc Tế', '5 Nguyễn An Ninh', 'Cần Thơ' , '450 triệu', 'Sở Thương Mại Du Lịch', 'Công Ty Xăng Dầu Số 6', '1994-12-13'); 
insert into cgtrinh values 
(2, 'Công Viên Thiếu Nhi', '100 Nguyễn Thái Học', 'Cần Thơ', '200 triệu', 'Sở Văn Hóa Thông Tin', 'Công Ty Xăng Dầu Số 6', '1994-05-08'); 
insert into cgtrinh values 
(3, 'Hội Chợ Nông Nghiệp', 'Bãi Cát', 'Vĩnh Long', '1 tỷ', 'Sở Thương Mại Du Lịch', 'Phòng Dịch Vụ Sở Xây Dựng', '1994-06-10'); 
insert into cgtrinh values 
(4, 'Trường mẫu giáo Măng Non', '48 Cách Mạng Tháng 8', 'Cần Thơ', '30 triệu', 'Sở Giáo Dục', 'Lê Văn Sơn', '1994-06-10'); 
insert into cgtrinh values 
(5, 'Khoa Trồng Trọt ĐHCT', 'Khu II ĐHCT', 'Cần Thơ', '3 tỷ', 'Đại Học Cần Thơ', 'Lê Văn Sơn', '1994-06-10'); 
insert into cgtrinh values 
(6, 'Văn Phòng Bitis', '25 Phan Đình Phùng', 'Hà Nội', '40 triệu', 'Công Ty Bitis', 'Lê Văn Sơn', '1994-10-05'); 
insert into cgtrinh values 
(7, 'Nhà riêng 1', '124/5 Nguyễn Trãi', 'TP Hồ Chí Minh', '65 triệu', 'Nguyễn Thanh Hà', 'Phòng Dịch Vụ Sở Xây Dựng', '1994-11-15'); 
insert into cgtrinh values 
(8, 'Nhà riêng 2',' 76 Châu Văn Liêm', 'Hà Nội', '100 triệu', 'Phan Thanh Liêm', 'Trần Khải Hoàn', '1994-09-06'); 

insert into  thamgia values ('Nguyễn Thị Sửu', 2, '1994-05-08', 20);
insert into  thamgia values ('Nguyễn Thị Sửu', 4, '1994-09-07', 20);
insert into  thamgia values ('Nguyễn Thị Sửu', 1, '1994-12-15', 5);
insert into  thamgia values ('Lê Mạnh Quốc', 1, '1994-12-18', 6);
insert into  thamgia values ('Võ Văn Chín', 2, '1994-05-10', 10);
insert into  thamgia values ('Lê Quyết Thắng', 2, '1994-05-12', 5);
insert into  thamgia values ('Nguyễn Hồng Vân', 1, '1994-12-16', 7);
insert into  thamgia values ('Nguyễn Hồng Vân', 4, '1994-09-14', 7);
insert into  thamgia values ('Đặng Văn Sơn', 3, '1994-06-10', 18);
insert into  thamgia values ('Võ Văn Chín', 3, '1994-06-10', 10);


insert into  thietke values ('Lê Thanh Tùng', 1, 25);
insert into  thietke values ('Lê Kim Dung', 5, 30);
insert into  thietke values ('Trương Minh Thái', 8, 18);
insert into  thietke values ('Lê Kim Dung', 6, 40);
insert into  thietke values ('Nguyễn Anh Thư', 3, 12);
insert into  thietke values ('Lê Thanh Tùng', 7, 10);
insert into  thietke values ('Nguyễn Song Đỗ Quyên', 2, 6);
insert into  thietke values ('Trương Minh Thái', 6, 27);
insert into  thietke values ('Lê Kim Dung', 4, 20);
insert into  thietke values ('Trương Minh Thái', 1, 12);

-- 17
SELECT DISTINCT HOTEN_KTS 
FROM THIETKE 
WHERE THU_LAO < (SELECT AVG(THU_LAO) FROM THIETKE); 

-- 18 
SELECT CT.TEN_THAU, DCHI_THAU 
FROM CGTRINH CT JOIN CHUTHAU C ON CT.TEN_THAU = C.TEN_THAU
WHERE KINH_PHI = (SELECT MIN(KINH_PHI)FROM CGTRINH);

-- 19
SELECT T.HOTEN_CN, CH_MON
FROM THAMGIA T JOIN CGTRINH CT ON T.STT_CTR = CT.STT_CTR
			   JOIN CONGNHAN C ON C.HOTEN_CN = T.HOTEN_CN 
               JOIN THIETKE K ON K.STT_CTR = CT.STT_CTR 
WHERE HOTEN_KTS = 'Lê Kim Dung';

-- 20 
SELECT DISTINCT C1.TEN_THAU, C2.TEN_THAU
FROM CGTRINH C1 JOIN CGTRINH C2 ON C1.TINH_THANH = C2.TINH_THANH 
WHERE C1.TEN_THAU < C2.TEN_THAU;

-- 21
SELECT T1.HOTEN_CN, T2.HOTEN_CN
FROM THAMGIA T1 JOIN THAMGIA T2 ON T1.STT_CTR = T2.STT_CTR 
WHERE T1.HOTEN_CN > T2.HOTEN_CN 
GROUP BY T1.HOTEN_CN, T2.HOTEN_CN HAVING COUNT(*)>1;

-- 22 
SELECT TEN_THAU, SUM(KINH_PHI) TỔNG 
FROM CGTRINH 
GROUP BY TEN_THAU;

-- 23 
SELECT HOTEN_KTS, SUM(THU_LAO) TỔNG 
FROM THIETKE 
GROUP BY HOTEN_KTS HAVING SUM(THU_LAO) > 25;

-- 24 
SELECT COUNT(*)
FROM (SELECT HOTEN_KTS, SUM(THU_LAO) TỔNG
FROM THIETKE 
GROUP BY HOTEN_KTS HAVING SUM(THU_LAO) > 25) C24;

-- 25 
SELECT HOTEN_KTS, COUNT(*) SỐ_CTR
FROM THIETKE 
GROUP BY HOTEN_KTS;

-- 26 
SELECT STT_CTR, COUNT(*) SO_CN
FROM THAMGIA GROUP BY STT_CTR;

-- 27 
CREATE TABLE CAU27
	SELECT STT_CTR, COUNT(*) SO_CN 
    FROM THAMGIA 
    GROUP BY STT_CTR;
SELECT TEN_CTR, DIACHI_CTR
FROM CAU27 JOIN CGTRINH C ON CAU27.STT_CTR = C.STT_CTR 
WHERE SO_CN = (SELECT MAX(SO_CN) FROM CAU27);

-- 28 
SELECT TINH_THANH, AVG(KINH_PHI)
FROM CGTRINH 
GROUP BY TINH_THANH;

-- 29 
SELECT HOTEN_CN, SUM(SO_NGAY)
FROM THAMGIA 
GROUP BY HOTEN_CN HAVING SUM(SO_NGAY) > (SELECT SUM(SO_NGAY) FROM THAMGIA WHERE HOTEN_CN = 'Nguyễn Hồng Vân');

-- 30 
SELECT * FROM CGTRINH;

SELECT HOTEN_CN, COUNT(*) SỐ_CT 
FROM THAMGIA 
GROUP BY HOTEN_CN; -- HAVING COUNT(*) = (SELECT COUNT(*) FROM CGTRINH);

select * from cgtrinh;
CALL cgnhanThamgiatatcactrinh();



