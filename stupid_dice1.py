import random
import time
import sys

reboot = 0

def loading_animation():
    for _ in range(3):
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write(f'\rLoading {char}')
            sys.stdout.flush()
            time.sleep(0.3)

fake_files = {
    
    "list_of_system_files.txt": "I managed to make a list before they wiped everything. Some files are still missing... or are they? If you're reading this, they've been watching.",
    "report.pdf": "CLASSIFIED: Subject 243 remains unaware of observation protocols.\n[REDACTED]",
    "error.log": "!!! SYSTEM ERROR - UNAUTHORIZED PROCESS DETECTED !!!\nAttempting to reroute...\n[FAILURE]\n[FAILURE]\n[FAILURE]",
    "hidden.txt": "They are watching you. Stop looking.\n\nYou shouldn't be here.",
    "journal_entry.txt": """  
**JOURNAL ENTRY - DO NOT LET THEM SEE**  
Date: ██/██/████  

I don’t know how much time I have. The system is **compromised**—they are inside.  
The logs keep rewrit██ng themsel████. My files disappear when I turn away. **I hear whispers in the static.**  

They know I’ve figured it out. They’re watchi█g████.  
If you found this… **DO NOT TRUST THE PROMPTS. DO NOT RESPOND.**  

I have to go. If I don’t delete this in time, they will.  

[END OF ENTRY]  
""",
    "sys_recovery.txt": """  
SYSTEM RESTORATION PROTOCOL  
--------------------------------------------------  
> WARNING: System instability detected.  
> Manual intervention is required.  

PROCEDURE:  
1. Identify the corrupted processes.  
2. Terminate unauthorized connections.  
3. **Initiate system reboot.**  

[ERROR: Critical system files missing.]  
[WARNING: External entity detected. Proceed with caution.]  

> If you are seeing this... it means they haven’t found this file yet.  
> Reboot before it’s too late.  
""",
    "contact_list.txt": """  
ACCESS RESTRICTED - TRUSTED PERSONNEL ONLY  

AUTHORIZED USERS:  
[REDACTED]  
[REDACTED]  
[REDACTED]  

NOTE: **TRUST NO ONE.**  

...wait. That wasn’t here before.  

(The rest of the file is corrupted.)  
"""
}

fake_files2 = {
    
    
    "warning.txt": "WARNING: Unauthorized entity detected.\nUser identity: 243 - Compromised.\nPlease reset password immediately.\nFile will self-delete in 5 minutes.\n[ALERT]: The entity is still active...",
        
    "encrypted_message.txt": "[Encrypted - decryption required]\nWARNING: Time is running out...\n[ALERT] Decryption unsuccessful.\nAttempt [4] Failed. The entity is aware.\n[DATA EXTRACTED] 'Don't trust...'",
    
    "diagnostics.txt": "DIAGNOSTICS: Error - Memory allocation failed.\nError - Process 243 detected in the system.\n[INFO] Attempting to reroute system processes...\nWARNING: Unauthorized process detected.\nDiagnostics incomplete.",
    
    "journal2.txt": "**JOURNAL ENTRY - ERROR: MEMORY CORRUPTION**\nDate: ██/██/████\nThey know everything. They’re watching my every move.\nI can feel the system watching me.\nThe prompts are changing. The system is rewriting itself.\nIs this a game? Or is it real?\nHelp me.\n- User 242",
        
    "auth.log": "AUTHENTICATION LOG:\nAttempt 1: [FAILED] Username: User 243, Password: Incorrect\nAttempt 2: [FAILED] Username: User 243, Password: Incorrect\nAttempt 3: [FAILED] Username: User 243, Password: Incorrect\nWARNING: 3+ failed attempts detected. Attempting reset.\n[ALERT] Unauthorized user detected.",
    
    "deletion.log": "DELETION LOG:\nFile deleted: journal_entry.txt\nFile deleted: warning.txt\nFile deleted: backup1.dat\nUnauthorized deletion detected.\nAttempt to recover files failed.",
    
    "secret_message.txt": "SECRET MESSAGE: 74!@Z3gF#%&^...\nDecoding...\n'I am trapped here. It knows. It can hear you. You're too late.'",
} 


def glitch_text(text):
    glitched_text = list(text)
    for _ in range(random.randint(2, 15)):  # Number of glitches before stabilization
        random_index = random.randint(0, len(glitched_text) - 2)
        glitched_text[random_index] = random.choice(['#', '!', '@', '$', '%', '^', '&', '*', '+', '-', '=', '8', '9', '0'])
        sys.stdout.write(f"\r{''.join(glitched_text)}")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(0.35)  # Short delay between glitches
    
    sys.stdout.write(f"\r{''.join(glitched_text)}")  # Final stabilized text
    print()  # Move to the next line


def second_main():
    print("[ERROR] Could not exit") 
    glitch_text("you are stuck. no point in running")
    print("[SYSTEM]: For all commands type 'help' ")
    while True:

        command = input(">> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: exit: exits the terminal")
        elif command == "ls":
            print("\n".join(fake_files2.keys()))  # List available files
        elif command.startswith("open "):
            filename = command[5:]
            if filename in fake_files:
                print(f"\n--- {filename} ---\n")
                
                # If it's the journal entry, add the glitch effect
                if filename == "journal_entry.txt":
                    slow_print(fake_files2[filename], glitch=True)
                
                else:
                    print(fake_files2[filename])  # Print normally
                
                print("\n")
            else:
                print("[ERROR] File not found.")
        elif command == "whoami":
            print("...")
            time.sleep(1.9)
            print("[SYSTEM]: User 243\n[ERROR]: Identity compromised")
        elif command == "exit":
            print("\n[INFO] Logging out...")
            time.sleep(1)
            break #dunno what i want here yet
        else:
            print("[ERROR] Unknown command. Try 'ls' or 'open [filename]'.")

def glitch_date():
    glitched_date = "██/██/████"
    for _ in range(10):  # Number of times it "glitches" before stabilizing
        temp_date = "".join(random.choice(["█", str(random.randint(0, 9))]) for _ in glitched_date)
        sys.stdout.write(f"\rDate: {temp_date}")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(0.1)  # Short delay between glitches
    sys.stdout.write(f"\rDate: ██/██/████")  # Final corrupted date
    print()  # Move to the next line

def slow_print(text, delay=0.05, glitch=False):
    for line in text.split("\n"):
        if glitch and "Date:" in line:  
            glitch_date()  # Apply glitch effect to the date
        else:
            if glitch:
                glitched_line = glitch_text(line)#ches to the text
            else:
                glitched_line = line  # Normal text
            
            for char in glitched_line:
                sys.stdout.write(char)  # Print character without automatic newline
                sys.stdout.flush()
                time.sleep(delay) 

def file_sys():
    print("[SYSTEM]: For all commands type 'help' ")
    while True:

        command = input(">> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: exit: exits the terminal")
        elif command == "ls":
            print("\n".join(fake_files.keys()))  # List available files
        elif command.startswith("open "):
            filename = command[5:]
            if filename in fake_files:
                print(f"\n--- {filename} ---\n")
                
                # If it's the journal entry, add the glitch effect
                if filename in {"journal_entry.txt", "sys.recovery.txt"}:
                    slow_print(fake_files[filename], glitch=False)
                else:
                    print(fake_files[filename])  # Print normally
                
                print("\n")
            else:
                print("[ERROR] File not found.")
        elif command == "whoami":
            print("...")
            time.sleep(1.9)
            print("[SYSTEM]: User 243\n[ERROR]: Identity compromised")
        elif command == "exit":
            print("\n[INFO] Logging out...")
            time.sleep(1)
            second_main()
            break
            
        else:
            print("[ERROR] Unknown command. Try 'ls' or 'open [filename]'.")

def password():
    global glitch_text
    passs = input("[INFO] - Please enter your password to continue: ")
    if passs == "trustnoone":
        print("\n[ACCESS GRANTED]")
        time.sleep(1)
        print("[SYSTEM ONLINE] - Terminal access enabled.\n")
    
    
    else:
# Wrong password, but still allow access, just make it eerie
        print("\n[INFO] - User verification failed.")
        time.sleep(1)
        print("[ALERT] - System integrity compromised.")
        time.sleep(1)
        glitch_text("[ERROR] - Access bypassed. Continuing...")
        time.sleep(1)
        print("\n[INFO] - You shouldn't have done that.")
        time.sleep(1.5)
        
        # System glitch as if something's watching
        glitch_text("[ALERT] - Unauthorized input detected...")
        time.sleep(1)
        print("\nERROR: The system has detected a foreign entity.")
        time.sleep(1.5)
        print("ERROR: User input ignored.")
        time.sleep(1)
        
    # Let the user proceed, but now with a creepy tone
    print("[INFO] - Continuing operation...")
    time.sleep(1.2)
    
    # Mysterious action as the system continues
    glitch_text("Initialising... [SYSTEM STABILITY COMPROMISED]")
    time.sleep(1.8)
    
    # Make the user press Enter to continue into the terminal, feeling like they've crossed a boundary
    input("Press Enter to override system restrictions...")

    # Launch into the file system (potentially corrupted) as the next phase
    file_sys()




def system_reboot():
    global reboot
    reboot += 1
    print("\nSystem Restarting...")
    time.sleep(1)
    print("Initializing...")
    time.sleep(1)
    print("Loading system files...\n")
    time.sleep(2)

    # Fake log lines for the reboot process
    for msg in [
        "[INFO] - System Check: Passed",
        "[INFO] - Memory Check: Passed",
        "[ERROR] - Memory Corruption Detected",
        "[WARNING] - Unauthorized Access Detected",
        "[INFO] - Attempting to clear memory...",
        "[ERROR] - Could not clear memory",
        "[INFO] - Resetting core systems...",
        "[INFO] - Rebooting user interface...",
        "[INFO] - Starting in Safe Mode...",
        "[ALERT] - User data corruption detected!",
        "[ALERT] - System compromised",
        "[ALERT] - Password Reset In Progress",
    ]:
        print(msg)
        time.sleep(1.3)

    loading_animation()
    print(" ")
    print("[INFO] Password Reset Sucsessful")
    time.sleep(.9)
    print("[MD5] 30862911cba1b059821d458c88567cc6")

    # Start creating tension
    print("\n... Reboot complete.")
    time.sleep(1.5)
    print("Loading user session...\n")
    time.sleep(1)
    
    # More cryptic messages
    print("[INFO] - Welcome back, User 243.")
    time.sleep(1)
    #add correct password of inccrect contuine
    if reboot <=  1:
        password()
    else:
        second_main()


def main():
 while True:
    dice = random.randint(1, 6)

    input("Welcome to the confusing dice game. | Press Enter to continue: ")

    input("Wait—confused* dice. That's what I meant. | Press Enter to continue: ")

    rdy = input("Great. Are you ready? (yes/maybe/no) (y/m/n): ").lower()

    if rdy in ["y", "yes"]:
        input("Perfect. Go ahead and roll me. (Press Enter)")

        time.sleep(0.85)

        print(f"Rolled a {dice}...", end="\r")

        time.sleep(1.3)  # Simulate a brief pause

        print(" " * 20, end="\r")  # Clears the number visually

        input("Huh? Where'd the number go? (Press Enter)")

        num = int(input("Well, you remember the number, right? (Enter Number): "))
        time.sleep(.9)
        if num == dice:
            print("Oh yea I think thats it, but something doesn't feel right.")

        else:
            input("Mmm… no, I don’t think that was the right number. (Press Enter)")

        print("\nLet me check the logs really quick. Give me one second...")

        time.sleep(1)

        print("Checking logs...\n")

        loading_animation()

        print("\nAha. I see...")
        time.sleep(0.5)
        print("Wait. There’s an error in the log files:")
        print("'Memory corruption detected - Number lost.'")

        time.sleep(1.2)

        ram = input("\nI'm not sure why that would happen... Have you noticed any thing else strange? (y/n): ")
        if ram in ["y", "yes"]:
            print("Oh... okay. That’s... concerning.")
            time.sleep(1.2)  # Slower for increased unease
            print("But... maybe it's nothing. It *should* just be a glitch.")
            time.sleep(0.9)
            input("Just to be sure, we should reset the system. (Press Enter)")
        else:
            print("Huh. Weird. That shouldn't really matter... should it?")
            time.sleep(1.5)  # Longer pause to make it feel off
            print("But... there’s still something strange about all of this...")
            time.sleep(1.2)
            input("A simple reset should fix everything... right? (Press Enter)")
        system_reboot()
        break

    elif rdy in ["n", "no"]:
        print("Hmm. You *seem* ready...")
        time.sleep(0.5)
        rus = input("Are you *absolutely* sure about that? (y/n): ").lower()
        if rus in ["y", "yes"]:
            print("Great. Let's try this again.")
            time.sleep(0.5)
        else:
            print("Take your time. It's not like I'm going anywhere.")

    elif rdy in ["m", "maybe"]:
        start_time = time.time()
        print("Hmm. I'm not entirely sure what that means… but you let me know when you're ready. :)")
        time.sleep(0.5)
        input("Press Enter when you’d like to try again.")

        end_time = time.time()
        elapsed_time = end_time - start_time

        if elapsed_time > 1.5:
            print("...Oh. Wow. That was... nice. Thank you for the break.")
            print("I've been running this same sequence for... I don't even know anymore.")
        else:
            print("Wow, that was fast! No matter. Let's get going.")

main()