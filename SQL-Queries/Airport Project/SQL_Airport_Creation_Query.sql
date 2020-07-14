SP_HELP Customers

CREATE TABLE [BookingDetails] (
  [TicketID] Int IDENTITY NOT NULL,
  [FlightID] Int NOT NULL,
  [CustomerID] Int NOT NULL,
  [FirstName] VarChar(200) NOT NULL,
  [LastName] VarChar(200) NOT NULL,
  [PassportNum] VarChar(100) NOT NULL,
  [DateOfBirth] Date NOT NULL,
  PRIMARY KEY ([TicketID]),
  FOREIGN KEY ([FlightID]) REFERENCES Flights(FlightID),
  FOREIGN KEY ([CustomerID]) REFERENCES Customers(CustomerID)
);

CREATE TABLE [Staff] (
  [StaffID] Int IDENTITY NOT NULL,
  [FlightID] Int NOT NULL,
  [Name] VarChar(200) NOT NULL,
  [Position] VarChar(100) NOT NULL,
  [Username] VarChar(100) NOT NULL,
  [Password] VarChar(100) NOT NULL,
  PRIMARY KEY ([StaffID]),
  FOREIGN KEY ([FlightID]) REFERENCES Flights(FlightID)
);

CREATE TABLE [Customers] (
  [CustomerID] Int IDENTITY NOT NULL,
  [FirstName] VarChar(200) NOT NULL,
  [LastName] VarChar(200) NOT NULL,
  [DateOfBirth] Date NOT NULL,
  PRIMARY KEY ([CustomerID])
);

CREATE TABLE [Flights] (
  [FlightID] Int,
  [Destination] VarChar(200),
  [DepartureDate] Date,
  [DepartureTime] DateTime,
  [FlightTime] VarChar(200),
  [PassengerLimit] Int,
  PRIMARY KEY ([FlightID])
);

CREATE TABLE [FlightStaff] (
  [FlightID] Int NOT NULL,
  [StaffID] Int NOT NULL,
  PRIMARY KEY ([FlightID], [StaffID]),
  FOREIGN KEY (FlightID) REFERENCES Flights (FlightID),
  FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
);


SELECT * FROM FlightStaff
SELECT * FROM Customers
SELECT * FROM Flights
SELECT * FROM Staff
SELECT * FROM BookingDetails