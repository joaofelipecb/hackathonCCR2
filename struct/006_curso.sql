CREATE TABLE `curso` (
	`curso_id` INT(11) NOT NULL AUTO_INCREMENT,
	`curso_nome` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`curso_descricao` TEXT(65535) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`curso_id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=16
;
