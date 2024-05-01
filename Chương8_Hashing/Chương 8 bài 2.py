class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, tranghia=None):
        """
        Nhập một từ và các từ đồng nghĩa, từ trái nghĩa (nếu có) vào từ điển.
        Hàm băm lấy ký tự đầu tiên của từ để sử dụng làm key.
        """
        first_char = tu[0].lower()
        
        # Kiểm tra xem key (ký tự đầu tiên của từ) có trong từ điển chưa
        if first_char not in self.dictionary:
            # Nếu chưa có, thêm key và giá trị là một dictionary chứa thông tin từ và các từ đồng nghĩa, trái nghĩa
            self.dictionary[first_char] = {'tu': tu, 'dongnghia': [], 'tranghia': []}
        
        # Truy cập vào entry của từ trong từ điển
        entry = self.dictionary[first_char]
        
        # Nếu có từ đồng nghĩa, thêm vào danh sách đồng nghĩa của từ
        if dongnghia:
            entry['dongnghia'].append(dongnghia)
        
        # Nếu có từ trái nghĩa, thêm vào danh sách trái nghĩa của từ
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

# Sử dụng lớp TuDien để thực hiện nhập từ và tra cứu từ điển
if __name__ == "__main__":
    # Tạo đối tượng từ điển
    td = TuDien()
    
    # Nhập từ và các từ đồng nghĩa, trái nghĩa vào từ điển
    td.NhapTu('mèo', 'con mèo', 'chó')
    td.NhapTu('chó', 'con chó', 'mèo')
    
    # Nhập từ cần tra từ bàn phím
    tu_can_tra = input("Nhập từ cần tra trong từ điển: ")
    
    # Tra cứu từ điển và in kết quả
    dong_nghia = td.DongNghia(tu_can_tra)
    trai_nghia = td.TraiNghia(tu_can_tra)
    
    print(f'Các từ đồng nghĩa của "{tu_can_tra}" là: {dong_nghia}')
    print(f'Các từ trái nghĩa của "{tu_can_tra}" là: {trai_nghia}')
