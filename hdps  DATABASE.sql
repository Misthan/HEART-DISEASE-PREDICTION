-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2024 at 01:03 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hdps`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `name`, `email`, `password`) VALUES
(1, 'miskan', 'mohamed@gmail.com', '1234'),
(2, 'mmm', 'wylulito@closetab.email', '1526'),
(3, 'misthan', 'mohamedmsikan71@gmail.com', '7412'),
(4, 'akmal', 'padihov386@taobudao.com', '85264vdvrvrw'),
(5, 'fefwf', 'colemu@pelagius.net', '8521'),
(6, 'dewrgrw', 'wylulitog@closetab.email', 'eye5yh5e6'),
(7, 'bfxbb', 'mohamedmsikan7b1@gmail.com', 'bfbxf'),
(8, 'gege', 'mohamgedmsikan7b1@gmail.com', 'gerg'),
(9, 'akmalg', 'mohamedmsiggkan7b1@gmail.com', 'gjuybuyb yu'),
(10, 'brgnry', 'mohamenyrnd@gmail.com', 'nrnsry'),
(11, 'gnntrdne', 'padihovnten386@taobudao.com', 'netnedfn'),
(12, ' dfntfb', 'mohamedmbrfsikan7b1@gmail.com', 'wrhrbte'),
(13, 'MISKAN', 'mohamed123@gmail.com', '123123'),
(14, 'test_user', 'test@example.com', 'test_password'),
(15, 'misthan', 'mohamed1@gmail.com', '1256');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
