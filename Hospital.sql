CREATE DATABASE Hospital;

USE Hospital;

CREATE TABLE Doctor (
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  ssn VARCHAR(255),
  PRIMARY KEY (ssn)
);

CREATE TABLE Patient (
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  ssn VARCHAR(255),
  Doctor VARCHAR(255),
  FOREIGN KEY (Doctor) REFERENCES Doctor(ssn),
  PRIMARY KEY (ssn)
);

CREATE TABLE Building (
  address VARCHAR(255),
  department VARCHAR(255),
  name VARCHAR(255)
);
