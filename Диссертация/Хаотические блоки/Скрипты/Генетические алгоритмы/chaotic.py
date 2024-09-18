class chaotic():
    def __init__(self, Sbox):
        self.K = Sbox
        self.V = []
        self.K1 = []
        self.res = [0 for i in range(256)]
        self.mobius = [
            94, 30, 171, 84, 96, 215, 28, 246, 3, 216, 245, 255, 152, 86, 31, 180,
            118, 208, 184, 237, 204, 112, 185, 109, 183, 182, 76, 159, 19, 149, 44, 239,
            123, 173, 103, 12, 195, 154, 63, 244, 256, 188, 65, 130, 18, 194, 38, 72,
            162, 45, 78, 137, 119, 83, 165, 98, 27, 142, 249, 125, 100, 238, 120, 199,
            9, 7, 20, 200, 174, 42, 243, 136, 91, 102, 52, 139, 242, 117, 213, 59,
            60, 47, 232, 43, 145, 181, 114, 167, 229, 8, 150, 221, 172, 132, 23, 210,
            192, 231, 35, 69, 22, 115, 201, 151, 247, 193, 222, 39, 54, 178, 56, 85,
            138, 104, 214, 48, 107, 175, 240, 108, 16, 21, 17, 141, 62, 88, 74, 14,
            61, 248, 226, 144, 90, 95, 71, 202, 10, 81, 53, 163, 110, 254, 75, 32,
            11, 224, 101, 129, 177, 253, 111, 37, 24, 33, 140, 131, 113, 2, 155, 206,
            68, 197, 66, 147, 6, 79, 189, 25, 187, 49, 134, 5, 64, 146, 241, 70,
            217, 168, 124, 205, 158, 170, 143, 209, 207, 191, 223, 196, 15, 51, 50, 169,
            153, 73, 36, 160, 127, 219, 87, 122, 135, 55, 97, 41, 190, 233, 126, 157,
            13, 133, 121, 235, 1, 252, 93, 34, 251, 211, 212, 179, 92, 106, 67, 82,
            29, 99, 234, 148, 227, 176, 225, 203, 40, 198, 105, 220, 58, 4, 250, 166,
            186, 26, 218, 156, 161, 236, 164, 57, 128, 46, 89, 228, 230, 77, 116, 80
        ]
    
    def find_pos_min(self, f1, f2):
        length = len(f1)
        f = [f2 for i in range(length)]
        diff = [abs(f1[i] - f[i]) for i in range(length)]
        return diff.index(min(diff))

    def logisticFragment(self, yk, p):
        return p * yk * (1 - yk)

    def logistic(self, y0, p):
        map = [y0]
        for i in range(255):
            yk = self.logisticFragment(map[len(map) - 1], p)
            map.append(yk)

        return map
    
    def calc(self):
        i = 0
        x0 = 0.5
        x1 = 0.6

        k0 = 3.99234689
        k1 = 3.99777777

        f1 = self.logistic(x0, k0)
        y = self.logistic(x1, k1)

        while i < 255:
            pos_min = self.find_pos_min(f1, y[154])
            p = 0

            for j in range(len(self.V)):
                if pos_min == self.V[j]:
                    p = 1

            if p == 0:
                self.V.append(pos_min)
                self.K1.append(self.K[pos_min])
                x1 = 0.9 * x1 + 0.1 * self.K[pos_min]/255
                y = self.logistic(x1, k1)
                i = i + 1
            else:
                x0 = 0.9 * x0 + 0.1 * self.K[pos_min]/255
                f1 = self.logistic(x0, k0)

    def calcChaotic(self):
        self.calc()
        Km = [0 for i in range(256)]
        for i in range(0,256):
            if (i not in self.K1):
                self.K1.append(i)
                break

        for i in range (256):
            Km[self.mobius[i] - 1] = self.K1[i]

        for i in range(256):
            self.res[self.K[i] - 1] = Km[i]

        return self.res