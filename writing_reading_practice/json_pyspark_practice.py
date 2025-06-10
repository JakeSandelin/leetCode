from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, expr, sum as spark_sum

# Initialize Spark session
spark = SparkSession.builder.appName("AggregateNestedJSON").getOrCreate()

# Sample JSON string (in practice, you’d read this from a file or data source)
json_data = """
[
  {
    "customer_id": "C001",
    "customer_name": "Alice",
    "orders": [
      {"product_id": "P100", "product_name": "Widget", "quantity": 2, "price": 10.0},
      {"product_id": "P101", "product_name": "Gadget", "quantity": 1, "price": 15.5}
    ]
  },
  {
    "customer_id": "C002",
    "customer_name": "Bob",
    "orders": [
      {"product_id": "P100", "product_name": "Widget", "quantity": 1, "price": 10.0},
      {"product_id": "P102", "product_name": "Thingamajig", "quantity": 3, "price": 7.0}
    ]
  }
]
"""

# Create DataFrame from JSON string (for demo purpose)
rdd = spark.sparkContext.parallelize([json_data])
df = spark.read.json(rdd)

# Explode the nested 'orders' array to have one row per order item
df_exploded = df.select(
    "customer_id",
    "customer_name",
    explode("orders").alias("order")
)

# Calculate total spent per order item (quantity * price)
df_with_amount = df_exploded.withColumn(
    "amount_spent",
    col("order.quantity") * col("order.price")
)

# Aggregate total amount spent by customer
result_df = df_with_amount.groupBy("customer_id", "customer_name") \
                         .agg(spark_sum("amount_spent").alias("total_spent"))

# Show the results
result_df.show()

# Save to CSV if needed (uncomment below)
# result_df.coalesce(1).write.csv("output/customer_spending.csv", header=True)

spark.stop()
