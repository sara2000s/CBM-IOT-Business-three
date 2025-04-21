import pandas as pd

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت
MIN_TOKEN_VALUE = 10  # حداقل ارزش توکن (دلار)
MAX_TOKEN_VALUE = 50  # حداکثر ارزش توکن (دلار)
TOKENS_PER_USER_PER_MONTH = 0.1  # تعداد توکن‌های اعطایی به هر کاربر در ماه
TOTAL_USERS = 500  # تعداد کل کاربران

# تابع تحلیل نوسانات ارزش توکن
def analyze_token_value_impact(file_path):
    try:
        # بارگذاری داده‌ها
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return

        # محاسبه درآمد بر اساس حداقل و حداکثر ارزش توکن
        low_token_value_income = TOTAL_USERS * TOKENS_PER_USER_PER_MONTH * MIN_TOKEN_VALUE
        high_token_value_income = TOTAL_USERS * TOKENS_PER_USER_PER_MONTH * MAX_TOKEN_VALUE

        # نمایش نتایج
        print("\nToken Value Impact Analysis:")
        print(f"Low Token Value Income (at ${MIN_TOKEN_VALUE} per token): ${low_token_value_income:.2f} per month")
        print(f"High Token Value Income (at ${MAX_TOKEN_VALUE} per token): ${high_token_value_income:.2f} per month")
        print("\nInterpretation:")
        print("Market volatility could significantly impact the revenue potential for healthcare providers based on token value fluctuations.")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_token_value_impact(file_path)
