DROP DATABASE IF EXISTS `taskrecord`;
CREATE DATABASE IF NOT EXISTS `taskrecord`;
USE `taskrecord`;

CREATE TABLE IF NOT EXISTS `category` (
	category_no INT(3) NOT NULL,
	category_name VARCHAR(50) NOT NULL,
	date_created DATE NOT NULL,
	CONSTRAINT category_no_pk PRIMARY KEY(category_no)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO category (category_no, category_name, date_created) VALUES 
	(001, 'Academics', '2022-04-24'),
	(002, 'Org related', '2022-04-24'),
	(003, 'Personal tasks', '2022-04-24');

CREATE TABLE IF NOT EXISTS `task` (
	task_no INT(3) NOT NULL,
	category_no INT(3) NOT NULL,
	task_name VARCHAR(50) NOT NULL,
	due_date DATE NOT NULL,
	date_created DATE NOT NULL,
	description VARCHAR(50) NOT NULL,
	status VARCHAR(20) NOT NULL,
	CONSTRAINT task_task_no_pk PRIMARY KEY(task_no),
	CONSTRAINT task_category_no_fk FOREIGN KEY(category_no) REFERENCES category(category_no)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO task (task_no, category_no, task_name, due_date, date_created, description, status) VALUES 
	(001, 001, 'CMSC127 Project', '2022-06-03', '2022-04-25', 'Accomplish milestone 3', 'Ongoing'),
	(002, 001, 'STAT151 Exercise 5', '2022-05-05', '2022-04-27', 'Accomplish exercise on module 3', 'Done'),
	(003, 002, 'UPLB DOSTSS Publication work', '2022-05-01', '2022-04-26', 'Create publication material for SW', 'Not yet started'),
	(004, 001, 'STAT151 Exercise 6', '2022-05-10', '2022-05-12', 'Accomplish exercise on module 4', 'Ongoing');




