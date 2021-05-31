-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 31, 2021 at 11:16 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `co2messen`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `ID` int(11) NOT NULL,
  `Time` timestamp NOT NULL DEFAULT current_timestamp(),
  `Value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`ID`, `Time`, `Value`) VALUES
(123, '2021-05-19 17:24:20', 12),
(6969, '2021-05-19 19:07:21', 1234),
(6969, '2021-05-19 19:07:48', 1234),
(6969, '2021-05-19 19:08:53', 1234),
(6969, '2021-05-19 19:09:25', 1234),
(6969, '2021-05-19 19:10:59', 1234),
(6969, '2021-05-19 19:11:42', 1234),
(6969, '2021-05-19 19:15:47', 1234),
(6969, '2021-05-19 19:15:57', 1234),
(6969, '2021-05-19 19:16:50', 1234),
(6969, '2021-05-19 19:17:08', 1234),
(6969, '2021-05-19 19:19:41', 1234),
(6969, '2021-05-19 19:20:21', 1234),
(6969, '2021-05-19 19:20:40', 1234),
(6969, '2021-05-19 19:20:50', 1234),
(6969, '2021-05-19 19:25:58', 1234),
(6969, '2021-05-19 20:25:16', 1234),
(6969, '2021-05-19 20:32:38', 1234),
(6969, '2021-05-19 20:33:03', 1234);

-- --------------------------------------------------------

--
-- Table structure for table `devices`
--

CREATE TABLE `devices` (
  `ID` int(11) NOT NULL,
  `Room` int(11) NOT NULL,
  `Alarm` text NOT NULL,
  `Config` int(11) NOT NULL,
  `Hash` text NOT NULL,
  `Updated` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `devices`
--

INSERT INTO `devices` (`ID`, `Room`, `Alarm`, `Config`, `Hash`, `Updated`) VALUES
(6969, 156, 'schuan', 22, 'schuan123456789', 1),
(6969, 151, '1', 1, '12', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
