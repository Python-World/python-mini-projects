-- Insert your database name in place of DATABASE_NAME and table name in place of TABLE_NAME

CREATE DATABASE DATABASE_NAME;

USE DATABASE_NAME;

CREATE TABLE `DATABASE_NAME`.`TABLE_NAME` ( `Name` VARCHAR(100) NOT NULL , `Username` VARCHAR(80) NOT NULL , `Email` VARCHAR(150) NOT NULL , `Password` VARCHAR(100) NOT NULL , `ConfirmPassword` VARCHAR(100) NOT NULL , PRIMARY KEY (`Name`, `Username`), UNIQUE (`Username`));

CREATE TABLE `DATABASE_NAME`.`TABLE_NAME` (`longLink` VARCHAR(300) NOT NULL , `shortLink` VARCHAR(100) NOT NULL , `username` VARCHAR(100) NOT NULL , `linkCode` VARCHAR(100) NOT NULL , PRIMARY KEY (`longLink`), UNIQUE (`linkCode`));