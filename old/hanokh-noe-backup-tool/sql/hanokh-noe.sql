-- CREATE DATABASE noe;

-- USE noe;

CREATE TABLE country (
  id_country SERIAL PRIMARY KEY,
  country_name VARCHAR(50),
  initials_country TEXT
);

CREATE TABLE state (
  id_state SERIAL PRIMARY KEY,
  state_name VARCHAR(50),
  initials_state VARCHAR(5),
  id_country INT REFERENCES country(id_country)
);

CREATE TABLE city (
  id_city SERIAL PRIMARY KEY,
  city_name VARCHAR(50),
  id_state INT REFERENCES state(id_state)
);

CREATE TABLE neighborhood (
  id_neighborhood SERIAL PRIMARY KEY,
  neighborhood_name VARCHAR(50),
  id_city INT REFERENCES city(id_city)
);

CREATE TABLE street (
  id_street SERIAL PRIMARY KEY,
  cep VARCHAR(50),
  street_name VARCHAR(50),
  id_neighborhood INT REFERENCES neighborhood(id_neighborhood)
);

CREATE TABLE address (
  id_address SERIAL PRIMARY KEY,
  home_number INT,
  additional_information VARCHAR(500),
  id_street INT REFERENCES street(id_street)
);

CREATE TABLE person (
  id_person SERIAL PRIMARY KEY,
  name VARCHAR(50),
  surname VARCHAR(50),
  email VARCHAR(50),
  username VARCHAR(50),
  password VARCHAR(500),
  id_address INT REFERENCES address(id_address)
);

CREATE TABLE profile(
  id_profile SERIAL PRIMARY KEY,
  name_profile VARCHAR(50),
  desc_profile VARCHAR(500)
);

CREATE TABLE team (
  id_team SERIAL PRIMARY KEY,
  team_name VARCHAR(200),
  id_profile INT REFERENCES profile(id_profile)
);

CREATE TABLE team_person (
  id_team_person SERIAL PRIMARY KEY,
  id_person INT REFERENCES person(id_person),
  id_team INT REFERENCES team(id_team)
);

CREATE TABLE type_backup(
  id_type_backup SERIAL PRIMARY KEY,
  name_type_backup VARCHAR(200),
  desc_type_backup VARCHAR(500),
  is_local_storage INT,
  is_remote_storage INT
);

CREATE TABLE access_rights(
  id_access_rights SERIAL PRIMARY KEY,
  access_user VARCHAR(200),
  access_password VARCHAR(500),
  has_private_key INT,
  private_key VARCHAR(10000),
  id_type_backup INT REFERENCES type_backup(id_type_backup)
);

CREATE TABLE backup(
  id_backup SERIAL PRIMARY KEY,
  folder_backup VARCHAR(200),
  folder_dest_baackup VARCHAR(200),
  id_type_backup INT REFERENCES type_backup(id_type_backup)
);

CREATE TABLE team_backup(
  id_team_backup SERIAL PRIMARY KEY,
  id_team INT REFERENCES team(id_team),
  id_backup INT REFERENCES backup(id_backup)
);
