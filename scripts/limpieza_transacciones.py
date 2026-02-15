# limpieza_transacciones.py
# Este script contendría funciones de limpieza de datos de transacciones.
# Actualmente todo está en notebooks.
"""
FinTrans-Analytics
Data Cleaning & Transformation Layer
Author: Manuel Velez
"""

from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType, DateType


def clean_transactions(df):
    """
    Cleans and transforms raw transaction dataset.
    
    Parameters:
        df (DataFrame): Raw transaction DataFrame
        
    Returns:
        DataFrame: Cleaned and enriched DataFrame
    """

    # Ensure correct data types
    df = df.withColumn(
        "TransactionAmount",
        F.col("TransactionAmount").cast(DoubleType())
    )

    df = df.withColumn(
        "TransactionDate",
        F.to_date("TransactionDate")
    )

    # Normalize negative values
    df = df.withColumn(
        "TransactionAmount_Positive",
        F.abs(F.col("TransactionAmount"))
    )

    # Create transaction flags
    df = df.withColumn(
        "IsCredit",
        F.when(F.col("TransactionAmount") > 0, 1).otherwise(0)
    )

    df = df.withColumn(
        "IsDebit",
        F.when(F.col("TransactionAmount") < 0, 1).otherwise(0)
    )

    # Extract time attributes
    df = df.withColumn("Year", F.year("TransactionDate"))
    df = df.withColumn("Month", F.month("TransactionDate"))

    return df


def validate_dataset(df):
    """
    Basic validation checks.
    """

    total_records = df.count()
    null_counts = {
        col: df.filter(F.col(col).isNull()).count()
        for col in df.columns
    }

    return {
        "total_records": total_records,
        "null_counts": null_counts
    }
