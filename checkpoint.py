import pickle
import streamlit as st
from sklearn.ensemble import AdaBoostClassifier
import sklearn
from sklearn.preprocessing import LabelEncoder

# Load your trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
model_file.close()

# Load your encoder model
with open('le.pkl', 'rb') as model_file:
    model_le = pickle.load(model_file)
model_file.close()


# Main Streamlit app
def main():
    st.title('ML Model Prediction App')

    # Add input fields for features
    region = st.selectbox('Region', ['FATICK','DAKAR','LOUGA','TAMBACOUNDA','KAOLACK','THIES','SAINT-LOUIS','KOLDA','KAFFRINE','DIOURBEL','ZIGUINCHOR','MATAM','SEDHIOU','EDOUGOU'])
    tenure = st.selectbox('Tenure', ['K > 24 months', 'I 18-21 months', 'G 12-15 months', 'H 15-18 months', 'J 21-24 months', 'F 9-12 months', 'D 3-6 months', 'E 6-9 months'])
    montant = st.number_input('Montant')
    frequence_rech = st.number_input('Frequence Recharge')
    revenue = st.number_input('Revenue')
    arpu_segment = st.number_input('ARPU Segment')
    frequence = st.number_input('Frequence')
    data_volume = st.number_input('Data Volume')
    on_net = st.number_input('On Net')
    orange = st.number_input('Orange')
    tigo = st.number_input('Tigo')
    zone1 = st.number_input('Zone 1')
    zone2 = st.number_input('Zone 2')
    mrg = st.checkbox('MRG')
    # If the checkbox is checked, set value to 0; otherwise, set value to 1
    mrg = 0 if mrg else 1
    regularity = st.number_input('Regularity')
    top_pack = st.text_input('Top Pack')
    freq_top_pack = st.number_input('freq_top_pack')
    try:
        top_pack = model_le.transform([[top_pack]])[0] if top_pack else None
    except:
        top_pack = -1

    # Validation button
    if st.button('Predict'):
        try:
            region = model_le.transform([[region]])[0] if region else None
        except:
            region = -1
        try:
            tenure = model_le.transform([[tenure]])[0] if tenure else None
        except:
            tenure = -1

        resultat=model.predict([[region, tenure, montant, frequence_rech, revenue,arpu_segment,frequence, data_volume,on_net,orange,tigo, zone1, zone2, mrg, regularity,top_pack,freq_top_pack]])
        if resultat == 0:
            st.success(' The customer is staying')
        else:
            st.warning('customer will churn')

if __name__ == '__main__':
    main()


