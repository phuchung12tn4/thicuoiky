class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, tranghia=None):
        """
        Nhập một từ và các từ đồng nghĩa, từ trái nghĩa (nếu có) vào từ điển.
        Hàm băm lấy ký tự đầu tiên của từ để sử dụng làm key.
        """
        first_char = tu[0].lower()
        if first_char not in self.dictionary:
            self.dictionary[first_char] = {'tu': tu, 'dongnghia': [], 'tranghia': []}

        entry = self.dictionary[first_char]
        if dongnghia:
            entry['dongnghia'].append(dongnghia)
        if tranghia:
            entry['tranghia'].append(tranghia)

    def DongNghia(self, tu):
        """
        Trả về một mảng chứa các từ đồng nghĩa của từ cần tra.
        """
        first_char = tu[0].lower()
        if first_char in self.dictionary:
            return self.dictionary[first_char]['dongnghia']
        else:
            return []

    def TraiNghia(self, tu):
        """
        Trả về một mảng chứa các từ trái nghĩa của từ cần tra.
        """
        first_char = tu[0].lower()
        if first_char in self.dictionary:
            return self.dictionary[first_char]['tranghia']
        else:
            return []

# Sử dụng lớp TuDien
td = TuDien()

# Nhập các từ vào từ điển
td.NhapTu('mèo', 'con mèo', 'chó')
td.NhapTu('chó', 'con chó', 'mèo')

# Nhập từ cần tra từ bàn phím
tu_can_tra = input("Nhập từ cần tra trong từ điển tiếng Việt: ")

# Tra cứu từ điển
dong_nghia = td.DongNghia(tu_can_tra)
trai_nghia = td.TraiNghia(tu_can_tra)

print(f'Các từ đồng nghĩa của "{tu_can_tra}" là: {dong_nghia}')
print(f'Các từ trái nghĩa của "{tu_can_tra}" là: {trai_nghia}')
