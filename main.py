from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os, sys

os.system("clear")



def run(playwright: Playwright) -> None:
    email = input("Email / Telepon          : ")
    password = input("Password                 : ")
    comment = input("Comment                  : ")
    jmlhComment = int(input("Jumlah comment           : "))
    delay = int(input("Masukkan delay comment   : "))


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/?_rdc=1&_rdr")
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill(email)
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill(password)
    page.get_by_test_id("royal_pass").press("Enter")
    time.sleep(5)
    global default
    default = 0


    def mainCom():
        page.locator(".x1ed109x > div > div > div").first.click()
        page.get_by_label("Tulis").fill(comment)
        page.get_by_label("Komentari", exact=True).click()
        time.sleep(delay)
        page.goto("https://www.facebook.com/")

    while (True):
    #    page.get_by_label("Tulis komentar publik…").click()
    #    page.get_by_label("Tulis komentar publik…").fill("izin share bot wa buatan ane bang:v 085942073830")
        if default < jmlhComment:
            mainCom()
            default = default + 1
        else:
            break
    



#        if (jumlah < 5):
#            print ("hello")
#            jumlah = jumlah + 1


with sync_playwright() as playwright:
    run(playwright)



# KREDITS

# ALLAH SWT
# IRHAN SAPUTRA