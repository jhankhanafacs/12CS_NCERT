'''21. Create a student table and insert data. Implement the following SQL commands on the student table:
o ALTER table to add new attributes / modify data type / drop attribute
o UPDATE table to modify data
o ORDER By to display data in ascending / descending order
o DELETE to remove tuple(s)
o GROUP BY and find the min, max, sum, count and average'''
-- Create a student table
CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    marks INT
);

-- Insert data into the student table
INSERT INTO student (student_id, first_name, last_name, age, marks)
VALUES
    (1, 'John', 'Doe', 18, 85),
    (2, 'Jane', 'Smith', 19, 92),
    (3, 'Alice', 'Johnson', 20, 78),
    (4, 'Bob', 'Williams', 18, 95);

-- Display the student table
SELECT * FROM student;

-- ALTER table to add a new attribute
ALTER TABLE student
ADD COLUMN email VARCHAR(100);

-- ALTER table to modify data type
ALTER TABLE student
MODIFY COLUMN age VARCHAR(3);

-- ALTER table to drop an attribute
ALTER TABLE student
DROP COLUMN marks;

-- UPDATE table to modify data
UPDATE student
SET age = 21
WHERE student_id = 3;

-- ORDER BY to display data in ascending order of age
SELECT * FROM student
ORDER BY age ASC;

-- ORDER BY to display data in descending order of marks
SELECT * FROM student
ORDER BY marks DESC;

-- DELETE to remove a tuple
DELETE FROM student
WHERE student_id = 2;

-- GROUP BY and find the min, max, sum, count, and average
SELECT
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    SUM(age) AS total_age,
    COUNT(*) AS total_students,
    AVG(age) AS avg_age
FROM student;

