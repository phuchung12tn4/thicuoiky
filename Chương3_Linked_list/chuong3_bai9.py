class DaThuc:
    def __init__(self):
        self.head = None
        
    def Cong(self, dathuc2):
        result = DaThuc()
        current1 = self.head
        current2 = dathuc2.head

        while current1 != self.head and current2 != dathuc2.head:
            if current1.somu == current2.somu:
                heso_moi = current1.heso + current2.heso
                result.Them(heso_moi, current1.somu)
                current1 = current1.next
                current2 = current2.next
            elif current1.somu > current2.somu:
                result.Them(current1.heso, current1.somu)
                current1 = current1.next
            else:
                result.Them(current2.heso, current2.somu)
                current2 = current2.next

        while current1 != self.head:
            result.Them(current1.heso, current1.somu)
            current1 = current1.next

        while current2 != dathuc2.head:
            result.Them(current2.heso, current2.somu)
            current2 = current2.next

        result.RutGon()
        return result
