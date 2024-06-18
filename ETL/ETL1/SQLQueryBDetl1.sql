

CREATE TABLE Casts (
	Cast_id INT IDENTITY(1,1) PRIMARY KEY ,
	Name_cast Varchar(50)
);

CREATE TABLE Type_show (
	Type_show_id INT IDENTITY(1,1) PRIMARY KEY,
	Type_show Varchar(50)NOT NULL
);

CREATE TABLE Caracteristics (
	Caracteristic_id INT IDENTITY(1,1) PRIMARY KEY,
	Listen_id Varchar(50),
	Description_caract Varchar(500)

);

CREATE TABLE Date_show_added (
	Date_show_added_id INT IDENTITY(1,1) PRIMARY KEY,
	Fecha DATE,
	Year_added INT,
	Month_added INT,
	Day_added INT
);

CREATE TABLE Date_show_release (
	Date_show_release_id INT IDENTITY(1,1) PRIMARY KEY,
	Year_release INT
);


CREATE TABLE Shows (
	Show_id VARCHAR(4) PRIMARY KEY,
	Title VARCHAR(70) NOT NULL,
	Country VARCHAR(50),
	Rating VARCHAR(5),
	Director VARCHAR(70),
	Cast_id INT,
	Type_show_id INT,
	Caracteristic_id INT,
	Date_show_added_id INT,
	Date_show_release_id INT,
	CONSTRAINT FK_Cast FOREIGN KEY (Cast_id) REFERENCES Casts(Cast_id),
	CONSTRAINT FK_Type_show FOREIGN KEY (Type_show_id) REFERENCES Type_show(Type_show_id),
	CONSTRAINT FK_Caracteristic FOREIGN KEY (Caracteristic_id) REFERENCES Caracteristics(Caracteristic_id),
	CONSTRAINT FK_Show_added FOREIGN KEY (Date_show_added_id) REFERENCES Date_show_added(Date_show_added_id),
	CONSTRAINT FK_Show_release FOREIGN KEY (Date_show_release_id) REFERENCES Date_show_release(Date_show_release_id)

);