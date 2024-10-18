\c rsdb

INSERT INTO users (username, password) 
VALUES ('admin', 'admin123');

INSERT INTO user_profiles (user_id, email, phone) 
VALUES (1, 'admin.admin@mail.mail', '1234567890');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Toms Classic Suburban Home', 2000.5, 'Enjoy a peaceful, suburban lifestyle in this cozy home from the world of Tom and Jerry. With its spacious interiors and traditional charm, this home is perfect for those who appreciate classic comfort and quiet surroundings.', 'tom_jerry_house.png');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Planktons Secretive Chum Bucket Hideout', 1800.75, 'Dive into an undersea adventure with this unique, compact home located inside the infamous Chum Bucket! Ideal for someone who values privacy and a quirky lifestyle, this small, industrial-style home is perfect for minimalist living.', 'Plankton_House.jpg');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Undersea Living at its Best', 2200.0, 'Experience a unique and whimsical living space at Patricks rent-listed house! This cozy, stone-built undersea residence is located in Bikini Bottom, close to major attractions like Jellyfish Fields and the Krusty Krab. Ideal for the laid-back individual, this charming rock-shaped home comes fully furnished with a sand bed and a spacious living area perfect for hosting starfish-style parties. Whether you love napping all day or stargazing (underwater style), Patricks house offers the perfect retreat for a relaxed, aquatic lifestyle.', 'Patrick_house.jpg');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'Mickys partyhouse', 1600.0, 'Enjoy Disney magic in this charming, cartoon-style house in Toontown! With its playful design and Mickey-inspired décor, this cozy home is perfect for anyone seeking a fun and whimsical living experience. Ideal for small families or Disney fans!', 'Mickeys_Country_House.jpg');

INSERT INTO properties (user_id, title, price, description, image_url) 
VALUES (1, 'The Simpsons House', 1800.0, 'Step into the world of Springfield with this classic, cozy home from the Simpsons universe! Bright and welcoming, this house is ideal for families looking for a fun and vibrant space to call home. Complete with a spacious backyard and plenty of room for all kinds of shenanigans, this home is ready for your next adventure!', 'simpsons_house.png');

-- Adding new users
INSERT INTO users (username, password) VALUES 
('user1', 'user123'), 
('user2', 'user123'), 
('user3', 'user123'), 
('user4', 'user123'), 
('user5', 'user123');

-- Adding user profiles
INSERT INTO user_profiles (user_id, email, phone) VALUES 
(2, 'user1@example.com', '1234567891'), 
(3, 'user2@example.com', '1234567892'), 
(4, 'user3@example.com', '1234567893'), 
(5, 'user4@example.com', '1234567894'), 
(6, 'user5@example.com', '1234567895');

-- Adding bookings for the existing properties from the admin user
INSERT INTO bookings (property_id, user_id, start_date, end_date) VALUES 
(1, 2, '2024-10-10', '2024-10-20'), 
(2, 2, '2024-10-15', '2024-10-25'), 
(3, 3, '2024-11-01', '2024-11-10'), 
(4, 3, '2024-11-05', '2024-11-15'), 
(5, 4, '2024-12-01', '2024-12-10'), 
(1, 4, '2024-12-15', '2024-12-25'), 
(2, 5, '2024-12-05', '2024-12-15'), 
(3, 5, '2024-12-10', '2024-12-20');

-- Adding reviews for properties
INSERT INTO reviews (user_id, property_id, review) VALUES 
(2, 1, 'Amazing suburban home, very comfortable!'), 
(2, 2, 'Chum Bucket is quirky but fun!'), 
(3, 3, 'Patrick’s house was a unique experience!'), 
(3, 4, 'Toontown party house was magical!'), 
(4, 5, 'Classic Simpsons house, loved the experience!'), 
(4, 1, 'Second stay, still perfect!'), 
(5, 2, 'Chum Bucket hideout was unexpectedly cozy!'), 
(5, 3, 'Patrick’s place is fantastic for a quiet retreat!');
