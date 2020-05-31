from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from datetime import datetime

Ahora=datetime.now()
Ho=Ahora.hour
Min=Ahora.minute

Oferta=["Oferta"]
Seccion_Oferta=["Indicador-aportes-hidricos.aspx","Indicador-detalle-aportes-hidricos.aspx","Indicador-reservas-hidricas.aspx","Indicador-detalle-reservas-hidricas.aspx",
        "Indicador-generacion-sin.aspx","Indicador-capacidad-sin.aspx","Indicador-consumo-combustibles.aspx","Indicador-vertimientos.aspx","Indicador-detalle-vertimientos.aspx"]
LLaves=[['#cambiarVista','#exportarIndicador'],["#exportarExcellDetalle"],["#cambiarVista","#exportarIndicador"],["#exportarExcellDetalle"],["#cambiarVista","#exportarIndicador"],["#exportarIndicador"],
       ['#cambiarVista','#exportarIndicador'],['#cambiarVista','#exportarIndicador'],["#exportarExcellDetalle"]]            

class Toma_de_datos:
	def KEYS(self,Llave,url,Seccion,Hora,Minutos):
		self.url=url+'/'+Seccion
		self.Llave=Llave
		self.Carpeta=[url,str(Hora)+':'+str(Minutos)]
		self.Tamaño_keys=len(Llave)
		return (self.url,self.Llave,self.Carpeta,self.Tamaño_keys)		
class Mercado_XM:
	
	def Keys_CAMBIAR(self,Url,LLave1,driver,URL_Original):
		self.url=URL_Original+Url
		driver.get(self.url)
		time.sleep(5)
		driver.find_element_by_css_selector(LLave1[0]).click()
		time.sleep(5)
		driver.find_element_by_css_selector(LLave1[1]).click()	
		time.sleep(5)
	def Keys_Exportar(self,Url,LLave1,driver,URL_Original):
		self.url=URL_Original+Url
		driver.get(self.url)
		time.sleep(5)
		driver.find_element_by_css_selector(LLave1[0]).click()
		time.sleep(5)
		
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.dir",os.getcwd());
profile.set_preference("browser.download.folderList",2);
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream,image/png");
profile.set_preference("browser.download.manager.showWhenStarting",False);
profile.set_preference("browser.helperApps.neverAsk.openFile","application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream,image/png");
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.useWindow", False);
profile.set_preference("browser.download.manager.focusWhenStarting", False);
profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
profile.set_preference("browser.download.manager.showAlertOnComplete", False);
profile.set_preference("browser.download.manager.closeWhenDone", True);
profile.set_preference("pdfjs.disabled", True);

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)
URL_Original="https://www.xm.com.co/Paginas/Indicadores/"
for i in range(len(Seccion_Oferta)):
	Datos=Toma_de_datos()
	Url,LLave,Carpeta,Tamaño_keys=Datos.KEYS(LLaves[i],Oferta[0],Seccion_Oferta[i],Ho,Min)
	if Tamaño_keys==2:
		a=Mercado_XM()
		a.Keys_CAMBIAR(Url,LLave,driver,URL_Original)
	else:
		a=Mercado_XM()
		a.Keys_Exportar(Url,LLave,driver,URL_Original)
driver.quit()
print("-----FINALIZADO------")

