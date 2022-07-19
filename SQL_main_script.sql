create database if not exists Course_work_db;
use Course_work_db;

-- MySQL Script generated by MySQL Workbench
-- Sun Jun 26 16:05:36 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Course_work_db` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Course_work_db` DEFAULT CHARACTER SET utf8 ;
USE `Course_work_db` ;

-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Course_work_db`.`User` ;

CREATE TABLE IF NOT EXISTS `Course_work_db`.`User` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User_enter_and_exit`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Course_work_db`.`User_enter_and_exit` ;

CREATE TABLE IF NOT EXISTS `Course_work_db`.`User_enter_and_exit` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `open_close` VARCHAR(1) NULL,
  `time` datetime not null,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`)
)

ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=0;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
