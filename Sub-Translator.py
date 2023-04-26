import os
from googletrans import Translator

# Define file paths and names
file_path = r"C:\Users\Amirh\Desktop"
file_name1 = "Rick.and.Morty.S06E03.720p.WEBRip.x264-BAE.srt"
file_name2 = "Rick.and.Morty.S06E03.720p.WEBRip.x264-BAE.srt"

# Define a list of numbers to identify subtitle lines (if needed)
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Initialize the translator object
translator = Translator()

# Read the original subtitle file
with open(os.path.join(file_path, file_name1)) as subtitle_file:
    # Get all the subtitle lines
    subtitle_lines = subtitle_file.readlines()

# Open the output file for writing translated subtitles
with open(os.path.join(file_path, file_name2), "w", encoding="utf-8") as output_file:
    for line in subtitle_lines:
        # If the first character of the line is a number, write it as is
        if line[0] in nums:
            output_file.write(line)
        # If the line is empty, write a new line character
        elif line == "\n":
            output_file.write("\n")
        else:
            # Translate the rest of the lines from English to Persian
            if line:
                # If the line is not empty, translate it using the Google Translate API.
                translated_line = translator.translate(line, src="en", dest="fa")
                if "gt;" in translated_line.text:
                    # If "gt;" appears in the translation, remove it.
                    corrected_line = translated_line.replace("gt;", "")
                    output_file.write(corrected_line.text + "\n")
                else:
                    # Otherwise, write the translated line to the output file followed by a new line character.
                    output_file.write(translated_line.text + "\n")
    # Write a new line character after the last subtitle line
    output_file.write("\n")
