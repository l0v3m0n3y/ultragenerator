import requests
class Client():
	def __init__(self):
		self.api="https://ultragenerator.com"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def yes_no(self):
		return requests.get(f"{self.api}/yes-no/handler.php",headers=self.headers).text
	def citaty(self):
		return requests.get(f"{self.api}/citaty/handler.php",headers=self.headers).text
	def random_numbers(self,first:int,second:int):
		data=f"first={first}&second={second}"
		return requests.post(f"{self.api}/randomnumbers/handler.php",data=data,headers=self.headers).text
	def word_generator(self,iter):
		data=f"iter={iter}"
		return requests.post(f"{self.api}/wordgenerator/handler.php",data=data,headers=self.headers).text
	def stihov(self):
		return requests.get(f"{self.api}/stihov/handler.php",headers=self.headers).text
	def countries(self):
		return requests.get(f"{self.api}/countries/handler.php",headers=self.headers).text
	def big_cities(self,cou:int=2):
		data=f"cou={cou}"
		return requests.post(f"{self.api}/big-cities/handler.php",data=data,headers=self.headers).text
	def card_numbers_cvv(self):
		return requests.get(f"{self.api}/card-numbers-cvv/handler.php",headers=self.headers).text
	def lottery_number(self,count):
		data=f"count={count}"
		return requests.post(f"{self.api}/lottery-number/handler.php",data=data,headers=self.headers).text
	def peremeshat_spisok(self,array):
		data=f"array={array}"
		return requests.post(f"{self.api}/peremeshat-spisok/handler.php",data=data,headers=self.headers).text
	def ball_8(self):
		return requests.get(f"{self.api}/ball-8/handler.php",headers=self.headers).text
	def kosti(self,count):
		data=f"count={count}"
		return requests.post(f"{self.api}/kosti/handler.php",data=data,headers=self.headers).text
	def splitgroups(self,count,array):
		data=f"array={array}&count={count}"
		return requests.post(f"{self.api}/splitgroups/handler.php",data=data,headers=self.headers).text
	def lots_online(self,count,array):
		data=f"array={array}&count={count}"
		return requests.post(f"{self.api}/lotsonline/handler.php",data=data,headers=self.headers).text
	def movies(self,cat):
		data=f"cat={cat}"
		return requests.post(f"{self.api}/movies/handler.php",data=data,headers=self.headers).text
	def family_name(self):
		return requests.get(f"{self.api}/familyname/handler.php",headers=self.headers).text
	def anekdotov(self):
		return requests.get(f"{self.api}/anekdotov/handler.php",headers=self.headers).text
	def html_color(self):
		return requests.get(f"{self.api}/htmlcolor/handler.php",headers=self.headers).text
	def cards(self,count):
		data=f"count={count}"
		return requests.post(f"{self.api}/cards/handler.php",data=data,headers=self.headers).text
	def rhymes(self,word):
		data=f"word={word}"
		return requests.post(f"{self.api}/rhymes/handler.php",data=data,headers=self.headers).text
	def facts(self):
		return requests.get(f"{self.api}/facts/handler.php",headers=self.headers).json()
	def compliment(self):
		return requests.get(f"{self.api}/compliment/handler.php",headers=self.headers).json()
	def monetka(self):
		return requests.get(f"{self.api}/monetka/handler.php",headers=self.headers).json()
	def nickname_animals(self,sex,type,count):
		data=f"sex={sex}&type={type}&count={count}"
		return requests.post(f"{self.api}/nickname-animals/handler.php",data=data,headers=self.headers).json()
	def slogans(self,word):
		data=f"custom_word={word}"
		return requests.post(f"{self.api}/slogans/handler.php",data=data,headers=self.headers).json()