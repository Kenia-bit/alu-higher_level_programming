-- For user_0d_1
DO
BEGIN
  DECLARE user_exists INT DEFAULT 0;
  SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

  IF user_exists = 1 THEN
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
  ELSE
    SELECT 'There is no such grant defined for user ''user_0d_1'' on host ''localhost''' AS ErrorMessage;
  END IF;
END;

-- For user_0d_2
DO
BEGIN
  DECLARE user_exists INT DEFAULT 0;
  SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';

  IF user_exists = 1 THEN
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
  ELSE
    SELECT 'There is no such grant defined for user ''user_0d_2'' on host ''localhost''' AS ErrorMessage;
  END IF;
END;
