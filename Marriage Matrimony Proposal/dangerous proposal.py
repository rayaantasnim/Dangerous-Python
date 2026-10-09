import os
import sys
import time
import random
from datetime import datetime

# উইন্ডোজের জন্য সাউন্ড ইঞ্জিন ইম্পোর্ট
try:
    import winsound
    def play_beep(freq, duration):
        winsound.Beep(freq, duration)
except ImportError:
    def play_beep(freq, duration):
        pass

# পিসির আসল ইউজারনেম ডিটেক্ট করা (ভয় বাড়ানোর জন্য)
try:
    PC_USER = os.getlogin()
except Exception:
    PC_USER = "Administrator"

# =======================================================================
# 1. PREMIUM LEXICONS (50+ Lowercased Terms Each)
# =======================================================================
Allowed_Answers = [
    "yes", "yeah", "yep", "absolutely", "of course", "no problem", "sure", "ok", "okay", 
    "i do", "definitely", "indeed", "certainly", "totally", "affirmative", "yup", "ya", 
    "aye", "you bet", "gladly", "willingly", "with pleasure", "without a doubt", 
    "most certainly", "by all means", "i would love to", "sounds perfect", "undoubtedly", 
    "one hundred percent", "100%", "positive", "agreed", "right on", "count me in", "amen", 
    "bet", "ja", "si", "oui", "absolutely yes", "sure thing", "for sure", "i'm down", 
    "im down", "why not", "deal", "pleasure", "naturally", "obviously", "always", "forever"
]

Banned_Answers = [
    "no", "never", "nope", "absolutely not", "sorry", "think later", "nah", "nay", "no way", 
    "not at all", "never ever", "i don't think so", "idont think so", "pass", "decline", 
    "refuse", "not interested", "negative", "non", "nein", "hard pass", "maybe next time", 
    "gross", "ew", "please no", "not really", "unlikely", "impossible", "no thanks", 
    "nopes", "na", "cancel", "forget it", "no sir", "no maam", "don't want to", 
    "dont want to", "i can't", "i cant", "not a chance", "not in a million years", 
    "rather not", "hate to say it but no", "bye", "get lost", "no thank you", 
    "unfortunate no", "rejection", "i disagree", "stop", "never in my life"
]

# =======================================================================
# 2. ELITE TERMINAL GRAPHICS & COLOR ENGINE
# =======================================================================
C_RESET  = "\033[0m"
C_BOLD   = "\033[1m"
C_GOLD   = "\033[38;5;220m"
C_ROSE   = "\033[38;5;211m"
C_CYAN   = "\033[36m"
C_GREEN  = "\033[32m"
C_RED    = "\033[31m"
C_CRIMSON = "\033[38;5;196m"

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
        percent = int((i / bar_width) * 100)
        bar = "█" * i + "░" * (bar_width - i)
        sys.stdout.write(f"\r{color}{label} [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_width)
    print(C_RESET + "\n")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# =======================================================================
# 3. HIGH-INTENSITY SIMULATED MELTDOWN WITH AUDIO & REBOOT EFFECT
# =======================================================================
def danger():
    print(C_CRIMSON + "\n" + "!" * 70)
    elite_print(" !!! SYSTEM EXCEPTION: KERNEL_SECURITY_CHECK_FAILURE !!! ".center(70, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
    print("!" * 70)
    
    play_beep(1000, 400)
    
    elite_print("Security protocol breach: Absolute emotional divergence recognized.", color=C_RED, speed=0.03)
    elite_print(f"Targeting Profile: C:\\Users\\{PC_USER}\\...", color=C_RED, speed=0.03)
    elite_print("Initiating raw hardware memory purge...", color=C_RED, speed=0.03)
    
    # ডাইনামিক ইউজার পাথ ডিলিট করার নাটক (১০০% নিরাপদ)
    mock_folders = ["Desktop", "Documents", "Downloads", "AppData\\Local", "Pictures"]
    for i in range(45):
        fake_address = f"0x{random.randint(0x10000000, 0x9FFFFFFF):08X}"
        chosen_folder = random.choice(mock_folders)
        sys.stdout.write(f"{C_CRIMSON}ERASING: C:\\Users\\{PC_USER}\\{chosen_folder}\\target_{i:02d}.dat -> [WIPED]{C_RESET}\n")
        sys.stdout.flush()
        
        if i % 8 == 0:
            play_beep(2500, 50)
        else:
            time.sleep(0.015)
        
    print(C_RED + "\n" + "-" * 70)
    elite_print(f"CRITICAL LOG: Host filesystem for user '{PC_USER}' has been unlinked.", color=C_CRIMSON, speed=0.04)
    print("-" * 70 + C_RESET)
    play_beep(800, 300)

    for count in range(3, 0, -1):
        play_beep(1500, 150)
        elite_print(f" -> HARDWARE TERMINATION STEP {count}...", color=C_BOLD + C_CRIMSON, speed=0.04, delay_after=0.5)
    
    play_beep(400, 800)
    render_progress_bar("DESTROYING MASTER BOOT RECORD (MBR)", duration=2.5, color=C_CRIMSON)
    disaster()

def disaster():
    clear_terminal()
    time.sleep(1.0)
    
    for _ in range(3):
        play_beep(3000, 100)
        time.sleep(0.05)
        
    print(C_RED + "\n" * 4)
    print("======================================================================")
    print("                    FATAL SYSTEM CRASH DETECTED                       ")
    print("======================================================================")
    print(f"\nNO BOOTABLE DEVICE FOUND. INTEGRITY CHECK FAILED FOR USER: {PC_USER.upper()}.")
    print("Core Operating System has been completely dissolved from the drive.")
    print("\nPress ENTER to attempt motherboard emergency hardware force-reboot...")
    print("======================================================================" + C_RESET)
    
    input()
    
    # নতুন ফিচার: ভুয়ো সিস্টেম রিবুট সিকোয়েন্স (ইউজারকে শান্ত করার জন্য)
    clear_terminal()
    elite_print("\n[+] Sending hardware reset signal to CMOS...", color=C_CYAN, speed=0.03)
    play_beep(1200, 200)
    elite_print("[+] Initializing Motherboard BIOS/UEFI...", color=C_CYAN, speed=0.03)
    elite_print("[+] Checking NVMe SSD Smart Status... [INTEGRITY OK]", color=C_GREEN, speed=0.02)
    elite_print("[+] Re-mounting Virtual Safemode Kernel...", color=C_GREEN, speed=0.02)
    render_progress_bar("RECOVERING SYSTEM ENVIRONMENT FROM CACHE", duration=2.0, color=C_GREEN)
    
    print(C_GREEN + "\n" + "=" * 65)
    elite_print(" SYSTEM SAFELY RESTORED ".center(65, "="), color=C_BOLD + C_GREEN, speed=0.01)
    print("=" * 65)
    elite_print(f"Relax, {PC_USER}! Your PC is 100% untouched. This was just an elite prank! 😉", color=C_GREEN, speed=0.03)
    print("=" * 65 + "\n" + C_RESET)

# =======================================================================
# 4. DATA LOGGING ENGINE
# =======================================================================
def log_engagement():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("engagement_manifest.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] User: {PC_USER} | Mutual Agreement Verified.\n")
    except Exception:
        pass

# =======================================================================
# 5. PRESTIGE SYSTEM USER INTERFACE
# =======================================================================
clear_terminal()
print(C_GOLD + "=" * 65)
print(f" {C_BOLD}THE LUXURY EMBASSY AUTOMATION MATRIX{C_RESET}{C_GOLD} ".center(74, "="))
print("=" * 65 + C_RESET)
elite_print("System Initialization Complete.", color=C_CYAN, speed=0.01)
render_progress_bar("LOADING PERSONALITY INDEX", duration=1.2, color=C_CYAN)

elite_print("Welcome to the Ultimate Luxury Matchmaking Interface.", color=C_BOLD + C_GOLD, speed=0.03)
elite_print("A moment of absolute clarity awaits your confirmation.\n", color=C_GOLD, speed=0.03)

strikes = 0
max_strikes = 3

while strikes < max_strikes:
    sys.stdout.write(C_GOLD + "✦ " + C_RESET)
    elite_print("Will you marry me? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
    
    sys.stdout.write(C_BOLD + C_CYAN)
    propose = input().strip().lower()
    sys.stdout.write(C_RESET)
    
    if propose in Allowed_Answers:
        clear_terminal()
        play_beep(1200, 150)
        play_beep(1500, 300)
        
        print(C_GREEN + "\n" + "♥" * 65)
        elite_print(" A MAGNIFICENT MATCH ACCEPTED ".center(65, "♥"), color=C_BOLD + C_GREEN, speed=0.02)
        print("♥" * 65 + C_RESET)
        
        elite_print("An exceptional response. The arrangements shall begin immediately.", color=C_GREEN, speed=0.03)
        elite_print("Let us step into this legacy together.", color=C_BOLD + C_GREEN, speed=0.03)
        
        render_progress_bar("WRITING LEGACY ENTRY TO ENCRYPTED LEDGER", duration=2.0, color=C_GREEN)
        log_engagement()
        
        print(C_GREEN + "=" * 65 + "\n")
        break
        
    elif propose in Banned_Answers:
        strikes += 1
        remaining = max_strikes - strikes
        
        play_beep(600, 200)
        
        print(C_RED + "\n" + "-" * 65)
        elite_print(f" [STRIKE {strikes} OF {max_strikes}] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
        print("-" * 65 + C_RESET)
        
        if remaining > 0:
            elite_print("An unexpected response. True elegance requires patience—let us reconsider.", color=C_RED, speed=0.03)
            elite_print(f"Please present a more favorable answer. You have {remaining} attempt(s) remaining.\n", color=C_RED, speed=0.03)
        else:
            elite_print("Patience exhausted. Initiating defensive counter-measures.", color=C_BOLD + C_CRIMSON, speed=0.03)
            danger()
            
    else:
        clear_terminal()
        print(C_CRIMSON + "!" * 65)
        elite_print(" UNRECOGNIZED INPUT DETECTED: SYSTEM LOCKDOWN INITIALIZED ".center(65, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
        print("!" * 65 + C_RESET)
        danger()
        break
