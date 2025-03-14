-- Table 1: CUSTOMER
CREATE TABLE CUSTOMER (
    customer_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    email_address VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY(customer_id),
    CHECK (gender IN ('Male', 'Female'))
);

-- Table 2: PHONE_NUMBERS
CREATE TABLE PHONE_NUMBERS (
    customer_id INT NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY(phone_number),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id)
);

-- Table 3: ADDRESSES
CREATE TABLE ADDRESSES (
    address_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    house VARCHAR(100) NOT NULL,
    street_name VARCHAR(100) NOT NULL,
    town_city VARCHAR(50) NOT NULL,
    county VARCHAR(50) NOT NULL,
    postcode VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    PRIMARY KEY(address_id),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id),
    CHECK (country IN ('England', 'Scotland', 'Wales', 'Northern Ireland'))
);

-- Table 4: MEMBERSHIP
CREATE TABLE MEMBERSHIP (
    member_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    membership_type VARCHAR(50) NOT NULL,
    end_ren_date DATE,
    PRIMARY KEY(member_id),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY(membership_type) REFERENCES DISCOUNT_RATE(member_type)
);

-- Table 5: DISCOUNT_RATE
CREATE TABLE DISCOUNT_RATE (
    member_type VARCHAR(50) NOT NULL,
    discount_rate REAL NOT NULL,
    PRIMARY KEY(member_type)
    CHECK (member_type IN ('Standard', 'Premium', 'Student'))
);

-- Table 6: GIFT_CARDS
CREATE TABLE GIFT_CARDS (
    gift_card_num INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    amount REAL NOT NULL,
    issue_date DATE NOT NULL,
    exp_date DATE NOT NULL,
    redeemed_status BOOLEAN NOT NULL,
    PRIMARY KEY(gift_card_num),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id)
);

-- Table 7: BASKET
CREATE TABLE BASKET (
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY(customer_id, product_id),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY(product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 8: FAVOURITE
CREATE TABLE FAVOURITE (
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY(customer_id, product_id),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY(product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 9: PRODUCTS
CREATE TABLE PRODUCTS (
    product_id INT NOT NULL AUTO_INCREMENT,
    brand VARCHAR(50) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    gift BOOLEAN NOT NULL,
    PRIMARY KEY(product_id)
);

-- Table 10: PERSONAL_FRAGRANCES
CREATE TABLE PERSONAL_FRAGRANCES (
    product_id INT NOT NULL,
    size VARCHAR(20) NOT NULL,
    fragrance_family VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    strength VARCHAR(20) NOT NULL,
    engraving VARCHAR(100) NOT NULL,
    PRIMARY KEY(product_id, size),
    FOREIGN KEY(product_id) REFERENCES PRODUCTS(product_id),
    CHECK (fragrance_family IN ('Floral', 'Oriental', 'Woody', 'Fresh', 'Citrus', 'Chypre')),
    CHECK (strength IN ('Eau de Parfum', 'Eau de Toilette', 'Parfum'))
);

-- Table 11: HOME_FRAGRANCES
CREATE TABLE HOME_FRAGRANCES (
    product_id INT NOT NULL,
    product_type VARCHAR(50) NOT NULL,
    bundle BOOLEAN NOT NULL,
    PRIMARY KEY(product_id),
    FOREIGN KEY(product_id) REFERENCES PRODUCTS(product_id),
    CHECK (product_type IN ('Scent Diffuser', 'Air Freshener', 'Scented Candles', 'Room Sprays', 'Reed Diffusers'))
);

-- Table 12: STORE
CREATE TABLE STORE (
    store_id INT NOT NULL AUTO_INCREMENT,
    branch_number VARCHAR(20),
    address VARCHAR(255),
    PRIMARY KEY(store_id)
);

-- Table 13: INVENTORY
CREATE TABLE INVENTORY (
    inventory_id INT NOT NULL AUTO_INCREMENT,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    restocking_threshold INT NOT NULL,
    last_restocking_date DATE NOT NULL,
    PRIMARY KEY(inventory_id),
    FOREIGN KEY(store_id) REFERENCES STORE(store_id),
    FOREIGN KEY(product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 14: ORDERS
CREATE TABLE ORDERS (
    order_id INT NOT NULL AUTO_INCREMENT,
    gift_card_num INT,
    order_date DATETIME NOT NULL,
    order_status VARCHAR(50) NOT NULL,
    order_type VARCHAR(50) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    installment BOOLEAN NOT NULL,
    total_payment REAL NOT NULL,
    PRIMARY KEY(order_id),
    FOREIGN KEY(gift_card_num) REFERENCES GIFT_CARDS(gift_card_num),
    CHECK (order_type IN ('Delivery', 'Pickup')),
    CHECK (payment_method IN ('Cash', 'Card', 'Paypal'))
);

-- Table 15: ORDER ITEMS
CREATE TABLE ORDER_ITEMS (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES `ORDER`(order_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 16: INSTALMENTS
CREATE TABLE INSTALMENTS (
    order_id INT NOT NULL,
    instalment_number INT NOT NULL,
    instalment_amount DECIMAL(10,2) NOT NULL,
    pay_due DATE NULL,
    payment_status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    PRIMARY KEY (order_id, instalment_number),
    FOREIGN KEY (order_id) REFERENCES `ORDER`(order_id),
    CHECK (payment_status IN ('Pending', 'Paid', 'Late'))
);

-- Table 17: ORDER REF
CREATE TABLE ORDER_REF (
    product_id INT NOT NULL,
    product INT NOT NULL, -- Potentially needs clarification (column name "product" is ambiguous)
    PRIMARY KEY (product_id, product),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 18: PLACES
CREATE TABLE PLACES (
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_id INT NOT NULL,
    PRIMARY KEY (customer_id, product_id, order_id),
    FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id),
    FOREIGN KEY (order_id) REFERENCES `ORDER`(order_id)
);

-- Table 19: PRODUCT INVENTORY
CREATE TABLE PRODUCT_INVENTORY (
    inventory_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (inventory_id, product_id),
    FOREIGN KEY (inventory_id) REFERENCES INVENTORY(inventory_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
);

-- Table 20: PRODUCT IMAGES
CREATE TABLE PRODUCT_IMAGES (
    image_id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    image LONGBLOB NOT NULL,
    PRIMARY KEY (image_id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
);