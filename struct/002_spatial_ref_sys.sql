CREATE TABLE `spatial_ref_sys` (
	`SRID` INT(11) NOT NULL,
	`AUTH_NAME` VARCHAR(256) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`AUTH_SRID` INT(11) NULL DEFAULT NULL,
	`SRTEXT` VARCHAR(2048) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci'
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;