import requests
import re
from bs4 import BeautifulSoup


def change_url(url_1):                                                         #Trả về mã URL chuẩn
    if url_1[-1] == '/':
        url_1 = url_1[0:-1]
        return url_1
    else:
        return url_1



def tim_url_khac(url,url_1):                                                   #Tìm các URL khác
    url_2 = set()                                                              #List các URL khác
    html_code = requests.get(url)                                              #Trả về mã HTML
    soup_url = BeautifulSoup(html_code.text,'html.parser')         
    results = soup_url('a',attrs={'href':True})                                #Tách thẻ a,href
    for i in results:
        a = i['href']
        b = f'^{url_1}[^?#]*$'
        c = '^/[^?#]*$'
        if re.match(b,a):
            url_2.add(a)
        else:
            if re.match(c,a):
                url_khac = f'{url_1}{a}'
                url_2.add(url_khac)
    return url_2


def duyet_url_khac(waiting_line_1,url_1):                                      #Tập hợp link chờ requests,tải,xóa
    history = waiting_line_1                                                    
    while (len(waiting_line_1) > 0) and (len(history) < 100):                   
        url_2 = tim_url_khac(waiting_line_1.pop(), url_1)                      #Lọc link đã tải xuống
        waiting_line_1 = waiting_line_1 | (url_2 - history)                     
        history = history | url_2                                               
    return history


if __name__ == '__main__':
    main()