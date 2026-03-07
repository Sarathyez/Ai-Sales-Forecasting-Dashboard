use NewDB;
/*sales per region*/
SELECT
region,
SUM(sales) AS revenue
FROM sales_data
GROUP BY region;

/*Monthly Sales*/
SELECT
MONTH(order_date) month,
SUM(sales)
FROM sales_data
GROUP BY month;

/*Category Revenue*/
SELECT
product_category,
SUM(sales)
FROM sales_data
GROUP BY product_category;

