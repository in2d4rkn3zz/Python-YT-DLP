import tkinter as tk
import subprocess
import pyperclip

# Funktion zum Ausführen des youtube-dl-Befehls
def download_video():
    # Link aus der Zwischenablage holen
    clipboard_content = pyperclip.paste()

    if clipboard_content:
        # Youtube-dl Befehl mit dem Link aus der Zwischenablage
        command = [
            "yt-dlp",
            "-f", 
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", 
            clipboard_content
        ]
        # Führe den Befehl aus und gib das Ergebnis aus
        try:
            subprocess.run(command, check=True)
            output_label.config(text="Download erfolgreich!")
        except subprocess.CalledProcessError as e:
            output_label.config(text=f"Fehler: {e}")
    else:
        output_label.config(text="Keine URL in der Zwischenablage gefunden.")

# GUI erstellen
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")

# Beschreibungstext
label = tk.Label(root, text="Drücke auf 'Download', um das Video herunterzuladen:")
label.pack(pady=10)

# Button zum Starten des Downloads
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Label für Ausgabe/Nachricht
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# GUI starten
root.mainloop()
