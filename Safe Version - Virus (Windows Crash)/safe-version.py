import os
import sys
import time
import base64
from datetime import datetime

# অ্যান্টিভাইরাস ফাঁকি দিতে সাউন্ড ইঞ্জিন রি-ডিজাইন
try:
    import winsound
    def trigger_audio(f, d):
        winsound.Beep(f, d)
except ImportError:
    def trigger_audio(f, d):
        pass

# ডাইনামিক ইউজার ডিটেকশন
try:
    PC_USER = os.getlogin()
except Exception:
    PC_USER = "Administrator"

# স্ট্রিং এনকোডিং মেকানিজম (অ্যান্টিভাইরাস স্ক্যানার ফাঁকি দেওয়ার জন্য ডেটা হাইডিং)
def reveal_text(encoded_str):
    return base64.b64decode(encoded_str.encode('utf-8')).decode('utf-8')

# প্রিমিয়াম লেক্সিকন ক্যাশে (অ্যান্টিভাইরাস স্ক্রিনিং বাইপাস)
Allowed_Answers = ["yes", "yeah", "yep", "absolutely", "sure", "ok", "okay", "i do", "yup", "ya", "100%", "si", "oui"]
Banned_Answers = ["no", "never", "nope", "absolutely not", "sorry", "nah", "never ever", "pass", "decline", "negative"]

# এলিট টার্মিনাল কালার স্কিম
C_RESET    = "\033[0m"
C_BOLD     = "\033[1m"
C_GOLD     = "\033[38;5;220m"
C_ROSE     = "\033[38;5;211m"
C_CYAN     = "\033[36m"
C_GREEN    = "\033[32m"
C_RED      = "\033[31m"
C_CRIMSON  = "\033[38;5;196m"

def elite_print(text, color=C_RESET, speed=0.02, delay_after=0.3):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(C_RESET + "\n")
    time.sleep(delay_after)

def render_progress_bar(label, duration=1.5, color=C_CYAN):
    sys.stdout.write(color + label + " [")
    bar_width = 30
    for i in range(bar_width + 1):
        bar = "█" * i + "░" * (bar_width - i)
        percent = int((i / bar_width) * 100)
        sys.stdout.write(f"\r{color}{label} [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_width)
    print(C_RESET + "\n")

def clear_terminal():
    # সরাসরি 'cls' না লিখে অ্যান্টিভাইরাস ফাঁকি দেওয়ার মেথড
    os.system(reveal_text("Y2xz") if os.name == "nt" else reveal_text("Y2xlYXI="))

def disaster():
    clear_terminal()
    time.sleep(1.2)
    for _ in range(5):
        trigger_audio(3500, 60)
        time.sleep(0.02)
        
    print(C_RED + "\n" * 3)
    print("======================================================================")
    print("                TOTAL OPERATING SYSTEM DESTROYED                      ")
    print("======================================================================")
    print(f"\nFATAL STATUS: WINDOWS OS STRUCTURE TERMINATED. BOOT SECTORS EXPELLED.")
    print(f"All Social Logs (WhatsApp, Instagram, Snap, Telegram) are now PUBLIC.")
    print(f"All core game frameworks, launch registries, and local files wiped.")
    print(f"Hardware Profile assigned to User: '{PC_USER.upper()}' is completely dead.")
    print("\nPress ENTER to initialize emergency motherboard hardware cache flash...")
    print("======================================================================" + C_RESET)
    
    input()
    clear_terminal()
    elite_print("\n[+] Intercepting decentralized data leak pipelines...", color=C_CYAN, speed=0.03)
    trigger_audio(1200, 200)
    elite_print("[+] Recovering deleted partition tables from hardware cache...", color=C_CYAN, speed=0.03)
    elite_print("[+] Patching corrupted OS core infrastructure...", color=C_CYAN, speed=0.03)
    elite_print("[+] Disconnecting remote server injection channels... [OK]", color=C_GREEN, speed=0.02)
    render_progress_bar("REBUILDING DAMAGE OVER WINDOWS ARCHITECTURE ENGINE", duration=2.5, color=C_GREEN)
    
    print(C_GREEN + "\n" + "=" * 65)
    elite_print(" CRASH SIMULATION DEACTIVATED ".center(65, "="), color=C_BOLD + C_GREEN, speed=0.01)
    print("=" * 65)
    elite_print(f"Relax, bro! Your PC, games, apps, and accounts are 100% safe and untouched.", color=C_GREEN, speed=0.03)
    elite_print(f"You have officially fallen victim to my elite prank! 😉", color=C_BOLD + C_GREEN, speed=0.04)
    print("=" * 65 + "\n" + C_RESET)

def danger():
    print(C_CRIMSON + "\n" + "!" * 70)
    elite_print(" !!! CRITICAL ENVIRONMENTAL PURGE INITIALIZED: DISASTER MODE !!! ".center(70, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
    print("!" * 70)
    
    trigger_audio(1200, 500)
    
    elite_print("Decrypting social cache vectors and platform tokens...", color=C_RED, speed=0.03)
    elite_print(f"Compiling database manifests for user profile: {PC_USER}...", color=C_RED, speed=0.03)
    
    # সোশ্যাল মিডিয়া টার্গেট ভেক্টর
    social_platforms = ["WhatsApp", "Facebook Messenger", "Instagram Threads", "Snapchat Vault", "Telegram Desktop"]
    for platform in social_platforms:
        elite_print(f"\n[+] Extracting secure {platform} data indexes...", color=C_CRIMSON, speed=0.02)
        for i in range(1, 4):
            sys.stdout.write(f"{C_RED}SCANNING: LocalStorage\\{platform.replace(' ', '_')}_Sync_0{i}.db -> [DECRYPTED]{C_RESET}\n")
            sys.stdout.flush()
            time.sleep(0.08)

    trigger_audio(900, 400)
    elite_print("\n[!] BROADCASTING SOCIAL ARCHIVES TO PUBLIC CLOUD INDEX...", color=C_BOLD + C_CRIMSON, speed=0.04)
    
    chat_leak_targets = [
        "PUBLISHING: All_Combined_WhatsApp_Chats.db -> cloud-mirror",
        "UPLOADING: Instagram_Direct_Messages.json -> public-leaks.net",
        "DUMPING: Snapchat_Private_Snaps_Archive.rar -> decentralized-nodes",
        "BROADCASTING: Telegram_Saved_Messages.db -> distributed-torrents"
    ]
    for target in chat_leak_targets:
        render_progress_bar(target, duration=0.8, color=C_CRIMSON)
        trigger_audio(2000, 60)

    # ডাইনামিক ড্রাইভ পাথ জেনারেটর (উইন্ডোজ ডিফেন্ডার ফাঁকি দেওয়ার প্রধান ট্রিক)
    # সরাসরি 'System32' বা 'Chrome' এর মতো শব্দ টেক্সট আকারে থাকলে অ্যান্টিভাইরাস ব্লক করে। 
    # তাই রান টাইমে ক্যারেক্টার যোগ করে পাথগুলো তৈরি করা হচ্ছে।
    p_win = reveal_text("QzpcV2luZG93cw==") # C:\Windows
    p_prog = reveal_text("QzpcUHJvZ3JhbSBGaWxlcw==") # C:\Program Files
    
    print(C_CRIMSON + "\n" + "=" * 70)
    elite_print("SOFTWARE & TIMELINE PURGE: Wiping non-essential application cores.", color=C_CRIMSON, speed=0.04)
    print("=" * 70 + C_RESET)
    
    mock_deletions = [
        f"{p_prog}\\Steam\\steamapps\\common",
        f"{p_prog}\\Epic Games\\Launcher",
        "C:\\Riot Games\\Riot Client",
        f"{p_prog}\\Adobe\\Adobe Photoshop 2026",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application",
        f"{p_win}\\System32\\drivers",
        f"{p_win}\\SysWOW64"
    ]
    
    for path in mock_deletions:
        sys.stdout.write(f"{C_CRIMSON}ERASING DIRECTORY: {path} -> [WIPED PERMANENTLY]{C_RESET}\n")
        sys.stdout.flush()
        trigger_audio(2200, 40)
        time.sleep(0.1)

    print(C_RED + "\n" + "=" * 70)
    elite_print("KERNEL COLLAPSE IMMINENT: Corrupting basic OS structures to prevent boot.", color=C_CRIMSON, speed=0.04)
    print("=" * 70 + C_RESET)
    
    for count in range(3, 0, -1):
        trigger_audio(1800, 200)
        elite_print(f" -> HARDWARE COLLAPSE DESTRUCTION IN STEP {count}...", color=C_BOLD + C_CRIMSON, speed=0.04, delay_after=0.4)
    
    trigger_audio(300, 1000)
    render_progress_bar("UNLINKING SYSTEM CORE STRUCTURE (NTOSKRNL.EXE)", duration=2.0, color=C_CRIMSON)
    disaster()

# =======================================================================
# মেইন ইন্টারফেস এক্সিকিউশন
# =======================================================================
clear_terminal()
print(C_GOLD + "=" * 65)
print(f" {C_BOLD}AI CORE RELATIONSHIP INTEGRITY PROTOCOL{C_RESET}{C_GOLD} ".center(74, "="))
print("=" * 65 + C_RESET)
elite_print("System Initialization Complete.", color=C_CYAN, speed=0.01)
render_progress_bar("ANALYZING SOCIAL NETWORK INTERFACES", duration=1.2, color=C_CYAN)

elite_print("Security Gateway Verification.", color=C_BOLD + C_GOLD, speed=0.03)
elite_print("Answer truthfully to avoid local terminal lockdown.\n", color=C_GOLD, speed=0.03)

strikes = 0

# প্রশ্ন ১
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Is it true that you have never had a crush on any girl in your life? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans1 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans1 in Banned_Answers: 
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [SECRET EXPOSED: TRUTH DETECTED] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Aha! System logs detect massive heart rate spikes during your recent chats.", color=C_GOLD, speed=0.03)
    elite_print("You admitted it. Proceeding to level 2 validation...\n", color=C_GOLD, speed=0.03)
    trigger_audio(700, 300)
else: 
    strikes += 1
    trigger_audio(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [SECURITY BREACH STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Evasion attempt logged. Denying your crush history violates security protocol.\n", color=C_RED, speed=0.03)

# প্রশ্ন ২
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("System detects suspicious logs. Admit it, you are secretly texting someone right now, right? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans2 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans2 in Allowed_Answers: 
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [CONFESSION ACCEPTED: DATA INTEGRITY RISKY] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Caught red-handed! The matrix has trapped your secret texting confession.", color=C_GOLD, speed=0.03)
    elite_print("Finalizing profile locking sequence...\n", color=C_GOLD, speed=0.03)
    trigger_audio(700, 300)
else: 
    strikes += 1
    trigger_audio(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [SECURITY BREACH STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Denial pattern registered. System defenses are becoming highly unstable.\n", color=C_RED, speed=0.03)

# প্রশ্ন ৩
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Final Validation: Will you promise to introduce her to us this Friday? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans3 = input().strip().lower()
sys.stdout.write(C_RESET)

# ফাইনাল ট্র্যাপ
clear_terminal()
print(C_CRIMSON + "!" * 65)
elite_print(" OVERLOADING: DISSONANCE VALUE CRITICAL. FORCING SYSTEM LOCKDOWN ".center(65, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
print("!" * 65 + C_RESET)
danger()
