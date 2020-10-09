import requests
from fake_useragent import FakeUserAgent

cookies = 'anonymid=kg1kkuxosc1qxt; depovince=GW; jebecookies=a3f052d0-5b3b-440c-bfbd-12886ecd5d29|||||; _r01_=1; taihe_bi_sdk_uid=7925eec3b25f0c3ad8759bbb7c0aa470; taihe_bi_sdk_session=d71452c21dfb360e8d799af7867a718d; ick_login=95759bfc-de05-498b-9f20-a0feb9b3bfb5; _de=C70150869B4894BBB68784D5AEB12133; p=4254ff40548e2919d1810cc9b60eb5819; first_login_flag=1; ln_uact=19834406344; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=0d5f63e10dd952a94e758120a2d917929; societyguester=0d5f63e10dd952a94e758120a2d917929; id=974245919; xnsid=f507719c; ver=7.0; loginfrom=null; wpsid=15889675082855; wp_fold=0'

headers = {
    "User-Agent": FakeUserAgent().chrome,
    "Cookie": cookies

}
url = 'http://www.renren.com/974245919/profile'
req = requests.get(url, headers=headers)
print(req.text)
html_content = req.text
with open("renren.txt", 'w', encoding='utf-8') as f:
    f.write(html_content)
