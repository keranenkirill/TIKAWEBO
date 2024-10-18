CREATE TABLE if not exists users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL 
);

CREATE TABLE if not exists user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    email VARCHAR(255) DEFAULT 'email:NONE',
    phone VARCHAR(20) DEFAULT 'phone:NONE',
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE if not exists properties (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER NOT NULL REFERENCES users(id), 
    title TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,  
    description TEXT NOT NULL,      
    image_url TEXT NOT NULL,        
    CHECK (image_url ~* '\.(png|jpg|jpeg)$')  
);

CREATE TABLE if not exists bookings (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    UNIQUE(property_id, start_date, end_date)  
);

CREATE TABLE if not exists reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    property_id INTEGER NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    review TEXT NOT NULL,
    CONSTRAINT fk_user_review FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_property_review FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_user_id ON users (id);
CREATE INDEX idx_properties_user_id ON properties(user_id);
CREATE INDEX idx_bookings_property_id ON bookings(property_id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_profile_user ON user_profiles (user_id);
CREATE INDEX idx_reviews_user_id ON reviews(user_id);  
CREATE INDEX idx_reviews_property_id ON reviews(property_id);  
