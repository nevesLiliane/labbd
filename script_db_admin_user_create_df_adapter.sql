
CREATE USER "admin" WITH PASSWORD 'monetdb' NAME 'Administrator' SCHEMA "sys";
CREATE SCHEMA "provdf" AUTHORIZATION "admin";
ALTER USER "admin" SET SCHEMA "provdf";