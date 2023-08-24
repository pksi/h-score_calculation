import csv


def main():
    filename_list = "Autobahn_filenames.csv"
    with open(filename_list, newline="") as csvfile:
        filename = csv.DictReader(csvfile)
        for cell in filename:
            obj_data = str(cell["File Name"])
            print (obj_data)
            with open(obj_data, newline="") as new_csvfile:
                reader = csv.DictReader(new_csvfile)

                bin0_count = 0
                bin1_count = 0
                bin2_count = 0
                bin3_count = 0
                bin4_count = 0
                for data in reader:
                    if int(data["Fitc Classification"]) != 0 and int(data["spOrange Classification"]) == 0:
                        bin0_count += 0
                    if int(data["Fitc Classification"]) != 0 and int(data["spOrange Classification"]) == 1:
                        bin1_count += 1
                    if int(data["Fitc Classification"]) != 0 and int(data["spOrange Classification"]) == 2:
                        bin2_count += 2
                    if int(data["Fitc Classification"]) != 0 and int(data["spOrange Classification"]) == 3:
                        bin3_count += 1
                    if int(data["Fitc Classification"]) != 0 and int(data["spOrange Classification"]) == 4:
                        bin4_count += 1
            total_count = bin0_count+bin1_count+bin2_count+bin3_count+bin4_count

            percent_bin1 = bin1_count / total_count * 100
            percent_bin2 = bin2_count / total_count * 100
            percent_bin3 = bin3_count / total_count * 100
            percent_bin4 = bin4_count / total_count * 100

            H_score = percent_bin1 + percent_bin2*2 + percent_bin3*3 + percent_bin4*4
            print('H-Score:', H_score)

if __name__ == '__main__':
    main()
