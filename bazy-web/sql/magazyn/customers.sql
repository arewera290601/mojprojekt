DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS subscriptions;

CREATE TABLE customers(
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_name TEXT,
	address TEXT
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
    subscription_id INTEGER,
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id)
);

CREATE TABLE subscriptions(
		subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
		description TEXT,
		price_per_month INTEGER,
		subscription_length TEXT
);
