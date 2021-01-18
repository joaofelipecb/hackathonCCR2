CREATE TABLE `negocio` (
	`negocio_id` INT(11) NOT NULL AUTO_INCREMENT,
	`negocio_nome` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`negocio_descricao` TEXT(65535) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`negocio_id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=16
;
