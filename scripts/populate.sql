\c rsdb

INSERT INTO users (username, password) 
VALUES ('john_doe', 'password123');

INSERT INTO users (username, password) 
VALUES ('jane_smith', 'pass456');

INSERT INTO users (username, password) 
VALUES ('peter_parker', 'secret789');

INSERT INTO users (username, password) 
VALUES ('bruce_wayne', 'batman123');

INSERT INTO users (username, password) 
VALUES ('clark_kent', 'superman456');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (2, 'Cozy Apartment', 1500.0, 'A very cozy place to stay.', 'https://placehold.co/600x400/000000/FFFFFF.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Modern Loft', 2000.5, 'Spacious loft with modern amenities.', 'https://placehold.co/600x400/000000/FFFFFF.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (4, 'Spacious Condo', 1800.75, 'Perfect for family vacations.', 'https://placehold.co/600x400/000000/FFFFFF.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Beach House', 2200.0, 'A serene place near the beach.', 'https://placehold.co/600x400/000000/FFFFFF.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (3, 'Mountain Cabin', 1600.0, 'Perfect for a winter getaway.', 'https://placehold.co/600x400/000000/FFFFFF.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (5, 'City Studio', 1450.5, 'Small but very well located.', 'simpsons_house.png');

INSERT INTO bookings (property_id, user_id, start_date, end_date) 
VALUES (1, 1, '2024-10-10', '2024-10-12');

INSERT INTO bookings (property_id, user_id, start_date, end_date) 
VALUES (2, 2, '2024-10-15', '2024-10-18');

INSERT INTO bookings (property_id, user_id, start_date, end_date) 
VALUES (3, 3, '2024-10-20', '2024-10-22');

INSERT INTO bookings (property_id, user_id, start_date, end_date) 
VALUES (4, 4, '2024-10-25', '2024-10-28');

INSERT INTO bookings (property_id, user_id, start_date, end_date) 
VALUES (5, 5, '2024-10-30', '2024-11-01');