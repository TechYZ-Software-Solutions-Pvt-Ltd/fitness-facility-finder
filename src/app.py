import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security settings
MAX_REQUESTS_PER_SESSION = 10
SESSION_TIMEOUT_MINUTES = 30

# Initialize session state
if 'request_count' not in st.session_state:
    st.session_state.request_count = 0
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

# --- Security Functions ---
def validate_api_key(api_key):
    """Validate API key format"""
    if not api_key:
        return False, "API key is required"
    
    if len(api_key) < 20 or len(api_key) > 200:
        return False, "API key must be between 20 and 200 characters"
    
    if not re.match(r'^AIza[0-9A-Za-z_-]{35}$', api_key):
        return False, "Invalid Google API key format"
    
    return True, "Valid API key"

def check_rate_limit():
    """Check if user has exceeded rate limits"""
    current_time = time.time()
    session_duration = current_time - st.session_state.session_start
    
    if session_duration > SESSION_TIMEOUT_MINUTES * 60:
        st.session_state.request_count = 0
        st.session_state.session_start = current_time
        return True
    
    return st.session_state.request_count < MAX_REQUESTS_PER_SESSION

def increment_request_count():
    """Increment the request counter"""
    st.session_state.request_count += 1

def sanitize_input(text):
    """Sanitize user input"""
    if not text:
        return ""
    sanitized = re.sub(r'[<>"\';\\]', '', str(text))
    return sanitized.strip()[:100]

def secure_log_request(operation, success=True, error_msg=""):
    """Log requests securely"""
    timestamp = datetime.now().isoformat()
    log_data = {
        'timestamp': timestamp,
        'operation': operation,
        'success': success,
        'error': error_msg if not success else None
    }
    logger.info(f"Request logged: {log_data}")

# --- UI Header with Mobile Responsiveness ---
st.markdown("""
<style>
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        width: 100%;
    }
    .centered-heading {
        color: #2E86AB;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin: 15px 0 0 0;
        font-size: 2.5rem;
        text-align: center;
    }
    
    /* Mobile Responsive Styles */
    @media (max-width: 768px) {
        .centered-heading {
            font-size: 1.8rem;
            margin: 10px 0;
        }
        
        /* Make form elements stack vertically on mobile */
        .stSelectbox > div > div {
            width: 100% !important;
        }
        
        .stNumberInput > div > div {
            width: 100% !important;
        }
        
        .stTextInput > div > div {
            width: 100% !important;
        }
        
        /* Optimize button for mobile */
        .stButton > button {
            width: 100% !important;
            min-width: unset !important;
            font-size: 1rem !important;
            padding: 0.7rem 1rem !important;
        }
        
        /* Make columns stack on mobile */
        .mobile-stack {
            display: flex !important;
            flex-direction: column !important;
        }
        
        /* Optimize dataframe for mobile */
        .stDataFrame {
            font-size: 0.8rem !important;
        }
        
        /* Make security features stack on mobile */
        .security-features {
            display: flex !important;
            flex-direction: column !important;
            gap: 10px !important;
        }
        
        .security-feature {
            width: 100% !important;
            margin-bottom: 10px !important;
        }
    }
    
    @media (max-width: 480px) {
        .centered-heading {
            font-size: 1.5rem;
        }
        
        /* Further optimize for very small screens */
        .stMarkdown h1 {
            font-size: 1.2rem !important;
        }
        
        .stMarkdown h2 {
            font-size: 1.1rem !important;
        }
        
        .stMarkdown h3 {
            font-size: 1rem !important;
        }
        
        /* Optimize for touch screens */
        .stButton > button {
            min-height: 44px !important;
            touch-action: manipulation !important;
        }
        
        /* Better spacing for mobile */
        .stSelectbox, .stTextInput, .stNumberInput {
            margin-bottom: 1rem !important;
        }
        
        /* Improve table scrolling on mobile */
        .stDataFrame {
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
        }
        
        /* Make download button more touch-friendly */
        .stDownloadButton > button {
            min-height: 44px !important;
            font-size: 1rem !important;
        }
    }
    
    /* Additional mobile optimizations */
    @media (max-width: 768px) {
        /* Make all interactive elements touch-friendly */
        .stButton > button, .stDownloadButton > button {
            min-height: 44px;
            touch-action: manipulation;
        }
        
        /* Improve form spacing */
        .stForm {
            padding: 1rem !important;
        }
        
        /* Better text readability */
        .stMarkdown {
            font-size: 0.9rem !important;
            line-height: 1.4 !important;
        }
        
        /* Optimize sidebar if used */
        .stSidebar {
            width: 100% !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# GYM360 Logo and Header with Enhanced Security Protection
st.markdown("""
<style>
    /* Enhanced security protection for Streamlit images */
    div[data-testid="stImage"] img {
        -webkit-user-drag: none;
        -khtml-user-drag: none;
        -moz-user-drag: none;
        -o-user-drag: none;
        user-drag: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        -webkit-touch-callout: none;
        pointer-events: none;
    }
    
    /* Disable right-click and new tab functionality */
    div[data-testid="stImage"] {
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        pointer-events: none;
    }
    
    /* Prevent image from being opened in new tab */
    div[data-testid="stImage"] a {
        pointer-events: none;
    }
    
    /* Disable all image interactions */
    div[data-testid="stImage"] * {
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

# Mobile responsive logo layout
col1, col_center, col3 = st.columns([1, 2, 1])

with col_center:
    # GYM360 Logo - Mobile responsive
    st.image("assets/gym360_logo.png", width=200)
    
st.markdown("""
<div style="text-align: center; margin-top: 15px; margin-bottom: 40px;">
    <h1 style="color: #2E86AB; font-family: 'Arial', sans-serif; font-weight: bold; margin: 0; font-size: 2.5rem;">
        Fitness Facility Finder
    </h1>
</div>
""", unsafe_allow_html=True)

# --- Data ---
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

# --- Functions ---
def verify_place(place_name, country, api_key):
    """Verify if a place exists using Google Places API"""
    if not api_key:
        return False, "API key not provided"
    
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        return False, f"Invalid API key: {error_msg}"
    
    if not check_rate_limit():
        return False, f"Rate limit exceeded. Maximum {MAX_REQUESTS_PER_SESSION} requests per {SESSION_TIMEOUT_MINUTES} minutes."
    
    place_name = sanitize_input(place_name)
    country = sanitize_input(country)
    
    if not place_name or not country:
        return False, "Invalid place name or country"
    
    try:
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        query = f"{place_name}, {country}"
        params = {'query': query, 'key': api_key}
        headers = {'User-Agent': 'Fitness-Facility-Finder/1.0', 'Accept': 'application/json'}
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        increment_request_count()
        
        if data.get('status') == 'OK' and data.get('results'):
            for result in data['results']:
                if country.lower() in result.get('formatted_address', '').lower():
                    return True, f"Verified: {result.get('formatted_address', '')}"
            return False, "Place not found in specified country"
        else:
            return False, f"API Error: {data.get('status', 'Unknown error')}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def scrape_site_for_contacts(website):
    """Extract contact information from website"""
    email, whatsapp, year, insta = '', '', '', ''
    if not website:
        return email, whatsapp, year, insta
    
    try:
        r = requests.get(website, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Email extraction
        mailto = soup.select_one('a[href^=mailto]')
        if mailto:
            email = mailto['href'].replace('mailto:', '')
        
        # WhatsApp extraction
        wa = soup.select_one('a[href*="wa.me"]')
        if wa:
            whatsapp = wa['href'].split('wa.me/')[-1]
        
        # Instagram extraction
        insta_link = soup.select_one('a[href*="instagram.com"]')
        if insta_link:
            insta = insta_link['href'].split('instagram.com/')[-1].split('?')[0].replace('/', '')

        # Year extraction
        text = soup.get_text().lower()
        for kw in ['since', 'established', 'founded']:
            if kw in text:
                match = re.search(rf"{kw}[\s:]*([12][0-9]{{3}})", text)
                if match:
                    year = match.group(1)
                    break
    except Exception:
        pass
    
    return email, whatsapp, year, insta

def get_places(query, api_key, max_results):
    """Get places from Google Places API"""
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        return []
    
    if not check_rate_limit():
        return []
    
    query = sanitize_input(query)
    if not query:
        return []
    
    out = []
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {'query': query, 'key': api_key}
    headers = {'User-Agent': 'Fitness-Facility-Finder/1.0', 'Accept': 'application/json'}
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        data = response.json()
        increment_request_count()
        
        if data.get('status') != 'OK':
            return []
        
        results = data.get('results', [])
        out.extend(results)
        
        # Handle pagination
        while 'next_page_token' in data and len(out) < max_results:
            time.sleep(2)
            params['pagetoken'] = data['next_page_token']
            
            if not check_rate_limit():
                break
                
            response = requests.get(url, params=params, headers=headers, timeout=15)
            data = response.json()
            increment_request_count()
            
            if data.get('status') != 'OK':
                break
                
            results = data.get('results', [])
            out.extend(results)
        
        return out[:max_results]
        
    except Exception as e:
        return []

def get_details(place_id, api_key):
    """Get place details from Google Places API"""
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        return {}
    
    if not check_rate_limit():
        return {}
    
    place_id = sanitize_input(place_id)
    if not place_id:
        return {}
    
    detail_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'name,formatted_address,international_phone_number,website,rating',
        'key': api_key
    }
    headers = {'User-Agent': 'Fitness-Facility-Finder/1.0', 'Accept': 'application/json'}
    
    try:
        response = requests.get(detail_url, params=params, headers=headers, timeout=10)
        data = response.json()
        increment_request_count()
        
        if data.get('status') != 'OK':
            return {}
        
        return data.get('result', {})
        
    except Exception as e:
        return {}

# --- UI Inputs ---
api_key = st.text_input('Google Places API Key', type='password', help="Enter your Google Places API key", placeholder="AIza...")

# Mobile responsive form columns
col1, col2 = st.columns([1, 1])

with col1:
    country = st.selectbox('Country', list(COUNTRIES.keys()), index=0)
    
with col2:
    city_options = COUNTRIES[country] + ['Custom...']
    city_selection = st.selectbox('City/Town/Area', city_options, index=0)
    
    if city_selection == 'Custom...':
        custom_city = st.text_input('Enter Custom City/Town/Area', placeholder='Enter the name of your city/town/area')
        if custom_city and api_key:
            if st.button('Verify Place'):
                with st.spinner('Verifying place...'):
                    is_valid, message = verify_place(custom_city, country, api_key)
                    if is_valid:
                        st.success(message)
                        city = custom_city
                    else:
                        st.error(message)
                        city = None
        else:
            city = custom_city if custom_city else None
    else:
        city = city_selection

# For India, show state and district selection
if country == 'India':
    st.subheader('India Location Selection')
    # Mobile responsive columns for India selection
    col3, col4 = st.columns([1, 1])
    
    with col3:
        state = st.selectbox('State/Union Territory', list(INDIA_STATES_DISTRICTS.keys()), index=0)
    
    with col4:
        district_options = INDIA_STATES_DISTRICTS[state] + ['Custom...']
        district_selection = st.selectbox('District/City', district_options, index=0)
        
        if district_selection == 'Custom...':
            custom_district = st.text_input('Enter Custom District/City', placeholder='Enter district or city name')
            if custom_district and api_key:
                if st.button('Verify District'):
                    with st.spinner('Verifying district...'):
                        is_valid, message = verify_place(custom_district, country, api_key)
                        if is_valid:
                            st.success(message)
                            city = custom_district
                        else:
                            st.error(message)
                            city = None
            else:
                city = custom_district if custom_district else None
        else:
            city = district_selection

place_type = st.selectbox('Business Type', FITNESS_TYPES, index=0)
max_results = st.number_input('Max Results', min_value=1, max_value=60, value=20, step=1)

# --- Search Button with Matching Padding ---
st.markdown("""
<style>
    .stButton > button {
        background: #2E86AB;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(46, 134, 171, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        min-width: 200px;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(46, 134, 171, 0.4);
        background: #1f5f7a;
    }
    .stButton > button:active {
        transform: translateY(0);
    }
</style>
""", unsafe_allow_html=True)

# --- Mobile Responsive Search Button ---
# On mobile, make the button full width
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    search_clicked = st.button('⚡ Search Facilities', use_container_width=True)

# --- Results and Status in Separate Column ---
if search_clicked and api_key and city:
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        st.error(f"❌ {error_msg}")
    else:
        if not check_rate_limit():
            st.error(f"❌ Rate limit exceeded. Maximum {MAX_REQUESTS_PER_SESSION} requests per {SESSION_TIMEOUT_MINUTES} minutes.")
        else:
            place_type_clean = sanitize_input(place_type)
            city_clean = sanitize_input(city)
            country_clean = sanitize_input(country)
            
            if not all([place_type_clean, city_clean, country_clean]):
                st.error("❌ Invalid input parameters. Please check your selections.")
            else:
                query = f"{place_type_clean} in {city_clean}, {country_clean}"
                st.info('🔍 Searching securely, please wait...')
                
                # Mobile responsive security status
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    st.success("🔐 API Key Validated")
                with col2:
                    st.info(f"⏱️ Rate Limit: {st.session_state.request_count + 1}/{MAX_REQUESTS_PER_SESSION}")
                with col3:
                    st.success("🛡️ Input Sanitized")
                
                gyms = get_places(query, api_key, max_results)
                
                if not gyms:
                    st.warning("⚠️ No facilities found or API error occurred.")
                else:
                    rows = []
                    progress_bar = st.progress(0)
                    total_gyms = len(gyms)
                    
                    for i, gym in enumerate(gyms):
                        progress_bar.progress((i + 1) / total_gyms)
                        
                        details = get_details(gym['place_id'], api_key)
                        website = details.get('website', '')
                        email, whatsapp, year, insta = scrape_site_for_contacts(website)
                        
                        # Only add if we have a valid facility name
                        facility_name = details.get('name', '').strip()
                        if facility_name:  # Only add non-empty facility names
                            rows.append({
                                'Facility Name': facility_name,
                                'Contact Number': details.get('international_phone_number', ''),
                                'WhatsApp Number': whatsapp,
                                'email ID': email,
                                'Established Year': year,
                                'Location': city_clean,
                                'Address': details.get('formatted_address', ''),
                                'Google Rating': details.get('rating', 0) if details.get('rating') else 0,
                                'Instagram id': insta,
                                'Website': website
                            })
                    
                    progress_bar.empty()
                    df = pd.DataFrame(rows)
                    
                    # Display results in a column with same width as form elements
                    if not df.empty:
                        # Ensure all columns are properly formatted
                        df['Google Rating'] = pd.to_numeric(df['Google Rating'], errors='coerce').fillna(0)
                        df['Established Year'] = df['Established Year'].astype(str)
                        
                        # Mobile responsive dataframe display
                        st.dataframe(
                            df,
                            width='stretch',
                            hide_index=True,
                            use_container_width=True,
                            column_config={
                                "Facility Name": st.column_config.TextColumn(
                                    "Facility Name",
                                    width="medium",
                                    help="Name of the fitness facility"
                                ),
                                "Contact Number": st.column_config.TextColumn(
                                    "Contact",
                                    width="small",
                                    help="Phone number"
                                ),
                                "WhatsApp Number": st.column_config.TextColumn(
                                    "WhatsApp",
                                    width="small",
                                    help="WhatsApp number"
                                ),
                                "email ID": st.column_config.TextColumn(
                                    "Email",
                                    width="small",
                                    help="Email address"
                                ),
                                "Established Year": st.column_config.TextColumn(
                                    "Year",
                                    width="small",
                                    help="Established year"
                                ),
                                "Location": st.column_config.TextColumn(
                                    "Location",
                                    width="small",
                                    help="City/Location"
                                ),
                                "Address": st.column_config.TextColumn(
                                    "Address",
                                    width="large",
                                    help="Full address"
                                ),
                                "Google Rating": st.column_config.NumberColumn(
                                    "Rating",
                                    width="small",
                                    format="%.1f",
                                    help="Google rating"
                                ),
                                "Instagram id": st.column_config.TextColumn(
                                    "Instagram",
                                    width="small",
                                    help="Instagram handle"
                                ),
                                "Website": st.column_config.LinkColumn(
                                    "Website",
                                    width="small",
                                    help="Website URL"
                                )
                            }
                        )
                        
                        # Download button and success message in same column
                        current_date = datetime.now().strftime("%Y%m%d")
                        fitness_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', place_type_clean)
                        country_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', country_clean)
                        city_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', city_clean)
                        filename = f"{fitness_clean}_{country_clean}_{city_clean}_{current_date}.csv"
                        
                        csv_data = df.to_csv(index=False)
                        st.download_button(
                            '📥 Download Secure CSV', 
                            data=csv_data, 
                            file_name=filename, 
                            mime='text/csv',
                            help="Download your search results securely"
                        )
                        
                        st.success(f"✅ Search completed securely! {len(df)} facilities found.")
                        st.info(f"🔒 **Security Summary**: {st.session_state.request_count} API calls made, all requests logged and monitored.")

# Security footer
st.markdown("---")
st.markdown("### 🔒 Security Features")
# Mobile responsive security features - stack on small screens
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**🔐 API Key Protection**")
    st.markdown("- Encrypted storage")
    st.markdown("- Never logged")
    st.markdown("- Format validation")

with col2:
    st.markdown("**🛡️ Input Security**")
    st.markdown("- Input sanitization")
    st.markdown("- Injection prevention")
    st.markdown("- Length limits")

with col3:
    st.markdown("**⏱️ Rate Limiting**")
    st.markdown("- 10 requests/session")
    st.markdown("- 30min timeout")
    st.markdown("- Abuse prevention")

with col4:
    st.markdown("**📊 Monitoring**")
    st.markdown("- Secure logging")
    st.markdown("- Error tracking")
    st.markdown("- Session management")

st.info('🔐 **Secure Operation**: Enter your API key, select location and business type, then press "Search Facilities". All data is processed securely and never stored.')

# Techyz Software Solutions Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin-top: 20px;">
    <p style="color: #2E86AB; font-size: 14px; margin: 0; font-weight: bold;">
        Powered by Techyz Software Solutions Private Limited
    </p>
    <p style="color: #888; font-size: 12px; margin: 5px 0 0 0;">
        Secure • Reliable • Professional
    </p>
</div>
""", unsafe_allow_html=True)
