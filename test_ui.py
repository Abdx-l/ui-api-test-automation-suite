from playwright.sync_api import expect
from pages import Shop
def test_checkout(page,base_url):
 shop=Shop(page);shop.open(base_url);shop.login("standard_user","secret_sauce");shop.add();shop.checkout("Test User");expect(page.get_by_role("status")).to_have_text("Thank you for your order")
def test_invalid_login(page,base_url):
 shop=Shop(page);shop.open(base_url);shop.login("wrong","wrong");expect(page.get_by_role("alert")).to_have_text("Invalid credentials")
def test_checkout_requires_name(page,base_url):
 shop=Shop(page);shop.open(base_url);shop.login("standard_user","secret_sauce");shop.add();shop.checkout("");expect(page.get_by_role("alert")).to_have_text("Name is required")
