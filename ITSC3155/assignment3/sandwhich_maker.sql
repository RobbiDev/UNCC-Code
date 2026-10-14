-- assignment 3 - sandwich maker database

-- make the database and switch to it
create database sandwich_maker;
use sandwich_maker;

-- tables
create table resources (
    item varchar(50),
    amount int
);

create table sandwiches (
    sandwich_size varchar(50),
    price decimal(5,2)
);

create table recipes (
    sandwich_size varchar(50),
    item varchar(50),
    amount int
);

-- data
insert into resources (item, amount) values
('bread', 12),
('ham', 18),
('cheese', 24);

insert into sandwiches (sandwich_size, price) values
('small', 1.75),
('medium', 3.25),
('large', 5.5);

insert into recipes (sandwich_size, item, amount) values
('small', 'bread', 2),
('small', 'ham', 4),
('small', 'cheese', 4),
('medium', 'bread', 4),
('medium', 'ham', 6),
('medium', 'cheese', 8),
('large', 'bread', 6),
('large', 'ham', 8),
('large', 'cheese', 12);

-- check everything went in
select * from resources;
select * from sandwiches;
select * from recipes;
