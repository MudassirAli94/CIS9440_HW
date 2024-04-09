CREATE SCHEMA la_crime;

CREATE TABLE la_crime.dim_date_time ( 
	date_occ int64 NOT NULL  ,
	date_rptd_int64 string NOT NULL  ,
	time_occ string NOT NULL  ,
	hour int32 NOT NULL  ,
	minute int32 NOT NULL,
	day_of_week string NOT NULL
 );

ALTER TABLE la_crime.date_time ADD PRIMARY KEY ( date_occ )  NOT ENFORCED;

CREATE TABLE la_crime.dim_area ( 
	area_cd int32 NOT NULL  ,
	area_name string NOT NULL
 );

ALTER TABLE la_crime.dim_area ADD PRIMARY KEY ( area_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_crime ( 
	crm_cd int32 NOT NULL  ,
	crm_desc string NOT NULL
 );

ALTER TABLE la_crime.crime ADD PRIMARY KEY ( crm_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_premise ( 
	premise_cd int32 NOT NULL  ,
	premise_desc string NOT NULL
 );

ALTER TABLE la_crime.premise ADD PRIMARY KEY ( premise_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_weapon ( 
	weapon_cd int32 NOT NULL  ,
	weapon_desc string NOT NULL
 );

ALTER TABLE la_crime.weapon ADD PRIMARY KEY ( weapon_cd )  NOT ENFORCED;

CREATE TABLE la_crime.la_crime_facts(
	dr_no int64 NOT NULL,
	crm_cd int32 NOT NULL,
	premis_cd int32 NOT NULL,
	weapon_cd int32 NOT NULL,
	area_cd int32 NOT NULL,
	date_occ int64 NOT NULL,
	status_desc string NOT NULL,
	vict_age int32 NOT NULL,
	vict_sex string NOT NULL,
	vict_descent string NOT NULL


);

ALTER TABLE la_crime.la_crime_facts ADD PRIMARY KEY ( dr_no )  NOT ENFORCED;


ALTER TABLE la_crime.la_crime_facts
ADD FOREIGN KEY (date_occ) REFERENCES la_crime.dim_date_time(date_occ);

ALTER TABLE la_crime.la_crime_facts
ADD FOREIGN KEY (area_cd) REFERENCES la_crime.dim_area(area_cd);


ALTER TABLE la_crime.la_crime_facts
ADD FOREIGN KEY (crm_cd) REFERENCES la_crime.dim_crime(crm_cd);


ALTER TABLE la_crime.la_crime_facts
ADD FOREIGN KEY (premis_cd) REFERENCES la_crime.dim_premise(premise_cd);


ALTER TABLE la_crime.la_crime_facts
ADD FOREIGN KEY (weapon_cd) REFERENCES la_crime.dim_weapon(weapon_cd);
