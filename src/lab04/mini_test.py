from io_txt_csv import read_text, write_csv
txt = read_text("src/data/lab04/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "src/data/lab04/check.csv")  # создаст CSV
print('Файл создан')