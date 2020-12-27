CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cgtrinh`
--

DROP TABLE IF EXISTS `cgtrinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cgtrinh` (
  `STT_CTR` int NOT NULL,
  `TEN_CTR` varchar(50) DEFAULT NULL,
  `DIACHI_CTR` varchar(50) DEFAULT NULL,
  `TINH_THANH` varchar(50) DEFAULT NULL,
  `KINH_PHI` int DEFAULT NULL,
  `TEN_CHU` varchar(50) DEFAULT NULL,
  `TEN_THAU` varchar(50) DEFAULT NULL,
  `NGAY_BD` date DEFAULT NULL,
  PRIMARY KEY (`STT_CTR`),
  KEY `TEN_CHU` (`TEN_CHU`),
  KEY `TEN_THAU` (`TEN_THAU`),
  CONSTRAINT `cgtrinh_ibfk_1` FOREIGN KEY (`TEN_CHU`) REFERENCES `chunhan` (`TEN_CHU`) ON DELETE SET NULL,
  CONSTRAINT `cgtrinh_ibfk_2` FOREIGN KEY (`TEN_THAU`) REFERENCES `chuthau` (`TEN_THAU`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cgtrinh`
--

LOCK TABLES `cgtrinh` WRITE;
/*!40000 ALTER TABLE `cgtrinh` DISABLE KEYS */;
INSERT INTO `cgtrinh` VALUES (1,'Khách Sạn Quốc Tế','5 Nguyễn An Ninh','Cần Thơ',450,'Sở Thương Mại Du Lịch','Công Ty Xăng Dầu Số 6','1994-12-13'),(2,'Công Viên Thiếu Nhi','100 Nguyễn Thái Học','Cần Thơ',200,'Sở Văn Hóa Thông Tin','Công Ty Xăng Dầu Số 6','1994-05-08'),(3,'Hội Chợ Nông Nghiệp','Bãi Cát','Vĩnh Long',1000,'Sở Thương Mại Du Lịch','Phòng Dịch Vụ Sở Xây Dựng','1994-06-10'),(4,'Trường mẫu giáo Măng Non','48 Cách Mạng Tháng 8','Cần Thơ',30,'Sở Giáo Dục','Lê Văn Sơn','1994-06-10'),(5,'Khoa Trồng Trọt ĐHCT','Khu II ĐHCT','Cần Thơ',3000,'Đại Học Cần Thơ','Lê Văn Sơn','1994-06-10'),(6,'Văn Phòng Bitis','25 Phan Đình Phùng','Hà Nội',40,'Công Ty Bitis','Lê Văn Sơn','1994-10-05'),(7,'Nhà riêng 1','124/5 Nguyễn Trãi','TP Hồ Chí Minh',65,'Nguyễn Thanh Hà','Phòng Dịch Vụ Sở Xây Dựng','1994-11-15'),(8,'Nhà riêng 2',' 76 Châu Văn Liêm','Hà Nội',100,'Phan Thanh Liêm','Trần Khải Hoàn','1994-09-06'),(9,'Vincom Hưng Phú','123 Hưng Phú','Cần Thơ',1000,'Trọng Bùi','Công ty TNHH HMCN','2020-10-10');
/*!40000 ALTER TABLE `cgtrinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chunhan`
--

DROP TABLE IF EXISTS `chunhan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chunhan` (
  `TEN_CHU` varchar(50) NOT NULL,
  `DCHI_CHU` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TEN_CHU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chunhan`
--

LOCK TABLES `chunhan` WRITE;
/*!40000 ALTER TABLE `chunhan` DISABLE KEYS */;
INSERT INTO `chunhan` VALUES ('Công Ty Bitis','29 Phan Đình Phùng'),('Đại Học Cần Thơ','56 đường 30/4'),('Nguyễn Thanh Hà','45 Đề Thám'),('Phan Thanh Liêm','48/6 Huỳnh Thúc Kháng'),('Sở Giáo Dục','29 đường 3/2'),('Sở Thương Mại Du Lịch','54 Xô Viết Nghệ Tĩnh'),('Sở Văn Hóa Thông Tin','101 Hai Bà Trưng'),('Trọng Bùi','123 Ô Môn');
/*!40000 ALTER TABLE `chunhan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chuthau`
--

DROP TABLE IF EXISTS `chuthau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chuthau` (
  `TEN_THAU` varchar(50) NOT NULL,
  `TEL` char(7) DEFAULT NULL,
  `DCHI_THAU` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TEN_THAU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chuthau`
--

LOCK TABLES `chuthau` WRITE;
/*!40000 ALTER TABLE `chuthau` DISABLE KEYS */;
INSERT INTO `chuthau` VALUES ('Công ty TNHH HMCN','01234','Vĩnh Long'),('Công ty Xăng Dầu số 6','567456','5 Phan Chu Trinh'),('Lê Văn Sơn','028374','12 Trần Nhân Tông'),('Phòng Dịch Vụ Sở Xây Dựng','206481','2 Lê Văn Sỹ'),('Trần Khải Hoàn','658432','20 Nguyễn Thái Học');
/*!40000 ALTER TABLE `chuthau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `congnhan`
--

DROP TABLE IF EXISTS `congnhan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `congnhan` (
  `HOTEN_CN` varchar(50) NOT NULL,
  `NAMS_CN` int DEFAULT NULL,
  `NAM_VAO_N` int DEFAULT NULL,
  `CH_MON` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`HOTEN_CN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `congnhan`
--

LOCK TABLES `congnhan` WRITE;
/*!40000 ALTER TABLE `congnhan` DISABLE KEYS */;
INSERT INTO `congnhan` VALUES ('Bùi \"Kai\" Trọng',2000,2018,'Hàn'),('Đặng Văn Sơn',1948,1965,'điện'),('Lê Mạnh Quốc',1956,1971,'mộc'),('Lê Quyết Thắng',1954,1974,'sơn'),('Nguyễn Hồng Vân',1950,1970,'điện'),('Nguyễn Thị Sửu',1945,1960,'hồ'),('Vĩ Chí A',1966,1987,'hàn'),('Võ Văn Chín',1940,1952,'sơn');
/*!40000 ALTER TABLE `congnhan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ktrucsu`
--

DROP TABLE IF EXISTS `ktrucsu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ktrucsu` (
  `HOTEN_KTS` varchar(50) NOT NULL,
  `NAMS_KTS` int DEFAULT NULL,
  `PHAI` char(10) DEFAULT NULL,
  `NOI_TN` varchar(50) DEFAULT NULL,
  `DCHI_LL_KTS` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`HOTEN_KTS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ktrucsu`
--

LOCK TABLES `ktrucsu` WRITE;
/*!40000 ALTER TABLE `ktrucsu` DISABLE KEYS */;
INSERT INTO `ktrucsu` VALUES ('Lê Kim Dung',1952,'Nữ','Hà Nội','18/5 Phan Văn Trị TP Cần Thơ'),('Lê Thanh Tùng',1956,'Nam','TP Hồ Chí Minh','25 đường 3/2 TP Biên Hòa'),('Nguyễn Anh Thư',1970,'Nữ','New York USA','Khu 1 ĐH Cần Thơ'),('Nguyễn Song Đỗ Quyên',1970,'Nữ','TP Hồ Chí Minh','73 Trần Hưng Đạo TP Hồ Chí Minh'),('Trần Văn Lampard',1970,'Nam','London, Anh','123 Sài Gòn'),('Trương Minh Thái',1950,'Nam','Paris France','12/2/5 Trần Phú TP Hà Nội');
/*!40000 ALTER TABLE `ktrucsu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thamgia`
--

DROP TABLE IF EXISTS `thamgia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thamgia` (
  `HOTEN_CN` varchar(50) NOT NULL,
  `STT_CTR` int NOT NULL,
  `NGAY_TGIA` date DEFAULT NULL,
  `SO_NGAY` int DEFAULT NULL,
  PRIMARY KEY (`HOTEN_CN`,`STT_CTR`),
  KEY `STT_CTR` (`STT_CTR`),
  CONSTRAINT `thamgia_ibfk_1` FOREIGN KEY (`STT_CTR`) REFERENCES `cgtrinh` (`STT_CTR`) ON DELETE CASCADE,
  CONSTRAINT `thamgia_ibfk_2` FOREIGN KEY (`HOTEN_CN`) REFERENCES `congnhan` (`HOTEN_CN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thamgia`
--

LOCK TABLES `thamgia` WRITE;
/*!40000 ALTER TABLE `thamgia` DISABLE KEYS */;
INSERT INTO `thamgia` VALUES ('Đặng Văn Sơn',3,'1994-06-10',18),('Đặng Văn Sơn',9,'2020-10-10',60),('Lê Mạnh Quốc',1,'1994-12-18',6),('Lê Mạnh Quốc',9,'2020-10-10',60),('Lê Quyết Thắng',2,'1994-05-12',5),('Lê Quyết Thắng',9,'2020-10-10',60),('Nguyễn Hồng Vân',1,'1994-12-16',7),('Nguyễn Hồng Vân',4,'1994-09-14',7),('Nguyễn Thị Sửu',1,'1994-12-15',5),('Nguyễn Thị Sửu',2,'1994-05-08',20),('Nguyễn Thị Sửu',4,'1994-09-07',20),('Võ Văn Chín',2,'1994-05-10',10),('Võ Văn Chín',3,'1994-06-10',10);
/*!40000 ALTER TABLE `thamgia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thietke`
--

DROP TABLE IF EXISTS `thietke`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thietke` (
  `HOTEN_KTS` varchar(50) NOT NULL,
  `STT_CTR` int NOT NULL,
  `THU_LAO` int DEFAULT NULL,
  PRIMARY KEY (`HOTEN_KTS`,`STT_CTR`),
  KEY `STT_CTR` (`STT_CTR`),
  CONSTRAINT `thietke_ibfk_1` FOREIGN KEY (`STT_CTR`) REFERENCES `cgtrinh` (`STT_CTR`) ON DELETE CASCADE,
  CONSTRAINT `thietke_ibfk_2` FOREIGN KEY (`HOTEN_KTS`) REFERENCES `ktrucsu` (`HOTEN_KTS`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thietke`
--

LOCK TABLES `thietke` WRITE;
/*!40000 ALTER TABLE `thietke` DISABLE KEYS */;
INSERT INTO `thietke` VALUES ('Lê Kim Dung',4,20),('Lê Kim Dung',5,30),('Lê Kim Dung',6,40),('Lê Kim Dung',9,50),('Lê Thanh Tùng',1,25),('Lê Thanh Tùng',7,10),('Nguyễn Anh Thư',3,12),('Nguyễn Song Đỗ Quyên',2,6),('Trần Văn Lampard',9,15),('Trương Minh Thái',1,12),('Trương Minh Thái',6,27),('Trương Minh Thái',8,18);
/*!40000 ALTER TABLE `thietke` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'project'
--

--
-- Dumping routines for database 'project'
--
/*!50003 DROP FUNCTION IF EXISTS `cgtrinhHon1ty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `cgtrinhHon1ty`(kphiCt int) RETURNS int
    DETERMINISTIC
BEGIN
	declare motTy int;
    
    if kphiCt >= 1000 then
		set motTy=True;
	else
		set motTy=False;
	end if;
    
    return (motTy);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `soCtr1cgnhanLamnhieuI` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `soCtr1cgnhanLamnhieuI`() RETURNS int
    DETERMINISTIC
BEGIN
	declare motTy int;
    
    if kphiCt >= 1000 then
		set motTy=True;
	else
		set motTy=False;
	end if;
    
    return (motTy);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `congNhanLamViecNhieuCongTrinhNhat` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `congNhanLamViecNhieuCongTrinhNhat`()
Begin
		select hoten_cn from thamgia
		group by hoten_cn having count(stt_ctr) = 
			(select max(tg) from 
				(select hoten_cn, count(stt_ctr) tg
				from thamgia
				group by hoten_cn) as T);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `congNhanLamViecNhieuNgayNhat` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `congNhanLamViecNhieuNgayNhat`()
Begin
		select hoten_cn, sum(so_ngay) from thamgia
		group by hoten_cn having sum(so_ngay) = 
			(select max(tg) from 
				(select hoten_cn, sum(so_ngay) tg
				from thamgia
				group by hoten_cn) as T);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `getCongNhanTuCTrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `getCongNhanTuCTrinh`(sttctr varchar(50))
Begin
		select hoten_cn, ngay_tgia, so_ngay from thamgia
        where stt_ctr=sttctr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `getCongTrinhTuKTS` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `getCongTrinhTuKTS`(hotenkts varchar(50))
Begin
		select ten_ctr, tk.thu_lao
        from cgtrinh c inner join thietke tk
        on c.stt_ctr=tk.stt_ctr
        where tk.hoten_kts=hotenkts;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `getKTSTuCTrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `getKTSTuCTrinh`(sttctr int)
Begin
		select hoten_kts, thu_lao from thietke
        where stt_ctr = sttctr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `getTenCongTrinhTuCongNhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `getTenCongTrinhTuCongNhan`(hotencn varchar(50))
Begin
		select ten_ctr, ngay_tgia, so_ngay
        from cgtrinh c inner join thamgia tg 
        on c.stt_ctr=tg.stt_ctr
        where tg.hoten_cn=hotencn;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insertIntoCgtrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertIntoCgtrinh`(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
Begin
		insert into  cgtrinh values (stt , tenCtr, dchi, tthanh, kphi , tenchu, tenthau, nbatdau); 
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insertIntoChunhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertIntoChunhan`(tenthau varchar(50), dchi varchar(50))
Begin
		insert into chunhan values (tenthau, dchi); 
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insertIntoChuthau` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertIntoChuthau`(tenthau varchar(50), tel char(7), dchi varchar(50))
Begin
		insert into  chuthau values (tenthau, tel, dchi); 
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insertIntoCongnhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertIntoCongnhan`(tencn varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
Begin
		insert into congnhan values (tencn, nsinh, nvaonghe, cmon); 
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insertIntoKtrucsu` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertIntoKtrucsu`(tenKts varchar(50), nskts int, phai varchar(10), noitn varchar(50), dchi varchar(50))
Begin
		insert into ktrucsu values (tenkts, nskts, phai, noitn, dchi); 
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ktsCoThulaoNhieuNhat` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ktsCoThulaoNhieuNhat`()
Begin
		select hoten_kts from thietke
		group by hoten_kts having sum(thu_lao) = 
			(select max(tg) from 
				(select hoten_kts, sum(thu_lao) tg
				from thietke
				group by hoten_kts) as T);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ktsLamViecNhieuCtrinhNhat` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ktsLamViecNhieuCtrinhNhat`()
Begin
		select hoten_kts from thietke
		group by hoten_kts having count(stt_ctr) = 
			(select max(tg) from 
				(select hoten_kts, count(stt_ctr) tg
				from thietke
				group by hoten_kts) as T);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `layCgtrinhHon1ty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `layCgtrinhHon1ty`()
Begin
		
		select ten_ctr
        from cgtrinh
        where cgtrinhHon1ty(kinh_phi)=True;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `suaThongTinCongNhanLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `suaThongTinCongNhanLamViec`(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
Begin
		update thamgia set so_ngay=songay, ngay_tgia=ngayTg
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `suaThongTinKTSLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `suaThongTinKTSLamViec`(hotenkts varchar(50), sttCtr int, thulao int)
Begin
		update thietke set thu_lao=thulao
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `themCongNhanLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `themCongNhanLamViec`(hotencn varchar(50), sttCtr int, ngayTg date, songay int)
Begin
		insert into thamgia values (hotencn, sttCtr, ngayTg, songay);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `themKTSLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `themKTSLamViec`(hotenkts varchar(50), sttCtr int, thulao int)
Begin
		insert into thietke values (hotenkts, sttCtr, thulao);
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `tongKinhPhiCacCongTrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `tongKinhPhiCacCongTrinh`()
Begin
		select sum(kinh_phi) from cgtrinh;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateCgtrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateCgtrinh`(stt int, tenCtr varchar(50), dchi varchar(50), tthanh varchar(50), kphi int, tenchu varchar(50), tenthau varchar(50), nbatdau date)
Begin
		update cgtrinh set ten_ctr=tenCtr,diachi_ctr=dchi,tinh_thanh=tthanh,kinh_phi=kphi,ten_chu=tenchu,ten_thau=tenthau,ngay_bd=nbatdau where stt_ctr=stt;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateChunhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateChunhan`(tenchucu varchar(50),tenchumoi varchar(50), dchi varchar(50))
Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chunhan set ten_chu=tenchumoi, dchi_chu=dchi where ten_chu=tenchucu; 
        update cgtrinh set ten_chu=tenchumoi where ten_chu=tenchucu;
        set FOREIGN_KEY_CHECKS = 1;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateChuthau` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateChuthau`(tenthaucu varchar(50), tenthaumoi varchar(50), sdt char(7), dchi varchar(50))
Begin
		set FOREIGN_KEY_CHECKS = 0;
		update chuthau set ten_thau=tenthaumoi, tel=sdt, dchi_thau=dchi where ten_thau=tenthaucu;
        update cgtrinh set ten_thau=tenthaumoi where ten_thau=tenthaucu;
        set FOREIGN_KEY_CHECKS = 1;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateCongnhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateCongnhan`(tencncu varchar(50),tencnmoi varchar(50), nsinh int, nvaonghe int, cmon varchar(50))
Begin
		set FOREIGN_KEY_CHECKS = 0;
		update congnhan set HOTEN_CN = tencnmoi, NAMS_CN = nsinh, NAM_VAO_N = nvaonghe, CH_MON = cmon where HOTEN_CN = tencncu;
        update thamgia set HOTEN_CN = tencnmoi where HOTEN_CN = tencncu;
        set FOREIGN_KEY_CHECKS = 1;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateKtrucsu` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateKtrucsu`(tenKtscu varchar(50),tenKtsmoi varchar(50), nskts int, phai varchar(10), noitn varchar(50), dchi varchar(50))
Begin
		set FOREIGN_KEY_CHECKS = 0;
		update ktrucsu set HOTEN_KTS = tenKtsmoi, NAMS_KTS = nskts, PHAI = phai, NOI_TN = noitn, DCHI_LL_KTS = dchi where hoten_kts = tenKtscu; 
        update thietke set HOTEN_KTS = tenKtsmoi where HOTEN_KTS = tenKtscu;
        set FOREIGN_KEY_CHECKS = 1;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaCgtrinh` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaCgtrinh`(stt int)
Begin
		delete from cgtrinh where stt_ctr=stt;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaChuNhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaChuNhan`(tenchu varchar(50))
Begin
		delete from chunhan where ten_chu=tenchu;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaChuThau` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaChuThau`(tenthau varchar(50))
Begin
		delete from chuthau where ten_thau=tenthau;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaCongNhan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaCongNhan`(tencn varchar(50))
Begin
		delete from congnhan where hoten_cn=tencn;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaCongNhanLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaCongNhanLamViec`(hotencn varchar(50), sttCtr int)
Begin
		delete from thamgia 
        where hoten_cn=hotencn and stt_ctr=sttCtr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaKtrucsu` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaKtrucsu`(tenKts varchar(50))
Begin
		delete from ktrucsu where hoten_kts=tenKts;
    End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `xoaKTSLamViec` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `xoaKTSLamViec`(hotenkts varchar(50), sttCtr int)
Begin
		delete from thietke 
        where hoten_kts=hotenkts and stt_ctr=sttCtr;
	End ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-27 18:09:35
