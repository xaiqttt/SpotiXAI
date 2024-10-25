import os
import sys
import time
from termcolor import colored
from threading import Thread

def print_styled_title():
    title = """
       _       _   _   _
__  ____ _(_) __ _| |_| |_| |_
\\ \\/ / _` | |/ _` | __| __| __|
 >  < (_| | | (_| | |_| |_| |_
/_/\\_\\__,_|_|\\__, |\\__|\\__|\\__|
                |_|
    """
    subtitle = "A little Spotify Downloader"
    print(colored(title, "green"))
    print(colored(subtitle, "yellow", attrs=['bold']))
    print(colored("Made by xaiqttt (Darwin)", "cyan"))

def loading_animation():
    """Function to display a loading animation."""
    animation = ["|", "/", "-", "\\"]
    for _ in range(20):  # Adjust this range for longer loading
        for symbol in animation:
            sys.stdout.write(f"\r{colored('Downloading', 'cyan')} {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust the delay for speed of the animation

def download_album(url):
    print(colored(f"\nDownloading album from URL: {url}...", "cyan"))

    # Start loading animation in a separate thread
    loading_thread = Thread(target=loading_animation)
    loading_thread.start()
    
    # Actual download command using spotDL
    os.system(f"spotdl {url}")
    
    # Stop loading animation
    loading_thread.join()
    print(colored("\n-----------------------------------", "green"))

def main():
    while True:
        print_styled_title()
        album_url = input(colored("\nPlease enter the Spotify album URL: ", "yellow"))
        
        download_album(album_url)
        
        another = input(colored("\nDo you want to download another album? (yes/no): ", "yellow")).lower()
        if another != 'yes':
            print(colored("\nThank you for using SpotiXai!", "green"))
            break

if __name__ == "__main__":
    main()
