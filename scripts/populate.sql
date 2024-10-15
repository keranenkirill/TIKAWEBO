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
VALUES (1, 'The Simpsons Classic Springfield Home', 1450.5, 'Live in the iconic Springfield neighborhood with this cozy, family-friendly house. Known for its warm and familiar design, this home offers a comfortable living space perfect for families or individuals who love a classic vibe.', 'simpsons_house.png');

