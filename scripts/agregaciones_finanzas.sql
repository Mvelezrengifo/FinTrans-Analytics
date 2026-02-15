-- agregaciones_finanzas.sql
-- Este script contendría consultas SQL para agregar métricas por mes/producto/cuenta.
-- Actualmente todo está en notebooks.
-- FinTrans-Analytics
-- Business Metrics Layer

-- Monthly Revenue Aggregation
SELECT 
    Year,
    Month,
    COUNT(TransactionID) AS Total_Transactions,
    SUM(TransactionAmount_Positive) AS Total_Revenue,
    SUM(IsCredit) AS Total_Credits,
    SUM(IsDebit) AS Total_Debits
FROM FactTransaction
GROUP BY Year, Month
ORDER BY Year, Month;


-- Top 5 Products by Revenue
SELECT 
    ProductID,
    SUM(TransactionAmount_Positive) AS Total_Revenue
FROM FactTransaction
GROUP BY ProductID
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Top 5 Accounts by Transaction Volume
SELECT 
    AccountID,
    COUNT(TransactionID) AS Transaction_Count,
    SUM(TransactionAmount_Positive) AS Total_Revenue
FROM FactTransaction
GROUP BY AccountID
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Revenue Distribution by Channel
SELECT 
    TransactionChannel,
    SUM(TransactionAmount_Positive) AS Total_Revenue
FROM FactTransaction
GROUP BY TransactionChannel
ORDER BY Total_Revenue DESC;
