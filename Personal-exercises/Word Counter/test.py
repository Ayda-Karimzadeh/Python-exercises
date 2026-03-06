import os

def count_words(file_path):
    if not os.path.exists(file_path):
        print(f"خطا: فایل '{file_path}' یافت نشد.")
        return 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                print("فایل خالی است.")
                return 0
            words = content.split()
            return len(words)
    except Exception as e:
        print(f"خطا در خواندن فایل: {e}")
        return 0

# مسیر فایل رو می‌تونی تغییر بدی
file_path = "D:/Python developer/Python-exercises/Personal-exercises/Word Counter/text.txt"
word_count = count_words(file_path)
print(f"تعداد کلمات: {word_count}")
