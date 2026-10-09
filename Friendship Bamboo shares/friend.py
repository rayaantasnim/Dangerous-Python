import os
import sys
import time
import random
from datetime import datetime

# Windows Audio Engine Configuration
try:
    import winsound
    def play_beep(freq, duration):
        winsound.Beep(freq, duration)
except ImportError:
    def play_beep(freq, duration):
        pass

# Dynamic System Username Retrieval
try:
    PC_USER = os.getlogin()
except Exception:
    PC_USER = "User"

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
    """Prints text character-by-character with custom speeds and color styling."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(C_RESET + "\n")
    time.sleep(delay_after)

def render_progress_bar(label, duration=1.5, color=C_CYAN):
    """Displays a premium loading or wiping progress bar."""
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
    """Clears the terminal window for a clean interface display."""
    os.system('cls' if os.name == 'nt' else 'clear')

# =======================================================================
# 3. APPS, GAMES & ALL-PLATFORM SOCIAL LEAK BREAKDOWN SIMULATION
# =======================================================================
def danger():
    print(C_CRIMSON + "\n" + "!" * 70)
    elite_print(" !!! CRITICAL ENVIRONMENTAL PURGE INITIALIZED: DISASTER MODE !!! ".center(70, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
    print("!" * 70)
    
    play_beep(1200, 500)
    
    elite_print("Decrypting social cache vectors and platform tokens...", color=C_RED, speed=0.03)
    elite_print(f"Compiling database manifests for user profile: {PC_USER}...", color=C_RED, speed=0.03)
    
    # Target Social Media Data Dumps
    social_platforms = ["WhatsApp", "Facebook Messenger", "Instagram Threads", "Snapchat Vault", "Telegram Desktop"]
    for platform in social_platforms:
        elite_print(f"\n[+] Extracting secure {platform} data indexes...", color=C_CRIMSON, speed=0.02)
        for i in range(1, 4):
            sys.stdout.write(f"{C_RED}SCANNING: LocalStorage\\{platform.replace(' ', '_')}_Sync_0{i}.db -> [DECRYPTED]{C_RESET}\n")
            sys.stdout.flush()
            time.sleep(0.08)

    play_beep(900, 400)
    elite_print("\n[!] BROADCASTING SOCIAL ARCHIVES TO PUBLIC CLOUD INDEX...", color=C_BOLD + C_CRIMSON, speed=0.04)
    
    chat_leak_targets = [
        "PUBLISHING: All_Combined_WhatsApp_Chats.db -> cloud-mirror",
        "UPLOADING: Instagram_Direct_Messages.json -> public-leaks.net",
        "DUMPING: Snapchat_Private_Snaps_Archive.rar -> decentralized-nodes",
        "BROADCASTING: Telegram_Saved_Messages.db -> distributed-torrents"
    ]
    for target in chat_leak_targets:
        render_progress_bar(target, duration=0.8, color=C_CRIMSON)
        play_beep(2000, 60)

    # Simulated App, Game and OS Software Destruction Engine
    print(C_CRIMSON + "\n" + "=" * 70)
    elite_print("SOFTWARE & TIMELINE PURGE: Wiping non-essential application cores.", color=C_CRIMSON, speed=0.04)
    print("=" * 70 + C_RESET)
    
    mock_deletions = [
        "C:\\Program Files\\Steam\\steamapps\\common",
        "C:\\Program Files\\Epic Games\\Launcher",
        "C:\\Riot Games\\Riot Client",
        "C:\\Program Files\\Adobe\\Adobe Photoshop 2026",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application",
        "C:\\Windows\\System32\\drivers",
        "C:\\Windows\\SysWOW64"
    ]
    
    for path in mock_deletions:
        sys.stdout.write(f"{C_CRIMSON}ERASING DIRECTORY: {path} -> [WIPED PERMANENTLY]{C_RESET}\n")
        sys.stdout.flush()
        play_beep(2200, 40)
        time.sleep(0.1)

    print(C_RED + "\n" + "=" * 70)
    elite_print("KERNEL COLLAPSE IMMINENT: Corrupting basic OS structures to prevent boot.", color=C_CRIMSON, speed=0.04)
    print("=" * 70 + C_RESET)
    
    for count in range(3, 0, -1):
        play_beep(1800, 200)
        elite_print(f" -> HARDWARE COLLAPSE DESTRUCTION IN STEP {count}...", color=C_BOLD + C_CRIMSON, speed=0.04, delay_after=0.4)
    
    play_beep(300, 1000)
    render_progress_bar("UNLINKING SYSTEM CORE STRUCTURE (NTOSKRNL.EXE)", duration=2.0, color=C_CRIMSON)
    disaster()

def disaster():
    clear_terminal()
    time.sleep(1.2)
    
    # Motherboard fatal error sequence emulation (Rapid sharp beeps)
    for _ in range(4):
        play_beep(3300, 80)
        time.sleep(0.04)
        
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
    
    # Advanced Mock Safe-Mode Restoration Routine
    clear_terminal()
    elite_print("\n[+] Intercepting decentralized data leak pipelines...", color=C_CYAN, speed=0.03)
    play_beep(1200, 200)
    elite_print("[+] Recovering deleted partition tables from hardware cache...", color=C_CYAN, speed=0.03)
    elite_print("[+] Patching corrupted NTOSKRNL.EXE core infrastructure...", color=C_CYAN, speed=0.03)
    elite_print("[+] Disconnecting remote server injection channels... [OK]", color=C_GREEN, speed=0.02)
    render_progress_bar("REBUILDING DAMAGE OVER WINDOWS ARCHITECTURE ENGINE", duration=2.5, color=C_GREEN)
    
    print(C_GREEN + "\n" + "=" * 65)
    elite_print(" CRASH SIMULATION DEACTIVATED ".center(65, "="), color=C_BOLD + C_GREEN, speed=0.01)
    print("=" * 65)
    elite_print(f"Relax, bro! Your PC, games, apps, and accounts are 100% safe and untouched.", color=C_GREEN, speed=0.03)
    elite_print(f"You have officially fallen victim to my elite prank! 😉", color=C_BOLD + C_GREEN, speed=0.04)
    print("=" * 65 + "\n" + C_RESET)

# =======================================================================
# 4. INITIAL INTERFACE & DYNAMIC SOCIAL REACTION LOGIC ENGINE
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

# -----------------------------------------------------------------------
# QUESTION 1: The Crush Check
# -----------------------------------------------------------------------
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Is it true that you have never had a crush on any girl in your life? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans1 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans1 in Banned_Answers: # User admits truth (Types 'No')
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [SECRET EXPOSED: TRUTH DETECTED] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Aha! System logs detect massive heart rate spikes during your recent chats.", color=C_GOLD, speed=0.03)
    elite_print("You admitted it. Proceeding to level 2 validation...\n", color=C_GOLD, speed=0.03)
    play_beep(700, 300)
else: # User denies past (Types 'Yes' -> Strike 1)
    strikes += 1
    play_beep(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [SECURITY BREACH STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Evasion attempt logged. Denying your crush history violates security protocol.\n", color=C_RED, speed=0.03)

# -----------------------------------------------------------------------
# QUESTION 2: The Secret Texting Check
# -----------------------------------------------------------------------
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("System detects suspicious logs. Admit it, you are secretly texting someone right now, right? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans2 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans2 in Allowed_Answers: # User confesses (Types 'Yes')
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [CONFESSION ACCEPTED: DATA INTEGRITY RISKY] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Caught red-handed! The matrix has trapped your secret texting confession.", color=C_GOLD, speed=0.03)
    elite_print("Finalizing profile locking sequence...\n", color=C_GOLD, speed=0.03)
    play_beep(700, 300)
else: # User attempts evasion (Types 'No' -> Strike added)
    strikes += 1
    play_beep(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [SECURITY BREACH STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Denial pattern registered. System defenses are becoming highly unstable.\n", color=C_RED, speed=0.03)

# -----------------------------------------------------------------------
# QUESTION 3: The Ultimate Catch-All Trap
# -----------------------------------------------------------------------
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Final Validation: Will you promise to introduce her to us this Friday? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans3 = input().strip().lower()
sys.stdout.write(C_RESET)

# Terminal self-terminates immediately into full environmental lockdown
clear_terminal()
print(C_CRIMSON + "!" * 65)
elite_print(" OVERLOADING: DISSONANCE VALUE CRITICAL. FORCING SYSTEM LOCKDOWN ".center(65, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
print("!" * 65 + C_RESET)
danger()
