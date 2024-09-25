import os
import tkinter as tk
from tkinter import filedialog, messagebox

def pdforganiser():
    # Create a root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select the PDF
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    
    if not pdf_path:
        messagebox.showwarning("Warning", "No file selected!")
        return

    # Define a new window for inputs
    input_window = tk.Tk()
    input_window.title("Enter PDF Details")
    
    # Create and organize input fields
    tk.Label(input_window, text="Studienjahr").grid(row=0)
    tk.Label(input_window, text="Datum").grid(row=1)
    tk.Label(input_window, text="Uhrzeit").grid(row=2)
    tk.Label(input_window, text="Themenblock").grid(row=3)
    tk.Label(input_window, text="Titel").grid(row=4)
    tk.Label(input_window, text="Professor").grid(row=5)

    studienjahr_entry = tk.Entry(input_window)
    datum_entry = tk.Entry(input_window)
    uhrzeit_entry = tk.Entry(input_window)
    themenblock_entry = tk.Entry(input_window)
    titel_entry = tk.Entry(input_window)
    prof_entry = tk.Entry(input_window)

    # Place the input fields
    studienjahr_entry.grid(row=0, column=1)
    datum_entry.grid(row=1, column=1)
    uhrzeit_entry.grid(row=2, column=1)
    themenblock_entry.grid(row=3, column=1)
    titel_entry.grid(row=4, column=1)
    prof_entry.grid(row=5, column=1)

    # Function to process inputs
    def process_inputs():
        # Get user inputs from the GUI fields
        studienjahr = studienjahr_entry.get()
        datum = datum_entry.get()
        uhrzeit = uhrzeit_entry.get()
        themenblock = themenblock_entry.get()
        titel = titel_entry.get()
        prof = prof_entry.get()

        # Validate inputs
        if not (studienjahr and datum and uhrzeit and themenblock and titel and prof):
            messagebox.showwarning("Warning", "All fields must be filled!")
            return

        # Format the new filename
        formatted_string = f'{studienjahr}_{datum}_{uhrzeit}_{themenblock}_{prof}_{titel}.pdf'

        # Get the directory and new full path for the renamed PDF
        directory = os.path.dirname(pdf_path)
        new_pdf_path = os.path.join(directory, formatted_string)

        # Rename the PDF file
        try:
            os.rename(pdf_path, new_pdf_path)
            messagebox.showinfo("Success", f"File has been renamed to: {new_pdf_path}")
            input_window.destroy()  # Close the window after renaming
        except FileNotFoundError:
            messagebox.showerror("Error", "The specified PDF file was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Create a button to submit inputs
    tk.Button(input_window, text='Submit', command=process_inputs).grid(row=6, column=1)

    input_window.mainloop()

# Call the function
pdforganiser()
