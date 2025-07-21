-- ---------------------------------------------
-- 1. DROP USERS IF THEY EXIST (to start fresh)
-- ---------------------------------------------
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- ---------------------------------------------
-- 2. CASE: Users don't exist (run only above drops)
--    Then try: SHOW GRANTS FOR 'user_0d_1'@'localhost';
--    This will error out, so do NOT run this directly!
-- ---------------------------------------------
-- (No user creation, so error expected)

-- ---------------------------------------------
-- 3. CASE: Create user_0d_1 as root user
-- ---------------------------------------------
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- To check grants run:
-- SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- ---------------------------------------------
-- 4. CASE: Create user_0d_1 and user_0d_2 both as root users
-- ---------------------------------------------
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- To check grants run:
-- SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- ---------------------------------------------
-- 5. CASE: user_0d_1 root user; user_0d_2 has SELECT and INSERT on database user_2_db
-- ---------------------------------------------

-- Drop previous user_0d_2 to redefine
DROP USER IF EXISTS 'user_0d_2'@'localhost';

CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password';

-- Grant only SELECT and INSERT on user_2_db.*
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;

-- To check grants run:
-- SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- SHOW GRANTS FOR 'user_0d_2'@'localhost';
