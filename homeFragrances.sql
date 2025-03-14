-------------------------------------------
-- 1. Jo Malone London Pomegranate Noir Home Candle
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Jo Malone London', 'Pomegranate Noir Home Candle', 'Fruity – A luxurious candle combining rich fruits, white flowers, and spicy musks to create a dark and enigmatic scent.', 56, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scented Candles', FALSE);

-------------------------------------------
-- 2. Jo Malone London Pomegranate Noir Scent Surround Diffuser
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Jo Malone London', 'Pomegranate Noir Scent Surround Diffuser', 'Fruity – A sophisticated diffuser releasing the dark and enigmatic scent of Pomegranate Noir, blending rich fruits, white flowers, and spicy musks.', 65, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scent Diffuser', FALSE);

-------------------------------------------
-- 3. O L I V Wild Mint & Camellia Reed Diffuser
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('O L I V', 'Wild Mint & Camellia Reed Diffuser', 'Fresh – A flameless diffuser offering a refreshing scent of wild mint and camellia.', 20, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Reed Diffusers', FALSE);

-------------------------------------------
-- 4. O L I V Egyptian Amber Reed Diffuser
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('O L I V', 'Egyptian Amber Reed Diffuser', 'Oriental – A reed diffuser emitting the warm and exotic scent of Egyptian amber, adding a touch of luxury.', 20, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Reed Diffusers', FALSE);

-------------------------------------------
-- 5. Nomad Noé Visionary in Esfahan Scented Candle
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Nomad Noé', 'Visionary in Esfahan Scented Candle', 'Floral – A candle inspired by Esfahan, blending saffron and rose to create a captivating aroma.', 75, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scented Candles', FALSE);

-------------------------------------------
-- 6. Nomad Noé Hero in Niani Scented Candle
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Nomad Noé', 'Hero in Niani Scented Candle', 'Woody – A candle inspired by the ancient city of Niani, combining amber and patchouli for a rich, earthy scent.', 75, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scented Candles', FALSE);

-------------------------------------------
-- 7. Amelia-Rae Vanilla Lime Wax Melts
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Amelia-Rae', 'Vanilla Lime Wax Melts', 'Gourmand – Wax melts offering a sweet and zesty blend of vanilla and lime, perfect for freshening up any room.', 5, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Air Freshener', FALSE);

-------------------------------------------
-- 8. Amelia-Rae Spring Awakening Wax Melts
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Amelia-Rae', 'Spring Awakening Wax Melts', 'Fresh – Wax melts with a fresh, clean scent reminiscent of spring mornings, bringing a sense of renewal.', 5, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Air Freshener', FALSE);

-------------------------------------------
-- 9. Moncrief Sea Salt Hand Poured Scented Candle
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Moncrief', 'Sea Salt Hand Poured Scented Candle', 'Fresh – A hand-poured scented candle with a refreshing aroma of sea salt and subtle citrus.', 40, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scented Candles', FALSE);

-------------------------------------------
-- 10. Moncrief Ocean Breeze Room Spray
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Moncrief', 'Ocean Breeze Room Spray', 'Fresh – A room spray that delivers a crisp, oceanic scent with hints of sea salt and citrus.', 30, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Room Sprays', FALSE);

-------------------------------------------
-- 11. Jo Malone London Home Fragrance Bundle (Bundle Extra)
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Jo Malone London', 'Home Fragrance Bundle', 'A curated bundle featuring a scented candle and a scent diffuser for an immersive home experience.', 100, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Scented Candles', TRUE);

-------------------------------------------
-- 12. Nomad Noé Luxury Home Fragrance Bundle (Bundle Extra)
INSERT INTO PRODUCTS (brand, product_name, description, price, gift)
VALUES ('Nomad Noé', 'Luxury Home Fragrance Bundle', 'A luxurious bundle featuring a scented candle and a reed diffuser, offering an opulent fragrance experience.', 120, FALSE);
INSERT INTO HOME_FRAGRANCES (product_id, product_type, bundle)
VALUES (LAST_INSERT_ID(), 'Reed Diffusers', TRUE);