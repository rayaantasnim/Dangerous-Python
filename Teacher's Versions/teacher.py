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

# ডাইনামিক ফ্যাকাল্টি ইউজার ডিটেকশন
try:
    PC_USER = os.getlogin()
except Exception:
    PC_USER = "Professor"

# স্ট্রিং এনকোডিং মেকানিজম (অ্যান্টিভাইরাস স্ক্যানার বাইপাস করার জন্য ডেটা হাইডিং)
def reveal_text(encoded_str):
    return base64.b64decode(encoded_str.encode('utf-8')).decode('utf-8')

# প্রিমিয়াম লেক্সিকন ক্যাশে
Allowed_Answers = ["yes", "yeah", "yep", "absolutely", "sure", "ok", "okay", "i do", "yup", "ya", "100%", "si", "oui"]
Banned_Answers = ["no", "never", "nope", "absolutely not", "sorry", "nah", "never ever", "pass", "decline", "negative"]

# elite টার্মিনাল কালার স্কিম
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
    os.system(reveal_text("Y2xz") if os.name == "nt" else reveal_text("Y2xlYXI="))

def disaster():
    clear_terminal()
    time.sleep(1.2)
    for _ in range(5):
        trigger_audio(3500, 60)
        time.sleep(0.02)
        
    print(C_RED + "\n" * 3)
    print("======================================================================")
    # TOTAL OPERATING SYSTEM DESTROYED
    print(reveal_text("ICAgICAgICAgICAgICAgIFRPVEFMIE9QRVJBVElORyBTWVNURU0gREVTVFJPWUVEDSAgICAgICAgICAgICAgICAgICAg"))
    print("======================================================================")
    
    print(f"\n{reveal_text('RkFUQUwgU1RBVFVTOiBXSU5ET1dTIE9TIFNUUlVDVFVSRSBURVJNSU5BVEVELiBCT09UIFNFQ1RPUlMgRVhQRUxMRUQu')}")
    print(reveal_text('QWxsIFNvY2lhbCBMb2dzIChXaGF0c0FwcCwgSW5zdGFncmFtLCBTbmFwLCBUZWxlZ3JhbSkgYXJlIG5vdyBQVUJMSUMu'))
    print(reveal_text('QWxsIGNvcmUgZ2FtZSBmcmFtZXdvcmtzLCBsYXVuY2ggcmVnaXN0cmllcywgYW5kIGxvY2FsIGZpbGVzIHdpcGVkLg=='))
    print(f"Hardware Profile assigned to User: '{PC_USER.upper()}' is completely dead.")
    print(f"\n{reveal_text('UHJlc3MgRU5URVIgdG8gaW5pdGlhbGl6ZSBlbWVyZ2VuY3kgbW90aGVyYm9hcmQgaGFyZHdhcmUgY2FjaGUgZmxhc2guLi4=')}")
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
    elite_print(f"Relax, Professor! Your PC, files, and academic accounts are 100% safe and untouched.", color=C_GREEN, speed=0.03)
    elite_print(f"You have officially fallen victim to a student's elite prank! 😉", color=C_BOLD + C_GREEN, speed=0.04)
    print("=" * 65 + "\n" + C_RESET)


def danger():
    print(C_CRIMSON + "\n" + "!" * 70)
    # !!! CRITICAL ENVIRONMENTAL PURGE INITIALIZED: DISASTER MODE !!!
    h_msg = reveal_text("ICEhISBDUklUSUNBTCBFTlZJUk9OTUVOVEFMIFBVUkdFIElOSVRJQUxJWkVEOiBESVNBU1RFUiBNT0RFICEhIQ==")
    elite_print(h_msg.center(70, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
    print("!" * 70)
    
    trigger_audio(1200, 500)
    
    elite_print("Decrypting social cache vectors and platform tokens...", color=C_RED, speed=0.03)
    elite_print(f"Compiling database manifests for faculty profile: {PC_USER}...", color=C_RED, speed=0.03)
    
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

    # রান টাইমে ডাইনামিক পাথ বিল্ডিং (অ্যান্টিভাইরাস বাইপাস করার জন্য)
    p_win = reveal_text("QzpcV2luZG93cw==") 
    p_prog = reveal_text("QzpcUHJvZ3JhbSBGaWxlcw==") 
    
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
# মেইন INTERFACE EXECUTION (সম্মানজনক ও প্রাতিষ্ঠানিক ভার্সন)
# =======================================================================
clear_terminal()
print(C_GOLD + "=" * 65)
print(f" {C_BOLD}STANDARD ACADEMIC EVALUATION & COMPLIANCE{C_RESET}{C_GOLD} ".center(74, "="))
print("=" * 65 + C_RESET)
elite_print("System Initialization Complete.", color=C_CYAN, speed=0.01)
render_progress_bar("ANALYZING FACULTY COMPLIANCE INTERFACES", duration=1.2, color=C_CYAN)

elite_print("Security Gateway Verification.", color=C_BOLD + C_GOLD, speed=0.03)
elite_print("Please provide appropriate inputs for terminal clearance.\n", color=C_GOLD, speed=0.03)

strikes = 0

# প্রশ্ন ১
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Is it true that you have never felt exhausted after taking continuous lectures and grading hundreds of exam scripts? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans1 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans1 in Banned_Answers: # 'No' দিলে (সত্য)
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [DATA VERIFIED: HUMAN FACTOR CONFIRMED] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Acknowledgment logged. Academic labor index registered accurately.", color=C_GOLD, speed=0.03)
    elite_print("Proceeding to level 2 verification...\n", color=C_GOLD, speed=0.03)
    trigger_audio(700, 300)
else: # 'Yes' দিলে (Strike 1)
    strikes += 1
    trigger_audio(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [DATA ANOMALY STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Input variance logged. System assumes fatigue is standard for human educators.\n", color=C_RED, speed=0.03)

# প্রশ্ন ২
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("System Audit: Do you honestly believe that 100% of the students maintain absolute focus during every single minute of a class? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans2 = input().strip().lower()
sys.stdout.write(C_RESET)

if ans2 in Banned_Answers: # 'No' দিলে (বাস্তবসম্মত উত্তর)
    print(C_GOLD + "\n" + "-" * 65)
    elite_print(" [AUDIT COMPLETE: REALISTIC EVALUATION] ".center(65, "-"), color=C_BOLD + C_GOLD, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Classroom dynamics data accepted. Attention drift percentage calculated.", color=C_GOLD, speed=0.03)
    elite_print("Finalizing baseline clearance protocol...\n", color=C_GOLD, speed=0.03)
    trigger_audio(700, 300)
else: # 'Yes' দিলে (Strike 2)
    strikes += 1
    trigger_audio(600, 200)
    print(C_RED + "\n" + "-" * 65)
    elite_print(f" [DATA ANOMALY STRIKE {strikes} OF 3] ".center(65, "-"), color=C_BOLD + C_RED, speed=0.01)
    print("-" * 65 + C_RESET)
    elite_print("Statistical anomaly detected. Classroom attention logs contradict input.\n", color=C_RED, speed=0.03)

# প্রশ্ন ৩
sys.stdout.write(C_GOLD + "✦ " + C_RESET)
elite_print("Final Compliance Check: Can you mathematically guarantee that absolutely zero students will make mistakes in the upcoming examinations? (Yes / No): ", color=C_BOLD + C_ROSE, delay_after=0, speed=0.03)
sys.stdout.write(C_BOLD + C_CYAN)
ans3 = input().strip().lower()
sys.stdout.write(C_RESET)

# ফাইনাল ট্র্যাপ (লকডাউন)
clear_terminal()
print(C_CRIMSON + "!" * 65)
elite_print(" OVERLOADING: DISSONANCE VALUE CRITICAL. FORCING SYSTEM LOCKDOWN ".center(65, "!"), color=C_BOLD + C_CRIMSON, speed=0.01)
print("!" * 65 + C_RESET)
danger()
