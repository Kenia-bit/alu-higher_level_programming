-- Drop users if they exist to simulate 'users don't exist' case first
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Try showing grants now — should error out with "There is no such grant defined for user ..."

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Now create user_0d_1 with root privileges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create user_0d_2 with limited privileges on a specific database

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'password2';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Flush privileges

FLUSH PRIVILEGES;

-- Show grants again to verify

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
