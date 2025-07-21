#!/bin/bash
# Usage: ./check_privileges.sh

MYSQL_USER="root"
MYSQL_PASS="your_root_password"
MYSQL_CMD="mysql -u$MYSQL_USER -p$MYSQL_PASS -sNe"

for user in user_0d_1 user_0d_2; do
  exists=$($MYSQL_CMD "SELECT COUNT(*) FROM mysql.user WHERE user='$user' AND host='localhost';")

  if [ "$exists" -eq 1 ]; then
    echo "Grants for $user@localhost"
    $MYSQL_CMD "SHOW GRANTS FOR '$user'@'localhost';"
  else
    echo "There is no such grant defined for user '$user' on host 'localhost'"
  fi
done
