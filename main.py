import csv
from KepalaKeluarga import KepalaKeluarga

kepalaKeluargas = []


def csv_reader():
    with open("3218_17748_DataTugas2.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                kepalaKeluargas.append(KepalaKeluarga(row[0], float(row[1].replace(" ", "")), float(row[2].replace(" ", ""))))
                line_count += 1

def csv_writer():
    with open('TebakanTugas2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['no', 'pendapatan', 'hutang'])
        for kk in kepalaKeluargas:
            if kk.kelayakan:
                writer.writerow([kk.no, kk.pendapatan, kk.hutang])

def main():
    csv_reader()

    for kk in kepalaKeluargas:
        kk.fungsi_anggota_pendapatan()
        kk.fungsi_anggota_hutang()
        kk.inferensi()
        kk.defuzzyfication()
        # counter_kk += 1
        # kk.fuzzy_rules()
        # print(f'\t{kk.no} \tPendapatan : \t{kk.nilai_derajat_keanggotaan_pendapatan_SB, kk.nilai_derajat_keanggotaan_pendapatan_Baik, kk.nilai_derajat_keanggotaan_pendapatan_Biasa, kk.nilai_derajat_keanggotaan_pendapatan_TB, kk.nilai_derajat_keanggotaan_pendapatan_STB}')
        # print(f'\t{kk.no} \tHutang : \t{kk.nilai_derajat_keanggotaan_hutang_SB, kk.nilai_derajat_keanggotaan_hutang_banyak, kk.nilai_derajat_keanggotaan_hutang_sedang, kk.nilai_derajat_keanggotaan_hutang_TB, kk.nilai_derajat_keanggotaan_hutang_STB}')
        # print(f'\t{kk.no} \t\t\t{kk.kelayakan}')
            

    csv_writer()
    print("Done processs")
if __name__ == "__main__":
    main()
    # print(max([2,1]))