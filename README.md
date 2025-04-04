# Fragrance Database
The purpose is to design, create and populate a Database that manages online orders and Inventory of a fictional store called the Fragrance Shop.

## ER Diagram
![image](https://github.com/user-attachments/assets/8387a279-d785-477a-96ea-a3e8cf160a2b)

## Relational Model
![image](https://github.com/user-attachments/assets/e7c80278-14ee-451d-9351-ac6fdcc78bc3)

## Data Dictionary

## CUSTOMER

| **Key** | **Name**         | **Data Type**  | **Data Format** | **Constraints**              | **Description**                                     |
|---------|------------------|----------------|-----------------|------------------------------|-----------------------------------------------------|
| PK      | customer_id      | INT            |                 | NOT NULL, AUTO_INCREMENT     | Used to uniquely identify a customer.              |
|         | first_name       | VARCHAR(50)    |                 | NOT NULL                     | Customer’s first name.                             |
|         | middle_name      | VARCHAR(50)    |                 | NULLABLE                     | Customer’s middle name(s) if the customer chooses. |
|         | last_name        | VARCHAR(50)    |                 | NOT NULL                     | Customer’s last name.                              |
|         | DOB              | DATE           | YYYY-MM-DD      | NULLABLE                     | Customer's Date of Birth.                          |
|         | gender           | VARCHAR(6)     |                 | NOT NULL                     | Customer's gender (e.g., 'Male' or 'Female').      |
|         | email_address    | VARCHAR(100)   |                 | NOT NULL, UNIQUE             | Customer’s email address (must be unique).         |
|         | password         | VARCHAR(255)   |                 | NOT NULL                     | Customer's password (hashed for security).         |

---

## PHONE NUMBERS

| **Key** | **Name**       | **Data Type** | **Data Format** | **Constraints**          | **Description**                                 |
|---------|----------------|--------------|-----------------|--------------------------|-------------------------------------------------|
| FK      | customer_id    | INT          |                 | NOT NULL                 | Associates the phone number with a customer.   |
| PK      | phone_number   | VARCHAR(15)  |                 | NOT NULL                 | Customer’s phone number.                        |

---

## ADDRESSES

| **Key** | **Name**       | **Data Type** | **Data Format** | **Constraints**              | **Description**                                                 |
|---------|----------------|--------------|-----------------|------------------------------|-----------------------------------------------------------------|
| PK      | address_id     | INT          |                 | NOT NULL, AUTO_INCREMENT     | Uniquely identifies address records.                            |
| FK      | customer_id    | INT          |                 | FOREIGN KEY, NOT NULL        | Associates the customer with the corresponding address.         |
|         | house          | VARCHAR(50)  |                 | NOT NULL                     | House address.                                                  |
|         | street_name    | VARCHAR(50)  |                 | NOT NULL                     | Street name the house address resides in.                       |
|         | town_city      | VARCHAR(50)  |                 | NOT NULL                     | City or town.                                                   |
|         | county         | VARCHAR(50)  |                 | NOT NULL                     | County of the city or town.                                     |
|         | postcode       | VARCHAR(8)   |                 | NOT NULL                     | Postal Code.                                                    |
|         | country        | VARCHAR(50)  |                 | NOT NULL                     | Country of the address.                                         |

---

## MEMBERSHIP

| **Key** | **Name**        | **Data Type**  | **Data Format** | **Constraints**              | **Description**                                      |
|---------|-----------------|----------------|-----------------|------------------------------|------------------------------------------------------|
| PK      | member_id       | INT            |                 | NOT NULL, AUTO_INCREMENT     | Uniquely identifies membership.                      |
| FK      | customer_id     | INT            |                 | NOT NULL                     | Associates the membership with the customer.         |
|         | member_type     | VARCHAR(50)    |                 | NOT NULL                     | The type of membership the customer holds.           |
|         | end_ren_date    | DATE           | YYYY-MM-DD      | NOT NULL                     | Date the membership ends or is due for renewal.      |
|         | discount_rate   | REAL           |                 | NOT NULL                     | Discount rate for this membership type.             |

---

## DISCOUNT RATE

| **Key** | **Name**       | **Data Type** | **Data Format** | **Constraints** | **Description**                               |
|---------|---------------|---------------|-----------------|-----------------|-----------------------------------------------|
| PK      | member_type   | VARCHAR(50)   |                 | NOT NULL        | Type of membership (links to `MEMBERSHIP`).   |
|         | discount_rate | REAL          |                 | NOT NULL        | Discount rate derived from the membership.    |

---

## GIFT CARDS

| **Key** | **Name**        | **Data Type**   | **Data Format** | **Constraints**          | **Description**                                              |
|---------|-----------------|-----------------|-----------------|--------------------------|--------------------------------------------------------------|
| PK      | gift_card_num   | INT             |                 | NOT NULL, AUTO_INCREMENT | A code that is to be redeemed with an order.                |
| FK      | customer_id     | INT             |                 | NOT NULL                 | Identifies the customer who bought the gift card.           |
|         | amount          | DECIMAL(10,2)   |                 | NOT NULL                 | Value stored on the gift card.                              |
|         | issue_date      | DATE            | YYYY-MM-DD      | NOT NULL                 | Issuance date for the gift card.                            |
|         | exp_date        | DATE            | YYYY-MM-DD      | NOT NULL                 | Expiry date for the gift card.                              |
|         | redeemed_status | BOOLEAN         |                 | NOT NULL                 | Indicates if the gift card has been redeemed.               |

---

## BASKET

| **Key** | **Name**      | **Data Type**   | **Data Format** | **Constraints**         | **Description**                                         |
|---------|--------------|-----------------|-----------------|-------------------------|---------------------------------------------------------|
| PK, FK  | customer_id  | INT             |                 | NOT NULL                | Identifies the customer who added the product.         |
| PK, FK  | product_id   | INT             |                 | NOT NULL                | Identifies the product added to the basket.            |
|         | quantity     | INT             |                 | NOT NULL, DEFAULT 1     | Quantity of a product in the basket.                   |
|         | total_amount | DECIMAL(10,2)   |                 | NOT NULL                | Total amount for the products in the basket.           |

---

## FAVOURITE

| **Key** | **Name**     | **Data Type** | **Data Format** | **Constraints** | **Description**                                      |
|---------|-------------|---------------|-----------------|-----------------|------------------------------------------------------|
| PK, FK  | customer_id | INT           |                 | NOT NULL        | Identifies the customer who favorited the product.  |
| PK, FK  | product_id  | INT           |                 | NOT NULL        | Identifies the product that was favorited.          |

---

## PRODUCTS

| **Key** | **Name**       | **Data Type**   | **Data Format** | **Constraints**           | **Description**                           |
|---------|---------------|-----------------|-----------------|---------------------------|-------------------------------------------|
| PK      | product_id    | INT             |                 | NOT NULL, AUTO_INCREMENT | Used to identify a product.              |
|         | brand         | TEXT            |                 | NOT NULL                 | Product’s brand.                         |
|         | product_name  | VARCHAR(75)     |                 | NOT NULL                 | Name of the product.                     |
|         | description   | TEXT            |                 | NULLABLE                 | Detailed description of the product.     |
|         | price         | DECIMAL(10,2)   |                 | NOT NULL                 | Price of each product.                   |
|         | gift          | BOOLEAN         |                 | NOT NULL, DEFAULT "NULL" | Gift option if available.                |

---

## PERSONAL_FRAGRANCES

| **Key** | **Name**           | **Data Type**  | **Data Format** | **Constraints** | **Description**                                              |
|---------|--------------------|----------------|-----------------|-----------------|--------------------------------------------------------------|
| PK, FK  | product_id         | INT            |                 | NOT NULL        | Identifies the personal fragrance product (FK to `PRODUCTS`). |
| PK      | size              | VARCHAR(50)    |                 | NOT NULL        | Size or volume (e.g., 50ml, 100ml).                          |
|         | fragrance_family  | VARCHAR(50)    |                 | NOT NULL        | Category of scent (e.g., floral, oriental).                 |
|         | gender            | VARCHAR(50)    |                 | NOT NULL        | Target gender for the fragrance.                            |
|         | strength          | VARCHAR(50)    |                 | NOT NULL        | Perfume concentration (e.g., Eau de Parfum).                |
|         | engraving         | VARCHAR(50)    |                 | NULLABLE        | Engraving option.                                           |

---

## HOME_FRAGRANCES

| **Key** | **Name**       | **Data Type** | **Data Format** | **Constraints** | **Description**                             |
|---------|---------------|---------------|-----------------|-----------------|---------------------------------------------|
| PK, FK  | product_id    | INT           |                 | NOT NULL        | Identifies the home fragrance (FK to `PRODUCTS`). |
|         | product_type  | VARCHAR(50)   |                 | NOT NULL        | Indicates the type of home fragrance.       |
|         | bundle        | BOOLEAN       |                 | NULLABLE        | Indicates if the product is a bundle.       |

---

## STORE

| **Key** | **Name**        | **Data Type**   | **Data Format** | **Constraints**              | **Description**                                |
|---------|-----------------|-----------------|-----------------|------------------------------|------------------------------------------------|
| PK      | store_id        | INT             |                 | NOT NULL, AUTO_INCREMENT     | Unique identifier for the store.               |
|         | branch_number   | VARCHAR(50)     |                 | NULLABLE                     | Identifies the branch within a specific area.  |
|         | address         | VARCHAR(255)    |                 | NULLABLE                     | Address details of the store.                  |

---

## INVENTORY

| **Key** | **Name**               | **Data Type** | **Data Format** | **Constraints**              | **Description**                                      |
|---------|------------------------|---------------|-----------------|------------------------------|------------------------------------------------------|
| PK      | inventory_id           | INT           |                 | NOT NULL, AUTO_INCREMENT     | Unique identifier for the inventory.                |
| FK      | store_id              | INT           |                 | NOT NULL                     | Identifies which store this inventory belongs to.    |
| FK      | product_id            | INT           |                 | NOT NULL                     | Identifies the product in inventory.                 |
|         | quantity              | INT           |                 | NOT NULL, DEFAULT 0          | The current quantity of products stored.             |
|         | restocking_threshold  | INT           |                 | NOT NULL, DEFAULT 10         | Threshold used for restocking.                       |
|         | last_restocking_date  | DATE          | YYYY-MM-DD      | NULLABLE                     | Last restocking date for the product.                |

---

## ORDERS

| **Key** | **Name**        | **Data Type**   | **Data Format**      | **Constraints**              | **Description**                                   |
|---------|-----------------|-----------------|----------------------|------------------------------|---------------------------------------------------|
| PK      | order_id        | INT             |                      | NOT NULL, AUTO_INCREMENT     | Unique identifier for the order.                 |
| FK      | giftcard        | VARCHAR(50)     |                      | NULLABLE                     | Gift card reference if used in this order.       |
|         | order_date      | DATETIME        | YYYY-MM-DD HH:MM     | NOT NULL                     | Date and time of the order.                      |
|         | order_status    | VARCHAR(50)     |                      | NOT NULL                     | Status of the order (e.g., pending, shipped).    |
|         | order_type      | VARCHAR(50)     |                      | NOT NULL                     | Fulfillment option: delivery or pickup.          |
|         | payment_method  | VARCHAR(50)     |                      | NOT NULL                     | Method used to pay (e.g., credit card, PayPal).  |
|         | installment     | BOOLEAN         |                      | NULLABLE                     | Pay in full or installments?                     |
|         | total_payment   | DECIMAL(10,2)   |                      | NOT NULL                     | Total payment amount for the order.              |

---

## ORDER_ITEMS

| **Key** | **Name**     | **Data Type**   | **Data Format** | **Constraints**          | **Description**                                        |
|---------|-------------|-----------------|-----------------|--------------------------|--------------------------------------------------------|
| PK, FK  | order_id    | INT             |                 | NOT NULL                 | Identifies the order to which this item belongs.       |
| PK, FK  | product_id  | INT             |                 | NOT NULL                 | Identifies the product being ordered.                  |
|         | quantity    | INT             |                 | NOT NULL, DEFAULT 1      | Number of units of the product in this line item.      |
|         | price       | DECIMAL(10,2)   |                 | NOT NULL                 | Price of each product in this order line.             |

---

## INSTALMENTS

| **Key** | **Name**             | **Data Type**   | **Data Format** | **Constraints**              | **Description**                                             |
|---------|----------------------|-----------------|-----------------|------------------------------|-------------------------------------------------------------|
| PK, FK  | order_id            | INT             |                 | NOT NULL                     | Identifies the order with installments.                     |
| PK      | installment_number  | INT             |                 | NOT NULL                     | The installment number.                                     |
|         | installment_amount  | DECIMAL(10,2)   |                 | NOT NULL                     | The amount of the installment.                              |
|         | pay_due             | DATE            | YYYY-MM-DD      | NULLABLE                     | The date the installment was paid.                          |
|         | payment_status      | VARCHAR(50)     |                 | NOT NULL, DEFAULT 'Pending' | Status of the installment (e.g., 'Pending', 'Paid', 'Late').|

---

## ORDER_REF

> **Note:** This table’s purpose isn’t entirely clear from the original description.  
> It appears to link a product (`product_id`) to some reference (`product`?), but the naming is ambiguous.

| **Key** | **Name**     | **Data Type** | **Constraints** | **Description**                                          |
|---------|-------------|---------------|-----------------|----------------------------------------------------------|
| PK, FK  | product_id  | INT           | NOT NULL        | Identifies the product.                                 |
| PK      | product     | INT           | NOT NULL        | Identifies the order item associated with the product.  |

---

## PLACES

> **Note:** The role of this table needs clarification.

| **Key** | **Name**      | **Data Type** | **Constraints** | **Description**                                 |
|---------|--------------|---------------|-----------------|-------------------------------------------------|
| PK, FK  | customer_id  | INT           | NOT NULL        | Identifies the customer who ordered.           |
| PK, FK  | product_id   | INT           | NOT NULL        | Identifies the product being purchased.        |
| PK, FK  | order_id     | INT           | NOT NULL        | Identifies the order in which the product is placed. |

---

## PRODUCT_INVENTORY

> **Note:** This appears to be a junction table linking `inventory` and `product`.

| **Key** | **Name**       | **Data Type** | **Constraints** | **Description**                                |
|---------|---------------|---------------|-----------------|------------------------------------------------|
| PK, FK  | inventory_id  | INT           | NOT NULL        | Identifies the inventory entry.                |
| PK, FK  | product_id    | INT           | NOT NULL        | Identifies the product for the inventory.      |

---

## PRODUCT_IMAGES

| **Key** | **Name**       | **Data Type** | **Constraints**             | **Description**                                   |
|---------|---------------|---------------|-----------------------------|---------------------------------------------------|
| PK      | image_id      | INT           | NOT NULL, AUTO_INCREMENT    | Uniquely identifies the image of the product.     |
| FK      | product_id    | INT           | FOREIGN KEY, NOT NULL       | The product that is associated with the image.    |
|         | image         | LONGBLOB      | NOT NULL                    | The actual image (binary data) of the product.    |
"""

## Conceptual Schema

### CUSTOMER
| customer_id | first_name | middle_name | last_name | DOB | gender | email_address | password |
|-------------|-----------|-------------|-----------|-----|--------|--------------|----------|

### PHONENUMBERS (references CUSTOMER customer_id)
| customer_id | phone_number |
|-------------|-------------|

### ADDRESSES (references CUSTOMER customer_id)
| customer_id | address_id | house | street_name | town_city | county | postcode | country |
|-------------|-----------|-------|-------------|-----------|--------|---------|--------|

### MEMBERSHIP (references CUSTOMER customer_id)
| customer_id | member_id | member_type | end_ren_date | discount_rate |
|-------------|----------|------------|--------------|--------------|

### DISCOUNT_RATE (references MEMBERSHIP member_type)
| member_type | discount_rate |
|-------------|--------------|

### GIFTCARDS (references CUSTOMER customer_id)
| gift_card_num | customer_id | amount | issue_date | exp_date | redeemed_status |
|--------------|-------------|--------|------------|---------|----------------|

### BASKET (references CUSTOMER customer_id, references PRODUCTS product_id)
| customer_id | product_id | quantity | total_amount |
|-------------|-----------|----------|--------------|

### FAVOURITE (references CUSTOMER customer_id, references PRODUCTS product_id)
| customer_id | product_id |
|-------------|-----------|

### PRODUCTS
| product_id | brand | product_name | product_image | description | price | gift |
|------------|-------|-------------|--------------|------------|------|-----|

### PERSONAL_FRAGRANCES (references PRODUCTS product_id)
| product_id | size | fragrance_family | gender | strength | engraving |
|------------|------|-----------------|--------|---------|-----------|

### HOME_FRAGRANCES (references PRODUCTS product_id)
| product_id | bundle | product_type |
|------------|--------|-------------|

### STORE
| store_id | branch_number | address |
|----------|--------------|--------|

### INVENTORY (references STORE store_id)
| inventory_id | store_id | product_id | quantity | last_restocking_date | restocking_threshold |
|-------------|---------|-----------|----------|-------------------|----------------|

### ORDER
| order_id | giftcard | order_date | order_status | order_type | payment_method | installment | total_payment |
|----------|---------|------------|-------------|-----------|--------------|------------|-------------|

### ORDER ITEMS (references ORDER order_id, references PRODUCTS product_id)
| order_id | product_id | quantity | price |
|----------|-----------|----------|------|

### INSTALMENTS (references ORDER order_id)
| order_id | instalment_number | instalment_amount | pay_due | payment_status |
|----------|----------------|----------------|-------|--------------|

### ORDER REF (references PRODUCT customer_id, references ORDERITEMS product)
| product_id | product |
|------------|--------|

### PLACES
| customer_id | product_id | order_id |
|-------------|-----------|---------|

### PRODUCT INVENTORY (references INVENTORY inventory_id, references PRODUCTS product_id)
| inventory_id | product_id |
|-------------|-----------|

### PRODUCT IMAGES (references PRODUCTS product_id)
| image_id | product_id | image |
|----------|-----------|------|

