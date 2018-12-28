-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-12-2018 a las 17:28:01
-- Versión del servidor: 10.1.35-MariaDB
-- Versión de PHP: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `my-trac`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `activities`
--

CREATE TABLE `activities` (
  `id` int(5) DEFAULT NULL,
  `activity_date` date DEFAULT NULL,
  `views` int(4) DEFAULT NULL,
  `reputation` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `limits_activities`
--

CREATE TABLE `limits_activities` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `weight` float NOT NULL,
  `maximum` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `limits_user`
--

CREATE TABLE `limits_user` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `weight` float NOT NULL,
  `maximum` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ratings`
--

CREATE TABLE `ratings` (
  `id_user` int(4) DEFAULT NULL,
  `id_activity` int(4) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL,
  `reputation_user` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `registration` date NOT NULL,
  `valuations` int(11) NOT NULL DEFAULT '0',
  `uses_app` int(11) NOT NULL DEFAULT '0',
  `tickets_purchased` int(11) NOT NULL DEFAULT '0',
  `groups` int(11) NOT NULL DEFAULT '0',
  `reputation` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `limits_activities`
--
ALTER TABLE `limits_activities`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `limits_user`
--
ALTER TABLE `limits_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `limits_activities`
--
ALTER TABLE `limits_activities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `limits_user`
--
ALTER TABLE `limits_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
