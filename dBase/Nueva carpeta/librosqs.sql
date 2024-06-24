-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-06-2024 a las 01:16:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `csv_db 6`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (id,descripcion,idioma,tipo,ubicacion,instrumento_asociado)
VALUES
(C-00007,Operation Guide HP 53131A 225 MHz Universal Counter,ingles,guia de operacion,P4_01,HP 53131A),
(C-00012,Gu?a de iniciaci?n contador universal HP 53131A/132A 225 MHz,espanol,guia de inicio,P4_01,contador universal HP 53131A/132A 225 MHz),;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
