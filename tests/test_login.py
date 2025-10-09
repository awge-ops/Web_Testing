import re
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_successful_login(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    lp.wait_for_inventory()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_password(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("standard_user", "wrong_pass")
    assert "Username and password do not match" in lp.get_error()

def test_locked_out_user(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("locked_out_user", "secret_sauce")
    assert "locked out" in lp.get_error().lower()

