-- create  a table users 
-- attr id, email, name

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY_KEY,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255)
);
