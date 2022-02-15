web_driver_path = "C:/Users/sharnaga/WORK/sel/chromedriver.exe"
main_url = "https://www.flaconi.de/"

web_ele_path_for_makeup_menu = ["//a[contains(@class,'Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse')][normalize-space()='Teint']",
                "//a[@class='Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse'][normalize-space()='Augen']",
                "//a[@class='Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse'][normalize-space()='Lippen']",
                "//a[@class='Navigationstyle__CategoryLink-sc-1r9fvyg-8 jQNSse'][normalize-space()='Nägel']",
                "//a[@data-track-id='top.subnav.Make-up_Top Marken']",
                "//a[@data-track-id='top.subnav.Make-up_Specials']"]
web_ele_path_for_main_menu = ["//a[@data-track-id='top.nav.Marken']",
                              "//a[@data-track-id='top.nav.Parfum']",
                              "//a[@data-track-id='top.nav.Pflege']",
                              "//a[@data-track-id='top.nav.Make-up']",
                              "//a[@data-track-id='top.nav.Haare']",
                              "//a[@data-track-id='top.nav.Natur']",
                              "//a[@data-track-id='top.nav.Premium']",
                              "//a[@data-track-id='top.nav.Drogerie']",
                              "//a[normalize-space()='Neu']",
                              "//a[normalize-space()='Magazin']",
                              "//a[normalize-space()='Sale']",
                              "//a[normalize-space()='Gratis']"]

accept_cookies = "#usercentrics-root"
accept_cookies_cls = ".sc-gsDKAQ.kYPcOR"
makeup_menu = "//a[@data-track-id='top.nav.Make-up']"

expected_message = "Es tut uns Leid! Der Gutscheincode ist nicht verfügbar."

perfume = "//a[@class='Navigationstyle__MenuLink-sc-1r9fvyg-3 gpeuWL'][normalize-space()='Parfum']"
perfume_item = "//img[@alt='CHANEL COCO MADEMOISELLE Eau de Parfum']"
add_to_cart = "//button[@class='PDPActionBarstyle__Button-sc-19f0xfv-3 iIwkPr']"
nav_to_cart = "//a[@class='Buttons-sc-1nlw4r-1 AddedToCartFooterstyle__FooterLink-sc-1m6klf7-2 faHwCa']"
vinput =  "//input[@id='voucherCode']"
vcode = "abc123"
btn_submit =  "//button[normalize-space()='Einlösen']"
invalid_c_msg = "//div[@class='NotificationInlinestyle__Message-sc-1pbt3b7-2 dbYUMD']"