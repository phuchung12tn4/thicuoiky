def number(x, y):
  def tong_uoc_so(n):
      tong_uoc = 1  
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              tong_uoc += i
              if i != n // i: 
                  tong_uoc += n // i
      return tong_uoc

  for n in range(x, y + 1):
      s = tong_uoc_so(n)
      if s < n:
          print(f"{n} là số kém vì tổng của các ước của nó là {s} và nhỏ hơn {n}.")
      elif s == n:
          print(f"{n} là số hoàn hảo vì tổng của các ước của nó là {s} và bằng {n}.")
      else:
          print(f"{n} là số thặng vì tổng của các ước của nó là {s} và lớn hơn {n}.")

x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y: "))

number(x, y)
