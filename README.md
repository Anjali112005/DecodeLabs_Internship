# Data Cleaning & Preparation Project

## Project Overview
This project focuses on cleaning and preparing a raw e-commerce dataset for analysis. The objective was to identify and handle missing values, check for duplicate records, validate data integrity, and produce a clean dataset ready for business intelligence and analytics.

## Objectives
- Identify and handle missing values
- Remove duplicate records
- Correct and validate data formats
- Ensure data consistency and integrity
- Generate a cleaned dataset for further analysis

## Dataset Information
The dataset contains 1,200 e-commerce order records with 14 columns, including:

- OrderID
- Date
- CustomerID
- Product
- Quantity
- UnitPrice
- ShippingAddress
- PaymentMethod
- OrderStatus
- TrackingNumber
- ItemsInCart
- CouponCode
- ReferralSource
- TotalPrice

## Data Cleaning Process

### 1. Missing Value Handling
- Identified missing values using Pandas.
- Found 309 missing values in the `CouponCode` column.
- Replaced missing coupon values with `"No Coupon"`.

### 2. Duplicate Check
- Checked for duplicate rows.
- Checked for duplicate Order IDs.
- Checked for duplicate Tracking Numbers.
- No duplicate records were found.

### 3. Data Validation
Validated:
- Quantity > 0
- UnitPrice > 0
- TotalPrice > 0
- ItemsInCart > 0

No invalid records were found.

### 4. Data Consistency Verification
Verified the business rule:

```python
TotalPrice = Quantity * UnitPrice
```

Detected mismatches and corrected them to ensure complete consistency.

## Technologies Used
- Python
- Pandas
- Visual Studio Code
- Microsoft Excel

## Files Included

### Dataset.xlsx
Original raw dataset.

### cleaned_dataset.xlsx
Final cleaned dataset after preprocessing.

### cleaning.py
Python script used for data cleaning and validation.

## Results
- Missing values handled successfully
- No duplicate records found
- Data formats validated
- Pricing consistency verified
- Clean dataset generated for analytics

## Outcome
The dataset is now clean, consistent, and ready for:
- Exploratory Data Analysis (EDA)
- Dashboard Creation
- Business Intelligence Reporting
- Data Visualization

## Author
**Neelam Anjali**

Data Analytics Intern Project
