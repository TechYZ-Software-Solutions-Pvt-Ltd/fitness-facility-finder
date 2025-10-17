"""
Static data constants for countries, cities, and fitness types.
"""

# Unified hierarchical location data: Country -> State/Province -> City/Town
# For countries without states, state and city will be the same
UNIFIED_LOCATIONS = {
    'India': {
        'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Tirupati', 'Kadapa', 'Anantapur', 'Chittoor', 'Ongole'],
        'Arunachal Pradesh': ['Itanagar', 'Naharlagun', 'Pasighat', 'Tezpur', 'Dibrugarh', 'Tawang', 'Bomdila', 'Ziro', 'Along', 'Roing'],
        'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Tezpur', 'Nagaon', 'Tinsukia', 'Barpeta', 'Dhubri', 'Kokrajhar'],
        'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga', 'Purnia', 'Arrah', 'Begusarai', 'Katihar', 'Munger'],
        'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Rajnandgaon', 'Durg', 'Raigarh', 'Ambikapur', 'Jagdalpur', 'Chirmiri'],
        'Goa': ['Panaji', 'Margao', 'Vasco da Gama', 'Mapusa', 'Ponda', 'Mormugao', 'Curchorem', 'Sanquelim', 'Bicholim', 'Valpoi'],
        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Jamnagar', 'Junagadh', 'Gandhinagar', 'Nadiad', 'Morbi'],
        'Haryana': ['Gurgaon', 'Faridabad', 'Panipat', 'Ambala', 'Yamunanagar', 'Rohtak', 'Hisar', 'Karnal', 'Sonipat', 'Panchkula'],
        'Himachal Pradesh': ['Shimla', 'Dharamshala', 'Solan', 'Mandi', 'Palampur', 'Kullu', 'Manali', 'Chamba', 'Una', 'Bilaspur'],
        'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro', 'Deoghar', 'Phusro', 'Hazaribagh', 'Giridih', 'Ramgarh', 'Medininagar'],
        'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum', 'Gulbarga', 'Davanagere', 'Bellary', 'Bijapur', 'Shimoga'],
        'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Palakkad', 'Malappuram', 'Kannur', 'Kasaragod', 'Kollam', 'Alappuzha'],
        'Madhya Pradesh': ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur', 'Ujjain', 'Sagar', 'Dewas', 'Satna', 'Ratlam', 'Murwara'],
        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Aurangabad', 'Solapur', 'Amravati', 'Kolhapur', 'Sangli'],
        'Manipur': ['Imphal', 'Thoubal', 'Bishnupur', 'Churachandpur', 'Senapati', 'Tamenglong', 'Chandel', 'Ukhrul', 'Kangpokpi', 'Jiribam'],
        'Meghalaya': ['Shillong', 'Tura', 'Jowai', 'Nongstoin', 'Williamnagar', 'Baghmara', 'Resubelpara', 'Amlarem', 'Mawkyrwat', 'Mairang'],
        'Mizoram': ['Aizawl', 'Lunglei', 'Saiha', 'Champhai', 'Kolasib', 'Serchhip', 'Lawngtlai', 'Mamit', 'Saitual', 'Hnahthial'],
        'Nagaland': ['Kohima', 'Dimapur', 'Mokokchung', 'Tuensang', 'Wokha', 'Zunheboto', 'Phek', 'Mon', 'Longleng', 'Kiphire'],
        'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Berhampur', 'Sambalpur', 'Puri', 'Balasore', 'Bhadrak', 'Baripada', 'Jharsuguda'],
        'Punjab': ['Chandigarh', 'Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda', 'Mohali', 'Batala', 'Pathankot', 'Moga'],
        'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Bikaner', 'Ajmer', 'Bharatpur', 'Bhilwara', 'Alwar', 'Ganganagar'],
        'Sikkim': ['Gangtok', 'Namchi', 'Mangan', 'Gyalshing', 'Ravongla', 'Singtam', 'Rangpo', 'Jorethang', 'Pakyong', 'Rhenock'],
        'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli', 'Tiruppur', 'Erode', 'Vellore', 'Thoothukkudi'],
        'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Ramagundam', 'Mahbubnagar', 'Nalgonda', 'Adilabad', 'Suryapet'],
        'Tripura': ['Agartala', 'Dharmanagar', 'Udaipur', 'Ambassa', 'Kailashahar', 'Belonia', 'Khowai', 'Teliamura', 'Sabroom', 'Sonamura'],
        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Meerut', 'Varanasi', 'Allahabad', 'Bareilly', 'Aligarh', 'Moradabad'],
        'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Rudrapur', 'Kashipur', 'Haldwani', 'Rishikesh', 'Ramnagar', 'Pithoragarh', 'Manglaur'],
        'West Bengal': ['Kolkata', 'Asansol', 'Siliguri', 'Durgapur', 'Bardhaman', 'Malda', 'Bahraich', 'Habra', 'Kharagpur', 'Shantipur'],
        'Delhi': ['New Delhi', 'Central Delhi', 'East Delhi', 'North Delhi', 'North East Delhi', 'North West Delhi', 'Shahdara', 'South Delhi', 'South East Delhi', 'South West Delhi', 'West Delhi'],
        'Chandigarh': ['Chandigarh'],
        'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Pulwama', 'Kupwara', 'Budgam', 'Ganderbal', 'Bandipora', 'Kulgam'],
        'Ladakh': ['Leh', 'Kargil'],
        'Puducherry': ['Puducherry', 'Karaikal', 'Mahe', 'Yanam'],
        'Andaman and Nicobar Islands': ['Port Blair', 'Diglipur', 'Mayabunder', 'Rangat', 'Hut Bay', 'Car Nicobar', 'Nancowry', 'Katchal', 'Teressa', 'Chowra'],
        'Dadra and Nagar Haveli and Daman and Diu': ['Silvassa', 'Daman', 'Diu'],
        'Lakshadweep': ['Kavaratti', 'Agatti', 'Amini', 'Andrott', 'Kadmat', 'Kalpeni', 'Kiltan', 'Minicoy', 'Chettlat', 'Bitra']
    },
    'Singapore': {
        'Singapore': ['Singapore', 'Central Region', 'East Region', 'North Region', 'North-East Region', 'West Region']
    },
    'Malaysia': {
        'Kuala Lumpur': ['Kuala Lumpur', 'Petaling Jaya', 'Shah Alam', 'Subang Jaya', 'Klang', 'Ampang', 'Cheras', 'Kepong'],
        'Selangor': ['Shah Alam', 'Petaling Jaya', 'Subang Jaya', 'Klang', 'Kajang', 'Selayang', 'Ampang', 'Cheras'],
        'Penang': ['George Town', 'Butterworth', 'Bukit Mertajam', 'Nibong Tebal', 'Bayan Lepas', 'Tanjung Tokong', 'Gelugor', 'Air Itam'],
        'Johor': ['Johor Bahru', 'Iskandar Puteri', 'Kulai', 'Pasir Gudang', 'Tebrau', 'Ulu Tiram', 'Skudai', 'Kota Tinggi'],
        'Sabah': ['Kota Kinabalu', 'Sandakan', 'Tawau', 'Lahad Datu', 'Keningau', 'Kudat', 'Semporna', 'Papar'],
        'Sarawak': ['Kuching', 'Miri', 'Sibu', 'Bintulu', 'Limbang', 'Sri Aman', 'Kapit', 'Mukah']
    },
    'Sri Lanka': {
        'Western Province': ['Colombo', 'Gampaha', 'Kalutara', 'Negombo', 'Panadura', 'Wattala', 'Kaduwela', 'Kelaniya'],
        'Central Province': ['Kandy', 'Matale', 'Nuwara Eliya', 'Gampola', 'Dambulla', 'Hatton', 'Nawalapitiya', 'Talawakele'],
        'Southern Province': ['Galle', 'Matara', 'Hambantota', 'Weligama', 'Tangalle', 'Ambalantota', 'Deniyaya', 'Akuressa'],
        'Northern Province': ['Jaffna', 'Vavuniya', 'Mannar', 'Kilinochchi', 'Mullaitivu', 'Point Pedro', 'Chavakachcheri', 'Valvettithurai'],
        'Eastern Province': ['Batticaloa', 'Trincomalee', 'Ampara', 'Kalmunai', 'Eravur', 'Valaichchenai', 'Kattankudy', 'Oddamavadi'],
        'North Western Province': ['Kurunegala', 'Puttalam', 'Chilaw', 'Kuliyapitiya', 'Polonnaruwa', 'Anuradhapura', 'Medawachchiya', 'Habarana'],
        'North Central Province': ['Anuradhapura', 'Polonnaruwa', 'Medirigiriya', 'Habarana', 'Galnewa', 'Elahera', 'Dambulla', 'Kekirawa'],
        'Uva Province': ['Badulla', 'Monaragala', 'Bandarawela', 'Haputale', 'Ella', 'Passara', 'Welimada', 'Bibile'],
        'Sabaragamuwa Province': ['Ratnapura', 'Kegalle', 'Balangoda', 'Kegalle', 'Mawanella', 'Rambukkana', 'Eheliyagoda', 'Kuruwita']
    },
    'Bahrain': {
        'Bahrain': ['Manama', 'Muharraq', 'Riffa', 'Hamad Town', 'A\'ali', 'Isa Town', 'Sitra', 'Budaiya', 'Jidhafs', 'Sanabis']
    },
    'United Arab Emirates': {
        'Abu Dhabi': ['Abu Dhabi', 'Al Ain', 'Liwa', 'Ruwais'],
        'Dubai': ['Dubai', 'Jebel Ali', 'Hatta'],
        'Sharjah': ['Sharjah', 'Khor Fakkan', 'Kalba'],
        'Ajman': ['Ajman', 'Masfout'],
        'Ras Al Khaimah': ['Ras Al Khaimah', 'Jazirat Al Hamra'],
        'Fujairah': ['Fujairah', 'Dibba', 'Kalba'],
        'Umm Al Quwain': ['Umm Al Quwain', 'Falaj Al Mualla']
    },
    'Saudi Arabia': {
        'Riyadh': ['Riyadh', 'Diriyah', 'Al Kharj'],
        'Makkah': ['Mecca', 'Jeddah', 'Taif', 'Medina'],
        'Eastern Province': ['Dammam', 'Khobar', 'Dhahran', 'Jubail'],
        'Asir': ['Abha', 'Khamis Mushait', 'Bisha'],
        'Qassim': ['Buraidah', 'Unaizah', 'Riyadh Al Khabra'],
        'Hail': ['Hail', 'Al Qurayyat', 'Sakaka'],
        'Tabuk': ['Tabuk', 'Al Wajh', 'Duba'],
        'Northern Borders': ['Arar', 'Turaif', 'Rafha']
    },
    'Kuwait': {
        'Kuwait': ['Kuwait City', 'Hawalli', 'Farwaniya', 'Ahmadi', 'Jahra', 'Mubarak Al-Kabeer']
    },
    'Qatar': {
        'Qatar': ['Doha', 'Al Rayyan', 'Al Wakrah', 'Al Khor', 'Lusail', 'Mesaieed', 'Dukhan', 'Ras Laffan']
    },
    'Oman': {
        'Muscat': ['Muscat', 'Muttrah', 'Ruwi', 'Al Khuwair'],
        'Dhofar': ['Salalah', 'Mirbat', 'Taqah'],
        'Al Batinah': ['Sohar', 'Barka', 'Al Khaburah'],
        'Ad Dakhiliyah': ['Nizwa', 'Bahla', 'Manah'],
        'Ash Sharqiyah': ['Sur', 'Ibra', 'Al Mudaybi'],
        'Ad Dhahirah': ['Ibri', 'Yanqul', 'Dank'],
        'Al Buraimi': ['Buraimi', 'Mahdah', 'As Sunaynah']
    },
    'Jordan': {
        'Amman': ['Amman', 'Zarqa', 'Salt', 'Madaba'],
        'Irbid': ['Irbid', 'Ramtha', 'Mafraq'],
        'Aqaba': ['Aqaba', 'Wadi Rum', 'Tala Bay'],
        'Karak': ['Karak', 'Tafilah', 'Ma\'an'],
        'Ajloun': ['Ajloun', 'Jerash', 'Kufranjah']
    },
    'Lebanon': {
        'Beirut': ['Beirut', 'Achrafieh', 'Hamra', 'Verdun'],
        'Mount Lebanon': ['Jounieh', 'Byblos', 'Baalbek', 'Zahle'],
        'North Lebanon': ['Tripoli', 'Zgharta', 'Koura', 'Bcharre'],
        'South Lebanon': ['Sidon', 'Tyre', 'Nabatieh', 'Marjayoun'],
        'Bekaa': ['Zahle', 'Baalbek', 'Hermel', 'Rashaya']
    },
    'Egypt': {
        'Cairo': ['Cairo', 'Giza', 'Shubra El Kheima', 'Helwan'],
        'Alexandria': ['Alexandria', 'Borg El Arab', 'New Borg El Arab'],
        'Giza': ['Giza', '6th October City', 'Sheikh Zayed City'],
        'Suez': ['Suez', 'Port Said', 'Ismailia'],
        'Upper Egypt': ['Luxor', 'Aswan', 'Qena', 'Sohag'],
        'Delta': ['Tanta', 'Mansoura', 'Zagazig', 'Damanhur']
    },
    'Australia': {
        'New South Wales': ['Sydney', 'Newcastle', 'Wollongong', 'Maitland', 'Wagga Wagga', 'Albury', 'Tamworth', 'Orange'],
        'Victoria': ['Melbourne', 'Geelong', 'Ballarat', 'Bendigo', 'Shepparton', 'Warrnambool', 'Mildura', 'Traralgon'],
        'Queensland': ['Brisbane', 'Gold Coast', 'Townsville', 'Cairns', 'Toowoomba', 'Rockhampton', 'Mackay', 'Bundaberg'],
        'Western Australia': ['Perth', 'Fremantle', 'Rockingham', 'Mandurah', 'Bunbury', 'Geraldton', 'Albany', 'Broome'],
        'South Australia': ['Adelaide', 'Mount Gambier', 'Whyalla', 'Murray Bridge', 'Port Augusta', 'Port Pirie', 'Gawler', 'Kadina'],
        'Tasmania': ['Hobart', 'Launceston', 'Devonport', 'Burnie', 'Ulverstone', 'Kingston', 'George Town', 'Sorell'],
        'Australian Capital Territory': ['Canberra', 'Gungahlin', 'Tuggeranong', 'Weston Creek', 'Belconnen', 'Woden Valley', 'Inner North', 'Inner South'],
        'Northern Territory': ['Darwin', 'Alice Springs', 'Katherine', 'Nhulunbuy', 'Palmerston', 'Howard Springs', 'Humpty Doo', 'Tennant Creek']
    },
    'New Zealand': {
        'Auckland': ['Auckland', 'Manukau', 'North Shore', 'Waitakere', 'Papakura', 'Franklin', 'Rodney', 'Howick'],
        'Wellington': ['Wellington', 'Lower Hutt', 'Upper Hutt', 'Porirua', 'Kapiti Coast', 'Masterton', 'Carterton', 'South Wairarapa'],
        'Canterbury': ['Christchurch', 'Timaru', 'Ashburton', 'Rangiora', 'Kaiapoi', 'Rolleston', 'Lincoln', 'Leeston'],
        'Waikato': ['Hamilton', 'Tauranga', 'Rotorua', 'Taupo', 'Gisborne', 'Hastings', 'Napier', 'Palmerston North'],
        'Otago': ['Dunedin', 'Queenstown', 'Wanaka', 'Alexandra', 'Cromwell', 'Oamaru', 'Balclutha', 'Milton'],
        'Southland': ['Invercargill', 'Gore', 'Te Anau', 'Bluff', 'Riverton', 'Winton', 'Lumsden', 'Mataura']
    },
    'United Kingdom': {
        'England': ['London', 'Birmingham', 'Manchester', 'Liverpool', 'Leeds', 'Sheffield', 'Bristol', 'Leicester', 'Coventry', 'Bradford'],
        'Scotland': ['Glasgow', 'Edinburgh', 'Aberdeen', 'Dundee', 'Paisley', 'East Kilbride', 'Livingston', 'Hamilton'],
        'Wales': ['Cardiff', 'Swansea', 'Newport', 'Wrexham', 'Barry', 'Caerphilly', 'Rhondda', 'Port Talbot'],
        'Northern Ireland': ['Belfast', 'Derry', 'Lisburn', 'Newtownabbey', 'Bangor', 'Craigavon', 'Castlereagh', 'Carrickfergus']
    },
    'United States': {
        'California': ['Los Angeles', 'San Francisco', 'San Diego', 'San Jose', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland'],
        'New York': ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse', 'Albany', 'New Rochelle', 'Mount Vernon'],
        'Texas': ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington', 'Corpus Christi'],
        'Florida': ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St. Petersburg', 'Hialeah', 'Tallahassee', 'Fort Lauderdale'],
        'Illinois': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville', 'Springfield', 'Peoria', 'Elgin'],
        'Pennsylvania': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading', 'Scranton', 'Bethlehem', 'Lancaster'],
        'Ohio': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron', 'Dayton', 'Parma', 'Canton'],
        'Georgia': ['Atlanta', 'Augusta', 'Columbus', 'Savannah', 'Athens', 'Sandy Springs', 'Roswell', 'Macon']
    },
    'Germany': {
        'Bavaria': ['Munich', 'Nuremberg', 'Augsburg', 'Wurzburg', 'Regensburg', 'Ingolstadt', 'Furth', 'Erlangen'],
        'North Rhine-Westphalia': ['Cologne', 'Dusseldorf', 'Dortmund', 'Essen', 'Duisburg', 'Bochum', 'Wuppertal', 'Bielefeld'],
        'Baden-Wurttemberg': ['Stuttgart', 'Mannheim', 'Karlsruhe', 'Freiburg', 'Heidelberg', 'Heilbronn', 'Ulm', 'Pforzheim'],
        'Lower Saxony': ['Hannover', 'Braunschweig', 'Osnabruck', 'Oldenburg', 'Gottingen', 'Wolfsburg', 'Salzgitter', 'Hildesheim'],
        'Hesse': ['Frankfurt', 'Wiesbaden', 'Kassel', 'Darmstadt', 'Offenbach', 'Hanau', 'Marburg', 'Fulda'],
        'Saxony': ['Leipzig', 'Dresden', 'Chemnitz', 'Zwickau', 'Plauen', 'Gorlitz', 'Freiberg', 'Bautzen'],
        'Rhineland-Palatinate': ['Mainz', 'Ludwigshafen', 'Koblenz', 'Trier', 'Kaiserslautern', 'Worms', 'Neuwied', 'Speyer'],
        'Berlin': ['Berlin', 'Charlottenburg', 'Kreuzberg', 'Prenzlauer Berg', 'Friedrichshain', 'Mitte', 'Neukolln', 'Tempelhof']
    },
    'France': {
        'Ile-de-France': ['Paris', 'Boulogne-Billancourt', 'Saint-Denis', 'Argenteuil', 'Montreuil', 'Nanterre', 'Vitry-sur-Seine', 'Créteil'],
        'Provence-Alpes-Cote d\'Azur': ['Marseille', 'Nice', 'Toulon', 'Aix-en-Provence', 'Avignon', 'Antibes', 'Cannes', 'Fréjus'],
        'Auvergne-Rhone-Alpes': ['Lyon', 'Saint-Etienne', 'Grenoble', 'Villeurbanne', 'Valence', 'Chambéry', 'Annecy', 'Clermont-Ferrand'],
        'Occitanie': ['Toulouse', 'Montpellier', 'Nimes', 'Perpignan', 'Béziers', 'Montauban', 'Albi', 'Carcassonne'],
        'Hauts-de-France': ['Lille', 'Amiens', 'Roubaix', 'Tourcoing', 'Dunkerque', 'Calais', 'Boulogne-sur-Mer', 'Valenciennes'],
        'Grand Est': ['Strasbourg', 'Reims', 'Metz', 'Mulhouse', 'Nancy', 'Colmar', 'Troyes', 'Châlens-en-Champagne'],
        'Nouvelle-Aquitaine': ['Bordeaux', 'Limoges', 'Poitiers', 'La Rochelle', 'Angoulême', 'Pau', 'Bayonne', 'Agen'],
        'Brittany': ['Rennes', 'Brest', 'Quimper', 'Lorient', 'Vannes', 'Saint-Malo', 'Saint-Brieuc', 'Lannion']
    },
    'Portugal': {
        'Lisbon': ['Lisbon', 'Sintra', 'Cascais', 'Oeiras', 'Amadora', 'Odivelas', 'Loures', 'Vila Franca de Xira'],
        'Porto': ['Porto', 'Vila Nova de Gaia', 'Matosinhos', 'Gondomar', 'Valongo', 'Maia', 'Póvoa de Varzim', 'Vila do Conde'],
        'Braga': ['Braga', 'Guimarães', 'Barcelos', 'Famalicão', 'Vizela', 'Amares', 'Cabeceiras de Basto', 'Celorico de Basto'],
        'Coimbra': ['Coimbra', 'Figueira da Foz', 'Cantanhede', 'Condeixa-a-Nova', 'Lousã', 'Mira', 'Montemor-o-Velho', 'Penacova'],
        'Aveiro': ['Aveiro', 'Águeda', 'Albergaria-a-Velha', 'Anadia', 'Arouca', 'Estarreja', 'Ílhavo', 'Murtosa'],
        'Setúbal': ['Setúbal', 'Almada', 'Barreiro', 'Moita', 'Montijo', 'Palmela', 'Sesimbra', 'Sines'],
        'Faro': ['Faro', 'Albufeira', 'Lagos', 'Loulé', 'Portimão', 'Silves', 'Tavira', 'Vila Real de Santo António'],
        'Leiria': ['Leiria', 'Alcobaça', 'Batalha', 'Caldas da Rainha', 'Marinha Grande', 'Nazaré', 'Óbidos', 'Peniche']
    },
    'Spain': {
        'Madrid': ['Madrid', 'Alcala de Henares', 'Fuenlabrada', 'Leganes', 'Getafe', 'Alcorcon', 'Torrejon de Ardoz', 'Parla'],
        'Catalonia': ['Barcelona', 'L\'Hospitalet de Llobregat', 'Terrassa', 'Badalona', 'Sabadell', 'Mataro', 'Santa Coloma de Gramenet', 'Reus'],
        'Valencia': ['Valencia', 'Alicante', 'Elche', 'Castellon de la Plana', 'Torrevieja', 'Orihuela', 'Gandia', 'Benidorm'],
        'Andalusia': ['Seville', 'Malaga', 'Cordoba', 'Granada', 'Jerez de la Frontera', 'Almeria', 'Cadiz', 'Huelva'],
        'Galicia': ['Vigo', 'A Coruna', 'Ourense', 'Lugo', 'Santiago de Compostela', 'Pontevedra', 'Ferrol', 'Lalin'],
        'Castile and Leon': ['Valladolid', 'Leon', 'Burgos', 'Salamanca', 'Palencia', 'Ponferrada', 'Zamora', 'Avila'],
        'Basque Country': ['Bilbao', 'Vitoria-Gasteiz', 'San Sebastian', 'Barakaldo', 'Getxo', 'Portugalete', 'Santurtzi', 'Basauri'],
        'Canary Islands': ['Las Palmas', 'Santa Cruz de Tenerife', 'San Cristobal de La Laguna', 'Telde', 'Arona', 'Santa Lucia de Tirajana', 'Arrecife', 'San Bartolome de Tirajana']
    },
    'Kenya': {
        'Nairobi': ['Nairobi', 'Westlands', 'Kasarani', 'Embakasi', 'Makadara', 'Kamukunji', 'Starehe', 'Mathare'],
        'Mombasa': ['Mombasa', 'Changamwe', 'Jomvu', 'Kisauni', 'Likoni', 'Mvita', 'Nyali', 'Tudor'],
        'Kisumu': ['Kisumu', 'Kisumu Central', 'Kisumu East', 'Kisumu West', 'Nyando', 'Muhoroni', 'Nyakach', 'Seme'],
        'Nakuru': ['Nakuru', 'Bahati', 'Gilgil', 'Kuresoi North', 'Kuresoi South', 'Molo', 'Naivasha', 'Nakuru Town East'],
        'Eldoret': ['Eldoret', 'Ainabkoi', 'Kapseret', 'Kesses', 'Moiben', 'Soy', 'Turbo', 'Wareng'],
        'Thika': ['Thika', 'Gatundu North', 'Gatundu South', 'Juja', 'Kiambu', 'Kiambaa', 'Kikuyu', 'Lari'],
        'Malindi': ['Malindi', 'Ganze', 'Kaloleni', 'Kilifi', 'Magarini', 'Rabai', 'Malindi', 'Kilifi'],
        'Kitale': ['Kitale', 'Cherangany', 'Endebess', 'Kiminini', 'Kwanza', 'Saboti', 'Trans Nzoia East', 'Trans Nzoia West']
    },
    'South Africa': {
        'Gauteng': ['Johannesburg', 'Pretoria', 'Soweto', 'Tembisa', 'Benoni', 'Vereeniging', 'Kempton Park', 'Germiston'],
        'Western Cape': ['Cape Town', 'Paarl', 'Stellenbosch', 'Worcester', 'George', 'Oudtshoorn', 'Mossel Bay', 'Knysna'],
        'KwaZulu-Natal': ['Durban', 'Pietermaritzburg', 'Newcastle', 'Pinetown', 'Umlazi', 'Chatsworth', 'Phoenix', 'Amanzimtoti'],
        'Eastern Cape': ['Port Elizabeth', 'East London', 'Uitenhage', 'King Williams Town', 'Queenstown', 'Grahamstown', 'Jeffreys Bay', 'Graaff-Reinet'],
        'Free State': ['Bloemfontein', 'Welkom', 'Kroonstad', 'Bethlehem', 'Sasolburg', 'Virginia', 'Harrismith', 'Parys'],
        'Mpumalanga': ['Nelspruit', 'Witbank', 'Secunda', 'Middelburg', 'Standerton', 'Ermelo', 'Bethal', 'Lydenburg'],
        'Limpopo': ['Polokwane', 'Tzaneen', 'Mokopane', 'Lephalale', 'Musina', 'Thohoyandou', 'Giyani', 'Modimolle'],
        'North West': ['Mahikeng', 'Klerksdorp', 'Potchefstroom', 'Rustenburg', 'Brits', 'Lichtenburg', 'Vryburg', 'Wolmaransstad']
    },
    'Brazil': {
        'Sao Paulo': ['São Paulo', 'Guarulhos', 'Campinas', 'Sao Bernardo do Campo', 'Santo Andre', 'Osasco', 'Ribeirao Preto', 'Sorocaba'],
        'Rio de Janeiro': ['Rio de Janeiro', 'Sao Goncalo', 'Duque de Caxias', 'Nova Iguacu', 'Niteroi', 'Belford Roxo', 'Sao Joao de Meriti', 'Campos dos Goytacazes'],
        'Minas Gerais': ['Belo Horizonte', 'Uberlandia', 'Contagem', 'Juiz de Fora', 'Betim', 'Montes Claros', 'Ribeirao das Neves', 'Uberaba'],
        'Bahia': ['Salvador', 'Feira de Santana', 'Vitoria da Conquista', 'Camacari', 'Juazeiro', 'Itabuna', 'Lauro de Freitas', 'Ilheus'],
        'Parana': ['Curitiba', 'Londrina', 'Maringa', 'Ponta Grossa', 'Cascavel', 'Sao Jose dos Pinhais', 'Foz do Iguacu', 'Colombo'],
        'Rio Grande do Sul': ['Porto Alegre', 'Caxias do Sul', 'Pelotas', 'Canoas', 'Santa Maria', 'Gravatai', 'Viamao', 'Novo Hamburgo'],
        'Pernambuco': ['Recife', 'Jaboatao dos Guararapes', 'Olinda', 'Caruaru', 'Petrolina', 'Paulista', 'Cabo de Santo Agostinho', 'Camaragibe'],
        'Ceara': ['Fortaleza', 'Caucaia', 'Juazeiro do Norte', 'Maracanau', 'Sobral', 'Crato', 'Itapipoca', 'Maranguape']
    },
    'Canada': {
        'Ontario': ['Toronto', 'Ottawa', 'Hamilton', 'Kitchener', 'London', 'Windsor', 'Oshawa', 'Barrie'],
        'Quebec': ['Montreal', 'Quebec City', 'Laval', 'Gatineau', 'Longueuil', 'Sherbrooke', 'Saguenay', 'Levis'],
        'British Columbia': ['Vancouver', 'Surrey', 'Burnaby', 'Richmond', 'Abbotsford', 'Coquitlam', 'Saanich', 'Delta'],
        'Alberta': ['Calgary', 'Edmonton', 'Red Deer', 'Lethbridge', 'St. Albert', 'Medicine Hat', 'Grande Prairie', 'Airdrie'],
        'Manitoba': ['Winnipeg', 'Brandon', 'Steinbach', 'Thompson', 'Portage la Prairie', 'Winkler', 'Selkirk', 'Morden'],
        'Saskatchewan': ['Saskatoon', 'Regina', 'Prince Albert', 'Moose Jaw', 'Swift Current', 'Yorkton', 'North Battleford', 'Estevan'],
        'Nova Scotia': ['Halifax', 'Sydney', 'Dartmouth', 'Truro', 'New Glasgow', 'Glace Bay', 'Kentville', 'Amherst'],
        'New Brunswick': ['Moncton', 'Saint John', 'Fredericton', 'Dieppe', 'Riverview', 'Edmundston', 'Miramichi', 'Bathurst']
    }
}

# Legacy countries data for backward compatibility
COUNTRIES = {
    'Bahrain': ['Manama', 'Muharraq', 'Riffa', 'Hamad Town', 'A\'ali', 'Isa Town', 'Sitra', 'Budaiya', 'Jidhafs', 'Sanabis'],
    'United Arab Emirates': ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman', 'Ras Al Khaimah', 'Fujairah', 'Umm Al Quwain', 'Al Ain'],
    'Saudi Arabia': ['Riyadh', 'Jeddah', 'Mecca', 'Medina', 'Dammam', 'Khobar', 'Dhahran', 'Taif', 'Buraidah', 'Tabuk'],
    'Kuwait': ['Kuwait City', 'Hawalli', 'Farwaniya', 'Ahmadi', 'Jahra', 'Mubarak Al-Kabeer'],
    'Qatar': ['Doha', 'Al Rayyan', 'Al Wakrah', 'Al Khor', 'Lusail', 'Mesaieed'],
    'Oman': ['Muscat', 'Salalah', 'Sohar', 'Nizwa', 'Sur', 'Ibri', 'Buraimi'],
    'Jordan': ['Amman', 'Zarqa', 'Irbid', 'Aqaba', 'Salt', 'Madaba', 'Karak'],
    'Lebanon': ['Beirut', 'Tripoli', 'Sidon', 'Tyre', 'Zahle', 'Jounieh', 'Byblos'],
    'Egypt': ['Cairo', 'Alexandria', 'Giza', 'Shubra El Kheima', 'Port Said', 'Suez', 'Luxor', 'Aswan'],
    'Turkey': ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Antalya', 'Adana', 'Konya', 'Gaziantep'],
    'India': ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Chandigarh', 'Jammu and Kashmir', 'Ladakh', 'Puducherry', 'Andaman and Nicobar Islands', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep'],
    'Pakistan': ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Peshawar', 'Quetta'],
    'Bangladesh': ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi', 'Khulna', 'Barisal', 'Rangpur', 'Mymensingh'],
    'United States': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'United Kingdom': ['London', 'Birmingham', 'Manchester', 'Glasgow', 'Liverpool', 'Leeds', 'Sheffield', 'Edinburgh', 'Bristol', 'Leicester'],
    'Canada': ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Winnipeg', 'Quebec City', 'Hamilton', 'Kitchener'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Newcastle', 'Canberra', 'Wollongong', 'Hobart'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt', 'Stuttgart', 'Düsseldorf', 'Dortmund', 'Essen', 'Leipzig'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille'],
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania'],
    'Spain': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Málaga', 'Murcia', 'Palma', 'Las Palmas', 'Bilbao'],
    'Japan': ['Tokyo', 'Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Kawasaki', 'Kyoto', 'Saitama'],
    'China': ['Shanghai', 'Beijing', 'Chongqing', 'Tianjin', 'Guangzhou', 'Shenzhen', 'Wuhan', 'Dongguan', 'Chengdu', 'Nanjing'],
    'South Korea': ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon', 'Gwangju', 'Suwon', 'Ulsan', 'Changwon', 'Goyang'],
    'Brazil': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza', 'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre'],
    'Mexico': ['Mexico City', 'Guadalajara', 'Monterrey', 'Puebla', 'Tijuana', 'León', 'Juárez', 'Zapopan', 'Nezahualcóyotl', 'Chihuahua'],
    'Argentina': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'San Miguel de Tucumán', 'La Plata', 'Mar del Plata', 'Salta', 'Santa Fe', 'San Juan'],
    'South Africa': ['Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Port Elizabeth', 'Bloemfontein', 'East London', 'Pietermaritzburg', 'Nelspruit', 'Kimberley'],
    'Nigeria': ['Lagos', 'Kano', 'Ibadan', 'Benin City', 'Port Harcourt', 'Jos', 'Ilorin', 'Abuja', 'Kaduna', 'Maiduguri'],
    'Kenya': ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Thika', 'Malindi', 'Kitale', 'Garissa', 'Kakamega'],
    'Morocco': ['Casablanca', 'Rabat', 'Fez', 'Marrakech', 'Agadir', 'Tangier', 'Meknes', 'Oujda', 'Kenitra', 'Tetouan'],
    'Tunisia': ['Tunis', 'Sfax', 'Sousse', 'Kairouan', 'Bizerte', 'Gabès', 'Ariana', 'Gafsa', 'Monastir', 'Ben Arous'],
    'Algeria': ['Algiers', 'Oran', 'Constantine', 'Annaba', 'Blida', 'Batna', 'Djelfa', 'Sétif', 'Sidi Bel Abbès', 'Biskra'],
    'Libya': ['Tripoli', 'Benghazi', 'Misrata', 'Bayda', 'Zawiya', 'Ajdabiya', 'Zuwara', 'Tobruk', 'Sabha', 'Derna'],
    'Sudan': ['Khartoum', 'Omdurman', 'Port Sudan', 'Kassala', 'El Gedaref', 'Nyala', 'Wad Madani', 'El Fasher', 'Kosti', 'Al Qadarif'],
    'Ethiopia': ['Addis Ababa', 'Dire Dawa', 'Mekelle', 'Gondar', 'Awassa', 'Bahir Dar', 'Jimma', 'Dessie', 'Jijiga', 'Shashamane'],
    'Ghana': ['Accra', 'Kumasi', 'Tamale', 'Sekondi-Takoradi', 'Sunyani', 'Cape Coast', 'Koforidua', 'Techiman', 'Ho', 'Wa'],
    'Senegal': ['Dakar', 'Thiès', 'Kaolack', 'Ziguinchor', 'Saint-Louis', 'Touba', 'Diourbel', 'Louga', 'Tambacounda', 'Kolda'],
    'Ivory Coast': ['Abidjan', 'Bouaké', 'Daloa', 'San-Pédro', 'Divo', 'Korhogo', 'Anyama', 'Man', 'Gagnoa', 'Soubré'],
    'Cameroon': ['Douala', 'Yaoundé', 'Garoua', 'Bamenda', 'Maroua', 'Ngaoundéré', 'Kousséri', 'Bafoussam', 'Nkongsamba', 'Bertoua'],
    'Uganda': ['Kampala', 'Gulu', 'Lira', 'Mbarara', 'Jinja', 'Bwizibwera', 'Mbale', 'Mukono', 'Kasese', 'Masaka'],
    'Tanzania': ['Dar es Salaam', 'Mwanza', 'Arusha', 'Dodoma', 'Mbeya', 'Morogoro', 'Tanga', 'Kahama', 'Tabora', 'Zanzibar'],
    'Zambia': ['Lusaka', 'Ndola', 'Kitwe', 'Kabwe', 'Chingola', 'Mufulira', 'Luanshya', 'Livingstone', 'Kasama', 'Chipata'],
    'Zimbabwe': ['Harare', 'Bulawayo', 'Chitungwiza', 'Mutare', 'Gweru', 'Kwekwe', 'Kadoma', 'Masvingo', 'Chinhoyi', 'Marondera'],
    'Botswana': ['Gaborone', 'Francistown', 'Molepolole', 'Selebi-Phikwe', 'Maun', 'Serowe', 'Kanye', 'Mahalapye', 'Mochudi', 'Mogoditshane'],
    'Namibia': ['Windhoek', 'Rundu', 'Walvis Bay', 'Oshakati', 'Swakopmund', 'Katima Mulilo', 'Grootfontein', 'Rehoboth', 'Otjiwarongo', 'Okahandja'],
    'Lesotho': ['Maseru', 'Teyateyaneng', 'Mafeteng', 'Hlotse', 'Mohale\'s Hoek', 'Quthing', 'Peka', 'Butha-Buthe', 'Mokhotlong', 'Thaba-Tseka'],
    'Swaziland': ['Mbabane', 'Manzini', 'Big Bend', 'Malkerns', 'Nhlangano', 'Mhlume', 'Hluti', 'Simunye', 'Piggs Peak', 'Siteki']
}

# India States and Districts data
INDIA_STATES_DISTRICTS = {
    'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Tirupati', 'Kadapa', 'Anantapur', 'Chittoor', 'Ongole', 'Srikakulam', 'Vizianagaram', 'East Godavari', 'West Godavari', 'Krishna', 'Prakasam', 'YSR Kadapa'],
    'Arunachal Pradesh': ['Itanagar', 'Naharlagun', 'Pasighat', 'Tezpur', 'Dibrugarh', 'Tawang', 'Bomdila', 'Ziro', 'Along', 'Roing', 'Anini', 'Changlang', 'Khonsa', 'Namsai', 'Tezu'],
    'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Tezpur', 'Nagaon', 'Tinsukia', 'Barpeta', 'Dhubri', 'Kokrajhar', 'Goalpara', 'Bongaigaon', 'Karimganj', 'Hailakandi', 'Cachar'],
    'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga', 'Purnia', 'Arrah', 'Begusarai', 'Katihar', 'Munger', 'Chapra', 'Bettiah', 'Motihari', 'Saharsa', 'Hajipur'],
    'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Rajnandgaon', 'Durg', 'Raigarh', 'Ambikapur', 'Jagdalpur', 'Chirmiri', 'Dhamtari', 'Mahasamund', 'Kanker', 'Surguja', 'Balod'],
    'Goa': ['Panaji', 'Margao', 'Vasco da Gama', 'Mapusa', 'Ponda', 'Mormugao', 'Curchorem', 'Sanquelim', 'Bicholim', 'Valpoi', 'Canacona', 'Pernem', 'Sanguem', 'Quepem', 'Dharbandora'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Jamnagar', 'Junagadh', 'Gandhinagar', 'Nadiad', 'Morbi', 'Surendranagar', 'Mehsana', 'Bharuch', 'Anand', 'Palanpur'],
    'Haryana': ['Gurgaon', 'Faridabad', 'Panipat', 'Ambala', 'Yamunanagar', 'Rohtak', 'Hisar', 'Karnal', 'Sonipat', 'Panchkula', 'Bhiwani', 'Sirsa', 'Jind', 'Kaithal', 'Rewari'],
    'Himachal Pradesh': ['Shimla', 'Dharamshala', 'Solan', 'Mandi', 'Palampur', 'Kullu', 'Manali', 'Chamba', 'Una', 'Bilaspur', 'Nahan', 'Hamirpur', 'Kangra', 'Kinnaur', 'Lahaul Spiti'],
    'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro', 'Deoghar', 'Phusro', 'Hazaribagh', 'Giridih', 'Ramgarh', 'Medininagar', 'Chatra', 'Koderma', 'Jamtara', 'Sahibganj', 'Pakur'],
    'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum', 'Gulbarga', 'Davanagere', 'Bellary', 'Bijapur', 'Shimoga', 'Tumkur', 'Raichur', 'Bidar', 'Hassan', 'Chitradurga'],
    'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Palakkad', 'Malappuram', 'Kannur', 'Kasaragod', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam', 'Wayanad'],
    'Madhya Pradesh': ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur', 'Ujjain', 'Sagar', 'Dewas', 'Satna', 'Ratlam', 'Murwara', 'Singrauli', 'Rewa', 'Neemuch', 'Chhindwara', 'Guna'],
    'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Aurangabad', 'Solapur', 'Amravati', 'Kolhapur', 'Sangli', 'Malegaon', 'Jalgaon', 'Akola', 'Latur', 'Dhule'],
    'Manipur': ['Imphal', 'Thoubal', 'Bishnupur', 'Churachandpur', 'Senapati', 'Tamenglong', 'Chandel', 'Ukhrul', 'Kangpokpi', 'Jiribam', 'Kakching', 'Kamjong', 'Noney', 'Pherzawl', 'Tengnoupal'],
    'Meghalaya': ['Shillong', 'Tura', 'Jowai', 'Nongstoin', 'Williamnagar', 'Baghmara', 'Resubelpara', 'Amlarem', 'Mawkyrwat', 'Mairang', 'Mawphlang', 'Sohra', 'Nongpoh', 'Khliehriat', 'Mawkyrwat'],
    'Mizoram': ['Aizawl', 'Lunglei', 'Saiha', 'Champhai', 'Kolasib', 'Serchhip', 'Lawngtlai', 'Mamit', 'Saitual', 'Hnahthial', 'Khawzawl', 'Saitual', 'Darlawn', 'Tlabung', 'Vairengte'],
    'Nagaland': ['Kohima', 'Dimapur', 'Mokokchung', 'Tuensang', 'Wokha', 'Zunheboto', 'Phek', 'Mon', 'Longleng', 'Kiphire', 'Peren', 'Noklak', 'Shamator', 'Tseminyu', 'Niuland'],
    'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Berhampur', 'Sambalpur', 'Puri', 'Balasore', 'Bhadrak', 'Baripada', 'Jharsuguda', 'Bargarh', 'Sundargarh', 'Kendujhar', 'Mayurbhanj', 'Jajpur'],
    'Punjab': ['Chandigarh', 'Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda', 'Mohali', 'Batala', 'Pathankot', 'Moga', 'Abohar', 'Malerkotla', 'Khanna', 'Phagwara', 'Muktsar'],
    'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Bikaner', 'Ajmer', 'Bharatpur', 'Bhilwara', 'Alwar', 'Ganganagar', 'Sikar', 'Pali', 'Tonk', 'Kishangarh', 'Beawar'],
    'Sikkim': ['Gangtok', 'Namchi', 'Mangan', 'Gyalshing', 'Ravongla', 'Singtam', 'Rangpo', 'Jorethang', 'Pakyong', 'Rhenock', 'Chungthang', 'Lachung', 'Lachen', 'Yuksom', 'Pelling'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli', 'Tiruppur', 'Erode', 'Vellore', 'Thoothukkudi', 'Dindigul', 'Thanjavur', 'Ranipet', 'Sivakasi', 'Karur'],
    'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Ramagundam', 'Mahbubnagar', 'Nalgonda', 'Adilabad', 'Suryapet', 'Miryalaguda', 'Jagtial', 'Sangareddy', 'Vikarabad', 'Mancherial'],
    'Tripura': ['Agartala', 'Dharmanagar', 'Udaipur', 'Ambassa', 'Kailashahar', 'Belonia', 'Khowai', 'Teliamura', 'Sabroom', 'Sonamura', 'Kamalpur', 'Amarpur', 'Jirania', 'Melaghar', 'Santirbazar'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Meerut', 'Varanasi', 'Allahabad', 'Bareilly', 'Aligarh', 'Moradabad', 'Saharanpur', 'Gorakhpur', 'Firozabad', 'Jhansi', 'Muzaffarnagar'],
    'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Rudrapur', 'Kashipur', 'Haldwani', 'Rishikesh', 'Ramnagar', 'Pithoragarh', 'Manglaur', 'Nainital', 'Mussoorie', 'Almora', 'Pauri', 'Champawat'],
    'West Bengal': ['Kolkata', 'Asansol', 'Siliguri', 'Durgapur', 'Bardhaman', 'Malda', 'Bahraich', 'Habra', 'Kharagpur', 'Shantipur', 'Dankuni', 'Dhulian', 'Ranaghat', 'Haldia', 'Medinipur'],
    'Delhi': ['New Delhi', 'Central Delhi', 'East Delhi', 'North Delhi', 'North East Delhi', 'North West Delhi', 'Shahdara', 'South Delhi', 'South East Delhi', 'South West Delhi', 'West Delhi'],
    'Chandigarh': ['Chandigarh'],
    'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Pulwama', 'Kupwara', 'Budgam', 'Ganderbal', 'Bandipora', 'Kulgam', 'Shopian', 'Rajouri', 'Poonch', 'Doda', 'Ramban'],
    'Ladakh': ['Leh', 'Kargil'],
    'Puducherry': ['Puducherry', 'Karaikal', 'Mahe', 'Yanam'],
    'Andaman and Nicobar Islands': ['Port Blair', 'Diglipur', 'Mayabunder', 'Rangat', 'Hut Bay', 'Car Nicobar', 'Nancowry', 'Katchal', 'Teressa', 'Chowra'],
    'Dadra and Nagar Haveli and Daman and Diu': ['Silvassa', 'Daman', 'Diu'],
    'Lakshadweep': ['Kavaratti', 'Agatti', 'Amini', 'Andrott', 'Kadmat', 'Kalpeni', 'Kiltan', 'Minicoy', 'Chettlat', 'Bitra']
}

# Business Categories and Subcategories
BUSINESS_CATEGORIES = {
    'Fitness & Sports': {
        'Gym & Fitness': [
            'Gym', 'Fitness Centre', 'Personal Training Studio', 'Bootcamp', 'HIIT Studio', 
            'Functional Fitness', 'Strength Training', 'Weightlifting', 'Powerlifting', 'Bodybuilding',
            'Calisthenics', 'CrossFit', 'Functional Movement', 'Mobility Training', 'Flexibility Training'
        ],
        'Yoga & Pilates': [
            'Yoga Studio', 'Pilates Studio', 'Hot Yoga', 'Bikram Yoga', 'Ashtanga Yoga', 
            'Hatha Yoga', 'Vinyasa Yoga', 'Power Yoga', 'Yin Yoga', 'Restorative Yoga', 
            'Prenatal Yoga', 'Kids Yoga', 'Mat Pilates', 'Reformer Pilates', 'Contemporary Pilates',
            'Barre Studio', 'Aerial Yoga', 'Aerial Silks', 'Aerial Hoop'
        ],
        'Martial Arts': [
            'Martial Arts', 'Boxing Gym', 'Kickboxing', 'Karate Dojo', 'Taekwondo', 
            'Judo', 'Jujitsu', 'Muay Thai', 'Brazilian Jiu-Jitsu', 'Krav Maga'
        ],
        'Dance & Movement': [
            'Dance Studio', 'Ballet Studio', 'Zumba Studio', 'Aerobic Centre', 
            'Pole Dancing Studio', 'Contemporary Dance', 'Hip Hop Dance', 'Latin Dance',
            'Ballroom Dance', 'Salsa Studio', 'Belly Dance', 'Flamenco'
        ],
        'Water Sports': [
            'Swimming Pool', 'Aqua Fitness', 'Water Aerobics', 'Swimming Lessons',
            'Water Polo', 'Synchronized Swimming', 'Diving Training', 'Surfing School'
        ],
        'Sports & Athletics': [
            'Sports Centre', 'Sports Complex', 'Athletic Club', 'Tennis Club', 'Squash Club',
            'Badminton Club', 'Basketball Court', 'Volleyball Court', 'Football Training',
            'Soccer Training', 'Cricket Club', 'Hockey Club', 'Rugby Club', 'Athletics Track',
            'Running Club', 'Marathon Training', 'Triathlon Training', 'Cycling Club',
            'Mountain Biking', 'Rock Climbing Gym', 'Bouldering', 'Indoor Climbing',
            'Trampoline Park', 'Gymnastics Centre', 'Acrobatics', 'Circus Training'
        ],
        'Wellness & Recovery': [
            'Meditation Centre', 'Wellness Centre', 'Spa Fitness', 'Rehabilitation Centre',
            'Physiotherapy', 'Sports Therapy', 'Massage Therapy', 'Chiropractic',
            'Stretching Studio', 'Recovery Centre', 'Cryotherapy', 'Sauna Fitness',
            'Steam Room', 'Infrared Sauna', 'Salt Therapy', 'Floatation Therapy'
        ],
        'Specialized Training': [
            'Parkour', 'Free Running', 'Obstacle Course Training', 'Spin Studio', 
            'Cycling Studio', 'Indoor Cycling', 'Sports Nutrition', 'Fitness Nutrition',
            'Dietitian', 'Nutritionist', 'Fitness Equipment', 'Gym Equipment Rental',
            'Fitness Consulting', 'Corporate Wellness', 'Employee Fitness', 'Senior Fitness',
            'Youth Fitness', 'Adaptive Fitness', 'Inclusive Fitness', 'Therapeutic Recreation'
        ]
    },
    'Education': {
        'Schools & Universities': [
            'Primary School', 'Secondary School', 'High School', 'International School',
            'University', 'College', 'Community College', 'Technical Institute',
            'Vocational School', 'Trade School', 'Language School', 'Online School'
        ],
        'Training & Courses': [
            'Professional Training', 'Skill Development', 'Certification Courses',
            'Workshop Center', 'Seminar Hall', 'Conference Center', 'Training Institute',
            'Computer Training', 'IT Training', 'Business Training', 'Leadership Training'
        ],
        'Specialized Education': [
            'Music School', 'Art School', 'Drama School', 'Cooking School',
            'Driving School', 'Aviation School', 'Maritime School', 'Nursing School',
            'Medical School', 'Law School', 'Engineering School', 'Architecture School'
        ]
    },
    'Healthcare': {
        'Medical Services': [
            'Hospital', 'Clinic', 'Medical Center', 'Health Center', 'Urgent Care',
            'Emergency Room', 'Surgery Center', 'Diagnostic Center', 'Laboratory',
            'Pharmacy', 'Dental Clinic', 'Eye Clinic', 'ENT Clinic', 'Cardiology Center'
        ],
        'Specialized Care': [
            'Pediatric Clinic', 'Women\'s Health', 'Men\'s Health', 'Geriatric Care',
            'Mental Health Center', 'Psychiatric Clinic', 'Addiction Treatment',
            'Rehabilitation Center', 'Physical Therapy', 'Occupational Therapy',
            'Speech Therapy', 'Respiratory Therapy', 'Chiropractic Clinic'
        ],
        'Wellness & Alternative': [
            'Wellness Center', 'Spa', 'Massage Therapy', 'Acupuncture', 'Homeopathy',
            'Naturopathy', 'Ayurveda', 'Traditional Medicine', 'Holistic Health',
            'Meditation Center', 'Yoga Therapy', 'Energy Healing', 'Crystal Therapy'
        ]
    },
    'Food & Beverage': {
        'Restaurants': [
            'Fine Dining', 'Casual Dining', 'Fast Food', 'Cafe', 'Coffee Shop',
            'Tea House', 'Juice Bar', 'Smoothie Bar', 'Ice Cream Shop', 'Dessert Shop',
            'Bakery', 'Pizzeria', 'Burger Joint', 'Sandwich Shop', 'Deli'
        ],
        'Specialized Cuisine': [
            'Italian Restaurant', 'Chinese Restaurant', 'Indian Restaurant', 'Thai Restaurant',
            'Japanese Restaurant', 'Korean Restaurant', 'Mexican Restaurant', 'Mediterranean Restaurant',
            'Middle Eastern Restaurant', 'African Restaurant', 'Vegetarian Restaurant', 'Vegan Restaurant'
        ],
        'Food Services': [
            'Catering Service', 'Food Truck', 'Food Court', 'Market', 'Grocery Store',
            'Supermarket', 'Convenience Store', 'Butcher Shop', 'Fish Market', 'Organic Store',
            'Health Food Store', 'Wine Shop', 'Liquor Store', 'Beverage Store'
        ]
    },
    'Retail & Shopping': {
        'Fashion & Apparel': [
            'Clothing Store', 'Fashion Boutique', 'Shoe Store', 'Accessories Store',
            'Jewelry Store', 'Watch Store', 'Handbag Store', 'Luggage Store',
            'Sportswear Store', 'Swimwear Store', 'Lingerie Store', 'Children\'s Clothing'
        ],
        'Electronics & Technology': [
            'Electronics Store', 'Computer Store', 'Mobile Phone Store', 'Camera Store',
            'Audio Store', 'Gaming Store', 'Tech Accessories', 'Software Store',
            'IT Services', 'Computer Repair', 'Phone Repair', 'Electronics Repair'
        ],
        'Home & Lifestyle': [
            'Furniture Store', 'Home Decor', 'Kitchen Store', 'Bathroom Store',
            'Garden Center', 'Hardware Store', 'Paint Store', 'Lighting Store',
            'Carpet Store', 'Flooring Store', 'Appliance Store', 'Bedding Store'
        ],
        'Specialty Retail': [
            'Bookstore', 'Toy Store', 'Pet Store', 'Flower Shop', 'Gift Shop',
            'Stationery Store', 'Art Supply Store', 'Craft Store', 'Hobby Store',
            'Sports Store', 'Outdoor Store', 'Bicycle Shop', 'Auto Parts Store'
        ]
    },
    'Professional Services': {
        'Business Services': [
            'Accounting Firm', 'Law Firm', 'Consulting Firm', 'Marketing Agency',
            'Advertising Agency', 'PR Agency', 'HR Services', 'Recruitment Agency',
            'Business Center', 'Co-working Space', 'Virtual Office', 'Meeting Room'
        ],
        'Financial Services': [
            'Bank', 'Credit Union', 'Investment Firm', 'Insurance Agency',
            'Financial Advisor', 'Tax Service', 'Payday Loan', 'Currency Exchange',
            'ATM', 'Financial Planning', 'Wealth Management', 'Mortgage Broker'
        ],
        'Real Estate': [
            'Real Estate Agency', 'Property Management', 'Real Estate Developer',
            'Real Estate Consultant', 'Property Appraisal', 'Real Estate Investment',
            'Commercial Real Estate', 'Residential Real Estate', 'Land Development'
        ]
    },
    'Manufacturing & Industry': {
        'Manufacturing': [
            'Factory', 'Manufacturing Plant', 'Production Facility', 'Assembly Plant',
            'Textile Factory', 'Food Processing Plant', 'Chemical Plant', 'Pharmaceutical Plant',
            'Automotive Plant', 'Electronics Factory', 'Plastic Factory', 'Metal Factory'
        ],
        'Industrial Services': [
            'Industrial Equipment', 'Machinery Sales', 'Industrial Maintenance',
            'Industrial Cleaning', 'Industrial Safety', 'Quality Control', 'Testing Laboratory',
            'Packaging Service', 'Logistics Service', 'Warehouse', 'Distribution Center'
        ],
        'Construction & Engineering': [
            'Construction Company', 'Engineering Firm', 'Architecture Firm',
            'Contractor', 'Building Materials', 'Construction Equipment', 'Surveying Service',
            'Project Management', 'Construction Consulting', 'Building Inspection'
        ]
    },
    'Entertainment & Recreation': {
        'Entertainment Venues': [
            'Cinema', 'Theater', 'Concert Hall', 'Music Venue', 'Comedy Club',
            'Nightclub', 'Bar', 'Pub', 'Karaoke Bar', 'Bowling Alley', 'Arcade',
            'Gaming Center', 'Escape Room', 'Virtual Reality Center'
        ],
        'Recreation & Leisure': [
            'Amusement Park', 'Water Park', 'Theme Park', 'Adventure Park',
            'Mini Golf', 'Golf Course', 'Driving Range', 'Skating Rink', 'Ice Rink',
            'Billiards Hall', 'Pool Hall', 'Darts Bar', 'Board Game Cafe'
        ],
        'Cultural & Arts': [
            'Art Gallery', 'Museum', 'Cultural Center', 'Art Studio', 'Pottery Studio',
            'Photography Studio', 'Recording Studio', 'Film Studio', 'Dance Studio',
            'Music Studio', 'Theater Company', 'Art School', 'Cultural Institute'
        ]
    },
    'Transportation & Logistics': {
        'Transportation Services': [
            'Taxi Service', 'Ride Share', 'Bus Service', 'Shuttle Service',
            'Limousine Service', 'Car Rental', 'Truck Rental', 'Moving Service',
            'Delivery Service', 'Courier Service', 'Freight Service', 'Logistics Company'
        ],
        'Automotive Services': [
            'Car Dealership', 'Auto Repair', 'Auto Parts', 'Car Wash', 'Auto Detailing',
            'Tire Shop', 'Oil Change', 'Auto Body Shop', 'Auto Glass', 'Auto Insurance',
            'Driving School', 'Motorcycle Dealer', 'Boat Dealer', 'RV Dealer'
        ],
        'Transportation Infrastructure': [
            'Gas Station', 'Charging Station', 'Parking Garage', 'Parking Lot',
            'Toll Booth', 'Rest Area', 'Truck Stop', 'Bus Station', 'Train Station',
            'Airport', 'Port', 'Marina', 'Heliport'
        ]
    }
}

# Legacy fitness types for backward compatibility
FITNESS_TYPES = [
    'Gym', 'Fitness Centre', 'Yoga Studio', 'Pilates Studio', 'CrossFit', 'Martial Arts',
    'Boxing Gym', 'Kickboxing', 'Karate Dojo', 'Taekwondo', 'Judo', 'Jujitsu',
    'Swimming Pool', 'Aqua Fitness', 'Water Aerobics', 'Dance Studio', 'Ballet Studio',
    'Zumba Studio', 'Aerobic Centre', 'Spin Studio', 'Cycling Studio', 'Indoor Cycling',
    'Sports Centre', 'Sports Complex', 'Athletic Club', 'Tennis Club', 'Squash Club',
    'Badminton Club', 'Basketball Court', 'Volleyball Court', 'Football Training',
    'Soccer Training', 'Cricket Club', 'Hockey Club', 'Rugby Club', 'Athletics Track',
    'Running Club', 'Marathon Training', 'Triathlon Training', 'Cycling Club',
    'Mountain Biking', 'Rock Climbing Gym', 'Bouldering', 'Indoor Climbing',
    'Trampoline Park', 'Gymnastics Centre', 'Acrobatics', 'Circus Training',
    'Pole Dancing Studio', 'Aerial Yoga', 'Aerial Silks', 'Aerial Hoop',
    'Barre Studio', 'Reformer Pilates', 'Mat Pilates', 'Contemporary Pilates',
    'Hot Yoga', 'Bikram Yoga', 'Ashtanga Yoga', 'Hatha Yoga', 'Vinyasa Yoga',
    'Power Yoga', 'Yin Yoga', 'Restorative Yoga', 'Prenatal Yoga', 'Kids Yoga',
    'Meditation Centre', 'Wellness Centre', 'Spa Fitness', 'Rehabilitation Centre',
    'Physiotherapy', 'Sports Therapy', 'Massage Therapy', 'Chiropractic',
    'Personal Training Studio', 'Bootcamp', 'HIIT Studio', 'Functional Fitness',
    'Strength Training', 'Weightlifting', 'Powerlifting', 'Bodybuilding',
    'Calisthenics', 'Parkour', 'Free Running', 'Obstacle Course Training',
    'Functional Movement', 'Mobility Training', 'Flexibility Training',
    'Stretching Studio', 'Recovery Centre', 'Cryotherapy', 'Sauna Fitness',
    'Steam Room', 'Infrared Sauna', 'Salt Therapy', 'Floatation Therapy',
    'Sports Nutrition', 'Fitness Nutrition', 'Dietitian', 'Nutritionist',
    'Fitness Equipment', 'Gym Equipment Rental', 'Fitness Consulting',
    'Corporate Wellness', 'Employee Fitness', 'Senior Fitness', 'Youth Fitness',
    'Adaptive Fitness', 'Inclusive Fitness', 'Therapeutic Recreation'
]
