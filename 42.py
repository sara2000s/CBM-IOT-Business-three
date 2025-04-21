import pandas as pd
import random

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت
INITIAL_TOKEN_PRICE = 10  # قیمت اولیه توکن (دلار)
MAX_FLUCTUATION = 0.3  # حداکثر نوسان قیمت (%)
TOKEN_REWARD = 5  # تعداد توکن‌هایی که به ازای هر اشتراک داده اعطا می‌شود
USER_PARTICIPATION_THRESHOLD = 0.5  # حداقل احتمال مشارکت کاربر (%)
MARKET_IMPACT_FACTOR = 0.2  # تأثیر قیمت توکن بر مشارکت

# تابع شبیه‌سازی نوسان قیمت توکن
def simulate_token_price():
    fluctuation = random.uniform(-MAX_FLUCTUATION, MAX_FLUCTUATION)  # نوسان قیمت توکن
    return fluctuation

# تحلیل اقتصاد توکن
def analyze_token_economy(file_path):
    try:
        # بارگذاری داده‌ها
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        initial_price = INITIAL_TOKEN_PRICE
        total_rewards = 0
        user_participation_count = 0
        total_users = len(data)

        print("Analyzing token economy...")

        # پردازش کاربران برای شبیه‌سازی مشارکت و اعطای توکن
        for index, row in data.iterrows():
            # شبیه‌سازی نوسان قیمت توکن
            price_fluctuation = simulate_token_price()
            current_price = initial_price * (1 + price_fluctuation)

            # شبیه‌سازی مشارکت کاربر
            participation_chance = random.uniform(0, 1)
            if participation_chance > USER_PARTICIPATION_THRESHOLD - (MARKET_IMPACT_FACTOR * price_fluctuation):
                user_participation_count += 1
                rewards = TOKEN_REWARD * current_price  # ارزش توکن‌های اعطا شده
                total_rewards += rewards
                print(f"Row {index + 1}: User Participated - Token Price: ${current_price:.2f}, Rewards: ${rewards:.2f}")
            else:
                print(f"Row {index + 1}: User Did Not Participate - Token Price: ${current_price:.2f}")

        # محاسبات نهایی
        participation_rate = (user_participation_count / total_users) * 100

        print("\nToken Economy Analysis Report:")
        print(f"Total Users: {total_users}")
        print(f"Users Participated: {user_participation_count}")
        print(f"Participation Rate: {participation_rate:.2f}%")
        print(f"Total Token Rewards Distributed (Value): ${total_rewards:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_token_economy(file_path)
