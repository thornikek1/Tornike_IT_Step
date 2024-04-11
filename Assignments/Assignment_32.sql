-- 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
USE IT_STEP;
CREATE TABLE Author (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    AuthorName VARCHAR(255),
    AuthorCountry VARCHAR(100),
    AuthorDOB DATE,
    AuthorBio TEXT
);

-- 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    BookTitle VARCHAR(255),
    AuthorID INT,
    PublicationYear INT,
    Genre VARCHAR(100),
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Author (AuthorName, AuthorCountry, AuthorDOB, AuthorBio) VALUES
('Author 1', 'Country 1', '1990-01-01', 'Bio 1'),
('Author 2', 'Country 2', '1985-05-10', 'Bio 2'),
('Author 3', 'Country 3', '1978-11-20', 'Bio 3'),
('Author 4', 'Country 4', '1982-03-15', 'Bio 4'),
('Author 5', 'Country 5', '1995-07-25', 'Bio 5');

INSERT INTO Books (BookTitle, AuthorID, PublicationYear, Genre) VALUES
('Book 1', 1, 2010, 'Fiction'),
('Book 2', 2, 2005, 'Non-Fiction'),
('Book 3', 3, 2015, 'Mystery'),
('Book 4', 4, 2008, 'Thriller'),
('Book 5', 5, 2020, 'Science Fiction');

-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books SET PublicationYear = 2012 WHERE BookTitle = 'Book 1';

-- 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE FROM Author;
DELETE FROM Books;

-- 6. წაშალეთ Author და Books ცხრილები
DROP TABLE Author;
DROP TABLE Books;
