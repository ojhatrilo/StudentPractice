-- on delete cascade

create database if not exists tharani;
use tharani;
CREATE TABLE Student (
    sno INT PRIMARY KEY,
    sname VARCHAR(20),
    age INT

);
INSERT INTO Student(sno, sname,age) 
 VALUES(1,'Ankit',17),
       (2,'Ramya',18),
       (3,'Ram',16);
       
SELECT * FROM Student;       

use tharani;
CREATE TABLE Course (
    cno INT PRIMARY KEY,
    cname VARCHAR(20)
);
INSERT INTO Course(cno, cname) 
 VALUES(101,'c'),
       (102,'c++'),
       (103,'DBMS');
SELECT * FROM Course;

use tharani;
CREATE TABLE Enroll (
    sno INT,
    cno INT,
    jdate date,
    PRIMARY KEY(sno,cno),
    FOREIGN KEY(sno) 
        REFERENCES Student(sno)
        ON DELETE CASCADE,
	FOREIGN KEY(cno) 
        REFERENCES Course(cno)
        ON DELETE CASCADE
);

use tharani;
INSERT INTO Enroll(sno,cno,jdate) 
 VALUES(1, 101, '2021-05-01'),
       (1, 102, '2021-05-01'),
       (2, 103, '2021-05-01');

SELECT * FROM Enroll;

use tharani;
DELETE FROM Student
WHERE sname="Ramya";


SET SQL_SAFE_UPDATES=0;

CREATE TABLE Student_details (
ROLL_NO INT,
NAME VARCHAR(25),
ADDRESS VARCHAR(25),
PHONE INT ,
AGE INT); 
INSERT INTO Student_details(ROLL_NO,NAME,ADDRESS,PHONE,AGE) VALUES 
(1,'Ram','Delhi',94155366,24),
(2,'Ramesh','Gurgaon',94145766,21),
(3,'Sujit','Delhi',98155326,20),
(4,'Suresh','Noida',91155366,21),
(5,'Kajal','Gurgaon',89155367,28),
(6,'Garima','Rohtak',70155356,23);

select * from Student_details;


TRUNCATE TABLE Student_details;
select * from Student_details;

SET SQL_SAFE_UPDATES=1;


use ranju;
CREATE TABLE GFGemployees(employee_id 
INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT);

INSERT INTO GFGemployees (employee_id, employee_name, manager_id)
VALUES  (1, 'Zaid', 3),  (2, 'Rahul', 3),  (3, 'Raman', 4),  
(4, 'Kamran', NULL),  (5, 'Farhan', 4);

SELECT e.employee_name AS employee,
m.employee_name AS manager FROM 
GFGemployees AS e JOIN GFGemployees 
AS m ON m.manager_id = e.employee_id;




















