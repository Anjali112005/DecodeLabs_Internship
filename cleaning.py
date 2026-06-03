import pandas as pd

df = pd.read_excel("dataset.xlsx")

print(df.info())

#Phase 1: checking Missing Values
print(df.isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

#Phase 2: checking Duplicates
print("Duplicate Rows:",
      df.duplicated().sum())

print("Duplicate Order IDs:",
      df["OrderID"].duplicated().sum())

print("Duplicate Tracking Numbers:",
      df["TrackingNumber"].duplicated().sum())

#Phase 3: Data Validation & Business Rules
print("\nQuantity <= 0:")
print((df["Quantity"] <= 0).sum())

print("\nUnitPrice <= 0:")
print((df["UnitPrice"] <= 0).sum())

print("\nTotalPrice <= 0:")
print((df["TotalPrice"] <= 0).sum())

print("\nItemsInCart <= 0:")
print((df["ItemsInCart"] <= 0).sum())

#Phase 4: Verify TotalPrice Calculation
calculated_total = (df["Quantity"] * df["UnitPrice"]).round(2)

mismatch = (
    df["TotalPrice"].round(2) != calculated_total
).sum()

print("TotalPrice Mismatches:", mismatch)

#Phase 5: Standardize Text Columns
text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

#Phase 6: Handle CouponCode
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print(df.isnull().sum())

calculated_total = df["Quantity"] * df["UnitPrice"]

mismatch_rows = df[df["TotalPrice"] != calculated_total]

print(mismatch_rows[
    ["OrderID",
     "Quantity",
     "UnitPrice",
     "TotalPrice"]
].head(20))

#Phase 7:Save Clean Dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

print("\nDataset cleaned successfully!")