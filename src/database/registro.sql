CREATE TABLE IF NOT EXISTS `tareas` (
  `id_tarea` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `titulo` varchar(200) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_limite` date DEFAULT NULL,
  `hora_limite` time DEFAULT NULL,
  PRIMARY KEY (`id_tarea`)
) ENGINE=InnoDB;