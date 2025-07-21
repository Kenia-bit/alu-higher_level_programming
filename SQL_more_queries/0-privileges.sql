-- ======================================
-- CLEAN START: Drop users if they exist
-- ======================================
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- ======================================
-- CASE 1: Users don't exist
-- Trying to SHOW GRANTS now will give error
-- ======================================
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Expect: ERROR 1141: There is no such grant defined for user 'user_0d_1' on host 'localhost'

-- ======================================
-- CASE 2: Create user_0d_1 as root user with ALL PRIVILEGES
-- ======================================
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- ======================================
-- CASE 3: Create user_0d_2 as root user as well
-- ======================================
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Show grants for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- ======================================
-- CASE 4: user_0d_1 root user, user_0d_2 limited privileges
-- Drop user_0d_2 and recreate with limited privileges
-- ======================================
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password123';

-- Create database for user_0d_2
CREATE DATABASE IF NOT EXISTS user_2_db;

-- Grant SELECT and INSERT only on user_2_db to user_0d_2
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Show grants for both users again
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
