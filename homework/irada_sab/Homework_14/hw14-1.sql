INSERT INTO students(name, second_name) VALUES('Sabina', 'Sab')

INSERT INTO books(title) VALUES('The Financier')

INSERT INTO books(title) VALUES('Eat Pray Love')

INSERT INTO books(title) VALUES('Lessons in Chemistry')


UPDATE books
SET taken_by_student_id = 21310
WHERE id = 2990

UPDATE books SET taken_by_student_id = 21310 WHERE id = 2991

UPDATE books SET taken_by_student_id = 21310 WHERE id = 2992


INSERT INTO `groups` (title, start_date, end_date) VALUES('SW-HW', '9-19-2025', '11-01-2025')

UPDATE students SET group_id = 21286 WHERE id = 21310


INSERT INTO subjects (title) VALUES('Engineering')

INSERT INTO subjects (title) VALUES('Technology')

INSERT INTO subjects (title) VALUES('(Science')

UPDATE subjects SET title = 'Science' WHERE id = 12282


INSERT INTO lessons (title, subject_id) VALUES('Engineer-1', 12280)
INSERT INTO lessons (title, subject_id) VALUES('Engineer-2', 12280)

INSERT INTO lessons (title, subject_id) VALUES('Tech-1', 12281)
INSERT INTO lessons (title, subject_id) VALUES('Tech-2', 12281)

INSERT INTO lessons (title, subject_id) VALUES('Science-1', 12282)
INSERT INTO lessons (title, subject_id) VALUES('Science-2', 12282)

INSERT INTO marks (value, lesson_id) VALUES('(98', 12757)
UPDATE marks SET value = '98' WHERE lesson_id = 12757
UPDATE marks SET student_id = 21310 WHERE id = 9740

INSERT INTO marks (value, lesson_id) VALUES('97', 12758)
UPDATE marks SET student_id = 21310 WHERE id = 9741

INSERT INTO marks (value, lesson_id) VALUES('95', 12759)
UPDATE marks SET student_id = 21310 WHERE id = 9742

INSERT INTO marks (value, lesson_id) VALUES('96', 12760)
UPDATE marks SET student_id = 21310 WHERE id = 9743

INSERT INTO marks (value, lesson_id) VALUES('91', 12761)
UPDATE marks SET student_id = 21310 WHERE id = 9744

INSERT INTO marks (value, lesson_id) VALUES('93', 12762)
UPDATE marks SET student_id = 21310 WHERE id = 9745


SELECT
	students.name,
	marks.value
FROM
	students
INNER JOIN marks on students.id = marks.student_id WHERE students.name = 'Sabina'


SELECT
	books.title,	
	students.name	
FROM 
	books 
INNER JOIN students on books.taken_by_student_id = students.id WHERE books.taken_by_student_id = 21310


-- Для вашего студента выведите всё, что о нем есть в базе: 
-- группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

SELECT
	students.name as 'Student name',
	`groups`.title as 'Group name',
	subjects.title as 'Subject',
	lessons.title as 'Lesson',
	marks.value as 'Student mark',
	books.title as 'Book title'
FROM
	`groups`
JOIN students on `groups`.id = students.group_id
JOIN books on students.id = books.taken_by_student_id
JOIN marks on students.id = marks.student_id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjects on lessons.subject_id = subjects.id WHERE students.name = 'Sabina'



	
	
