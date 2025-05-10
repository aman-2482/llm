CREATE DATABASE IF NOT EXISTS ragdb;
USE ragdb;

CREATE TABLE IF NOT EXISTS federal_register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    document_number VARCHAR(255),
    publication_date DATE,
    summary TEXT
);
