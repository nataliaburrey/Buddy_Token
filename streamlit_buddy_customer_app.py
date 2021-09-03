#Importing required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

#Load in the .env file
load_dotenv()
 
#Defining and connecting the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
 
#Create a function to load the contract into the app
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path(r'abi/BuddyToken2_abi.json')) as f:
        buddy_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi= buddy_abi
    )
    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
token = load_contract()

#Create a function to load the oracle contract into the app
@st.cache(allow_output_mutation=True)
def load_oracle_contract():
    with open(Path(r'abi/Oracle_abi.json')) as f:
        oracle_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi= oracle_abi
    )
    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
oracle_contract = load_oracle_contract()

#Create welcome section for the app
st.image(r'resources\BUDlogo2.png')
st.title('Welcome to the Buddy Token Customer App!')

#Display value of Ethereum on sidebar widget
#eth_price = oracle_contract.functions.getLatestPrice().call()
#st.sidebar.write(eth_price)

#Set up accounts via Web3 connection
accounts = w3.eth.accounts
address = st.sidebar.selectbox('Select Ethereum Account', options = accounts)
st.sidebar.subheader('The value of Ethereum today is:')


st.header('What would you like to do today?')

#Ideally, we would want the following 3 buttons to navigate to a different page for the app
#st.button('Purchase Product')
#st.button('Purchase Buddy Tokens')
#st.button('Return/Exchanges')
 
#Creating the purchase order button for Streamlit app
st.header('Buddy Token Purchase Order')

#Create a slider widget allowing customers to select the quantity of tokens they want to purchase
token_quantity = st.slider('Select how many Buddy Tokens you want to purchase (per transaction limits: min. is 1; max is 10.):', 
                            min_value = 1, max_value = 10)

if token_quantity == 1:
    st.write('You are buying', token_quantity, 'Buddy Token.')
else:
    st.write('You are buying', token_quantity, 'Buddy Tokens.')

#Create button to confirm purchase of the tokens
if st.button('Purchase Buddy Tokens'):
    tx_hash = token.functions.purchase(token_quantity).transact({'from': address})
    st.write('Tokens Purchased!')
    st.balloons()

#Create section for customer to see their token balance
if st.button('Show Buddy Token Balance Snapshot'):
    token_balance_snapshot = token_quantity
    st.write('Your Buddy Token Balance is', token_balance_snapshot, 'Buddy Tokens.')

#Create section for customer to purchase store product
st.header('Product Purchase Order')
st.write('Please select your purchase options below:')

#Create a selection box of the product that the customer wants to purchase
st.selectbox('Product Type', ['Cannabis', 'Accessories'])

#Create a list of product options
product_options = ['1/8 oz - $10', '1/4 oz - $18', '1/2 oz - $26', '1 oz - $34']

#Set variables to the product selection and quantity to calculate the total cost
selection = st.selectbox('Select Product Unit', product_options)
quantity = st.number_input('Quantity - Please use whole numbers only.')

#Create a function to show the customer the total cost of their product purchase
@st.cache(suppress_st_warning=True)
def get_total_cost(selection, quantity):
    price = 0
    if selection == '1/8 oz - $10':
        price = 10
        total_cost = price * quantity
        st.write('The total cost for your order is $', round(total_cost, 2), '.')
    elif selection == '1/4 oz - $18':
        price = 18
        total_cost = price * quantity
        st.write('The total cost for your order is $', round(total_cost, 2), '.')
    elif selection == '1/2 oz - $26':
        price = 26
        total_cost = price * quantity
        st.write('The total costs for your order is $', round(total_cost, 2), '.')
    elif selection == '1 oz - $34':
        price = 34
        total_cost = price * quantity
        st.write('The total cost for your order is $', round(total_cost, 2), '.')

#Create button to display total cost of product purchase to customer
if st.button('Show Total Cost'):
    get_total_cost(selection, quantity)


#This button is still in process, to confirm the store product purchase from the store
confirm_purchase = st.button('Confirm Purchase')
if confirm_purchase:
    #Put in order for the product
    st.write("Purchase confirmed.")