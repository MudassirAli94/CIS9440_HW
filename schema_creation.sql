CREATE SCHEMA la_crime;

CREATE TABLE la_crime.dim_date_time ( 
	date_occ int64 NOT NULL  ,
	date_rptd int64 NOT NULL  ,
	time_occ string NOT NULL  ,
	hour int64 NOT NULL  ,
	minute int64 NOT NULL,
	day_of_week string NOT NULL
 );

ALTER TABLE la_crime.dim_date_time ADD PRIMARY KEY ( date_occ )  NOT ENFORCED;

CREATE TABLE la_crime.dim_area ( 
	area_cd int64 NOT NULL  ,
	area_name string NOT NULL
 );

ALTER TABLE la_crime.dim_area ADD PRIMARY KEY ( area_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_crime ( 
	crm_cd int64 NOT NULL  ,
	crm_desc string NOT NULL
 );

ALTER TABLE la_crime.dim_crime ADD PRIMARY KEY ( crm_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_premise ( 
	premise_cd int64 NOT NULL  ,
	premise_desc string NOT NULL
 );

ALTER TABLE la_crime.dim_premise ADD PRIMARY KEY ( premise_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_weapon ( 
	weapon_cd int64 NOT NULL  ,
	weapon_desc string NOT NULL
 );

ALTER TABLE la_crime.dim_weapon ADD PRIMARY KEY ( weapon_cd )  NOT ENFORCED;

CREATE TABLE la_crime.la_crime_facts(
	dr_no int64 NOT NULL,
	crm_cd int64 NOT NULL,
	premis_cd int64,
	weapon_cd int64,
	area_cd int64 NOT NULL,
	date_occ int64 NOT NULL,
	status_desc string NOT NULL,
	vict_age int64 NOT NULL,
	vict_sex string,
	vict_descent string


);

ALTER TABLE la_crime.la_crime_facts ADD PRIMARY KEY ( dr_no )  NOT ENFORCED;
