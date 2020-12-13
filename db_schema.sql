DROP TABLE IF EXISTS Registration;
DROP TABLE IF EXISTS Users;

CREATE TABLE Registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name TEXT,
    last_name TEXT,
    email TEXT,
    address TEXT,
    city TEXT,
    password TEXT,
    gender TEXT
);

CREATE TABLE Users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    reg_id INTEGER,
    item INTEGER,
    amount Float,
    date DATE
);



INSERT INTO Registration
                    (first_name, last_name, email, address, city, password, gender)VALUES("Marcus", "Brown", "mbrown@gmail.com", "123 Maiden Lane", "New York", "Cats123", "Male");
