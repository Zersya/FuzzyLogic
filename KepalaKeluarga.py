class KepalaKeluarga:

    def __init__(self, no, pendapatan, hutang):
        self.no = no
        self.pendapatan = pendapatan
        self.hutang = hutang

        self.pendapatan_sangat_baik          = [1.6, 1.7, 1.8, 2]
        self.pendapatan_baik                 = [1.1, 1.4, 1.5, 1.7]
        self.pendapatan_biasa                = [0.8, 1, 1.5, 1.3]
        self.pendapatan_tidak_baik           = [0.3, 0.5, 0.7, 0.9]
        self.pendapatan_sangat_tidak_baik    = [0, 0.25, 0.35, 0.5]

        self.hutang_sangat_banyak          = [70, 78, 80, 100]
        self.hutang_banyak                 = [60, 66, 70, 74]
        self.hutang_sedang                = [50, 56, 58, 63]
        self.hutang_sedikit           = [30, 42, 47, 52]
        self.hutang_sangat_sedikit    = [0, 20, 28, 35]

        
    #region fungsi keanggotaan segitiga
    # def fungsi_anggota_pendapatan(self):
    #     input = self.pendapatan

    #     if input == self.pendapatan_sangat_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_SB = 1
    #     elif input <= self.pendapatan_sangat_baik[0] or input > self.pendapatan_sangat_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_SB = 0
    #     elif input >= self.pendapatan_sangat_baik[0] and input <= self.pendapatan_sangat_baik[1]:
    #         self.nilai_derajat_keanggotaan_pendapatan_SB = (input - self.pendapatan_sangat_baik[0])/(self.pendapatan_sangat_baik[1] - self.pendapatan_sangat_baik[0])
    #     elif input >= self.pendapatan_sangat_baik[1] and input <= self.pendapatan_sangat_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_SB = (self.pendapatan_sangat_baik[2] - input)/(self.pendapatan_sangat_baik[2] - self.pendapatan_sangat_baik[1])

    #     if input == self.pendapatan_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Baik = 1
    #     elif input <= self.pendapatan_baik[0] or input >= self.pendapatan_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Baik = 0
    #     elif input >= self.pendapatan_baik[0] and input <= self.pendapatan_baik[1]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Baik = (input-self.pendapatan_baik[0])/(self.pendapatan_baik[1] - self.pendapatan_baik[0])
    #     elif input >= self.pendapatan_baik[1] and input <= self.pendapatan_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Baik = (self.pendapatan_baik[2] - input)/(self.pendapatan_baik[2] - self.pendapatan_baik[1])
        
    #     if input == self.pendapatan_biasa[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Biasa = 1
    #     elif input <= self.pendapatan_biasa[0] or input >= self.pendapatan_biasa[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Biasa = 0
    #     elif input >= self.pendapatan_biasa[0] and input <= self.pendapatan_biasa[1]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Biasa = (input-self.pendapatan_biasa[0])/(self.pendapatan_biasa[1] - self.pendapatan_biasa[0])
    #     elif input >= self.pendapatan_biasa[1] and input <= self.pendapatan_biasa[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_Biasa = (self.pendapatan_biasa[2] - input)/(self.pendapatan_biasa[2] - self.pendapatan_biasa[1])
        
    #     if input == self.pendapatan_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_TB = 1
    #     elif input <= self.pendapatan_tidak_baik[0] or input >= self.pendapatan_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_TB = 0
    #     elif input >= self.pendapatan_tidak_baik[0] and input <= self.pendapatan_tidak_baik[1]:
    #         self.nilai_derajat_keanggotaan_pendapatan_TB = (input-self.pendapatan_tidak_baik[0])/(self.pendapatan_tidak_baik[1] - self.pendapatan_tidak_baik[0])
    #     elif input >= self.pendapatan_tidak_baik[1] and input <= self.pendapatan_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_TB = (self.pendapatan_tidak_baik[2] - input)/(self.pendapatan_tidak_baik[2] - self.pendapatan_tidak_baik[1])
       
    #     if input == self.pendapatan_sangat_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_STB = 1
    #     elif input <= self.pendapatan_sangat_tidak_baik[0] or input >= self.pendapatan_sangat_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_STB = 0
    #     elif input >= self.pendapatan_sangat_tidak_baik[0] and input <= self.pendapatan_sangat_tidak_baik[1]:
    #         self.nilai_derajat_keanggotaan_pendapatan_STB = (input-self.pendapatan_sangat_tidak_baik[0])/(self.pendapatan_sangat_tidak_baik[1] - self.pendapatan_sangat_tidak_baik[0])
    #     elif input >= self.pendapatan_sangat_tidak_baik[1] and input <= self.pendapatan_sangat_tidak_baik[2]:
    #         self.nilai_derajat_keanggotaan_pendapatan_STB = (self.pendapatan_sangat_tidak_baik[2] - input)/(self.pendapatan_sangat_tidak_baik[2] - self.pendapatan_sangat_tidak_baik[1])
    # def fungsi_anggota_hutang(self):
        # input = self.hutang

        # if input == self.hutang_sangat_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_SB = 1
        # elif input <= self.hutang_sangat_banyak[0] or input > self.hutang_sangat_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_SB = 0
        # elif input >= self.hutang_sangat_banyak[0] and input <= self.hutang_sangat_banyak[1]:
        #     self.nilai_derajat_keanggotaan_hutang_SB = (input - self.hutang_sangat_banyak[0])/(self.hutang_sangat_banyak[1] - self.hutang_sangat_banyak[0])
        # elif input >= self.hutang_sangat_banyak[1] and input <= self.hutang_sangat_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_SB = (self.hutang_sangat_banyak[2] - input)/(self.hutang_sangat_banyak[2] - self.hutang_sangat_banyak[1])

        # if input == self.hutang_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_banyak = 1
        # elif input <= self.hutang_banyak[0] or input >= self.hutang_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_banyak = 0
        # elif input >= self.hutang_banyak[0] and input <= self.hutang_banyak[1]:
        #     self.nilai_derajat_keanggotaan_hutang_banyak = (input-self.hutang_banyak[0])/(self.hutang_banyak[1] - self.hutang_banyak[0])
        # elif input >= self.hutang_banyak[1] and input <= self.hutang_banyak[2]:
        #     self.nilai_derajat_keanggotaan_hutang_banyak = (self.hutang_banyak[2] - input)/(self.hutang_banyak[2] - self.hutang_banyak[1])
        
        # if input == self.hutang_sedang[2]:
        #     self.nilai_derajat_keanggotaan_hutang_sedang = 1
        # elif input <= self.hutang_sedang[0] or input >= self.hutang_sedang[2]:
        #     self.nilai_derajat_keanggotaan_hutang_sedang = 0
        # elif input >= self.hutang_sedang[0] and input <= self.hutang_sedang[1]:
        #     self.nilai_derajat_keanggotaan_hutang_sedang = (input-self.hutang_sedang[0])/(self.hutang_sedang[1] - self.hutang_sedang[0])
        # elif input >= self.hutang_sedang[1] and input <= self.hutang_sedang[2]:
        #     self.nilai_derajat_keanggotaan_hutang_sedang = (self.hutang_sedang[2] - input)/(self.hutang_sedang[2] - self.hutang_sedang[1])
        
        # if input == self.hutang_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_TB = 1
        # elif input <= self.hutang_sedikit[0] or input >= self.hutang_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_TB = 0
        # elif input >= self.hutang_sedikit[0] and input <= self.hutang_sedikit[1]:
        #     self.nilai_derajat_keanggotaan_hutang_TB = (input-self.hutang_sedikit[0])/(self.hutang_sedikit[1] - self.hutang_sedikit[0])
        # elif input >= self.hutang_sedikit[1] and input <= self.hutang_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_TB = (self.hutang_sedikit[2] - input)/(self.hutang_sedikit[2] - self.hutang_sedikit[1])
       
        # if input == self.hutang_sangat_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_STB = 1
        # elif input <= self.hutang_sangat_sedikit[0] or input >= self.hutang_sangat_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_STB = 0
        # elif input >= self.hutang_sangat_sedikit[0] and input <= self.hutang_sangat_sedikit[1]:
        #     self.nilai_derajat_keanggotaan_hutang_STB = (input-self.hutang_sangat_sedikit[0])/(self.hutang_sangat_sedikit[1] - self.hutang_sangat_sedikit[0])
        # elif input >= self.hutang_sangat_sedikit[1] and input <= self.hutang_sangat_sedikit[2]:
        #     self.nilai_derajat_keanggotaan_hutang_STB = (self.hutang_sangat_sedikit[2] - input)/(self.hutang_sangat_sedikit[2] - self.hutang_sangat_sedikit[1])
    #endregion

    #region fungsi keanggotaan trapesium
    def fungsi_anggota_pendapatan(self):
        if self.pendapatan > self.pendapatan_sangat_baik[3] or self.pendapatan < self.pendapatan_sangat_baik[0]:
            self.nilai_derajat_keanggotaan_pendapatan_SB = 0
        elif self.pendapatan >= self.pendapatan_sangat_baik[0] and self.pendapatan <= self.pendapatan_sangat_baik[1]:
            self.nilai_derajat_keanggotaan_pendapatan_SB = (self.pendapatan - self.pendapatan_sangat_baik[0])/(self.pendapatan_sangat_baik[1] - self.pendapatan_sangat_baik[0])
        elif self.pendapatan >= self.pendapatan_sangat_baik[2] and self.pendapatan <= self.pendapatan_sangat_baik[3]:
            self.nilai_derajat_keanggotaan_pendapatan_SB = (self.pendapatan_sangat_baik[3] - self.pendapatan)/(self.pendapatan_sangat_baik[3] - self.pendapatan_sangat_baik[2])
        elif self.pendapatan >= self.pendapatan_sangat_baik[1] and self.pendapatan <= self.pendapatan_sangat_baik[2]:
            self.nilai_derajat_keanggotaan_pendapatan_SB = 1

        if self.pendapatan > self.pendapatan_baik[3] or self.pendapatan < self.pendapatan_baik[0]:
            self.nilai_derajat_keanggotaan_pendapatan_Baik = 0
        elif self.pendapatan >= self.pendapatan_baik[0] and self.pendapatan <= self.pendapatan_baik[1]:
            self.nilai_derajat_keanggotaan_pendapatan_Baik = (self.pendapatan - self.pendapatan_baik[0])/(self.pendapatan_baik[1] - self.pendapatan_baik[0])
        elif self.pendapatan >= self.pendapatan_baik[2] and self.pendapatan <= self.pendapatan_baik[3]:
            self.nilai_derajat_keanggotaan_pendapatan_Baik = (self.pendapatan_baik[3] - self.pendapatan)/(self.pendapatan_baik[3] - self.pendapatan_baik[2])
        elif self.pendapatan >= self.pendapatan_baik[1] and self.pendapatan <= self.pendapatan_baik[2]:
            self.nilai_derajat_keanggotaan_pendapatan_Baik = 1

        if self.pendapatan > self.pendapatan_biasa[3] or self.pendapatan < self.pendapatan_biasa[0]:
            self.nilai_derajat_keanggotaan_pendapatan_Biasa = 0
        elif self.pendapatan >= self.pendapatan_biasa[0] and self.pendapatan <= self.pendapatan_biasa[1]:
            self.nilai_derajat_keanggotaan_pendapatan_Biasa = (self.pendapatan - self.pendapatan_biasa[0])/(self.pendapatan_biasa[1] - self.pendapatan_biasa[0])
        elif self.pendapatan >= self.pendapatan_biasa[2] and self.pendapatan <= self.pendapatan_biasa[3]:
            self.nilai_derajat_keanggotaan_pendapatan_Biasa = (self.pendapatan_biasa[3] - self.pendapatan)/(self.pendapatan_biasa[3] - self.pendapatan_biasa[2])
        elif self.pendapatan >= self.pendapatan_biasa[1] and self.pendapatan <= self.pendapatan_biasa[2]:
            self.nilai_derajat_keanggotaan_pendapatan_Biasa = 1

        if self.pendapatan > self.pendapatan_tidak_baik[3] or self.pendapatan < self.pendapatan_tidak_baik[0]:
            self.nilai_derajat_keanggotaan_pendapatan_TB = 0
        elif self.pendapatan >= self.pendapatan_tidak_baik[0] and self.pendapatan <= self.pendapatan_tidak_baik[1]:
            self.nilai_derajat_keanggotaan_pendapatan_TB = (self.pendapatan - self.pendapatan_tidak_baik[0])/(self.pendapatan_tidak_baik[1] - self.pendapatan_tidak_baik[0])
        elif self.pendapatan >= self.pendapatan_tidak_baik[2] and self.pendapatan <= self.pendapatan_tidak_baik[3]:
            self.nilai_derajat_keanggotaan_pendapatan_TB = (self.pendapatan_tidak_baik[3] - self.pendapatan)/(self.pendapatan_tidak_baik[3] - self.pendapatan_tidak_baik[2])
        elif self.pendapatan >= self.pendapatan_tidak_baik[1] and self.pendapatan <= self.pendapatan_tidak_baik[2]:
            self.nilai_derajat_keanggotaan_pendapatan_TB = 1

        if self.pendapatan > self.pendapatan_sangat_tidak_baik[3] or self.pendapatan < self.pendapatan_sangat_tidak_baik[0]:
            self.nilai_derajat_keanggotaan_pendapatan_STB = 0
        elif self.pendapatan >= self.pendapatan_sangat_tidak_baik[0] and self.pendapatan <= self.pendapatan_sangat_tidak_baik[1]:
            self.nilai_derajat_keanggotaan_pendapatan_STB = (self.pendapatan - self.pendapatan_sangat_tidak_baik[0])/(self.pendapatan_sangat_tidak_baik[1] - self.pendapatan_sangat_tidak_baik[0])
        elif self.pendapatan >= self.pendapatan_sangat_tidak_baik[2] and self.pendapatan <= self.pendapatan_sangat_tidak_baik[3]:
            self.nilai_derajat_keanggotaan_pendapatan_STB = (self.pendapatan_sangat_tidak_baik[3] - self.pendapatan)/(self.pendapatan_sangat_tidak_baik[3] - self.pendapatan_sangat_tidak_baik[2])
        elif self.pendapatan >= self.pendapatan_sangat_tidak_baik[1] and self.pendapatan <= self.pendapatan_sangat_tidak_baik[2]:
            self.nilai_derajat_keanggotaan_pendapatan_STB = 1

    def fungsi_anggota_hutang(self):
        if self.hutang > self.hutang_sangat_banyak[3] or self.hutang < self.hutang_sangat_banyak[0]:
            self.nilai_derajat_keanggotaan_hutang_SB = 0
        elif self.hutang >= self.hutang_sangat_banyak[0] and self.hutang <= self.hutang_sangat_banyak[1]:
            self.nilai_derajat_keanggotaan_hutang_SB = (self.hutang - self.hutang_sangat_banyak[0])/(self.hutang_sangat_banyak[1] - self.hutang_sangat_banyak[0])
        elif self.hutang >= self.hutang_sangat_banyak[2] and self.hutang <= self.hutang_sangat_banyak[3]:
            self.nilai_derajat_keanggotaan_hutang_SB = (self.hutang_sangat_banyak[3] - self.hutang)/(self.hutang_sangat_banyak[3] - self.hutang_sangat_banyak[2])
        elif self.hutang >= self.hutang_sangat_banyak[1] and self.hutang <= self.hutang_sangat_banyak[2]:
            self.nilai_derajat_keanggotaan_hutang_SB = 1

        if self.hutang > self.hutang_banyak[3] or self.hutang < self.hutang_banyak[0]:
            self.nilai_derajat_keanggotaan_hutang_banyak = 0
        elif self.hutang >= self.hutang_banyak[0] and self.hutang <= self.hutang_banyak[1]:
            self.nilai_derajat_keanggotaan_hutang_banyak = (self.hutang - self.hutang_banyak[0])/(self.hutang_banyak[1] - self.hutang_banyak[0])
        elif self.hutang >= self.hutang_banyak[2] and self.hutang <= self.hutang_banyak[3]:
            self.nilai_derajat_keanggotaan_hutang_banyak = (self.hutang_banyak[3] - self.hutang)/(self.hutang_banyak[3] - self.hutang_banyak[2])
        elif self.hutang >= self.hutang_banyak[1] and self.hutang <= self.hutang_banyak[2]:
            self.nilai_derajat_keanggotaan_hutang_banyak = 1

        if self.hutang > self.hutang_sedang[3] or self.hutang < self.hutang_sedang[0]:
            self.nilai_derajat_keanggotaan_hutang_sedang = 0
        elif self.hutang >= self.hutang_sedang[0] and self.hutang <= self.hutang_sedang[1]:
            self.nilai_derajat_keanggotaan_hutang_sedang = (self.hutang - self.hutang_sedang[0])/(self.hutang_sedang[1] - self.hutang_sedang[0])
        elif self.hutang >= self.hutang_sedang[2] and self.hutang <= self.hutang_sedang[3]:
            self.nilai_derajat_keanggotaan_hutang_sedang = (self.hutang_sedang[3] - self.hutang)/(self.hutang_sedang[3] - self.hutang_sedang[2])
        elif self.hutang >= self.hutang_sedang[1] and self.hutang <= self.hutang_sedang[2]:
            self.nilai_derajat_keanggotaan_hutang_sedang = 1

        if self.hutang > self.hutang_sedikit[3] or self.hutang < self.hutang_sedikit[0]:
            self.nilai_derajat_keanggotaan_hutang_TB = 0
        elif self.hutang >= self.hutang_sedikit[0] and self.hutang <= self.hutang_sedikit[1]:
            self.nilai_derajat_keanggotaan_hutang_TB = (self.hutang - self.hutang_sedikit[0])/(self.hutang_sedikit[1] - self.hutang_sedikit[0])
        elif self.hutang >= self.hutang_sedikit[2] and self.hutang <= self.hutang_sedikit[3]:
            self.nilai_derajat_keanggotaan_hutang_TB = (self.hutang_sedikit[3] - self.hutang)/(self.hutang_sedikit[3] - self.hutang_sedikit[2])
        elif self.hutang >= self.hutang_sedikit[1] and self.hutang <= self.hutang_sedikit[2]:
            self.nilai_derajat_keanggotaan_hutang_TB = 1

        if self.hutang > self.hutang_sangat_sedikit[3] or self.hutang < self.hutang_sangat_sedikit[0]:
            self.nilai_derajat_keanggotaan_hutang_STB = 0
        elif self.hutang >= self.hutang_sangat_sedikit[0] and self.hutang <= self.hutang_sangat_sedikit[1]:
            self.nilai_derajat_keanggotaan_hutang_STB = (self.hutang - self.hutang_sangat_sedikit[0])/(self.hutang_sangat_sedikit[1] - self.hutang_sangat_sedikit[0])
        elif self.hutang >= self.hutang_sangat_sedikit[2] and self.hutang <= self.hutang_sangat_sedikit[3]:
            self.nilai_derajat_keanggotaan_hutang_STB = (self.hutang_sangat_sedikit[3] - self.hutang)/(self.hutang_sangat_sedikit[3] - self.hutang_sangat_sedikit[2])
        elif self.hutang >= self.hutang_sangat_sedikit[1] and self.hutang <= self.hutang_sangat_sedikit[2]:
            self.nilai_derajat_keanggotaan_hutang_STB = 1
    #endregion

    def inferensi(self):
        self.low = [0]
        self.med = [0]
        self.hig = [0]

        if self.nilai_derajat_keanggotaan_pendapatan_SB and self.nilai_derajat_keanggotaan_hutang_SB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_SB, self.nilai_derajat_keanggotaan_hutang_SB])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_SB and self.nilai_derajat_keanggotaan_hutang_banyak:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_SB, self.nilai_derajat_keanggotaan_hutang_banyak])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_SB and self.nilai_derajat_keanggotaan_hutang_sedang:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_SB, self.nilai_derajat_keanggotaan_hutang_sedang])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_SB and self.nilai_derajat_keanggotaan_hutang_TB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_SB, self.nilai_derajat_keanggotaan_hutang_TB])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_SB and self.nilai_derajat_keanggotaan_hutang_STB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_SB, self.nilai_derajat_keanggotaan_hutang_STB])
            self.low = []
            self.low.append(getminVal)

        if self.nilai_derajat_keanggotaan_pendapatan_Baik and self.nilai_derajat_keanggotaan_hutang_SB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Baik, self.nilai_derajat_keanggotaan_hutang_SB])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Baik and self.nilai_derajat_keanggotaan_hutang_banyak:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Baik, self.nilai_derajat_keanggotaan_hutang_banyak])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Baik and self.nilai_derajat_keanggotaan_hutang_sedang:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Baik, self.nilai_derajat_keanggotaan_hutang_sedang])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Baik and self.nilai_derajat_keanggotaan_hutang_TB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Baik, self.nilai_derajat_keanggotaan_hutang_TB])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Baik and self.nilai_derajat_keanggotaan_hutang_STB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Baik, self.nilai_derajat_keanggotaan_hutang_STB])
            self.low = []
            self.low.append(getminVal)

        if self.nilai_derajat_keanggotaan_pendapatan_Biasa and self.nilai_derajat_keanggotaan_hutang_SB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Biasa, self.nilai_derajat_keanggotaan_hutang_SB])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Biasa and self.nilai_derajat_keanggotaan_hutang_banyak:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Biasa, self.nilai_derajat_keanggotaan_hutang_banyak])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Biasa and self.nilai_derajat_keanggotaan_hutang_sedang:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Biasa, self.nilai_derajat_keanggotaan_hutang_sedang])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Biasa and self.nilai_derajat_keanggotaan_hutang_TB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Biasa, self.nilai_derajat_keanggotaan_hutang_TB])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_Biasa and self.nilai_derajat_keanggotaan_hutang_STB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_Biasa, self.nilai_derajat_keanggotaan_hutang_STB])
            self.low = []
            self.low.append(getminVal)

        if self.nilai_derajat_keanggotaan_pendapatan_TB and self.nilai_derajat_keanggotaan_hutang_SB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_TB, self.nilai_derajat_keanggotaan_hutang_SB])
            self.hig = []
            self.hig.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_TB and self.nilai_derajat_keanggotaan_hutang_banyak:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_TB, self.nilai_derajat_keanggotaan_hutang_banyak])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_TB and self.nilai_derajat_keanggotaan_hutang_sedang:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_TB, self.nilai_derajat_keanggotaan_hutang_sedang])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_TB and self.nilai_derajat_keanggotaan_hutang_TB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_TB, self.nilai_derajat_keanggotaan_hutang_TB])
            self.low = []
            self.low.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_TB and self.nilai_derajat_keanggotaan_hutang_STB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_TB, self.nilai_derajat_keanggotaan_hutang_STB])
            self.low = []
            self.low.append(getminVal)

        if self.nilai_derajat_keanggotaan_pendapatan_STB and self.nilai_derajat_keanggotaan_hutang_SB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_STB, self.nilai_derajat_keanggotaan_hutang_SB])
            self.hig = []
            self.hig.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_STB and self.nilai_derajat_keanggotaan_hutang_banyak:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_STB, self.nilai_derajat_keanggotaan_hutang_banyak])
            self.hig = []
            self.hig.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_STB and self.nilai_derajat_keanggotaan_hutang_sedang:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_STB, self.nilai_derajat_keanggotaan_hutang_sedang])
            self.hig = []
            self.hig.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_STB and self.nilai_derajat_keanggotaan_hutang_TB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_STB, self.nilai_derajat_keanggotaan_hutang_TB])
            self.med = []
            self.med.append(getminVal)
        if self.nilai_derajat_keanggotaan_pendapatan_STB and self.nilai_derajat_keanggotaan_hutang_STB:
            getminVal = min([self.nilai_derajat_keanggotaan_pendapatan_STB, self.nilai_derajat_keanggotaan_hutang_STB])
            self.low = []
            self.low.append(getminVal)
        
        if len(self.low) > 1:
            getmaxVal = max(self.low)
            self.low = []
            self.low[0] = getmaxVal
        if len(self.med) > 1:
            getmaxVal = max(self.med)
            self.med = []
            self.med[0] = getmaxVal
        if len(self.hig) > 1:
            getmaxVal = max(self.hig)
            self.hig = []
            self.hig[0] = getmaxVal

    #defuzzyfication
    def sugeno(self):
        k = [2, 10, 20]

        if(self.low[0] == 0 and self.med[0] == 0 and self.hig[0] == 0):
            return 0
        else:
            return ((k[0] * self.low[0]) + (k[1] * self.med[0]) + (k[2] * self.hig[0]))/(k[0] + k[1] + k[2])

    def defuzzyfication(self):
        y = self.sugeno()
        print(f'{self.no}, {y}')
        if y > 0.065:
            self.kelayakan = True
        else:
            self.kelayakan = False
