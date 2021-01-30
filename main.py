import save_url
import check_url


def main():
    url_1 = input('Nhập link : ')
    url_1 = check_url.change_url(url_1)
    url_2 = check_url.tim_url_khac(url_1,url_1)
    waiting_line_2 = url_2
    history = check_url.duyet_url_khac(waiting_line_2,url_1)

    save_url.creat_folder('web_download')
    save_url.save_file(history)


if __name__ == '__main__':
    main()