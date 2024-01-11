import os


def split_csv(input_file, output_folder, max_rows_per_file):
    with open(input_file, 'r') as csvFile:
        header = csvFile.readline()
        file_number = 1
        row_count = 0
        current_output_file = None

        for line in csvFile:
            if row_count % max_rows_per_file == 0:
                if current_output_file:
                    current_output_file.close()
                output_file_name = os.path.join(
                    output_folder, f'csvPart_{file_number}.csv')
                current_output_file = open(
                    output_file_name, 'w', newline='', encoding='utf-8')
                current_output_file.write(header)
                file_number += 1
            current_output_file.write(line)
            row_count += 1

        if current_output_file:
            current_output_file.close()


if __name__ == "__main__":
    input_file = input("Enter the file Path to the large CSV: ")
    output_folder = input("Enter the output folder for the smaller CSV ")
    max_rows_per_file = int(
        input("How many rows do you want in each CSV? (headers will always be row 1) "))

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    split_csv(input_file, output_folder, max_rows_per_file)
    print("CSV file successfully split into smaller files.")
