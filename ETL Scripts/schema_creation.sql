CREATE SCHEMA la_crime;

CREATE TABLE la_crime.dim_area ( 
	area_cd int64 NOT NULL OPTIONS( description='area code, FK to facts table' )   ,
	area_desc string OPTIONS( description='description of area' )   
 );

ALTER TABLE la_crime.dim_area ADD PRIMARY KEY ( area_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_crime ( 
	crime_cd int64 NOT NULL  ,
	crime_desc string OPTIONS( description='description of crime' )   
 );

ALTER TABLE la_crime.dim_crime ADD PRIMARY KEY ( crime_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_date ( 
	date_occ int64 NOT NULL OPTIONS( description='date occured, FK to facts table' )   ,
	date_rptd int64 OPTIONS( description='date reported' )   ,
	year int64 OPTIONS( description='the year the crime occured' )   ,
	month int64 OPTIONS( description='integer month the crime happened' )   ,
	month_name string OPTIONS( description='name of the month' )   ,
	day int64 OPTIONS( description='integer day of the month' )   ,
	day_of_week string OPTIONS( description='day the crime happened' )   ,
	time_occ string OPTIONS( description='time the crime happened' )   ,
	hour int64 OPTIONS( description='hour the crime happened' )   ,
	minute int64 OPTIONS( description='the minute the crime happened' )   ,
	calendar_year_quarter int64 OPTIONS( description='integer quarter the crime happened' )   
 );

ALTER TABLE la_crime.dim_date ADD PRIMARY KEY ( date_occ )  NOT ENFORCED;

CREATE TABLE la_crime.dim_premis ( 
	premis_cd numeric NOT NULL OPTIONS( description='premise code, FK to facts table' )   ,
	premis_desc string  
 );

ALTER TABLE la_crime.dim_premis ADD PRIMARY KEY ( premis_cd )  NOT ENFORCED;

CREATE TABLE la_crime.dim_weapon ( 
	weapon_cd numeric NOT NULL OPTIONS( description='weapon code, FK to facts table' )   ,
	weapon_desc string OPTIONS( description='description of weapon' )   
 );

ALTER TABLE la_crime.dim_weapon ADD PRIMARY KEY ( weapon_cd )  NOT ENFORCED;

CREATE TABLE la_crime.crime_facts ( 
	dr_no int64 OPTIONS( description='primary key for facts table' )   ,
	crime_cd int64 OPTIONS( description='crime code, FK for dim crime' )   ,
	premis_cd numeric OPTIONS( description='premise code, FK for dim_premis' )   ,
	weapon_cd numeric OPTIONS( description='weapon code, FK for dim_weapon' )   ,
	area_cd int64 OPTIONS( description='area code, FK for dim_area' )   ,
	date_occ int64 OPTIONS( description='date occured of the crime, FK for dim_date table' )   ,
	status_desc string  ,
	vict_age int64 OPTIONS( description='age of victim' )   ,
	vict_sex string OPTIONS( description='sex of victim' )   ,
	vict_descent string OPTIONS( description='Descent of victim' )   
 );

ALTER TABLE la_crime.crime_facts ADD CONSTRAINT weapon_cd FOREIGN KEY ( weapon_cd ) REFERENCES la_crime.dim_weapon( weapon_cd ) NOT ENFORCED;

ALTER TABLE la_crime.crime_facts ADD CONSTRAINT area_cd FOREIGN KEY ( area_cd ) REFERENCES la_crime.dim_area( area_cd ) NOT ENFORCED;

ALTER TABLE la_crime.crime_facts ADD CONSTRAINT crime_cd FOREIGN KEY ( crime_cd ) REFERENCES la_crime.dim_crime( crime_cd ) NOT ENFORCED;

ALTER TABLE la_crime.crime_facts ADD CONSTRAINT premis_cd FOREIGN KEY ( premis_cd ) REFERENCES la_crime.dim_premis( premis_cd ) NOT ENFORCED;

ALTER TABLE la_crime.crime_facts ADD CONSTRAINT date_occ FOREIGN KEY ( date_occ ) REFERENCES la_crime.dim_date( date_occ ) NOT ENFORCED;

