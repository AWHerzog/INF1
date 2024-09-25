import os
import tkinter as tk
from tkinter import filedialog

def pdforganiser():
    
    root = tk.Tk()
    root.withdraw() 

    
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    
    if not pdf_path:
        print("No file selected!")
        return

    # Get user inputs
    Studienjahr = input("Studienjahr: ")
    datum = input("Datum: ")
    Uhrzeit = input("Uhrzeit: ")
    Themenblock = input("Themenblock: ")
    Titel = input("Titel: ")
    Prof = input("Professor: ")

    # Create the new filename from user input
    formatted_string = f'{Studienjahr}_{datum}_{Uhrzeit}_{Themenblock}_{Prof}_{Titel}.pdf'

    # Get the directory and new full path for the renamed PDF
    directory = os.path.dirname(pdf_path)  # Extract the directory path
    new_pdf_path = os.path.join(directory, formatted_string)  # Create the new full file path

    # Rename the PDF file
    try:
        os.rename(pdf_path, new_pdf_path)  # Rename the file
        print(f"File has been renamed to: {new_pdf_path}")
    except FileNotFoundError:
        print("The specified PDF file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return new_pdf_path

# Call the function
pdforganiser()
