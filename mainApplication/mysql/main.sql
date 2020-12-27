create database project character set utf8mb4;
use project;
drop database project;


CREATE TABLE CGTRINH (
	STT_CTR int NOT NULL ,
	TEN_CTR varchar(50)  NULL ,
	DIACHI_CTR varchar(50)  NULL ,
	TINH_THANH varchar (50)  NULL ,
	KINH_PHI int NULL ,
	TEN_CHU varchar (50)  NULL ,
	TEN_THAU varchar (50)  NULL ,
	NGAY_BD date NULL,
    primary key(stt_ctr),
    FOREIGN KEY (TEN_CHU) REFERENCES  CHUNHAN (	TEN_CHU	) on delete set null,
    FOREIGN KEY (TEN_THAU) REFERENCES  CHUTHAU (TEN_THAU) on delete set null
);


CREATE TABLE  CHUNHAN (
	TEN_CHU varchar (50)  NOT NULL ,
	DCHI_CHU varchar (50)  NULL ,
    primary key(ten_chu)
) ;


CREATE TABLE  CHUTHAU (
	TEN_THAU varchar (50)  NOT NULL ,
	TEL char (7)  NULL ,
	DCHI_THAU varchar (50)  NULL ,
    primary key(ten_thau)
) ;


CREATE TABLE  CONGNHAN (
	HOTEN_CN varchar (50)  NOT NULL ,
	NAMS_CN int NULL ,
	NAM_VAO_N int NULL ,
	CH_MON varchar (50)  NULL, 
    primary key(hoten_cn)
) ;


CREATE TABLE  KTRUCSU (
	HOTEN_KTS varchar (50)  NOT NULL ,
	NAMS_KTS int NULL ,
	PHAI char (10)  NULL ,
	NOI_TN varchar (50)  NULL ,
	DCHI_LL_KTS varchar (50)  NULL ,
    primary key(hoten_kts)
) ;


CREATE TABLE  THAMGIA (
	HOTEN_CN varchar (50)  NOT NULL ,
	STT_CTR int NOT NULL ,
	NGAY_TGIA date NULL ,
	SO_NGAY int NULL ,
    PRIMARY KEY  (HOTEN_CN,	STT_CTR	),
    FOREIGN KEY (STT_CTR) REFERENCES  CGTRINH (STT_CTR) on delete cascade,
    FOREIGN KEY (HOTEN_CN) REFERENCES  CONGNHAN (HOTEN_CN) on delete cascade
) ;


CREATE TABLE  THIETKE (
	HOTEN_KTS varchar (50)  NOT NULL ,
	STT_CTR int NOT NULL ,
	THU_LAO int NULL ,
	PRIMARY KEY  (HOTEN_KTS, STT_CTR),
	FOREIGN KEY (STT_CTR) REFERENCES  CGTRINH (STT_CTR) on delete cascade,
    FOREIGN KEY (HOTEN_KTS) REFERENCES  KTRUCSU (HOTEN_KTS) on delete cascade
) ;


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

insert into  congnhan values ('Nguyễn Thị Sửu', 1945, 1960, 'hồ');
insert into  congnhan values ('Vĩ Chí A',1966, 1987, 'hàn');
insert into  congnhan values ('Lê Mạnh Quốc', 1956, 1971, 'mộc');
insert into  congnhan values ('Võ Văn Chín', 1940 , 1952, 'sơn');
insert into  congnhan values ('Lê Quyết Thắng', 1954, 1974, 'sơn');
insert into  congnhan values ('Nguyễn Hồng Vân', 1950, 1970, 'điện');
insert into  congnhan values ('Đặng Văn Sơn', 1948, 1965, 'điện');


insert into  ktrucsu values ('Lê Thanh Tùng', 1956, 'Nam', 'TP Hồ Chí Minh', '25 đường 3/2 TP Biên Hòa');
insert into  ktrucsu values ('Lê Kim Dung', 1952, 'Nữ', 'Hà Nội', '18/5 Phan Văn Trị TP Cần Thơ');
insert into  ktrucsu values ('Nguyễn Anh Thư', 1970, 'Nữ', 'New York USA', 'Khu 1 ĐH Cần Thơ');
insert into  ktrucsu values ('Nguyễn Song Đỗ Quyên', 1970, 'Nữ', 'TP Hồ Chí Minh', '73 Trần Hưng Đạo TP Hồ Chí Minh');
insert into  ktrucsu values ('Trương Minh Thái', 1950, 'Nam', 'Paris France', '12/2/5 Trần Phú TP Hà Nội');
insert into  ktrucsu values ('Trương Minh Thái', 1950, 'Nam', 'Paris France', '12/2/5 Trần Phú TP Hà Nội');

insert into cgtrinh values 
(1, 'Khách Sạn Quốc Tế', '5 Nguyễn An Ninh', 'Cần Thơ' , 450, 'Sở Thương Mại Du Lịch', 'Công Ty Xăng Dầu Số 6', '1994-12-13'); 
insert into cgtrinh values 
(2, 'Công Viên Thiếu Nhi', '100 Nguyễn Thái Học', 'Cần Thơ', 200, 'Sở Văn Hóa Thông Tin', 'Công Ty Xăng Dầu Số 6', '1994-05-08'); 
insert into cgtrinh values 
(3, 'Hội Chợ Nông Nghiệp', 'Bãi Cát', 'Vĩnh Long', 1000, 'Sở Thương Mại Du Lịch', 'Phòng Dịch Vụ Sở Xây Dựng', '1994-06-10'); 
insert into cgtrinh values 
(4, 'Trường mẫu giáo Măng Non', '48 Cách Mạng Tháng 8', 'Cần Thơ', 30, 'Sở Giáo Dục', 'Lê Văn Sơn', '1994-06-10'); 
insert into cgtrinh values 
(5, 'Khoa Trồng Trọt ĐHCT', 'Khu II ĐHCT', 'Cần Thơ', 3000, 'Đại Học Cần Thơ', 'Lê Văn Sơn', '1994-06-10'); 
insert into cgtrinh values 
(6, 'Văn Phòng Bitis', '25 Phan Đình Phùng', 'Hà Nội', 40, 'Công Ty Bitis', 'Lê Văn Sơn', '1994-10-05'); 
insert into cgtrinh values 
(7, 'Nhà riêng 1', '124/5 Nguyễn Trãi', 'TP Hồ Chí Minh', 65, 'Nguyễn Thanh Hà', 'Phòng Dịch Vụ Sở Xây Dựng', '1994-11-15'); 
insert into cgtrinh values 
(8, 'Nhà riêng 2',' 76 Châu Văn Liêm', 'Hà Nội', 100, 'Phan Thanh Liêm', 'Trần Khải Hoàn', '1994-09-06'); 

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