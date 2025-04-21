import pandas as pd
import random

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت
BASE_DATA_PRICE = 100  # قیمت پایه برای جمع‌آوری و پردازش داده‌ها
BASE_USER_ENGAGEMENT_RATE = 0.6  # نرخ پایه مشارکت کاربران
BASE_REGULATORY_COST = 5000  # هزینه پایه ناشی از قوانین نظارتی

# تغییرات ممکن برای تحلیل حساسیت
PRICE_FLUCTUATIONS = [0.8, 1.0, 1.2]  # کاهش، ثابت و افزایش قیمت داده‌ها
USER_ENGAGEMENT_SCENARIOS = [0.4, 0.6, 0.8]  # کاهش، ثابت و افزایش مشارکت کاربران
REGULATORY_COST_SCENARIOS = [7000, 5000, 3000]  # افزایش، ثابت و کاهش هزینه‌های نظارتی

# تحلیل حساسیت
def sensitivity_analysis(file_path):
    try:
        # بارگذاری داده‌ها
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        total_users = len(data)
        base_cost = total_users * BASE_DATA_PRICE + BASE_REGULATORY_COST

        print("Performing sensitivity analysis...")
        
        # مدل‌سازی سناریوهای مختلف
        for price_factor in PRICE_FLUCTUATIONS:
            for engagement_rate in USER_ENGAGEMENT_SCENARIOS:
                for regulatory_cost in REGULATORY_COST_SCENARIOS:
                    adjusted_cost = total_users * BASE_DATA_PRICE * price_factor + regulatory_cost
                    engaged_users = int(total_users * engagement_rate)
                    potential_revenue = engaged_users * BASE_DATA_PRICE
                    net_gain_or_loss = potential_revenue - adjusted_cost

                    # نمایش سناریوی موردنظر
                    print(f"\nScenario: Data Price Factor: {price_factor}, Engagement Rate: {engagement_rate}, Regulatory Cost: ${regulatory_cost}")
                    print(f"Adjusted Cost: ${adjusted_cost:.2f}, Engaged Users: {engaged_users}, Potential Revenue: ${potential_revenue:.2f}, Net Gain/Loss: ${net_gain_or_loss:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
sensitivity_analysis(file_path)
