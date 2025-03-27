import streamlit as st
from datetime import datetime

def main():
    st.set_page_config(page_title='FraudShield - Banking App', layout='wide')
    st.title('🛡️ FraudShield')
    
    # Sidebar Navigation
    menu = ['🏠 Home', '💸 Money Transfer', '📑 Bill Payment', '🏦 Deposit', '💳 Withdrawal']
    choice = st.sidebar.radio('📌 Select Operation', menu)
    
    # Fraud Detection Logic
    def check_fraud(transaction_type, amount):
        if amount > 10000:  # Example threshold
            return f'⚠️ Potential Fraud Detected in {transaction_type}!', 'warning'
        return '✅ Transaction is Safe.', 'success'
    
    # Home Page
    if choice == '🏠 Home':
        st.subheader('Welcome to Your Secure Banking Dashboard')
        st.info('Navigate through banking services and stay protected against fraudulent transactions.')
    
    else:
        st.subheader(f'{choice}')
        account = st.text_input('🔹 Account Number')
        if choice == '💸 Money Transfer':
            receiver = st.text_input('🔹 Receiver Account Number')
        elif choice == '📑 Bill Payment':
            biller = st.text_input('🏢 Biller Name')
        elif choice in ['🏦 Deposit', '💳 Withdrawal']:
            location = st.text_input('📍 Location')
        amount = st.number_input('💰 Transaction Amount', min_value=0.0, format='%.2f')
        
        if st.button('📌 Submit Transaction'):
            fraud_status, status_type = check_fraud(choice, amount)
            if status_type == 'warning':
                st.warning(fraud_status)
            else:
                st.success(fraud_status)
        
        # Display Timestamp for Transactions
        st.markdown(f"🕒 Transaction Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    main()