class BaiHat:
    def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.ten_nhac_si = ten_nhac_si
        self.ten_ca_si = ten_ca_si

class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = []

    def them_bai_hat(self, bai_hat):
        self.danh_sach_bai_hat.append(bai_hat)

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album):
        """
        Nhập toàn bộ thông tin của một album vào từ điển.
        """
        if ten_album not in self.albums:
            album_moi = Album(ten_album)
            self.albums[ten_album] = album_moi
        else:
            print(f"Album '{ten_album}' đã tồn tại trong từ điển.")

    def XemAlbum(self, ten_album):
        """
        Hiển thị toàn bộ thông tin của album có tên là 'ten_album'.
        """
        if ten_album in self.albums:
            album = self.albums[ten_album]
            print(f"Thông tin album '{ten_album}':")
            for bai_hat in album.danh_sach_bai_hat:
                print(f"Tên bài hát: {bai_hat.ten_bai_hat}")
                print(f"Tác giả: {bai_hat.ten_nhac_si}")
                print(f"Ca sĩ: {bai_hat.ten_ca_si}")
                print("----------------------")
        else:
            print(f"Album '{ten_album}' không tồn tại trong từ điển.")

# Sử dụng lớp TuDien để nhập và xem thông tin album
if __name__ == "__main__":
    td = TuDien()

    # Nhập thông tin album
    td.NhapAlbum("Album A")
    td.NhapAlbum("Album B")

    # Thêm các bài hát vào album
    td.albums["Album A"].them_bai_hat(BaiHat("Bài hát 1", "Nhạc sĩ A", "Ca sĩ X"))
    td.albums["Album A"].them_bai_hat(BaiHat("Bài hát 2", "Nhạc sĩ B", "Ca sĩ Y"))
    td.albums["Album B"].them_bai_hat(BaiHat("Bài hát 3", "Nhạc sĩ C", "Ca sĩ Z"))

    # Xem thông tin album
    ten_album_can_xem = input("Nhập tên album cần xem: ")
    td.XemAlbum(ten_album_can_xem)
# Input: Album A
"""Output: Thông tin album 'Album A':
Tên bài hát: Bài hát 1
Tác giả: Nhạc sĩ A
Ca sĩ: Ca sĩ X
----------------------
Tên bài hát: Bài hát 2
Tác giả: Nhạc sĩ B
Ca sĩ: Ca sĩ Y"""