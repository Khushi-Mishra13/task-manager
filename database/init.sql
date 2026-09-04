create database if not exists tasks;
use tasks;

create table if not exists tasks(Serial_No int AUTO_INCREMENT PRIMARY KEY, title varchar(255) not null, completed BOOLEAN DEFAULT FALSE);

insert into tasks(Serial_No,title,completed)values(1,"Complete DST Assignment",FALSE),(2,"Revise Statistics",FALSE),(3,"Submit Documents",FALSE);

