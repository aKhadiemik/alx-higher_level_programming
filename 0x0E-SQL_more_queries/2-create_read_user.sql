-- Creates hbtn_0d_2 db and user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privileges to user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
