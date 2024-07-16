#22.	Similar exercise may be framed for other cases.
#Switched to a database
mysql> USE GVKCV;
Database changed

#Creating table student
mysql> create table student
    -> (ROLLNO INT NOT NULL PRIMARY KEY,
    -> NAME CHAR(10),
    -> English CHAR(10),
    -> HINDI CHAR(10),
    -> MATHS CHAR(10));
Query OK, 0 rows affected (1.38 sec)

#Inserting values into table
mysql> insert into student
    -> values(101,"student1",50,51,52),
    -> (102,"student2",60,61,62),
    -> (103,"student3",70,71,72),
    -> (104,"student4",80,81,82),
    -> (105,"student5",90,91,92),
    -> (106,"student6",40,41,42),
    -> (107,"student7",63,64,65);
Query OK, 7 rows affected (0.24 sec)
Records: 7  Duplicates: 0  Warnings: 0

#Adding new attribute computers
mysql> alter table student
    -> add (computers char(10));
Query OK, 0 rows affected (1.13 sec)
Records: 0  Duplicates: 0  Warnings: 0

#Describing table
mysql> desc student;
+-----------+----------+------+-----+---------+-------+
| Field     | Type     | Null | Key | Default | Extra |
+-----------+----------+------+-----+---------+-------+
| ROLLNO    | int      | NO   | PRI | NULL    |       |
| NAME      | char(10) | YES  |     | NULL    |       |
| English   | char(10) | YES  |     | NULL    |       |
| HINDI     | char(10) | YES  |     | NULL    |       |
| MATHS     | char(10) | YES  |     | NULL    |       |
| computers | char(10) | YES  |     | NULL    |       |
+-----------+----------+------+-----+---------+-------+
6 rows in set (0.21 sec)

#Modifying the datatype
mysql> alter table student
    -> modify column computers varchar(10);
Query OK, 7 rows affected (2.38 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> desc student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| ROLLNO    | int         | NO   | PRI | NULL    |       |
| NAME      | char(10)    | YES  |     | NULL    |       |
| English   | char(10)    | YES  |     | NULL    |       |
| HINDI     | char(10)    | YES  |     | NULL    |       |
| MATHS     | char(10)    | YES  |     | NULL    |       |
| computers | varchar(10) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
6 rows in set (0.11 sec)

#Droping a attribute
mysql> alter table student
    -> drop column computers;
Query OK, 0 rows affected (0.93 sec)
Records: 0  Duplicates: 0  Warnings: 0

#Describing table
mysql> desc student;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| ROLLNO | int      | NO   | PRI | NULL    |       |
| NAME   | char(10) | YES  |     | NULL    |       |
| English| char(10) | YES  |     | NULL    |       |
| HINDI  | char(10) | YES  |     | NULL    |       |
| MATHS  | char(10) | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
5 rows in set (0.14 sec)

#UPDATE DATA TO MODIFY DATA
#ACTUAL DATA
mysql> select *from student;
+--------+----------+--------+-------+-------+
| ROLLNO | NAME     | English| HINDI | MATHS |
+--------+----------+--------+-------+-------+
|    101 | student1 | 50     | 51    | 52    |
|    102 | student2 | 60     | 61    | 62    |
|    103 | student3 | 70     | 71    | 72    |
|    104 | student4 | 80     | 81    | 82    |
|    105 | student5 | 90     | 91    | 92    |
|    106 | student6 | 40     | 41    | 42    |
|    107 | student7 | 63     | 64    | 65    |
+--------+----------+--------+-------+-------+
7 rows in set (0.00 sec)

#UPDATE THE MARKS FOR ATTRIBUTE English FOR THE STUDENT101
mysql> UPDATE STUDENT
    -> SET English=99
    -> WHERE ROLLNO=101;
Query OK, 1 row affected (0.12 sec)
Rows matched: 1  Changed: 1  Warnings: 0

#DATA IN THE TABLE AFTER UPDATING
mysql> SELECT *FROM STUDENT;
+--------+----------+--------+-------+-------+
| ROLLNO | NAME     | English| HINDI | MATHS |
+--------+----------+--------+-------+-------+
|    101 | student1 | 99     | 51    | 52    |
|    102 | student2 | 60     | 61    | 62    |
|    103 | student3 | 70     | 71    | 72    |
|    104 | student4 | 80     | 81    | 82    |
|    105 | student5 | 90     | 91    | 92    |
|    106 | student6 | 40     | 41    | 42    |
|    107 | student7 | 63     | 64    | 65    |
+--------+----------+--------+-------+-------+
7 rows in set (0.00 sec)

#ORDER BY DESCENDING ORDER
mysql> SELECT *FROM STUDENT
    -> ORDER BY HINDI DESC;
+--------+----------+--------+-------+-------+
| ROLLNO | NAME     | English| HINDI | MATHS |
+--------+----------+--------+-------+-------+
|    105 | student5 | 90     | 91    | 92    |
|    104 | student4 | 80     | 81    | 82    |
|    103 | student3 | 70     | 71    | 72    |
|    107 | student7 | 63     | 64    | 65    |
|    102 | student2 | 60     | 61    | 62    |
|    101 | student1 | 99     | 51    | 52    |
|    106 | student6 | 40     | 41    | 42    |
+--------+----------+--------+-------+-------+
7 rows in set (0.05 sec)

#ORDER BY ASCENDING ORDER
mysql> SELECT *FROM STUDENT
    -> ORDER BY HINDI ASC;
+--------+----------+--------+-------+-------+
| ROLLNO | NAME     | English| HINDI | MATHS |
+--------+----------+--------+-------+-------+
|    106 | student6 | 40     | 41    | 42    |
|    101 | student1 | 99     | 51    | 52    |
|    102 | student2 | 60     | 61    | 62    |
|    107 | student7 | 63     | 64    | 65    |
|    103 | student3 | 70     | 71    | 72    |
|    104 | student4 | 80     | 81    | 82    |
|    105 | student5 | 90     | 91    | 92    |
+--------+----------+--------+-------+-------+
7 rows in set (0.00 sec)

#DELETING A TUPLE FROM THE TABLE
mysql> DELETE FROM STUDENT
    -> WHERE ROLLNO=101;
Query OK, 1 row affected (0.14 sec)

mysql> SELECT *FROM STUDENT;
+--------+----------+--------+-------+-------+
| ROLLNO | NAME     | English| HINDI | MATHS |
+--------+----------+--------+-------+-------+
|    102 | student2 | 60     | 61    | 62    |
|    103 | student3 | 70     | 71    | 72    |
|    104 | student4 | 80     | 81    | 82    |
|    105 | student5 | 90     | 91    | 92    |
|    106 | student6 | 40     | 41    | 42    |
|    107 | student7 | 63     | 64    | 65    |
+--------+----------+--------+-------+-------+
6 rows in set (0.06 sec)

#ORDER BY BRANCH

#ACTUAL DATA
mysql> SELECT *FROM STUDENT;
+--------+--------+----------+--------+-------+-------+
| ROLLNO | BRANCH | NAME     | English| HINDI | MATHS |
+--------+--------+----------+--------+-------+-------+
|    102 | Shilaj | student2 | 60     | 61    | 62    |
|    103 | Cant   | student3 | 70     | 71    | 72    |
|    104 | Cant   | student4 | 80     | 81    | 82    |
|    105 | Cant   | student5 | 90     | 91    | 92    |
|    106 | Cant   | student6 | 40     | 41    | 42    |
|    107 | Shilaj | student7 | 63     | 64    | 65    |
+--------+--------+----------+--------+-------+-------+
6 rows in set (0.00 sec)

mysql> SELECT BRANCH,COUNT(*)
    -> FROM STUDENT
    -> GROUP BY BRANCH;
+--------+----------+
| BRANCH | COUNT(*) |
+--------+----------+
| Shilaj    |        2 |
| Cant   |        4 |
+--------+----------+
2 rows in set (0.01 sec)

#e min, max, sum, count and average
mysql> SELECT MIN(English) "English MIN MARKS"
    -> FROM STUDENT;
+------------------+
| English MIN MARKS |
+------------------+
| 40               |
+------------------+
1 row in set (0.00 sec)

mysql> SELECT MAX(English) "English MAX MARKS"
    -> FROM STUDENT;
+------------------+
| English MAX MARKS |
+------------------+
| 90               |
+------------------+
1 row in set (0.00 sec)

mysql> SELECT SUM(English) "English TOTAL MARKS"
    -> FROM STUDENT;
+--------------------+
| English TOTAL MARKS |
+--------------------+
|                403 |
+--------------------+
1 row in set (0.00 sec)

mysql> SELECT COUNT(ROLLNO)
    -> FROM STUDENT;
+---------------+
| COUNT(ROLLNO) |
+---------------+
|             6 |
+---------------+
1 row in set (0.01 sec)

mysql> SELECT AVG(English) "English AVG MARKS"
    -> FROM STUDENT;
+-------------------+
| English AVG MARKS  |
+-------------------+
| 67.16666666666667 |
+-------------------+