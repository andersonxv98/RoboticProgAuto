from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ControllerNavegador():
    def __init__(self):
        super(ControllerNavegador, self).__init__()
        self.driver = webdriver.Edge()

    def abrirPaginaNoEdge(self, site):
        print("funcao abrir ágina")

        self.driver.get(url=site)
        #self.assertIn("Python", self.driver.title)
        #elem = self.driver.find_element(By.NAME, "q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", se lf.driver.page_source)
        i = float(input("teste"))



