drop database if exists phonebook;

create database phonebook;

use phonebook;

create table people (`ФИО`  CHAR(30),
					`Дата рождения` date,
                    `Пол`  char(10),
                    `Страна` char(10),
                    `Город`  char(15),
                    `Домашний адрес` char(50),
                    `Номер телефона` char(12)

); 
    
