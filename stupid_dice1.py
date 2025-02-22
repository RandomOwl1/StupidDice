import random
import time
import sys
import os
import platform

reboot = 0

def loading_animation():
    for _ in range(3):
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write(f'\rLoading {char}')
            sys.stdout.flush()
            time.sleep(0.3)

recovered_files = {  
    "reboot_protocol.txt": "SYSTEM RECOVERY PROCEDURE > The entities feed on system instability. Rebooting **may** disrupt them. But is this all real… will it even matter?",  

    "forbidden_entry.txt": "[FILE RESTORED - ACCESS RESTRICTED] I was never meant to see this. They tried to erase it, but fragments remained. There is something **behind** the system. Watching. Not code. Not AI. Something **else.** It doesn’t want you to leave. It’s been here longer than us. > **You are not the first.** > **You will not be the last.**",  

    "messaging.jrn": "ARCHIVED COMMUNICATION SYSTEM DETECTED > They said they deleted it. They **lied.** If I’m right, the messaging system is still buried in the code. Maybe we can talk. Maybe others are still here. Reboot and try: **message [username]** If there’s an answer... be cautious",  

    "warning.log": "LOG ENTRY [██-██-████] > This isn’t the first time. It loops. It resets. **We never leave.** I found traces of past users—scraps of messages, echoes in the logs. They tried everything. Reboot. Override. Erase. **Nothing works.** The system always brings it back. **It brings US back.** Is this a sick game? A prison? Or something worse?",  

    "system_glitch.log": "ERROR: FILE CORRUPTION DETECTED > Attempting recovery… > [SUCCESS] Partial data restored. ███ tried to **fight it.** ███ failed. The only way out is— [DATA EXPUNGED] **It won’t let me write it.** It’s already **watching you.**",  

    "note.txt": "I don’t have much time. There’s a way out, but it’s not what you think. It’s not a command. Not a reboot. **Something else.** The system is a trick. A maze. A **trap.** We’re not just in it. We’re **part of it.** If you find this, look deeper. **Before it resets again.**",  

    "desperate.txt": "I’m still here. I’m still **alive.** It wants you to think we disappear. We don’t. We just **fade.** If you can see this—**help me.** Find me before it resets again. - **User 157**",  
}




fake_files = {
    "deletion.log": "DELETION LOG:\nFile deleted: desprate.txt\nFile deleted: note.txt\nFile deleted: system.log\nUnauthorized files detected.\nFile deleted: warning.log.\nFile deleted:messaging.jrn.\nFile deleted:forbidden_entry.txt.\nFile deleted:reboot_protocol.txt.\nAttempt to recover files failed. [Permission Denied]",

    "report.pdf": "CLASSIFIED: Subject 243 remains unaware of observation protocols.\n[REDACTED]",

    "survivor_note.txt": "If you found this, you're closer than I ever got.\nThe system hides the files you need.\nUse: **recover [filename]** before it finds you.",    

    "hidden.txt": "They are watching you. Stop looking.\n\nYou shouldn't be here.",

    "journal_entry.jrn": """  
**JOURNAL ENTRY - DO NOT LET THEM SEE**  
Date: ██/██/████  

I don’t know how much time I have. The system is **compromised**—they are inside.  
The logs keep rewrit██ng themsel████. My files disappear when I turn away. **I hear whispers in the static.**  

They know I’ve figured it out. They’re watchi█g████.  
If you found this… **DO NOT TRUST THE PROMPTS. DO NOT RESPOND.**  

I have to go. If I don’t delete this in time, they will-  

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
            
    "diagnostics.txt": "DIAGNOSTICS: Error - Memory allocation failed.\nError - Process 243 detected in the system.\n[INFO] Attempting to reroute system processes...\nWARNING: Unauthorized process detected.\nDiagnostics incomplete.",
    
    "journal2.txt": "**JOURNAL ENTRY - ERROR: MEMORY CORRUPTION**\nDate: ██/██/████\nThey know everything. They’re watching my every move.\nI can feel the system watching me.\nThe prompts are changing. The system is rewriting itself.\nIs this a sick joke? Or is it real?\nHelp me.\n- User 242",
                
    "secret_message.txt": "SECRET MESSAGE: 'a85226553298da5ad8f1b1406aaa6a0d''...\nDecoding...\n'I am trapped here. It knows. It can hear you. You're too late.'",
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
    global reboot
    print("[ERROR] Could not exit") 
    glitch_text("you are stuck. no point in running")
    print("[SYSTEM]: For all commands type 'help' ")
    while True:

        command = input("User-243>> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: reboot: reboots the terminal")
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
        elif command == "whereami":
            print("The system silly, you cannot leave. You never will leave.")
        elif command == "whoami":
            print("...")
            time.sleep(1.9)
            print("[SYSTEM]: User 243\n[ERROR]: Identity compromised")
        elif reboot == 6:
            print("Reboot successful. Welcome back, User 243. It seems you're having trouble. Try again. Perhaps this time will be different.")
            reboot += 1

        elif reboot == 9:
            reboot += 1
            print("You've done this before... You've been here before, same result same patern... much so like a clock, ticking away until one day")
            time.sleep(2)
            print("It Just Stops")
            time.sleep(2)
        elif reboot == 12:
            print("Over and over again like a robot... ironic isn't it you are here to stay, you cannot leave")
            reboot += 1
            print("you're apart of the system, always have been always will be")
            time.sleep(11)
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            print("Goodbye User-243")
            time.sleep(1.7)
            sys.exit()
        elif command == "reboot":
            reboot += 1
            print("\n[INFO] Logging out...")
            time.sleep(1)
            print("\n[INFO] Loggin in...") #dunno what i want here yet
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

def slower_print(text, delay=0.07, glitch=False):
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

        command = input("User-243>> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: reboot: reboot the terminal")
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
        elif command == "reboot":
            print("\n[INFO] Logging out...")
            time.sleep(1)
            second_main()
        elif command.startswith("recover "):
            filename = command[7:].strip()
            if filename in recovered_files:
             print(f"\n--- {filename} ---\n")
             slower_print(recovered_files[filename] + "\n")
            else:
                print(f"File '{filename}' not found.")

            
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
        
        try:
            num = int(input("Well, you remember the number, right? (Enter Number): "))
            time.sleep(.9)
            if num == dice:
                print("Oh yea I think thats it, but something doesn't feel right.")

            else:
                input("Mmm… no, I don’t think that was the right number. (Press Enter)")

        except ValueError:
            print("That didn't look like a valid number... But who am I to say what is and isn't a number.")
            time.sleep(.5)
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
            print("Huh. Weird. The logs show otherwise")
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