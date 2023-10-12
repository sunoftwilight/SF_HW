CREATE TABLE contacts (
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

INSERT INTO contacts(email, name, age)
VALUES('ssafy@ssafy.com', 'ssafy', 10);

SELECT 
  rowid, *
FROM 
  contacts

PRAGMA table_info('contacts');