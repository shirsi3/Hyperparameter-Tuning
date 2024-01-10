import os
import hashlib


benign_folder = "/home/shirsi/Lab2_Malware/benignware"
malware_folder = "/home/shirsi/Lab2_Malware/malware"


samples_directory = "/home/shirsi/samples"


output_file = "sample_hashes_labels.txt"


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


with open(output_file, "w") as outfile:
    for filename in os.listdir(samples_directory):
        file_path = os.path.join(samples_directory, filename)
        if os.path.isfile(file_path):
            
            if filename in os.listdir(benign_folder):
                label = "benign"
            elif filename in os.listdir(malware_folder):
                label = "malware"
            else:
                label = "unknown"  

            
            md5_hash = calculate_md5(file_path)
            
            
            outfile.write(f"{md5_hash}\t{label}\n")
            
           
            print(f"Processed: {filename}, Label: {label}")

print("MD5 hashes and labels have been written to the output file.")
