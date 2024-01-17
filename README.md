# AskMate

You are tasked with creating an application where people can ask questions and post answers to questions.
Like this [tiny site](https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/),
but as a console application.

## Features

### 1st sprint

1. Users can see a list of questions.
2. Users can see which questions have answers.
3. Users can navigate to see one question and all the answers it might have.

### 2nd sprint

4. Users can register, login, and log out. 
5. Only logged-in users can post questions or answers. The author is shown next to questions and answers.

### Optional

6. Users can edit and delete questions and answers authored by them.
7. The list of questions can be ordered by date, author, or title.
8. The list of questions can be filtered for date, author, or title.

## Requirements

* Data must be saved to a database with a persistent layer behind the application.
* You must not expose your db user, db password, or db name to the public internet.
* Dates of posting should be saved with each question and answer.
* Please use a virtual environment and create `requirements.txt`.
* Please change the contents of the `README` file and add instructions on how to run your application.
  * Prerequisites (Python, PSQL)
  * Include DB setup script (table creation, with a few rows of sample data)
  * Steps to set up a virtual environment and install required packages
  * Necessary environment variables, if any
  * Command to start application
* Don't forget to commit and push your changes regularly.

## Recommendations

* Please try and create a user interface that provides good user experience.
* It is recommended to have UI-related code in its module.

## PostgreSQL Database Creation

* You can create the database, and tables and insert some data using the following.
```
  CREATE DATABASE askmate
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Turkish_Turkey.1254'
    LC_CTYPE = 'Turkish_Turkey.1254'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

drop table if exists answers,
drop table if exists questions,
drop table if exists users,

create table users (
	user_id serial primary key,
	username varchar(25) not null,
	email varchar(50) not null,
	is_active boolean not null
)

create table questions(
	question_id serial primary key,
	user_id int references users(user_id),
	title varchar(50) not null,
	description varchar(200) not null,
	created_on timestamp not null,
	modified_on timestamp null,
	is_active boolean not null,
	closed_on timestamp null
)

create table answers(
	answer_id serial primary key,
	user_id int references users(user_id),
	question_id int references questions(question_id),
	description varchar(200) not null,
	created_on timestamp not null,
	modified_on timestamp null,
	is_active boolean not null
)

-- Insert data into the users table
INSERT INTO users (username, email, is_active)
VALUES
    ('john_doe', 'john.doe@example.com', true),
    ('jane_smith', 'jane.smith@example.com', true),
    ('bob_jones', 'bob.jones@example.com', true),
    ('alice_wonder', 'alice.wonder@example.com', true),
    ('charlie_brown', 'charlie.brown@example.com', true);

-- Insert data into the questions table
INSERT INTO questions (user_id, title, description, created_on, is_active, closed_on)
VALUES
    (1, 'How to use Python libraries?', 'I am new to Python, and I want to learn how to use libraries like NumPy and Pandas. Any advice?', CURRENT_TIMESTAMP, true, null),
    (2, 'Best practices for web development', 'What are the best practices for secure and scalable web development? Any recommendations?', CURRENT_TIMESTAMP, true, null),
    (3, 'Trouble with database connections', 'I am having issues connecting to my database using SQLAlchemy. Can someone help me troubleshoot?', CURRENT_TIMESTAMP, true, null),
    (4, 'Career advice for data science', 'I am considering a career in data science. Any tips on getting started and building a successful career?', CURRENT_TIMESTAMP, true, null),
    (5, 'How to optimize SQL queries?', 'What are some techniques for optimizing SQL queries for better performance? Any examples or resources?', CURRENT_TIMESTAMP, true, null);

-- Insert data into the answers table
INSERT INTO answers (user_id, question_id, description, created_on, is_active)
VALUES
    (2, 1, 'You can start by installing these libraries using pip. After that...', CURRENT_TIMESTAMP, true),
    (4, 2, 'For secure web development, always use HTTPS and avoid storing sensitive information in cookies...', CURRENT_TIMESTAMP, true),
    (1, 3, 'Check your database connection string and make sure the credentials are correct. Also...', CURRENT_TIMESTAMP, true),
    (3, 4, 'Focus on building a strong foundation in statistics and programming. Gain hands-on experience...', CURRENT_TIMESTAMP, true),
    (5, 5, 'To optimize SQL queries, consider using indexes, avoiding SELECT * statements, and...', CURRENT_TIMESTAMP, true);
```
