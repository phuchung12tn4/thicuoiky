def Giaithua(n):
  if n == 0:
      return 1
  else:
      result = 1
      for i in range(1, n + 1):
          result *= i
      return result

def Neper(n):
  e = 0
  for k in range(n + 1):
      e += Giaithua(k)
  return e

n = int(input("Nhập vào số nguyên n ≥ 0: "))
print("Tổng của a0 + a1 + ... + an với n =", n, "là:", Neper(n))
