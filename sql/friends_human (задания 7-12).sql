DROP DATABASE IF EXISTS friends_human;
CREATE DATABASE friends_human;
USE friends_human;

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
    nickname VARCHAR(50) COMMENT 'кличка',
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


# удаляем верблюдов
delete from animals where parent_id = (select id from animals_title where name='верблюды');

select a.nickname , tit.name , typ.name , a.birthday
from animals a 
	left join animals_title tit on (a.parent_id = tit.id)
	left join animals_type typ on (tit.parent_id = typ.id)
;

# создаем новую таблицу “молодые животные”
DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals
	select * FROM animals a 
	where (TIMESTAMPDIFF(year,a.birthday, now()) between 1 and 3)
;

select  a.nickname , 
		tit.name , 
		typ.name , 
		a.birthday,
    	concat(
    		(@y := YEAR(CURRENT_DATE)-YEAR(a.birthday))-(RIGHT(CURRENT_DATE,5)<RIGHT(a.birthday,5)),
    		' год(а), ',
	    	(TIMESTAMPDIFF(MONTH, a.birthday, curdate()) - @y*(12-(RIGHT(CURRENT_DATE,5)<RIGHT(a.birthday,5)))),
	    	' месяца(цев)'
    	) as age
from young_animals a 
	left join animals_title tit on (a.parent_id = tit.id)
	left join animals_type typ on (tit.parent_id = typ.id)
;



