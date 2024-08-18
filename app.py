import streamlit as st

# Title of the application
st.title('Average Buying Price Calculator')

# Input fields for user to enter buying prices and quantities
st.header('Enter your buying prices and quantities')

# Input for the number of transactions
num_transactions = st.number_input('Number of transactions', min_value=1, step=1, value=1)

# Initialize lists to store inputs
prices = []
quantities = []

# Loop to input each transaction
for i in range(num_transactions):
    st.subheader(f'Transaction {i+1}')
    price = st.number_input(f'Price for Transaction {i+1}', key=f'price_{i}')
    quantity = st.number_input(f'Quantity for Transaction {i+1}', key=f'quantity_{i}')
    prices.append(price)
    quantities.append(quantity)

# Calculate average buying price
if prices and quantities:
    total_cost = sum(p * q for p, q in zip(prices, quantities))
    total_quantity = sum(quantities)
    average_buying_price = total_cost / total_quantity if total_quantity != 0 else 0

    # Display the results
    st.subheader('Results')
    st.write(f'Total Cost: Rs. {total_cost:.2f}')
    st.write(f'Total Quantity: {total_quantity}')
    st.write(f'Average Buying Price: Rs. {average_buying_price:.2f}')
else:
    st.write('No transactions entered yet.')
