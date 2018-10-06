import datetime
import json 
import scrapy
import sys

class QuotesSpider(scrapy.Spider):
	allowed_domains = ['www.emporis.com']
	name = "buildings"
	# start_urls = 'https://americanart.si.edu/'
	start_urls = ["https://www.emporis.com/city/100637/london-united-kingdom/status/all-buildings"
	]

	#start_urls = ['https://americanart.si.edu/artwork/untitled-individual-element-healing-machine-110156']
#	global buildings.out

	building_out = open("buildings_2.txt","w")
	building_url = open("buildings_url_2.txt","w")

	building_count = 0
	building_list = []



	def start_requests(self):
		print("start requests")
		# for url in self.start_urls:
		# 	if(self.artist_count<5000 or self.artwork_count<3000):
		# 		yield scrapy.Request(url, self.parse_2)
		if(self.building_count<10000 ):
			# print("begin to download others##############################")
			for url in self.start_urls:
				yield scrapy.Request(url,self.parse_1)

	def parse_1(self, response):
		print response.url
		if "/buildings/" in response.url :

			building_temp = {"doc_id":self.building_count,"url":response.url,"raw_content":response.text,"timestamp_crawl":str(datetime.datetime.now())}
			print("write in the artwork")
			self.building_out.write(json.dumps(building_temp))
			self.building_out.write("\n")
			self.building_count +=1 

			# print("@@@@@@@@@@@@@@write the url to artwork text")
			self.building_url.write(response.url)
			self.building_url.write("\n")
			# if(response.url in self.artwork_list):
			# 	artwork_list.remove(response.url)


		# elif "https://americanart.si.edu/artist/" in response.url:
						
		# 	artist_temp = {"doc_id":self.artist_count,"url":response.url,"raw_content":response.text,"timestamp_crawl":str(datetime.datetime.now())}
		# 	print("write in the artist")
		# 	self.artist_out.write(json.dumps(artist_temp))
		# 	self.artist_out.write("\n")
		# 	self.artist_count +=1 

		# 	# print("@@@@@@@@@@@@@@@@write the url to artist text")
		# 	self.artist_url.write(response.url)
		# 	self.artist_url.write("\n")
			# if(response.url in self.artist_list):
			# 	artist_list.remove(response.url)

		links = response.xpath('//td/a/@href').extract()
		if(self.building_count<10000):
			for link in links:
				# print(link)

				# if(self.artist_count>4999 and self.artwork_count>2999):
				# 	break
				# # print self.count
				# print(self.artist_count)
				# # print(self.artwork_count)
				# if(self.artist_list or  self.artwork_list):
				yield response.follow("https://www.emporis.com"+link,callback = self.parse_1)
				# if(self.count<10):
						# self.count+=1

	# def parse_2(self, response):
	# 	# s= response.url 
	# 	# if 'artwork' in s:
	# 	# 	print response.url
	# 	print response.url
	# 	if "https://americanart.si.edu/artwork/" in response.url :
	# 		art_temp = {"doc_id":self.artwork_count,"url":response.url,"raw_content":response.text,"timestamp_crawl":str(datetime.datetime.now())}
	# 		print("write in the artwork")
	# 		self.artwork_out.write(json.dumps(art_temp))
	# 		self.artwork_out.write("\n")
	# 		self.artwork_count +=1 

	# 		# print("@@@@@@@@@@@@@@write the url to artwork text")
	# 		self.artwork_url.write(response.url)
	# 		self.artwork_url.write("\n")
	# 		# if(response.url in self.artwork_list):
	# 		# 	artwork_list.remove(response.url)

	# 	elif "https://americanart.si.edu/artist/" in response.url:
	# 		artist_temp = {"doc_id":self.artist_count,"url":response.url,"raw_content":response.text,"timestamp_crawl":str(datetime.datetime.now())}
	# 		print("write in the artist")
	# 		self.artist_out.write(json.dumps(artist_temp))
	# 		self.artist_out.write("\n")
	# 		self.artist_count +=1 

	# 		# print("@@@@@@@@@@@@@@@@write the url to artist text")
	# 		self.artist_url.write(response.url)
	# 		self.artist_url.write("\n")

			# if(response.url in self.artist_list):
			# 	artist_list.remove(response.url)

		# links = response.xpath('//div/a/@href').extract()
		# if(self.artist_count<3):
		# 	for link in links:
		# 		if(self.artist_count>2):
		# 			break
		# 		# print self.count
		# 		print(self.artist_count)
		# 		# print(self.artwork_count)
		# 		if(self.artist_list or  self.artwork_list):
		# 			if(self.artwork_count<5):
		# 				yield response.follow(link)



      