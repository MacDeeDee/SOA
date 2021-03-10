-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema SOA
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `SOA` ;

-- -----------------------------------------------------
-- Schema SOA
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SOA` DEFAULT CHARACTER SET utf8 ;
USE `SOA` ;

-- -----------------------------------------------------
-- Table `SOA`.`personalInfo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SOA`.`personalInfo` ;

CREATE TABLE IF NOT EXISTS `SOA`.`personalInfo` (
  `SID` VARCHAR(20) NOT NULL,
  `name` VARCHAR(191) NOT NULL,
  `gender` VARCHAR(191) NOT NULL,
  `DOB` DATE NOT NULL,
  PRIMARY KEY (`SID`),
  UNIQUE INDEX `userID_UNIQUE` (`SID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `SOA`.`email`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SOA`.`email` ;

CREATE TABLE IF NOT EXISTS `SOA`.`email` (
  `SID` VARCHAR(20) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`SID`, `email`),
  CONSTRAINT `email_SID`
    FOREIGN KEY (`SID`)
    REFERENCES `SOA`.`personalInfo` (`SID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `SOA`.`relative`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SOA`.`relative` ;

CREATE TABLE IF NOT EXISTS `SOA`.`relative` (
  `SID` VARCHAR(20) NOT NULL,
  `relationship` VARCHAR(20) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `address` VARCHAR(191) NOT NULL,
  PRIMARY KEY (`SID`, `address`),
  CONSTRAINT `relative_SID`
    FOREIGN KEY (`SID`)
    REFERENCES `SOA`.`personalInfo` (`SID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
