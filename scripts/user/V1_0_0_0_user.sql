CREATE USER IF NOT EXISTS 'SUNDAY_MANAGER_ADMIN' IDENTIFIED BY 'SUNDAY_MANAGER_ADMIN';

CREATE SCHEMA [IF NOT EXISTS] `SUNDAY_MANAGER`;

GRANT ALL PRIVILEGES ON `SUNDAY_MANAGER`.* TO `SUNDAY_MANAGER_ADMIN`;
