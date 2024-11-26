import os

def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        print("Input file does not exist.")
        return False

    with open(path_reading, "r") as f:
        content = f.readlines()
    
    if not content:
        with open(path_writing, "w") as f_out:
            f_out.write("")  

    
    output_lines = ["Firstname,Lastname"]
    for line in content[1:]:
        line = line.strip()
        if not line:
            output_lines.append(",")
        elif ";" in line:
            last, first = line.split("; ")
            output_lines.append(f"{first},{last}")
        else:
            first, last = line.split(" ")
            output_lines.append(f"{first},{last}")

    
    with open(path_writing, "w") as f_out:
        f_out.write("\n".join(output_lines))

INPUT_PATH = r"C:\Users\Abraham Herzog\INF1\Assignments\Week10\Task1\my_data.txt"
OUTPUT_PATH = r"C:\Users\Abraham Herzog\INF1\Assignments\Week10\Task1\output_file.csv"

process_data(INPUT_PATH, OUTPUT_PATH)

if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH, "r") as resultfile:
        print(resultfile.read())
else:
    print("No output file exists.")
