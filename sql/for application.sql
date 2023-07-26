
DROP DATABASE IF EXISTS nursery;
CREATE DATABASE nursery;
USE nursery;

DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS animals_title;
DROP TABLE IF EXISTS animals_type;

CREATE TABLE animals_type (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE
) COMMENT 'тип животных';

SET @type1 := 'домашние животные';
SET @type2 := 'вьючные животные';
INSERT INTO `animals_type` (`name`) VALUES (@type1);
INSERT INTO `animals_type` (`name`) VALUES (@type2);
#

CREATE TABLE animals_title (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    parent_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES animals_type(id)
) COMMENT 'вид животных';

SET @id_type1 := (select id from animals_type where name=@type1);
SET @id_type2 := (select id from animals_type where name=@type2);

INSERT INTO `animals_title` (`name`, `parent_id`) VALUES 
('собаки', @id_type1),
('кошки', @id_type1),
('хомяки', @id_type1),
('лошади', @id_type2),
('верблюды', @id_type2),
('ослы', @id_type2)
;

CREATE TABLE animals (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(50) UNIQUE COMMENT 'кличка',
	birthday DATE,
	parent_id BIGINT UNSIGNED NOT NULL,
    INDEX animals_nickname_idx(nickname),
	FOREIGN KEY (parent_id) REFERENCES animals_title(id)
) COMMENT 'животные';

INSERT INTO `animals` (`nickname`, `birthday`, `parent_id`) VALUES 
('жучка',      '1996-11-08', (select id from animals_title where name='собаки')),
('белка',      '2022-12-09', (select id from animals_title where name='собаки')),
('стрелка',    '2021-01-04', (select id from animals_title where name='собаки')),
('васька',     '2020-03-11', (select id from animals_title where name='кошки')),
('мурзик',     '2010-11-15', (select id from animals_title where name='кошки')),
('жрун',       '2023-07-22', (select id from animals_title where name='хомяки')),
('спирит',     '1999-08-08', (select id from animals_title where name='лошади')),
('одногорбый', '2020-03-08', (select id from animals_title where name='верблюды')),
('двугорбый',  '2021-07-08', (select id from animals_title where name='верблюды')),
('леший',      '2016-12-02', (select id from animals_title where name='ослы')),
('агафон',     '2022-02-25', (select id from animals_title where name='ослы'))
;



DROP TABLE IF EXISTS commands;
CREATE TABLE commands(
	id SERIAL,
	name VARCHAR(150)
    #INDEX commands_name_idx(name)
);

INSERT INTO `commands` VALUES (1,'лежать'),(2,'голос'),(3,'ко мне'),(4,'брысь');

DROP TABLE IF EXISTS animals_commands;
CREATE TABLE animals_commands(
	animals_id BIGINT UNSIGNED NOT NULL,
	commands_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (animals_id, commands_id)
    #FOREIGN KEY (animals_id) REFERENCES animals(id) ON UPDATE CASCADE ON DELETE cascade,
    #FOREIGN KEY (commands_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE cascade
);

INSERT INTO `animals_commands` VALUES (1,1),(1,2),(2,2),(2,3),(4,4),(6,4);




