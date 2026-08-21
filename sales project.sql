-- CREATE TABLE customers AS
-- SELECT DISTINCT
--     Customer
-- FROM sales_import;
SELECT *
FROM customers
LIMIT 10;
-- ALTER TABLE customers
-- ADD COLUMN Customer_Segment VARCHAR(20);
-- -- UPDATE customers
-- SET Customer_Segment =
--     CASE
--         WHEN Customer IN (
--             SELECT Customer
--             FROM sales_import
--             GROUP BY Customer
--             HAVING SUM(Sales) >= 800000
--         )
--         THEN 'Premium'
--         ELSE 'Regular'
--     END;
SELECT Customer, Customer_Segment
FROM customers
LIMIT 10;
SET SQL_SAFE_UPDATES = 0;

UPDATE customers
SET Customer_Segment =
    CASE
        WHEN Customer IN (
            SELECT Customer
            FROM sales_import
            GROUP BY Customer
            HAVING SUM(Sales) >= 800000
        )
        THEN 'Premium'
        ELSE 'Regular'
    END;

SET SQL_SAFE_UPDATES = 1;
SELECT Customer, Customer_Segment
FROM customers
LIMIT 10;
SELECT
    s.Order_ID,
    s.Customer,
    c.Customer_Segment,
    s.Product,
    s.Sales,
    s.Profit
FROM sales_import s
JOIN customers c
    ON s.Customer = c.Customer
LIMIT 20;
SELECT
    c.Customer_Segment,
    COUNT(DISTINCT s.Customer) AS Number_of_Customers,
    SUM(s.Sales) AS Total_Sales,
    SUM(s.Profit) AS Total_Profit
FROM sales_import s
JOIN customers c
    ON s.Customer = c.Customer
GROUP BY c.Customer_Segment
ORDER BY Total_Sales DESC;
SELECT
    Customer,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_import
GROUP BY Customer
ORDER BY Total_Sales DESC
LIMIT 1;
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_import
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;