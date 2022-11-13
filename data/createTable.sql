create table publicacion (
   ID serial,
   text varchar(10485760),
	date TIMESTAMP,
	person varchar(100),
	classification varchar(50) CHECK(classification in ('suicide', 'non-suicide')),
	PRIMARY KEY (ID)
 );
 