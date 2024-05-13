tu_dien = []  # Mảng cục bộ lưu các từ để thực hiện các thao tác nhập, xóa, tìm kiếm, lưu từ điển và nạp từ điển

# Hàm nhập từ (kiểm tra lỗi và sử dụng append để thêm vào mảng cục bộ)
def Nhap_tu():
      global tu_dien
      while True:
          try:
              num_words = int(input('Enter the number of words you want to enter: '))
              if num_words <= 0:
                  print('The number of words must be a positive integer. Please re-enter.')
              else:
                  break
          except ValueError:
              print('This is not a positive integer. Please re-enter.')

      for _ in range(num_words):
          word = ''
          while True:
              word = input('Enter word (type "esc" to stop entering): ')
              if word.lower() == 'esc':
                  print('Exiting input.')
                  break
              elif all(item == ' ' or item.isalpha() for item in word):
                  break
              else:
                  print('These are not valid words. Please re-enter.')

          if word.lower() == 'esc':
              break

          word_type = ''
          while True:
              word_type = input('Enter word type (type "esc" to stop entering): ')
              if word_type.lower() == 'esc':
                  print('Exiting input.')
                  break
              elif all(item == ' ' or item.isalpha() for item in word_type):
                  break
              else:
                  print('This is not a valid word type. Please re-enter.')

          if word_type.lower() == 'esc':
              break

          meaning = input('Enter meaning: ')
          example = input('Enter example: ')

          tu_dien.append((word, [(word_type, meaning, example)]))
          print(f"The word '{word}' has been added to the dictionary.")

      return tu_dien

# Hàm xóa từ (Dùng remove để xóa khỏi mảng)
def Xoa_tu(tu_dien):
        word_to_delete = input('Enter the word to delete: ')
        for entry in tu_dien:
            if entry[0] == word_to_delete:
                tu_dien.remove(entry)
                print(f'Removed the word "{word_to_delete}" from the dictionary.')
                return
        print(f'The word "{word_to_delete}" was not found in the dictionary.')

# Hàm tra cứu (Dùng for để quét qua mảng nếu tìm được thì in từ đó và các thành phần của nó)
def Tra_cuu(tu_dien):
      word_to_lookup = input('Enter the word to find: ').lower()  # Convert to lowercase
      found = False
      for entry in tu_dien:
          if entry[0].lower() == word_to_lookup:
              found = True
              print(f'"{entry[0]}":')
              for meaning in entry[1]:
                  print(f' - Word type: {meaning[0]}')
                  print(f'   Definition: {meaning[1]}')
                  print(f'   Example: {meaning[2]}')
              break

      if not found:
          print(f'The word "{word_to_lookup}" was not found in the dictionary.')

# Hàm lưu từ điển (Sau khi chọn chức này và nhập 1 tên file txt bất kì nó sẽ tạo 1 file mới có toàn bộ những từ đang có trong mảng cục bộ bấy giờ)
def Luu_tu_dien(tu_dien, file_name):
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                for entry in tu_dien:
                    f.write(f'{entry[0]}:\n')
                    for meaning in entry[1]:
                        f.write(f' - Word type: {meaning[0]}\n')
                        f.write(f'   Definition: {meaning[1]}\n')
                        f.write(f'   Example: {meaning[2]}\n')
                    f.write('\n')
            print(f'Dictionary has been saved to the file "{file_name}".')
        except FileExistsError:
            print(f'File "{file_name}" already exists.')
        except Exception as e:
            print(f'Error when saving the file "{file_name}": {e}')

# Hàm nạp từ điển(Sau khi chọn và nhập tên 1 file txt có sẵn ví dụ "dictionary_animal.txt" hàm sẽ nạp toàn bộ từ trong file này vào mảng cục bộ để thực hiện các chức năng)
def Nap_tu_dien(file_name):
    global tu_dien
    tu_dien = [] 
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line != '':  
                    word = line.rstrip(':')  
                    meanings = []
                    i += 1
                    while i < len(lines) and lines[i].strip() != '':
                        parts = lines[i].strip().split(': ')
                        if len(parts) >= 2:  
                            if parts[0] == '- Word type':
                                word_type = parts[1]
                            elif parts[0] == 'Definition':
                                definition = parts[1]
                            elif parts[0] == 'Example':
                                example = parts[1]
                        i += 1
                    tu_dien.append((word, [(word_type, definition, example)]))

                i += 1

        print(f'Dictionary has been loaded from the file "{file_name}".')
    except FileNotFoundError:
        print(f'Error: Path or file "{file_name}" not found.')
    except Exception as e:
        print(f'Error when loading the dictionary from file "{file_name}": {e}')



# Hàm main (có 5 chức năng từ 1-5 và 0 nếu muốn exit)
def main():
        global tu_dien
        while True:
            print('DICTIONARY PROGRAM'.center(50, '*'))
            print('1. Add a new word to the dictionary')
            print('2. Remove a word from the dictionary')
            print('3. Look up meanings of a word in the dictionary')
            print('4. Save the dictionary to a file')
            print('5. Load the dictionary from a file')
            print('0. Exit the program')

            choice = input('Enter your choice (0-5): ')

            if choice == '1':
                Nhap_tu()
            elif choice == '2':
                Xoa_tu(tu_dien)
            elif choice == '3':
                Tra_cuu(tu_dien)
            elif choice == '4':
                file_name = input('Enter file name to save the dictionary: ')
                Luu_tu_dien(tu_dien, file_name)
            elif choice == '5':
                file_name = input('Enter file name to load the dictionary: ')
                Nap_tu_dien(file_name)
            elif choice == '6':
                print(tu_dien)
            elif choice == '0':
                print('Exiting the program.')
                break
            else:
                print('Invalid choice. Please try again.')

if __name__ == '__main__':
        main()
