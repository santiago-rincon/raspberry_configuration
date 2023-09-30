-- MariaDB dump 10.19  Distrib 10.5.19-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: nodos
-- ------------------------------------------------------
-- Server version	10.5.19-MariaDB-0+deb11u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `intervals`
--

DROP TABLE IF EXISTS `intervals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intervals` (
  `minutes` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intervals`
--

LOCK TABLES `intervals` WRITE;
/*!40000 ALTER TABLE `intervals` DISABLE KEYS */;
INSERT INTO `intervals` VALUES (180);
/*!40000 ALTER TABLE `intervals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodes`
--

DROP TABLE IF EXISTS `nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nodes` (
  `mac` varchar(20) DEFAULT NULL,
  `nodeId` int(11) DEFAULT NULL,
  `nodeStatus` tinyint(1) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `id_firebase` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodes`
--

LOCK TABLES `nodes` WRITE;
/*!40000 ALTER TABLE `nodes` DISABLE KEYS */;
INSERT INTO `nodes` VALUES ('ae:58:ff:d5:c1:56',1,0,4.27767,-74.3872,'zGqScmEoVnGpbP1RuUWi'),('dd:dd:dd:dd:dd:dd',2,1,9.6,6.4,'1xDeXod4YZnbPekUAvKX'),('55:55:11:66:77:88',3,0,2.5879,3.254,'jU6fA0rTwd2ysNwK3gtx'),('11:22:33:44:55:00',5,1,2.5,9.82,'6pgfCD5GUPmajX2X657z'),('54:af:87:96:dd:85',6,0,52.68,-69.355,'V6tKtTEap4hagGppwytz'),('ff:58:ff:d5:c1:26',9,0,4.27767,-74.3872,'01Lgbw4gwWrJ5wrkeR0h'),('da:da:da:da:da:da',4,1,5.25496,-43.654,'fcvDui6xR5uUbrpexMPY'),('ff:58:ff:d5:c1:88',7,0,4.27767,-74.3872,'bMRH7hvBIO9Jve5DDqVZ'),('ad:58:ff:d5:c1:56',8,0,4.27767,-74.3872,'VCs3Gw7P9GQZokRyHUf3'),('66:44:11:66:77:88',10,0,2.5879,3.254,'7ES6eSkrGwXOntxQ5TAg');
/*!40000 ALTER TABLE `nodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thresholds`
--

DROP TABLE IF EXISTS `thresholds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `thresholds` (
  `variable` varchar(20) DEFAULT NULL,
  `umbral` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thresholds`
--

LOCK TABLES `thresholds` WRITE;
/*!40000 ALTER TABLE `thresholds` DISABLE KEYS */;
INSERT INTO `thresholds` VALUES ('co2',500),('ha',60.36),('hs',72.5),('rad',550.32),('temp',27.65);
/*!40000 ALTER TABLE `thresholds` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 15:22:03
