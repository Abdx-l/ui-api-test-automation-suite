class Shop:
 def __init__(self,page):self.page=page
 def open(self,url):self.page.goto(url)
 def login(self,user,password):
  self.page.get_by_label("Username").fill(user);self.page.get_by_label("Password").fill(password);self.page.get_by_role("button",name="Login",exact=True).click()
 def add(self):self.page.get_by_role("button",name="Add to cart").click()
 def checkout(self,name):
  self.page.get_by_role("button",name="Cart",exact=True).click();self.page.get_by_label("Full name").fill(name);self.page.get_by_role("button",name="Place order").click()
