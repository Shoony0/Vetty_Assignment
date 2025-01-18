-- Grant all permissions to the user
GRANT ALL PRIVILEGES ON *.* TO 'vetty_user'@'%' WITH GRANT OPTION;

-- Reload the privilege tables
FLUSH PRIVILEGES;
