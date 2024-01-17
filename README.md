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

4. Users can register, log in and log out. 
5. Only logged in users can post questions or answers. Author is shown next to questions and answers.

### Optional

6. Users can edit and delete questions and answers authored by them.
7. The list of questions can be ordered by date or author or title.
8. The list of questions can be filtered for date or author or title.

## Requirements

* Data must be saved to a database that provides a persistent layer behind the application.
* You must not expose your db user, db password or db name to the public internet.
* Dates of posting should be saved with each question and answer.
* Please use a virtual environment and create `requirements.txt`.
* Please change the contents of the `README` file and add instructions on how to run your application.
  * Prerequisites (Python, PSQL)
  * Include DB setup script (table creation, with a few rows of sample data)
  * Steps to set up virtual environment and install required packages
  * Necessary environment variables, if any
  * Command to start application
* Don't forget to commit and push your changes regularly.

## Recommendations

* Please try and create a user interface that provides good user experience.
* It is recommended to have UI related code in its own module.
