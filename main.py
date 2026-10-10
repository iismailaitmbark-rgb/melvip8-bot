import os
import time
import threading
import requests
import schedule
from flask import Flask

# إعداد خادم ويب مصغر لإبقاء الخدمة نشطة على Render
app = Flask(__name__)

@app.route('/')
def home():
    return "AI Agent for @MELVIP8 is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

TOKEN = "8650027079:AAFqlJOKkc3Vq7gOT3lE0ZTEJakYHETrtbA"
CHANNEL_ID = "@MELVIP8"

def send_post(message_text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message_text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    try:
        res = requests.post(url, json=payload)
        if res.status_code == 200:
            print("[نجاح] تم النشر في القناة.")
        else:
            print(f"[خطأ] فشل النشر: {res.text}")
    except Exception as e:
        print(f"[استثناء] {e}")

def morning_update():
    text = """
🌅 **صباح الحماس والربح مع Al Best Arabia!** ⚽🔥

تابع معنا أحدث توقعات اليوم وإحصائيات المباريات الكبرى لنضمن لك أفضل النتائج.

🎁 **ضِاعف إيداعك الأول بنسبة 100%:**
🔑 البروموكود الحصري: `MELVIP8`
🔗 رابط التسجيل المباشر: 
https://refpa3665.com/L?tag=d_5490189m_2170c_MELVIP8

#AlBestArabia #مباريات_اليوم #توقعات_رياضية
    """
    send_post(text)

def evening_deep_dive():
    text = """
⚡ **تحليلات ما قبل قمم الليلة!** 🏆⚽

ساعات قليلة تفصلنا عن صافرة بداية أقوى مباريات الدوريات الكبرى.

💎 **لا تفوت الفرصة واستغل البونص الترحيبي:**
🔑 البروموكود: `MELVIP8`
🔗 رابط التسجيل والرهان: 
https://refpa3665.com/L?tag=d_5490189m_2170c_MELVIP8

#AlBestArabia #دوري_أبطال_أوروبا #الدوري_الإسباني
    """
    send_post(text)

def pre_kickoff_prediction():
    text = """
🚨 **توقعات الحسم - قبل انطلاق المباريات بـ 30 دقيقة!** ⏱️🔥

استغل عوائد الرهان المباشر (Live) بناءً على التشكيلات الرسمية والمعطيات الأخيرة.

🎯 **سجل الآن واعتمد الكود لضمان مكافأتك:**
🔑 البروموكود: `MELVIP8`
🔗 رابط الدخول السريع: 
https://refpa3665.com/L?tag=d_5490189m_2170c_MELVIP8

#AlBestArabia #مباريات_مباشرة
    """
    send_post(text)

schedule.every().day.at("08:00").do(morning_update)
schedule.every().day.at("17:00").do(evening_deep_dive)
schedule.every().day.at("19:30").do(pre_kickoff_prediction)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    t_web = threading.Thread(target=run_flask)
    t_web.daemon = True
    t_web.start()
    
    print("🤖 الوكيل الآلي لـ Al Best Arabia يعمل الآن في الخلفية...")
    run_scheduler()
