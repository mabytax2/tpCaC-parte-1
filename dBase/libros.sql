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

CREATE TABLE `libros` (
  `COL 1` varchar(278) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`COL 1`) VALUES
('id;descripcion;idioma;tipo;ubicacion;instrumento_asociado'),
('C-00007;Operation Guide HP 53131A 225 MHz Universal Counter;ingles;guia de operacion;P4_01;HP 53131A'),
('C-00012;Gu?a de iniciaci?n contador universal HP 53131A/132A 225 MHz;espanol;guia de inicio;P4_01;contador universal HP 53131A/132A 225 MHz'),
('DL-00001;National Appliccation Specific Analog Products Databook. Audio, automotive, video, special functions;ingles;manual;P4_01;Sin instrumento asociado'),
('DL-00002;National Operational Amplifiers Databook. Operational amplifiers, buffers, voltage comparators, active matrix/LCD display drivers, special functions, surface mount;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00003;National Discrete DMOS Power MOSFET Products Databook. Discrete Power and Signal Technologies;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00004;National Power ICs Databook. Linear voltage regulators, low dropout voltage regulators, switching voltage regulators, motion control, surface mount;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00005;National data acquisition Databook. Data acquisition systems, analog to digital converters, digital to analog converters, voltage reference, temperature sensors, sample and hold, active filters, analog switches/multiplexers ;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00006;National discrete diode, Bipolar transistor and JFET products Databook. Discrete Power and signal technologies;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00007;Reguladores de tensi?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('DL-00008;LS/S/TTL Logic Databook;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00009;National Interface Databook. Bus circuits, data transmition circuits, system design guide;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00010;Circuitos integrados CMOS, series CD4000 - CD4500;castellano;Manual;P4_01;Sin instrumento asociado'),
('DL-00011;Analog/Interface ICs. Device data. Vol. I;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00012;Motorola high-speed CMOS data;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00013;HC05. MC68HC705KJ1. MC68HLC705KJ1. MC68HRC705KJ1. HCMOS Microcontroller unit. Technical data;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00014;Transistores de Silicio Argentinos - SOT 54 -SOT 32;espanol;Libro;P4_01;Sin instrumento asociado'),
('DL-00015;embedded control handbook. Vol. 1;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00016;Timing solutions. Over 10 newly released parts!. Low skew fanout buffers, PC clock generators, PLL clock drivers, clock generation circuits ;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00017;Burr-Brown IC Data Book. Linear and mixed signal products;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00018;Motorola semiconductor master selection guide;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00019;Integrated circuits. Dream machine application reference book. Over 50 80C51 Application ideas;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00020;Bipolar Power. Transistor data-Motorola. Rev. 7;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00021;Telecommunications device data - Motorola. Rev. 2;ingles;Manual;P4_01;Sin instrumento asociado'),
('DL-00022;Introduccion a los sistemas de control: Conceptos, aplicaciones y simulaci?n con Matlab;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00001;Tecnolog?as avanzadas de Telecomunicaciones;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00002;M?quinas el?ctricas y transformadores. Tercera edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00003;Sistemas electr?nicos de comunicaciones. Segunda edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00004;Dibujo t?cnico;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00005;Geometr?a para la inform?tica gr?fica y CAD;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00006;Electr?nica y dispositivos electr?nicos;espanol;Libro;P4_01;Sin instrumento asociado'),
('EL-00007;Electricidad y magnetismo;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00008;Mediciones electr?nicas;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00009;Circuitos el?ctricos. An?lisis de modelos circuitales. Tomo 1. Segunda edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00010;Electr?nica del vac?o\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00011;Circuitos el?ctricos. Teor?a y 50 problemas resueltos;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00012;Amplificadores de audiofrecuencias;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00013;Electr?nica de los circuitos amplificadores;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00014;Circuitos electr?nicos. Segunda edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00015;Electr?nica aplicada;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00016;Circuitos microelectr?nicos. Quinta edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00017;Radioelectr?nica de barcos;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00018;Elementos de electromagnetismo;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00019;Principios fundamentales de electr?nica;espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00021;Teor?a de circuitos - Ejercicios de autoevaluaci?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00022;Electr?nica de Potencia. Circuitos. Dispositivos y aplicaciones. Tercera edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00024;Desiner?s guide to fiber optic transceivers;ingles;Manual;P4_01;Sin instrumento asociado'),
('EL-00025;Principios de electr?nica. Cuarta edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00026;Electr?nica anal?gica. An?lisis de circuitos. Amplificaci?n. Sistemas de alimentaci?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00027;Dibujo y comunicaci?n gr?fica. Tercera edici?n\";espanol;Manual;P4_01;Sin instrumento asociado'),
('EL-00028;Small-Signal. Transistors, FETs and Diodes Device Data-Motorola.Rev. 6 ;ingles;Libro;P4_01;Sin instrumento asociado'),
('EL-00029;Circuitos el?ctricos. Introducci?n al an?lisis y dise?o. Segunda edici?n\";espanol;Libro;P4_01;Sin instrumento asociado'),
('EL-00030;Circuitos el?ctricos. Introducci?n al an?lisis y dise?o. Tercera edici?n\";espanol;Libro;P4_01;Sin instrumento asociado'),
('EL-00031;Sistemas digitales de control de procesos. Tomo I. Edici?n 2006;espanol;Libro;P4_01;Sin instrumento asociado'),
('EL-00032;Mediciones de procesos industriales;espanol;Libro;P4_01;Sin instrumento asociado'),
('EL-00033;Illustrated AUTOCAD;ingles;Libro;P4_01;Sin instrumento asociado'),
('F-00001;Service Guide HP E3631A Triple Output DC Power Supply;ingles;guia de servicio;P4_01;HP E3631A '),
('F-00002;Manual de usuario Fuente de alimentaci?n de CC de Salida Triple HP E3631A;espanol;manual de usuario;P4_01;HP E3631A '),
('F-00003;User`s guide HP E3631A Triple Output DC Power Supply;ingles;guia de usuario;P4_01;HP E3631A'),
('F-00067;manual de usuario fuente DC de un canal KAISE V7.0  MPS 3005D;ingles;manual de usuario;P4_01;fuente DC de un canal KAISE V7.0  MPS 3005D'),
('F-00072;manual de operaci?n fuente Metex Universal MS-9140;ingles;manual de operaci?n\";P4_01;fuente Metex Universal MS-9140'),
('G-00034;Gu?a de usuario Generador de Pulsos HP 8110;ingles;guia de usuario;P4_01;hp 8110-generador de pulsos 150 mhz'),
('G-00035;Gu?a de operaci?n generador de de se?ales HP 8647;espanol;guia de operacion;P4_01;hp 8647-generador de se?al\"\r\nG-00036;Manual del generador de se?ales HP 8647A;ingles;guia de operacion;P4_01;hp 8647A'),
('G-00037;Gu?a de operador HP 8110;espanol;guia de operacion;P4_01;hp 8110-generador de pulsos 150 mhz'),
('G-00058;Manual de Escort EGC 3230-2MHz Generador de funcion con frec.;ingles;Manual de operador;P4_01;Escort EGC 3230-2MHz Generador de funcion con frec.'),
('G-00059;Manual de generador de funciones Tektronix CFG 250;ingles;Manual de usuario;P4_01;Generador de funciones Tektronix CFG 250'),
('G-00060;Manual de generador de funciones Tektronix CFG 253;ingles;Manual de usuario;P4_01;Generador de funciones Tektronix CFG 253'),
('G-00061;Manual del generador de funci?n arbitraria GW Instek Serie AFG-3000;ingles;Manual de usuario;P4_01;Generador de funci?n arbitraria GW Instek Serie AFG-3000'),
('G-00062;Gu?a r?pida Generador de formas de onda arbitrarias Rigol DG1000;ingles;Gu?a r?pida;P4_01;Generador de formas de onda arbitrarias Rigol DG1000'),
('G-00063;Manual de instrucciones del term?metro tipo K, CENTER 301;ingles;Manual de instrucciones;P4_01;Term?metro tipo K, CENTER 301'),
('K-00038;Libro de trabajo estudiantes comunicaciones an?logas 53-001S;ingles;cuaderno de estudiantes;P4_01;sin instrumento asociado'),
('K-00039;Libro de trabajo estudiantes comunicaciones digitales 53-002S;ingles;cuaderno de estudiantes;P4_01;sin instrumento asociado'),
('K-00040;comunicaciones digitales 53-002 Teknikit;ingles;Teknikit;P4_01;sin instrumento asociado'),
('K-00041;Libro 1 kit 2942 de transductores;ingles;libro;P4_01;sin instrumento asociado'),
('K-00042;Libro 2 del kit 2942 de transductores;ingles;libro;P4_01;sin instrumento asociado'),
('K-00043;manual de instructor, Teknikit de comunicaciones digitales 53-002I;ingles;manual de instructor;P4_01;sin instrumento asociado'),
('K-00044;Teknikit Series Telecommunications 53-001 Analogue;ingles;curso;P4_01;sin instrumento asociado'),
('K-00045;Teknikit Analogue Communication Instructor`s manual 53-001l;ingles;manual del instructor;P4_01;sin instrumento asociado'),
('K-00046;Interface for IBM PC MIC926;ingles;curso;P4_01;sin instrumento asociado'),
('K-00047;Transducers kit 2942 ? book 3;ingles;curso;P4_01;sin instrumento asociado'),
('K-00048;kit lab-volt varios;ingles;Catalogo;P4_01;sin instrumento asociado'),
('K-00049;no se encuentra la carpeta en el armario;ingles;catalogo;P4_01;lab-vlot kit varios'),
('M-00050;Service Guide HP 34401A Multimeter;ingles;guia de servicio;P4_01;HP 34401A multimeter'),
('M-00051;Guia del usuario Multimetro HP 34401A;espanol;guia de usuario;P4_01;HP 34401A multimeter'),
('M-00054;Manual mult?metro Goldstar DM-7333;espanol;Manual;P4_01;mult?metro Goldstar DM-7333'),
('M-00055;Manual mult?metro Escort EDM82B;ingles;Manual;P4_01;mult?metro Escort EDM82B'),
('M-00056;Manual mult?metro Goldstar DM-311;ingles;manual de operacion;P4_01;mult?metro Goldstar DM-311'),
('M-00057;Manual mult?metro Instek GDM-394;ingles;manual de usuario;P4_01;mult?metro Instek GDM-394'),
('M-00065;Referencia r?pida Mult?metro HP 34401A;ingles;Referencia r?pida;P4_01;mult?metro HP 34401A'),
('M-00073;Manual de operaci?n mult?metro Goldstar DM 310-341;ingles;Manual de operaci?n\";P4_01;mult?metro Goldstar DM 310-341'),
('O-00052;Tektronik TDS 210 y TDS 220 osciloscopios digitales 070-9560-04 ;espanol;manual de usuario;P4_01;Tektronik TDS 210 y TDS 220 osciloscopios digitales'),
('O-00053;TDS 340A - TDS 360 y TDS 380 osciloscopios digitales de tiempo real Tektronik 070-9433-03;espanol;manual de usuario;P4_01;TDS 340A - TDS 360 y TDS 380 osciloscopios digitales de tiempo real Tektronik'),
('O-00064;Instrucciones de cumplimiento y seguridad Osciloscopio Digital Tektronix TBS 1000;ingles;manual de instrucciones;P4_01;Osciloscopio Digital Tektronix TBS 1000'),
('O-00068;hoja con caracter?sticas de punta OCR-LP16BX;ingles-chino;hoja de datos;P4_01;OCR-LP16BX'),
('O-00069;Manual osciloscopio Leader 40 MHz Modelo 8041 y 8042;ingles;manual de usuario;P4_01;osciloscopio Leader 40 MHz Modelo 8041 y 8042'),
('O-00070;Hoja con caracter?sticas de punta de Osciloscopio OCR - HP 10071;ingles;hoja de datos;P4_01;OCR - HP 10071'),
('V-00004;Guia de usuario Analizador de Protocolos Serie J2300;espanol;Guia de usuario;P4_01;Analizador de Protocolos Serie J2300'),
('V-00013;Mainframe features HP internet advisor;ingles;Caracteristicas del Mainframe;P4_01;sin instrumento asociado'),
('V-00014;Caracteristicas del Mainframe Asistente de internet HP;espanol;Caracteristicas del Mainframe;P4_01;sin instrumento asociado'),
('V-00015;User`s guide HP High Speed Internet Advisor ;ingles;guia de usuario;P4_01;sin instrumento asociado'),
('V-00016;User`s guide Internet Advisor HP - LAN;ingles;guia de usuario;P4_01;sin instrumento asociado'),
('V-00017;HP Internet Advisor for Ethernet Training Manual;ingles;Manual de entrenamiento;P4_01;sin instrumento asociado'),
('V-00018;User`s guide HP Low Speed Internet Advisor;ingles;guia de usuario;P4_01;sin instrumento asociado'),
('V-00019;HP 4284A Precision LCR Meter Operation Manual;ingles;manual de operacion;P4_01;hp 4284A LCR meter'),
('V-00020;HP 4285A Precision LCR Meter Maintenance Manual;ingles;manual de mantenimiento;P4_01;HP 4285A Precision LCR Meter'),
('V-00021;HP 4285A Precision LCR Meter Getting Started Guide;ingles;guia de inicio;P4_01;HP 4285A Precision LCR Meter'),
('V-00022;HP 4285A Precision LCR Meter;ingles;manual de operacion;P4_01;HP 4285A Precision LCR Meter'),
('V-00023;guia de referencia rapida analizador de espectros serie HP 8590;espanol;guia rapida;P4_01;hp 8590 analizador de espectros'),
('V-00024;HP 8590 analizador de espectros;espanol;guia de usuario;P4_01;HP 8590 analizador de espectros'),
('V-00025;HP 8590 series E y L analizador de espectros;ingles;guia de usuario;P4_01;HP 8590 analizador de espectros serie E y L'),
('V-00026;HP 8590 analizador de espectros series E y HP 8591C guia de cable TV analizador de calibracion ;ingles;guia de calibracion;P4_01;hp 8590 analizador de espectros series E'),
('V-00027;guia del programador HP 8590 series E y L analizador de espectros y HP 8591C cable TV analizador;ingles;guia de programacion;P4_01;HP 8590 series E y L analizador de espectros y HP 8591C cable TV analizador'),
('V-00028;Guia de usuario Analizador de espectros HP 8590 Series D y E;espanol;guia de usuario;P4_01;Analizador de espectros HP 8590 Series D y E'),
('V-00029;guia de referencia rapida Analizador de espectros HP 8590 Series E y L;ingles;guia rapida;P4_01;Analizador de espectros HP 8590 Series E y L'),
('V-00030;HP 48251A Q adapter Maintenance Manual;ingles;manual de mantenimiento;P4_01;HP 48251A Q adapter'),
('V-00031;HP 48251A Q adapter Operatrion Manual;ingles;manual de operacion;P4_01;HP 48251A Q adapter'),
('V-00032;User`s reference HP 1660A series Timing logic analizer;ingles;referencia de usuario;P4_01;HP 1660A series Timing logic analizer'),
('V-00033;HP 1660A-AS series logic analizer Programmer`s guide;ingles;guia de programacion;P4_01;HP 1660A-AS series logic analizer'),
('V-00066;manual de usuario del analizador de arm?nicos FLUKE Modelo 41B;ingles;manual de usuario;P4_01;analizador de arm?nicos FLUKE Modelo 41B'),
('V-00071;manual de instrucciones estaci?n desoldadora Goot;ingles;manual de instrucciones;P4_01;Desoldadora Goot'),
('V-00074;manual de operador Digital LCR Meter;ingles;manual de operador;P4_01;Digital LCR Meter'),
('V-00075;manual de operador frecuenc?metro Escort EFC-3201-100 MHz;ingles;manual de operador;P4_01;frecuenc?metro Escort EFC-3201-100 MHz'),
('XX-0001;plc-512-logic analizer user`s manual;ingles;manual de usuario;P4_01;plc-512-logic analizer'),
('XX-0002;plc 812 G multilab card user`s manual;ingles;manual de usuario;P4_01;plc 812 G multilab card'),
('XX-0003;HP vee programming visual set de bibliografia;ingles;set de bibliografia;P4_01;sin instrumento asociado'),
('XX-0004;siemens simatic ti manual de uso;espanol;manual de uso;P4_01;sin instrumento asociado'),
('XX-0005;manual de uso wally for windows;ingles;manual de uso del lenguaje;P4_01;sin instrumento asociado'),
('XX-0006;manual de alumno experimentos con equipo electrico;espanol;manual de alumno;P4_01;experimentos con equipo electrico'),
('XX-0010;manual de practica alumno curso de comunicaciones de fibra optica ? lab volt;espanol;manual de practica alumno;P4_01;sin instrumento asociado');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
