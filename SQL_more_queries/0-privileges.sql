-- ======================================
-- CLEAN START: Drop users if they exist
-- ======================================
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- ======================================
-- CASE 1: Users don't exist
-- Expect: ERROR 1141 (42000)
-- ======================================
-- This should return:
-- "There is no such grant defined for user 'user_0d_1' on host 'localhost'"
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- ======================================
-- CASE 2: Create user_0d_1 as root user with ALL PRIVILEGES
-- Expect: user_0d_1 has root privileges
-- ======================================
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Confirm user_0d_1 privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- ======================================
-- CASE 3: Create user_0d_2 as root user as well
-- Expect: user_0d_1 and user_0d_2 both have root privileges
-- ======================================
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Confirm both users' privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- ======================================
-- CASE 4: Revoke root from user_0d_2 and assign limited privileges
-- Expect: user_0d_1 root, user_0d_2 has only SELECT and INSERT on user_2_db
-- ======================================
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password123';

-- Ensure database exists
CREATE DATABASE IF NOT EXISTS user_2_db;

-- Grant only SELECT and INSERT on user_2_db to user_0d_2
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Final verification of privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
