-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: nandanunni
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.21.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `students_20219023`
--

DROP TABLE IF EXISTS `students_20219023`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_20219023` (
  `regno` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `description` text,
  `photo` blob,
  `password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`regno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_20219023`
--

LOCK TABLES `students_20219023` WRITE;
/*!40000 ALTER TABLE `students_20219023` DISABLE KEYS */;
INSERT INTO `students_20219023` VALUES (20219023,'Nandanunni','CS',9188750806,'asnqln@gmail.com','s4','Yeah its working',_binary 'example.png','f2f0f7f960fcdc48db9350db844b689d69a976c0dd562e0d387a3472284c8f8c0ba0a859fd67265d578e01cbea9889a038d59eef01821de07b4ea4ef05e2a832'),(2021902300,'Nandanunni','CS',5188750800,'asnqln@gmail.com','s1','kandmsxwscdejnz',_binary 'example.png','6388d9a6c829d77a9a9fe5e5c935e2f0ba123fbe4ecf808543eb5af14f955c9c6358cf14109b1da90f2ae347afbaf4062a2c1adf28038bc49a8aba2582d6ad7b');
/*!40000 ALTER TABLE `students_20219023` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-17 15:43:01
