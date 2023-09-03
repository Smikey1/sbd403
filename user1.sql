-- Create a table for user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    unit VARCHAR(10),
    street VARCHAR(100),
    postal_code VARCHAR(10),
    state VARCHAR(50),
    suburb VARCHAR(50),
    phone_number VARCHAR(15),
    medical_status VARCHAR(20),
    credit_card_id INT
);

-- Create a table for credit card information (encrypted)
CREATE TABLE credit_cards (
    credit_card_id INT AUTO_INCREMENT PRIMARY KEY,
    card_number VARBINARY(128),  -- VARBINARY for encrypted data
    card_expiry DATE
);

-- Foreign key reference from 'users' to 'credit_cards'
ALTER TABLE users
ADD FOREIGN KEY (credit_card_id)
REFERENCES credit_cards(credit_card_id);


CREATE TABLE user_profile (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(15),
    bio TEXT
);

-- For the login system
SELECT * FROM users WHERE username = 'user_typed_username' AND password = 'user_typed_password';

OR '1'='1'
SELECT * FROM users WHERE username = 'user_typed_username' AND password = 'user_typed_password' OR '1'='1';
