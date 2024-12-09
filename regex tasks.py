import re
#%%
text = "Контакты: fw.ww@example.com, info@mail.ru и sup@company.org. mian@yandex.ru, sjsd@ma.s.ru"
#text = text.split()
#%%
email_list = re.findall(r'\b[a-zA-Z]+\S\w+@[\w+\.\w+.]+\b', text)
print(email_list)
#%%
text_2 = """
Посетите наши сайты: https://example.com, http://site.org, www.website.ru, ftp://ftp.server.com, https://sub.domain.com, 
http://localhost:8000, https://192.168.0.1, http://10.0.0.1:5000, https://shop.example.net/products?id=12345, 
http://news.site.net/article#top, https://longurl.example.com/path/to/page?query=abc, https://business.site.com, 
http://cdn.site.org/images, www.blog.com, www.news.org, www.portal.co.uk, ftp://download.server.org/file, 
https://backup.server.io, https://wiki.site.net, http://dev.local, https://shop.site.org/cart?id=6789&ref=promo, 
http://files.site.com/download.php, https://update.site.com, www.support.com, https://secure.site.org/login, 
http://beta.site.net/version, ftp://files.site.ru/upload, https://music.site.com/track/123, www.moviesite.com/watch, 
https://bank.example.com/transfer?id=98765.
"""
#%%
url_list = re.findall(r'\b[htpsfw]+(?=\W{1,3})[/:\.]+[\w+.+]+[\w+\S+\d+]+\b', text_2)
print(url_list)
#%%
text_3 = "Дата рождения: 17-05/1995. Выпускной: 30/06.2013. Следующая встреча 09//09/2025."
text_3 = re.sub(r'(\d\d)\S{,2}(\d\d)\S(\d{4})', r'\1-\2-\3', text_3)
print(text_3)