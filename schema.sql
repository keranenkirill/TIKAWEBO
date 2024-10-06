CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL 
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER NOT NULL REFERENCES users(id), 
    price NUMERIC(10, 2) NOT NULL,  
    description TEXT NOT NULL,      
    image_url TEXT NOT NULL,        
    CHECK (image_url ~* '\.(png|jpg|jpeg)$')  
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    UNIQUE(property_id, start_date, end_date)  
);


CREATE INDEX idx_properties_user_id ON properties(user_id);
CREATE INDEX idx_bookings_property_id ON bookings(property_id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);



