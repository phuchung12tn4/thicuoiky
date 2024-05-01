class DaThuc:
    def __init__(self):
        self.head = None
        
    def Tich(self, dathuc2):
        result = DaThuc()
        current1 = self.head
        while current1 != self.head:
            current2 = dathuc2.head
            while current2 != dathuc2.head:
                heso_moi = current1.heso * current2.heso
                somu_moi = current1.somu + current2.somu
                result.Them(heso_moi, somu_moi)
                current2 = current2.next
            current1 = current1.next
        result.RutGon()
        return result
