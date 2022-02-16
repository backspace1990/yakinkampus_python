import os
#os.O_RDONLY  # -- Read only      -- Sadece oku
#os.O_WRONLY  # -- Write Only     -- Sadece yaz
#os.O_RDWR    # -- Read and Write -- Oku ve yaz
#os.O_CREAT   # -- Create          -- Olustur

new_txt = os.open("new.txt", os.O_RDWR | os.O_CREAT)
os.write(new_txt, "Hello World!".encode())
os.write(new_txt, "\nI am Umit!".encode())
os.close(new_txt)

new_txt = os.open("new.txt", os.O_RDONLY)
print(os.read(new_txt, 22))
print(new_txt.bit_length())
os.close(new_txt)

print(50 * "&")

#static info file
new_txt = os.open("new.txt", os.O_RDONLY)
print(os.stat(new_txt))
print(os.stat(new_txt).st_size)
print(os.read(new_txt, os.stat(new_txt).st_size))
os.close(new_txt)

#os.unlink("new.txt") # olusturulan dosya silinir
#os.rename("new.txt","news.txt")