import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/NFT_abi.json')) as f:
        nft_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=nft_abi
    )

    return contract

contract = load_contract()


################################################################################
# Register New NFT
################################################################################
st.title("Register New NFT")
accounts = w3.eth.accounts
# Use a streamlit component to get the address of the NFT owner from the user
address = st.selectbox("Select NFT Owner", options=accounts)

# Use a streamlit component to get the NFT's URI
nft_uri = st.text_input("The URI to the NFT")

if st.button("Register NFT"):

    # Use the contract to send a transaction to the registerArtwork function
    tx_hash = contract.functions.registerArtwork(
        address,
        nft_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")

################################################################################
# Display an NFT
################################################################################
st.markdown("## Display an NFT")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} NFT")

token_id = st.selectbox("NFT's", list(range(tokens)))

if st.button("Display"):

    # Use the contract's `ownerOf` function to get the NFT owner
    owner = contract.functions.ownerOf(token_id).call()

    st.write(f"The token is registered to {owner}")

    # Use the contract's `tokenURI` function to get the NFT's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The nftURI is {token_uri}")
    st.image(token_uri)
