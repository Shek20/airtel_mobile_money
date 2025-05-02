import streamlit as st

from dotenv import load_dotenv
import os

import requests

load_dotenv()

payee_number = os.getenv("PAYEE_NUMBER")
url = os.getenv("URL")
pin = os.getenv("PIN")

headers = {
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'X-Country': 'UG',
  'X-Currency': 'UGX',
  'Authorization': 'Bearer UC*****2w'
}

def send_money(amount, payee_number, reference):
    if amount > 0:
        params = {
            "subscriber": {
                "msisdn": payee_number
            },
            "transaction": {
                "amount": amount,
                "id": payer_number
            },
            "additional_info": [],
            "reference": reference,
            "pin": pin
        }
        r = requests.post(url,  params=params,headers = headers)

        if r.json()["data"]["status_code"] == 200:
            st.success(f"Successfully sent {amount} to {payee_number}.")
        else:
            st.error(f"Failed to send money: {r.json()['data']['status_message']}")
    else:
        st.error("Please enter a valid amount.")


st.set_page_config(page_title="Airtel Money", page_icon=":money_with_wings:", layout="wide")
st.title("Airtel Money")
st.subheader("Send Money to us!")
st.write("Enter the amount you want to send then enter your phone number and click the button below.")
amount = st.number_input("Amount", min_value=0, step=1000)
payer_number = st.text_input("Your Phone Number", placeholder="+243811234567")
reference = st.text_input("Reference", placeholder="Enter a reference for the transaction")
if st.button("Send Money"):
    if payer_number and reference:
        send_money(amount, payer_number, reference)
    else:
        st.error("Please enter your phone number and a reference for the transaction.")
st.markdown("---")