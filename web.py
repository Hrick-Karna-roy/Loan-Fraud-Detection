from typing import Union

import pandas as pd
import streamlit as st
from pandas import Series, DataFrame
from sklearn.preprocessing import LabelEncoder
import pickle

st.write("""
# Loan Corruptness Prediction App

### This app Predicts weather a  person is **eligible** for loan or not

""")

st.sidebar.header('User Input Features')

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        House_Ownership = st.sidebar.selectbox('House_Ownership',('rented', 'norent_noown', 'owned'))
        MarriedorSingle = st.sidebar.selectbox('Married/Single',('single', 'married'))
        Car_Ownership = st.sidebar.selectbox('Car_Ownership', ('no', 'yes'))
        Profession = st.sidebar.selectbox('Profession', ('Mechanical_engineer', 'Software_Developer', 'Technical_writer',
       'Civil_servant', 'Librarian', 'Economist', 'Flight_attendant',
       'Architect', 'Designer', 'Physician', 'Financial_Analyst',
       'Air_traffic_controller', 'Politician', 'Police_officer', 'Artist',
       'Surveyor', 'Design_Engineer', 'Chemical_engineer',
       'Hotel_Manager', 'Dentist', 'Comedian', 'Biomedical_Engineer',
       'Graphic_Designer', 'Computer_hardware_engineer',
       'Petroleum_Engineer', 'Secretary', 'Computer_operator',
       'Chartered_Accountant', 'Technician', 'Microbiologist',
       'Fashion_Designer', 'Aviator', 'Psychologist', 'Magistrate',
       'Lawyer', 'Firefighter', 'Engineer', 'Official', 'Analyst',
       'Geologist', 'Drafter', 'Statistician', 'Web_designer',
       'Consultant', 'Chef', 'Army_officer', 'Surgeon', 'Scientist',
       'Civil_engineer', 'Industrial_Engineer', 'Technology_specialist'))
       #  CITY = st.sidebar.selectbox('CITY', ('Rewa', 'Parbhani', 'Alappuzha', 'Bhubaneswar',
       # 'Tiruchirappalli[10]', 'Jalgaon', 'Tiruppur', 'Jamnagar',
       # 'Kota[6]', 'Karimnagar', 'Hajipur[31]', 'Adoni', 'Erode[17]',
       # 'Kollam', 'Madurai', 'Anantapuram[24]', 'Kamarhati', 'Bhusawal',
       # 'Sirsa', 'Amaravati', 'Secunderabad', 'Ahmedabad', 'Ajmer',
       # 'Ongole', 'Miryalaguda', 'Ambattur', 'Indore', 'Pondicherry',
       # 'Shimoga', 'Chennai', 'Gulbarga', 'Khammam', 'Saharanpur',
       # 'Gopalpur', 'Amravati', 'Udupi', 'Howrah', 'Aurangabad[39]',
       # 'Hospet', 'Shimla', 'Khandwa', 'Bidhannagar', 'Bellary', 'Danapur',
       # 'Purnia[26]', 'Bijapur', 'Patiala', 'Malda', 'Sagar', 'Durgapur',
       # 'Junagadh', 'Singrauli', 'Agartala', 'Thanjavur', 'Hindupur',
       # 'Naihati', 'North_Dumdum', 'Panchkula', 'Anantapur', 'Serampore',
       # 'Bathinda', 'Nadiad', 'Kanpur', 'Haridwar', 'Berhampur',
       # 'Jamshedpur', 'Hyderabad', 'Bidar', 'Kottayam', 'Solapur',
       # 'Suryapet', 'Aizawl', 'Asansol', 'Deoghar', 'Eluru[25]',
       # 'Ulhasnagar', 'Aligarh', 'South_Dumdum', 'Berhampore',
       # 'Gandhinagar', 'Sonipat', 'Muzaffarpur', 'Raichur',
       # 'Rajpur_Sonarpur', 'Ambarnath', 'Katihar', 'Kozhikode', 'Vellore',
       # 'Malegaon', 'Kochi', 'Nagaon', 'Nagpur', 'Srinagar', 'Davanagere',
       # 'Bhagalpur', 'Siwan[32]', 'Meerut', 'Dindigul', 'Bhatpara',
       # 'Ghaziabad', 'Kulti', 'Chapra', 'Dibrugarh', 'Panihati',
       # 'Bhiwandi', 'Morbi', 'Kalyan-Dombivli', 'Gorakhpur', 'Panvel',
       # 'Siliguri', 'Bongaigaon', 'Patna', 'Ramgarh', 'Ozhukarai',
       # 'Mirzapur', 'Akola', 'Satna', 'Motihari[34]', 'Jalna', 'Jalandhar',
       # 'Unnao', 'Karnal', 'Cuttack', 'Proddatur', 'Ichalkaranji',
       # 'Warangal[11][12]', 'Jhansi', 'Bulandshahr', 'Narasaraopet',
       # 'Chinsurah', 'Jehanabad[38]', 'Dhanbad', 'Gudivada', 'Gandhidham',
       # 'Raiganj', 'Kishanganj[35]', 'Varanasi', 'Belgaum',
       # 'Tirupati[21][22]', 'Tumkur', 'Coimbatore', 'Kurnool[18]',
       # 'Gurgaon', 'Muzaffarnagar', 'Aurangabad', 'Bhavnagar', 'Arrah',
       # 'Munger', 'Tirunelveli', 'Mumbai', 'Mango', 'Nashik', 'Kadapa[23]',
       # 'Amritsar', 'Khora,_Ghaziabad', 'Ambala', 'Agra', 'Ratlam',
       # 'Surendranagar_Dudhrej', 'Delhi_city', 'Bhopal', 'Hapur', 'Rohtak',
       # 'Durg', 'Korba', 'Bangalore', 'Shivpuri', 'Thrissur',
       # 'Vijayanagaram', 'Farrukhabad', 'Nangloi_Jat', 'Madanapalle',
       # 'Thoothukudi', 'Nagercoil', 'Gaya', 'Chandigarh_city', 'Jammu[16]',
       # 'Kakinada', 'Dewas', 'Bhalswa_Jahangir_Pur', 'Baranagar',
       # 'Firozabad', 'Phusro', 'Allahabad', 'Guna', 'Thane', 'Etawah',
       # 'Vasai-Virar', 'Pallavaram', 'Morena', 'Ballia', 'Surat',
       # 'Burhanpur', 'Phagwara', 'Mau', 'Mangalore', 'Alwar',
       # 'Mahbubnagar', 'Maheshtala', 'Hazaribagh', 'Bihar_Sharif',
       # 'Faridabad', 'Lucknow', 'Tenali', 'Barasat', 'Amroha', 'Giridih',
       # 'Begusarai', 'Medininagar', 'Rajahmundry[19][20]', 'Saharsa[29]',
       # 'New_Delhi', 'Bhilai', 'Moradabad', 'Machilipatnam',
       # 'Mira-Bhayandar', 'Pali', 'Navi_Mumbai', 'Mehsana', 'Imphal',
       # 'Kolkata', 'Sambalpur', 'Ujjain', 'Madhyamgram', 'Jabalpur',
       # 'Jamalpur[36]', 'Ludhiana', 'Bareilly', 'Gangtok', 'Anand',
       # 'Dehradun', 'Pune', 'Satara', 'Srikakulam', 'Raipur', 'Jodhpur',
       # 'Darbhanga', 'Nizamabad', 'Nandyal', 'Dehri[30]', 'Jorhat',
       # 'Ranchi', 'Kumbakonam', 'Guntakal', 'Haldia', 'Loni',
       # 'Pimpri-Chinchwad', 'Rajkot', 'Nanded', 'Noida',
       # 'Kirari_Suleman_Nagar', 'Jaunpur', 'Bilaspur', 'Sambhal', 'Dhule',
       # 'Rourkela', 'Thiruvananthapuram', 'Dharmavaram', 'Nellore[14][15]',
       # 'Visakhapatnam[4]', 'Karawal_Nagar', 'Jaipur', 'Avadi',
       # 'Bhimavaram', 'Bardhaman', 'Silchar', 'Buxar[37]', 'Kavali',
       # 'Tezpur', 'Ramagundam[27]', 'Yamunanagar', 'Sri_Ganganagar',
       # 'Sasaram[30]', 'Sikar', 'Bally', 'Bhiwani', 'Rampur', 'Uluberia',
       # 'Sangli-Miraj_&_Kupwad', 'Hosur', 'Bikaner', 'Shahjahanpur',
       # 'Sultan_Pur_Majra', 'Vijayawada', 'Bharatpur', 'Tadepalligudem',
       # 'Tinsukia', 'Salem', 'Mathura', 'Guntur[13]', 'Hubliâ€“Dharwad',
       # 'Guwahati', 'Chittoor[28]', 'Tiruvottiyur', 'Vadodara',
       # 'Ahmednagar', 'Fatehpur', 'Bhilwara', 'Kharagpur', 'Bettiah[33]',
       # 'Bhind', 'Bokaro', 'Karaikudi', 'Raebareli', 'Pudukkottai',
       # 'Udaipur', 'Mysore[7][8][9]', 'Panipat', 'Latur', 'Tadipatri',
       # 'Bahraich', 'Orai', 'Raurkela_Industrial_Township', 'Gwalior',
       # 'Katni', 'Chandrapur', 'Kolhapur'))
        STATE = st.sidebar.selectbox('STATE', ('Madhya_Pradesh', 'Maharashtra', 'Kerala', 'Odisha', 'Tamil_Nadu',
       'Gujarat', 'Rajasthan', 'Telangana', 'Bihar', 'Andhra_Pradesh',
       'West_Bengal', 'Haryana', 'Puducherry', 'Karnataka',
       'Uttar_Pradesh', 'Himachal_Pradesh', 'Punjab', 'Tripura',
       'Uttarakhand', 'Jharkhand', 'Mizoram', 'Assam',
       'Jammu_and_Kashmir', 'Delhi', 'Chhattisgarh', 'Chandigarh',
       'Uttar_Pradesh[5]', 'Manipur', 'Sikkim'))
        Income = st.sidebar.slider('Income (Rs)', 10310,9999938,100000)
        Age = st.sidebar.slider('Age (yrs)', 20,80,27)
        Experience = st.sidebar.slider('Experience (yrs)', 0,20,7)
        CURRENT_JOB_YRS = st.sidebar.slider('CURRENT_JOB_YRS (yrs)', 0,14,3)
        CURRENT_HOUSE_YRS = st.sidebar.slider('CURRENT_HOUSE_YRS (yrs)', 8, 14, 10)
        data = {
                # 'CITY': CITY,
                'Income': Income,
                'Age': Age,
                'Experience': Experience,
                'Married/Single': MarriedorSingle,
                'House_Ownership': House_Ownership,
                'Car_Ownership': Car_Ownership,
                'Profession': Profession,
                'STATE': STATE,
                'CURRENT_JOB_YRS': CURRENT_JOB_YRS,
                'CURRENT_HOUSE_YRS': CURRENT_HOUSE_YRS}

        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
    # Combines user input features with entire penguins dataset
    # This will be useful for the encoding phase
    Dataset = pd.read_csv('Training Data.csv')

    Dataset_1 = Dataset.drop(columns=['Risk_Flag', 'CITY', 'Id'])

    # st.write(Dataset_1.head(5))

    df = pd.concat([input_df, Dataset_1], axis=0)

    st.write(df.head(5))

    labelEncoder = LabelEncoder()

    data = df
    # print(data.head())
    # Encode the object data to type int
    for e in data.columns:
        if data[e].dtype == 'object':
            labelEncoder.fit(list(data[e].values))
            data[e] = labelEncoder.transform(data[e].values)

            # Accommodate the data that has been changed
            tData = data

    df = tData[:1]  # Selects only the first row (the user input data)

    # Displays the user input features
    st.subheader('User Input features')

    if uploaded_file is not None:
        st.write(df)
    else:
        st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
        st.write("## Hi there Now choose according to your data from the **Sidebar** and wait for your **Outcome**")
        st.write(df)

    # Reads in saved classification model
    load_clf = pickle.load(open('loan_prediction.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)



    st.subheader('Prediction')
    # class = True
    if prediction == 1:
        st.write('Risky')
    else:
        st.write("Not Risky")
    st.subheader('Prediction proba')
    st.write(st.write(prediction_proba))

