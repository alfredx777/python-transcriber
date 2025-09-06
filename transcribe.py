import whisper
import os
from tkinter import Tk, filedialog
import warnings

# Suppress CPU FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Load model
model = whisper.load_model("base")

# File dialog
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select an audio file",
    filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")]
)

if file_path:
    print("Transcribing... please wait.")
    result = model.transcribe(file_path, verbose=False)
    transcript = result["text"]

    # --- Save transcript ---
    # Get audio file name without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    transcript_name = f"{base_name}_transcript.txt"

    # Create "transcripts" folder if not exists
    output_dir = os.path.join(os.path.dirname(__file__), "transcripts")
    os.makedirs(output_dir, exist_ok=True)

    # Save file
    output_path = os.path.join(output_dir, transcript_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print("\n--- Transcript Complete ---")
    print(f"Saved to: {output_path}")
else:
    print("No file selected.")
