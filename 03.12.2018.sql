-- #1
CREATE SCHEMA `cars` DEFAULT CHARACTER SET utf8;

CREATE TABLE `cars`.`brands` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `brand_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `cars`.`models` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_brand` INT UNSIGNED NOT NULL,
  `model_name` VARCHAR(255) NOT NULL,
  `year` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_models_1_idx` (`id_brand` ASC),
  CONSTRAINT `fk_models_1`
    FOREIGN KEY (`id_brand`)
    REFERENCES `cars`.`brands` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


INSERT INTO brands VALUES (NULL, 'Toyota');
INSERT INTO brands VALUES (NULL, 'Volkswagen');
INSERT INTO brands VALUES (NULL, 'Ford');
INSERT INTO brands VALUES (NULL, 'ВАЗ-2121');

INSERT INTO models VALUES (NULL, 1, 'Camry', 1997);
INSERT INTO models VALUES (NULL, 1, 'Corolla', 2002);
INSERT INTO models VALUES (NULL, 1, 'RAV 4', 2005);
INSERT INTO models VALUES (NULL, 2 'Polo', 2010);
INSERT INTO models VALUES (NULL, 2, 'Tiguan', 2011);
INSERT INTO models VALUES (NULL, 2, 'Golf', 2013);
INSERT INTO models VALUES (NULL, 3, 'F-150', 1996);
INSERT INTO models VALUES (NULL, 3, 'Focus', 2015);
INSERT INTO models VALUES (NULL, 4, 'Нива', 2000);


-- #2
CREATE SCHEMA `movies` DEFAULT CHARACTER SET utf8;

CREATE TABLE `movies`.`directors` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `movies`.`movies` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_dir` INT UNSIGNED NOT NULL,
  `movie_name` VARCHAR(255) NOT NULL,
  `year` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_movies_1_idx` (`id_dir` ASC),
  CONSTRAINT `fk_movies_1`
    FOREIGN KEY (`id_dir`)
    REFERENCES `movies`.`directors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


INSERT INTO directors VALUES (NULL, 'Christopher', 'Nolan');
INSERT INTO directors VALUES (NULL, 'David', 'Fincher');
INSERT INTO directors VALUES (NULL, 'Richard', 'Curtis');
INSERT INTO directors VALUES (NULL, 'Martin', 'Scorsese');


INSERT INTO movies VALUES (NULL, 1, 'Inception', 2010);
INSERT INTO movies VALUES (NULL, 1, 'Dunkirk', 2017);
INSERT INTO movies VALUES (NULL, 2, 'Fight Club', 1999);
INSERT INTO movies VALUES (NULL, 2, 'Seven', 1995);
INSERT INTO movies VALUES (NULL, 2, 'The Curious Case of Benjamin Button', 2008);
INSERT INTO movies VALUES (NULL, 3, 'About Time', 2013);
INSERT INTO movies VALUES (NULL, 4, 'Shutter Island', 2009);
INSERT INTO movies VALUES (NULL, 4, 'The Departed', 2006);
INSERT INTO movies VALUES (NULL, 4, 'Hugo', 2011);

-- #3
CREATE SCHEMA `schools_map` DEFAULT CHARACTER SET utf8;

CREATE TABLE `schools_map`.`districts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `district_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `schools_map`.`schools` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_dis` INT UNSIGNED NOT NULL,
  `type` VARCHAR(200) NULL,
  `number` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_schools_1_idx` (`id_dis` ASC),
  CONSTRAINT `fk_schools_1`
    FOREIGN KEY (`id_dis`)
    REFERENCES `schools_map`.`districts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO districts VALUES (NULL, 'Октябрьский район');
INSERT INTO districts VALUES (NULL, 'Ленинский район');
INSERT INTO districts VALUES (NULL, 'Свердловский район');
INSERT INTO districts VALUES (NULL, 'Первомайский район');


INSERT INTO schools VALUES (NULL, 1, 'школа-гимназия', 17);
INSERT INTO schools VALUES (NULL, 1, 'школа-гимназия', 37);
INSERT INTO schools VALUES (NULL, 1, 'средняя общеобразовательная школа', 14;
INSERT INTO schools VALUES (NULL, 2, 'школа-гимназия', 13);
INSERT INTO schools VALUES (NULL, 2, 'средняя общеобразовательная школа', 2);
INSERT INTO schools VALUES (NULL, 2, 'средняя общеобразовательная школа', 25;
INSERT INTO schools VALUES (NULL, 3, 'школа-гимназия', 12);
INSERT INTO schools VALUES (NULL, 3, 'школа-гимназия', 24);
INSERT INTO schools VALUES (NULL, 3, 'вспомогательная школа для детей с ОВЗ', 30);
INSERT INTO schools VALUES (NULL, 4, 'физ-мат школа-лицей', 61);
INSERT INTO schools VALUES (NULL, 4, 'средняя общеобразовательная школа', 69);