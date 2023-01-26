import os

def merge_txt_files(dir_path, output_file):
    with open(output_file, 'w') as outfile:
        for subdir, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(subdir, file), 'r') as f:
                        outfile.write(f.read())

merge_txt_files('/home/lamda/Desktop/Avd/trojai-master/Dronet/dronet_original', 'path/to/output/file.txt')

