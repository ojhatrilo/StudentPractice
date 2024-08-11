use abulaziz;
drop table student_data;
create table Student_Data(
id INT auto_increment primary key,
name char(50) not null,
age INT not null,
mark INT not null,
grade char(1) not null,
city varchar(100) not null,
DOB date not null
);
insert into Student_Data(name,age,mark,grade,city,DOB)values
("Suresh", 18, 79, "B", "Mumbai", '2001-04-25'),
("Satish", 18, 90, "A", "Delhi", '2001-05-24'),
("Nizam", 19, 50, "C", "Nagpur", '2001-08-29'),
("Anita", 20, 85, "A", "Chennai", '2000-12-15'),
("Ravi", 18, 65, "B", "Bangalore", '2001-07-10'),
("Priya", 19, 70, "B", "Hyderabad", '2001-03-22'),
("Kiran", 18, 55, "C", "Pune", '2001-11-05'),
("Meena", 20, 95, "A", "Kolkata", '2000-09-18'),
("Raj", 19, 60, "B", "Ahmedabad", '2001-01-30'),
("Vijay", 18, 75, "B", "Jaipur", '2001-06-14'),
("Divya", 19, 80, "A", "Surat", '2001-02-28');

select * from Student_Data where id = 1;
select id,mark,grade,name from Student_Data where name = "Divya";
select * from Student_Data where mark>=90;

select * from Student_Data where mark>60 and city = "Mumbai";

select * from Student_Data where mark between 80 and 90;

select * from Student_Data limit 5;

select * from Student_Data order by id desc;


create table Student_Enroll(
id INT auto_increment primary key,
course varchar(200) not null,
stu_id int,
foreign key (stu_id) references Student_data(id)
);
insert into Student_Enroll(course,stu_id)
values("Python",2),
("Power BI", 4),
("Java",3);

insert into Student_Enroll(course,stu_id)
values("Python",21);


select * from student_enroll;




