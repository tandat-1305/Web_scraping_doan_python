import requests
import codecs
import os


def creat_folder(name):
    os.mkdir(name)
    os.chdir(name)


#Đánh stt,lưu file
def luu_file(url, stt):                                       
    file = codecs.open('file' + 
                       str(stt) + 
                       '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


#Lưu, lọc URL hợp lệ vào list
def save_file(history):                                      
    for (stt, url_con) in enumerate(history):
        luu_file(url_con, stt)
        print(f'{stt} {url_con}')


if __name__ == "__main__":
    main()