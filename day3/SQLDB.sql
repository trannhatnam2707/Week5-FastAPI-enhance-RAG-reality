create database PostStatus
use PostStatus
go 

create table tasks 
( 
	ID int IDENTITY (1,1)Primary key not null ,
	title Nvarchar(255) not null, 
	content nvarchar (1000) null, 
	author nvarchar (255) null, 
); 
go