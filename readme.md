BookItKE
Deposit-based booking system
-It applies to dozens of businesses in Kenya

BookItKE - a simple booking + payment SaaS for Kenyan salons, barbershops, and small clinics. 

The concept
Small businesses still take bookings over WhatsApp and phone calls. The app enables them to have a simple link where customers can book time slots and pay a 20% deposit via M-Pesa STK Push. The owner gets a dashboard to manage appointments.
The deposit acts as a cancellation fee to protect the service provider's time.

INCLUDE PRODUCTS
If a user registers as a "Retail Store," the dashboard hides the "Calendar" and shows "Low Stock Alerts" instead.

For a product-only business (like a small kiosk or a clothing boutique), the “Service” and “Appointment” tables remains empty or hidden
e.g.
Chemists/Pharmacies (Product focus)
Mechanics (Hybrid: Spare parts + Labor)
Massage Parlors (Service focus)

The app solves the biggest headaches for the owners as follows:

It addresses friction points that local small businesses face every day.
-By combining Bookings, Inventory, and M-Pesa into one tool, a business moves from "surviving" to "organized."


1. Eliminating the "Loss of Time" (No-Show Protection)
In a service business like a salon, time is the only thing they have to sell. When a customer doesn't show up, that hour is gone forever.
The Problem: Customers book slots and vanish, leaving the chair empty and the stylist idle.
The Solution: The app forces a financial commitment via an M-Pesa deposit. Because the owner triggers the "No-Show" status manually, they have the power to keep that deposit. This turns a "lost hour" into "guaranteed partial revenue."

2. Inventory Security & Leakage Prevention/Stock Tracking
Many small businesses lose money because they don't know exactly how much stock they have.

The Problem: Staff might use or sell products without recording them, or the owner forgets to restock until they are completely out.
The Solution: By linking Sale_Items to Product stock, every sale automatically updates the inventory. The owner can see exactly how many bottles are left without being at the shop physically. This solves theft/forgetfulness. It creates accountability.

3. Financial Clarity (The M-Pesa Bridge)
Cash is hard to track. M-Pesa is easier, but matching an M-Pesa message to a specific customer or service is a manual nightmare.
The Problem: Messy Accounting .At the end of the day, the owner has to scroll through 50 M-Pesa messages to figure out who paid for what.
The Solution: The app records the mpesa_shortcode and links it directly to a Sale. This creates an automated "paper trail." When the owner looks at their Sales Reports, they aren't guessing, they are seeing verified data.

4. Enabling Passive Income via Online Sales
Salon owners usually only make money when they are physically working on a client.
The Problem: Revenue stops when the salon is closed or the chairs are full.
The Solution: By adding the Online Product Sale and Self-Managed Delivery options, the owner can sell hair products or accessories at any time of day. They can fulfill orders in their "downtime" between appointments, creating a second stream of income that doesn't depend on a chair being occupied.

5. Professionalism and Scalability
Small businesses often look "informal" because they use notebooks and manual records.
The Problem: It's hard to get a business loan or grow without professional records.
The Solution: The app provides a digital "Receipt" and a history of all transactions. If a bank asks for their turnover, the owner can export a report. It moves them from a "kiosk" mindset to a "professional enterprise" mindset.

6. Delivery
The Problem: Limited Reach
The Solution: Making the products reach more people anywhere in the country generating more sales

NB: Building this as a Universal System, it isn’t just helping one salon; it’s providing a "Business-in-a-Box" for any Kenyan entrepreneur with a phone and a product/service to sell.



DATABASE STRUCTURE
Entity-Relationship Diagram (ERD) with detailed relationships

Business to Service: A One-to-Many relationship. One business can offer multiple services (e.g., hair styling, manicure, massage).
Business to Appointment: A One-to-Many relationship. One business can have many appointments scheduled.
Service to Appointment: A One-to-Many relationship. One specific service type can be linked to many different appointments over time.
Business to Product: A One-to-Many relationship. One business can offer multiple products.
Business to Sale: A One-to-Many relationship. One business can carry out many sales.
Product to Sale_Item: A One-to-Many relationship. One product can have many sale items.
Service to Sale_Item: A One-to-Many relationship. One service many sale items.
Sale to Sale_Item: A One-to-Many relationship. One sale can have many sale items.
*Sale to Delivery: A One-to-One relationship. One sale one delivery. *(many sales can have one delivery though)


CREATE TABLE Business (
    id INT PRIMARY KEY SERIAL,
    name VARCHAR(255) NOT NULL,
    mpesa_shortcode VARCHAR(50),
    business_type ('service', 'retail', 'hybrid')
);

CREATE TABLE Product (
    id INT PRIMARY KEY SERIAL,
    business_id INT,
    name VARCHAR(255),
    price FLOAT,
    stock_quantity INT DEFAULT 0,
    FOREIGN KEY (business_id) REFERENCES Business(id)
);

CREATE TABLE Service (
    id INT PRIMARY KEY SERIAL,
    business_id INT,
    name VARCHAR(255),
    price FLOAT,
    duration_mins INT,
    FOREIGN KEY (business_id) REFERENCES Business(id)
);

CREATE TABLE Appointment (
    id INT PRIMARY KEY SERIAL,
    business_id INT,
    service_id INT,
    customer_name VARCHAR(255),
    status ENUM('Pending', 'Confirmed', 'Completed', 'No-Show') DEFAULT 'Pending',
    appointment_date DATE,
    FOREIGN KEY (business_id) REFERENCES Business(id),
    FOREIGN KEY (service_id) REFERENCES Service(id)
);

CREATE TABLE Sale (
    id INT PRIMARY KEY SERIAL,
    business_id INT,
    total_amount FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (business_id) REFERENCES Business(id)
);

CREATE TABLE Sale_Item (
    id INT PRIMARY KEY SERIAL,
    sale_id INT,
    product_id INT NULL,
    service_id INT NULL,
    quantity INT DEFAULT 1,
    unit_price FLOAT,
    FOREIGN KEY (sale_id) REFERENCES Sale(id),
    FOREIGN KEY (product_id) REFERENCES Product(id),
    FOREIGN KEY (service_id) REFERENCES Service(id)
);

CREATE TABLE Delivery (
    id INT PRIMARY KEY SERIAL,
    sale_id INT UNIQUE,
    delivery_address TEXT NOT NULL,
    customer_phone VARCHAR(20),
    shipping_fee FLOAT DEFAULT 0.00,
    delivery_status ENUM('Pending', 'In Transit', 'Delivered') DEFAULT 'Pending',
    FOREIGN KEY (sale_id) REFERENCES Sale(id)
);






