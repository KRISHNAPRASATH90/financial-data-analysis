import mysql.connector
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
import schedule
import time


def fetch_data():
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MYsql@9090",
    database="project_2"
  )
  
  
  categories_df=pd.read_sql("select * from categories",conn)
  payment_methods_df=pd.read_sql("select * from  payment_methods",conn)
  merchants_df =pd.read_sql("select * from merchants",conn)
  monthly_budgets_df=pd.read_sql("select * from monthly_budgets",conn)
  transactions_df=pd.read_sql("select * from transactions",conn)
  conn.close()
  

  pd.set_option("display.max_columns", None)
  pd.set_option("display.width", None)  
  
  
  
#   ----------------------------------------------------CLEAN DATA--------------------------------------------------------------------------------
  
  
  
  
 # MISSING DATA CHECK
  
  print("Categories - Missing values")
  print(categories_df.isnull().sum())

  print("\nPayment Methods - Missing values")
  print(payment_methods_df.isnull().sum())

  print("\nMerchants - Missing values")
  print(merchants_df.isnull().sum())

  print("\nMonthly Budgets - Missing values")
  print(monthly_budgets_df.isnull().sum())

  print("\nTransactions - Missing values")
  print(transactions_df.isnull().sum())
  
  print("\nTransactions with missing amounts:")
  print(
      transactions_df.loc[
          transactions_df["amount"].isnull(),
          ["transaction_id", "transaction_ref", "amount", "description"]
      ]
  )
  
  print("\nTransactions with missing dates:")
  print(
      transactions_df.loc[
        transactions_df["transaction_date"].isnull(),
        ["transaction_id", "transaction_ref", "transaction_date", "description"]
      ]
  )
  
  print("\nTransactions with missing category ID:")
  print(
      transactions_df.loc[
        transactions_df["category_id"].isnull(),
        ["transaction_id", "transaction_ref", "category_id", "description"]
      ]
  )
  
  print("\nTransactions with missing merchant ID:")
  print(
      transactions_df.loc[
          transactions_df["merchant_id"].isnull(),
          ["transaction_id", "transaction_ref", "merchant_id", "description"]
      ]
  )

  print("\nTransactions with missing payment method ID:")
  print(
      transactions_df.loc[
          transactions_df["payment_method_id"].isnull(),
          ["transaction_id", "transaction_ref", "payment_method_id", "description"]
      ]
  )
  
  print("\nAvailable categories:")
  print(categories_df)

  print("\nAvailable merchants:")
  print(merchants_df)

  print("\nAvailable payment methods:")
  print(payment_methods_df)
  
  
  print("\nTransaction 101 details:")
  print(transactions_df.loc[transactions_df["transaction_id"] == 101])

  print("\nTransaction 63 details:")
  print(transactions_df.loc[transactions_df["transaction_id"] == 63])

  print("\nTransaction 90 details:")
  print(transactions_df.loc[transactions_df["transaction_id"] == 90])   
  
  
    #------------------------------------- Fill missing amounts with the median amount----------------------------------------------------
    
    
    
  median_amount = transactions_df["amount"].median()

  transactions_df["amount"] = transactions_df["amount"].fillna(
      median_amount
  )

  print("\nMissing amounts after cleaning:")
  print(transactions_df["amount"].isnull().sum())
  
      
   # -----------------------------------Fill missing transaction dates with the most frequent date------------------------------------------------
  
  
  
  random_date=transactions_df["transaction_date"].mode()[0]
  transactions_df["transaction_date"]=transactions_df["transaction_date"].fillna(random_date)
  
  print("\n Missing date after cleaning:")
  print(transactions_df["transaction_date"].isnull().sum())
  
  
    #--------------------------------------------- Find the most common category ID ------------------------------------------------------------
 
 
 
  random_cat_id=transactions_df["category_id"].mode()[0]
  transactions_df["category_id"]=transactions_df["category_id"].fillna(random_cat_id)
  
  print("\n Missing category id after celaning:")
  print(transactions_df["category_id"].isnull().sum())
  
    
  # -----------------------------------------------Fill missing merchant ID---------------------------------------------------------------------
  
  
  common_merchant = transactions_df["merchant_id"].mode()[0]

  transactions_df["merchant_id"] = (
      transactions_df["merchant_id"].fillna(common_merchant)
  )
  
  print("\nMissing merchant IDs after cleaning:")
  print(transactions_df["merchant_id"].isnull().sum())
  

  # ---------------------------------------Fill missing payment method ID-------------------------------------------------------------------
  

  common_payment = transactions_df["payment_method_id"].mode()[0]

  transactions_df["payment_method_id"] = (
      transactions_df["payment_method_id"].fillna(common_payment)
  )

  print("\nMissing payment method IDs after cleaning:")
  print(transactions_df["payment_method_id"].isnull().sum())
  

  
  # --------------------------------------------------DUPLICATES CHECK -----------------------------------------------------------------------
  
  
  print("\nCategories - Duplicate rows:")
  print(categories_df.duplicated().sum())

  print("\nPayment Methods - Duplicate rows:")
  print(payment_methods_df.duplicated().sum())

  print("\nMerchants - Duplicate rows:")
  print(merchants_df.duplicated().sum())

  print("\nMonthly Budgets - Duplicate rows:")
  print(monthly_budgets_df.duplicated().sum())

  print("\nTransactions - Duplicate rows:")
  print(transactions_df.duplicated().sum())
  
  print("\nTransaction statuses:")
  print(transactions_df["transaction_status"].value_counts())

  print("\nTransaction types:")
  print(transactions_df["transaction_type"].value_counts())

  print("\nCurrency codes:")
  print(transactions_df["currency_code"].value_counts())
  
  
  # -------------------------------------------------REPLACE INCONSISTENT VALUES ----------------------------------------------------------
  
  #status
  transactions_df["transaction_status"]=(transactions_df["transaction_status"].replace({"completed":"Completed","completeed":"Completed"}))
  print("\nTransaction statuses after cleaning:")
  print(transactions_df["transaction_status"].value_counts())
  
#currency
  transactions_df["currency_code"] = (transactions_df["currency_code"].replace({"IN":"INR"}))
  print("\nCurrency codes AFTER CLEANING:")
  print(transactions_df["currency_code"].value_counts())
  
  
  print("\nCategories data types:")
  print(categories_df.dtypes)

  print("\nPayment Methods data types:")
  print(payment_methods_df.dtypes)

  print("\nMerchants data types:")
  print(merchants_df.dtypes)

  print("\nMonthly Budgets data types:")
  print(monthly_budgets_df.dtypes)

  print("\nTransactions data types:")
  print(transactions_df.dtypes)
  
  
#---------------------------------------------------- TEXT DATE - DATE TIME FORMAT -----------------------------------------------------------------


  # Convert transaction dates to datetime
  transactions_df["transaction_date"] = pd.to_datetime(
      transactions_df["transaction_date"]
  )


  # Convert budget month to datetime
  monthly_budgets_df["budget_month"] = pd.to_datetime(
      monthly_budgets_df["budget_month"]
  )
  
  print("\nTransaction date type:")
  print(transactions_df["transaction_date"].dtype)

  print("\nBudget month type:")
  print(monthly_budgets_df["budget_month"].dtype)
  
  
  
  # ----------------------------------------------------Convert ID columns from float to integer--------------------------------------------------
  
  
  transactions_df["category_id"] = transactions_df["category_id"].astype(int)
  transactions_df["merchant_id"] = transactions_df["merchant_id"].astype(int)
  transactions_df["payment_method_id"] = transactions_df["payment_method_id"].astype(int)

  print("\nTransaction ID column types after cleaning:")
  print(transactions_df[[
      "category_id",
      "merchant_id",
      "payment_method_id"
  ]].dtypes)
  
    
  # ----------------------------------------------FINAL VERIFY MISSING VALUES------------------------------------------------------------------------
  
  
  print("\nFINAL Missing values after cleaning:")

  print("\nCategories:")
  print(categories_df.isnull().sum())

  print("\nPayment Methods:")
  print(payment_methods_df.isnull().sum())

  print("\nMerchants:")
  print(merchants_df.isnull().sum())

  print("\nMonthly Budgets:")
  print(monthly_budgets_df.isnull().sum())

  print("\nTransactions:")
  print(transactions_df.isnull().sum())
  
  
      
#------------------------------------------------- FINAL INVALID CHECK ------------------------------------------------------------------------------
  
  
  
  print("\nFINAL INVALID values after cleaning:")
    
  print("\nTransaction statuses:")
  print(transactions_df["transaction_status"].value_counts())

  print("\nCurrency codes:")
  print(transactions_df["currency_code"].value_counts())

  print("\nTransaction amounts:")
  print(transactions_df["amount"].describe())

  print("\nNegative or zero amounts:")
  print(transactions_df[transactions_df["amount"] <= 0])

  print("\nTransaction types:")
  print(transactions_df["transaction_type"].value_counts())
  
  
  
  # MAKING STATUS IN  LOWER CASE AND NO SPACE
  
  transactions_df["transaction_status"] = (
      transactions_df["transaction_status"]
      .str.strip()
      .str.lower()
  )

  print("\nTransaction statuses after cleaning:")
  print(transactions_df["transaction_status"].value_counts())
  
  
  # INVALID AMOUNTS
  
  print("\nTransactions with unusually high amounts:")
  print(transactions_df[transactions_df["amount"] > 50000])

  print("\nTransaction ID 74:")
  print(transactions_df[transactions_df["transaction_id"] == 74].to_string(index=False))
  
  

  
  # -----------------------------------------------------REPEATED TRANSACTION REFERENCE -------------------------------------------------------------------
  
  
  print("\nRepeated transaction references:")

  duplicate_refs = transactions_df[
      transactions_df["transaction_ref"].duplicated(keep=False)
  ].sort_values("transaction_ref")

  print(duplicate_refs.to_string(index=False))  
  
  
  print("\nNumber of repeated transaction references:")
  print(transactions_df["transaction_ref"].duplicated().sum())
  

# REMOVE DUPLICATE REFERENCES

  transactions_df = transactions_df.drop_duplicates(
      subset="transaction_ref",
      keep="first"
  )

  print("\nTransactions after removing duplicates:")
  print("Total rows:", len(transactions_df))

  print(
      "Repeated references remaining:",
      transactions_df["transaction_ref"].duplicated().sum()
  )
  
  
  
# ----------------------------------------------------------INVALID AMOUNTS ----------------------------------------------------------------------------------



# Check negative or zero transaction amounts
  print("\nNegative or zero transaction amounts:")

  print(
      transactions_df[transactions_df["amount"] <= 0]
      .to_string(index=False)
  )

  # Check unusually high transaction amounts
  print("\nTransactions above ₹50,000:")

  print(
      transactions_df[transactions_df["amount"] > 50000]
      .to_string(index=False)
  )
  
  
  print("\nTransactions with amounts above ₹10,000:")

  print(
      transactions_df[transactions_df["amount"] > 10000][
          ["transaction_id", "transaction_ref", "amount", "description"]
      ].to_string(index=False)
  )
  
  # Flag unusually high transaction amounts
  transactions_df["high_amount_flag"] = (
      transactions_df["amount"] > 10000
  )

  print("\nHigh amount flags:")
  print(
      transactions_df.loc[
          transactions_df["high_amount_flag"],
          ["transaction_id", "amount", "high_amount_flag"]
      ]
  )
  
  

  
  # -------------------------------------------CHECK INVALID ID-----------------------------------------------------------------------------------------------
  
  
  
  # Check category IDs
  print("\nInvalid category IDs:")
  print(
      transactions_df[
          ~transactions_df["category_id"].isin(categories_df["category_id"])
      ][["transaction_id", "category_id"]]
  )

  # Check merchant IDs
  print("\nInvalid merchant IDs:")
  print(
      transactions_df[
          ~transactions_df["merchant_id"].isin(merchants_df["merchant_id"])
      ][["transaction_id", "merchant_id"]]
  )

  # Check payment method IDs
  print("\nInvalid payment method IDs:")
  print(
      transactions_df[
          ~transactions_df["payment_method_id"].isin(
              payment_methods_df["payment_method_id"]
          )
      ][["transaction_id", "payment_method_id"]]
  )

  # Check budget IDs
  print("\nInvalid budget IDs:")
  print(
      transactions_df[
          ~transactions_df["budget_id"].isin(monthly_budgets_df["budget_id"])
      ][["transaction_id", "budget_id"]]
  )
  
  
  
  # ------------------------------------------FINAL ROW COUNT-------------------------------------------------------------------------------------
  
  
  print("\nFINAL ROW COUNTS AFTER CLEANING:")

  print("Categories:", len(categories_df))
  print("Payment Methods:", len(payment_methods_df))
  print("Merchants:", len(merchants_df))
  print("Monthly Budgets:", len(monthly_budgets_df))
  print("Transactions:", len(transactions_df))
  


 # ------------------------------------------- RETURN CLEANED DATAFRAMES ----------------------------------------------------------------------------
  
  return (
        categories_df,
        payment_methods_df,
        merchants_df,
        monthly_budgets_df,
        transactions_df
    )


# ------------------------------------------- CALL FUNCTION ----------------------------------------------------------------------------------------------


def create_dashboard():

    categories_df, payment_methods_df, merchants_df, monthly_budgets_df, transactions_df = fetch_data()

    print("\nDataFrames returned successfully:")
    print("Transactions:", len(transactions_df))
    print("Categories:", len(categories_df))

    # ---------------------------------------- COMBINE ALL TABLE ----------------------------------------

    # COMBINE TRANSACTIONS WITH CATEGORIES
    transactions_categories_df = pd.merge(
        transactions_df,
        categories_df,
        on="category_id",
        how="left"
    )

    print("\nTransactions combined with categories:")
    print(transactions_categories_df.head())
    print("\nCombined row count:", len(transactions_categories_df))

    # COMBINE WITH MERCHANTS
    transactions_categories_merchants_df = pd.merge(
        transactions_categories_df,
        merchants_df,
        on="merchant_id",
        how="left"
    )

    print("\nTransactions combined with categories and merchants:")
    print(
        transactions_categories_merchants_df[
            ["transaction_id", "amount", "category_name", "merchant_name"]
        ].head()
    )
    print("\nCombined row count:", len(transactions_categories_merchants_df))

    # COMBINE WITH PAYMENT METHODS
    final_transactions_df = pd.merge(
        transactions_categories_merchants_df,
        payment_methods_df,
        on="payment_method_id",
        how="left"
    )

    print("\nTransactions with categories, merchants, and payment methods:")
    print(
        final_transactions_df[
            [
                "transaction_id",
                "amount",
                "category_name",
                "merchant_name",
                "method_name"
            ]
        ].head()
    )
    print("\nCombined row count:", len(final_transactions_df))

    # COMBINE WITH MONTHLY BUDGETS
    final_transactions_df = pd.merge(
        final_transactions_df,
        monthly_budgets_df,
        on="budget_id",
        how="left",
        suffixes=("_transaction", "_budget")
    )

    print("\nTransactions combined with monthly budgets:")
    print(
        final_transactions_df[
            [
                "transaction_id",
                "amount",
                "category_name",
                "merchant_name",
                "method_name",
                "budget_month",
                "budget_amount"
            ]
        ].head()
    )
    print("\nCombined row count:", len(final_transactions_df))

    # ------------------------------------------- FINAL COMBINED DATA VALIDATION -------------------------------------------

    print("\nFINAL COMBINED DATAFRAME")
    print("\nShape (rows, columns):")
    print(final_transactions_df.shape)

    print("\nColumn names:")
    print(final_transactions_df.columns.tolist())

    print("\nMissing values:")
    print(final_transactions_df.isnull().sum())

    print("\nFirst 5 rows:")
    print(final_transactions_df.head())

    # ------------------------------------------- CREATING CHARTS -------------------------------------------

    os.makedirs("reports", exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")

    # CHART 1: MONTHLY EXPENSE TREND
    final_transactions_df["month"] = (
        final_transactions_df["transaction_date"].dt.to_period("M")
    )

    monthly_expenses = (
        final_transactions_df
        .groupby("month")["amount"]
        .sum()
    )

    print("\nMonthly expenses:")
    print(monthly_expenses)

    monthly_expenses.plot(kind="line", marker="o")
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses (INR)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        f"reports/monthly_expense_trend_{today}.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    # CHART 2: EXPENSES BY CATEGORY
    category_expenses = (
        final_transactions_df
        .groupby("category_name")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nExpenses by category:")
    print(category_expenses)

    category_expenses.plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(8, 8)
    )

    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.tight_layout()

    plt.savefig(
        f"reports/expenses_by_category_{today}.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    # CHART 3: TOP MERCHANTS BY SPENDING
    merchant_expenses = (
        final_transactions_df
        .groupby("merchant_name")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nTop merchants by spending:")
    print(merchant_expenses)

    merchant_expenses.plot(kind="bar")
    plt.title("Top 10 Merchants by Spending")
    plt.xlabel("Merchant")
    plt.ylabel("Total Expenses (INR)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(
        f"reports/top_merchants_{today}.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    # CHART 4: BUDGET VS ACTUAL SPENDING

    actual_spending = (
        final_transactions_df
        .groupby("budget_id")["amount"]
        .sum()
    )

    budget_comparison = monthly_budgets_df[
        ["budget_id", "budget_amount", "budget_month", "category_id"]
    ].copy()

    budget_comparison = pd.merge(
        budget_comparison,
        actual_spending.rename("actual_spending"),
        on="budget_id",
        how="left"
    )

    budget_comparison["actual_spending"] = (
        budget_comparison["actual_spending"].fillna(0)
    )

    print("\nBudget vs Actual Spending:")
    print(budget_comparison.head(10))

    budget_comparison = budget_comparison.sort_values("budget_id")

    budget_comparison.set_index("budget_id")[
        ["budget_amount", "actual_spending"]
    ].plot(
        kind="barh",
        figsize=(11, 8),
        width=0.8
    )

    plt.title("Budget vs Actual Spending")
    plt.xlabel("Amount (INR)")
    plt.ylabel("Budget ID")
    plt.legend(["Budget Amount", "Actual Spending"])
    plt.tight_layout()

    plt.savefig(
        f"reports/budget_vs_actual_{today}.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    print("\nAll four charts have been saved successfully!")
    print("Check the 'reports' folder for today's chart images.")


# --------------------------------------- TASK AND SCHEDULE ------------------------------------------------------------------------------

def job():
    print(f"Running dashboard at {datetime.now()}")
    create_dashboard()


schedule.every().day.at("14:39").do(job)

print("Scheduler started — waiting for 2:39PM")

while True:
    schedule.run_pending()
    time.sleep(30)