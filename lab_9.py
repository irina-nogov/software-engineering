import datetime

if __name__ == "__main__":
    n = int(input("Введите количество дней: "))
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=n)
    print(f"День недели через {n} дней: {future_date.strftime('%A')}")