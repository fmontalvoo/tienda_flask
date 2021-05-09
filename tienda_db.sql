-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 08-05-2021 a las 23:35:00
-- Versión del servidor: 10.3.25-MariaDB-0ubuntu0.20.04.1
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `id` smallint(4) UNSIGNED NOT NULL,
  `apellidos` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nombres` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los autores.';

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`id`, `apellidos`, `nombres`, `fecha_nacimiento`) VALUES
(1, 'Vallejo Mendoza', 'César Abraham', '1892-03-16'),
(2, 'Vargas Llosa', 'Jorge Mario Pedro', '1936-03-28'),
(3, 'Alegría Bazán', 'Ciro', '1909-11-04'),
(4, 'García Márquez', 'Gabriel José de la Concordia', '1927-03-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE `compra` (
  `uuid` char(36) COLLATE utf8_unicode_ci NOT NULL,
  `libro_isbn` char(12) COLLATE utf8_unicode_ci NOT NULL,
  `usuario_id` smallint(3) UNSIGNED NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena las compras.';

--
-- Volcado de datos para la tabla `compra`
--

INSERT INTO `compra` (`uuid`, `libro_isbn`, `usuario_id`, `fecha`) VALUES
('925ce44e-b074-11eb-a302-0800279fd3a8', '762841019387', 2, '2021-05-08 22:30:05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `isbn` char(12) COLLATE utf8_unicode_ci NOT NULL,
  `titulo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `autor_id` smallint(4) UNSIGNED NOT NULL,
  `anio_edicion` year(4) NOT NULL,
  `precio` decimal(3,0) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los libros.';

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`isbn`, `titulo`, `autor_id`, `anio_edicion`, `precio`) VALUES
('238874100138', 'Conversación en La Catedral', 2, 1951, '70'),
('383370912281', 'El mundo es ancho y ajeno', 3, 1941, '65'),
('480129403571', 'La ciudad y los perros', 2, 1963, '81'),
('483240184226', 'La serpiente de oro', 3, 1935, '85'),
('589120131047', 'Los perros hambrientos', 3, 1939, '31'),
('591338770183', 'Paco Yunque', 1, 1951, '55'),
('661984010128', 'El general en su laberinto', 4, 1989, '110'),
('683425019133', 'El coronel no tiene quien le escriba', 4, 1961, '42'),
('762841019387', 'Cien años de soledad', 4, 1967, '75'),
('890366138239', 'La fiesta del Chivo', 2, 2000, '30'),
('892014771852', 'Poemas humanos', 1, 1939, '120'),
('930281938211', 'El amor en los tiempos del cólera', 4, 1985, '38'),
('978318472263', 'Los heraldos negros', 1, 1919, '48'),
('981402938251', 'La casa verde', 2, 1966, '105');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id` tinyint(1) UNSIGNED NOT NULL,
  `tipo` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los tipos de usuario.';

--
-- Volcado de datos para la tabla `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id`, `tipo`) VALUES
(1, 'Administrador'),
(2, 'Usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `usuario` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `clave` varchar(94) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_usuario_id` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los usuarios.';

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `clave`, `tipo_usuario_id`) VALUES
(1, 'fgmo', 'pbkdf2:sha256:150000$bW4G4msM$06d9e25caa17d87a3d6fb709ca31c93231d4bad2976cbd3fc93fe8fa16cb7f3d', 1),
(2, 'fulano', 'pbkdf2:sha256:150000$bW4G4msM$06d9e25caa17d87a3d6fb709ca31c93231d4bad2976cbd3fc93fe8fa16cb7f3d', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `fk_compra_libro` (`libro_isbn`),
  ADD KEY `fk_compra_usuario` (`usuario_id`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `fk_libro_autor` (`autor_id`);

--
-- Indices de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuario_tipo_usuario` (`tipo_usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `id` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  MODIFY `id` tinyint(1) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `fk_compra_libro` FOREIGN KEY (`libro_isbn`) REFERENCES `libro` (`isbn`),
  ADD CONSTRAINT `fk_compra_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `fk_libro_autor` FOREIGN KEY (`autor_id`) REFERENCES `autor` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_usuario_tipo_usuario` FOREIGN KEY (`tipo_usuario_id`) REFERENCES `tipo_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;