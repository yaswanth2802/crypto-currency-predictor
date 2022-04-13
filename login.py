import streamlit as st
import pandas as pd
import subprocess
import sys
import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	st.title("Made by code4BBS team")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				# pip install streamlit fbprophet yfinance plotly


				START = "2015-01-01"
				TODAY = date.today().strftime("%Y-%m-%d")

				st.title('CRYPTOCURRENCY PREDICTOR')

				stocks = ('BTC-USD', 'ETH-USD', 'DOGE-USD', 'BNB-USD', 'USDC-USD', 'XRP-USD', 'HEX-USD', 'ADA-USD', 'SOL-USD', 'LUNA1-USD', 'AVAX-USD', 'DOT-USD', 'BUSD-USD', 'SHIB-USD', 'MATIC-USD', 'CRO-USD', 'UST-USD', 'WBTC-USD', 'DAI-USD', 'LTC-USD', 'ATOM-USD', 'LINK-USD','NEAR-USD', 'UNI1-USD','TRX-USD','BCH-USD','FTT-USD','ALGO-USD','LEO-USD','XLM-USD')
				selected_stock = st.selectbox('Select coin for prediction', stocks)

				n_years = st.slider('Years of prediction:', 1, 4)
				period = n_years * 365


				@st.cache
				def load_data(ticker):
					data = yf.download(ticker, START, TODAY)
					data.reset_index(inplace=True)
					return data

					
				data_load_state = st.text('Loading data...')
				data = load_data(selected_stock)
				data_load_state.text('Loading data... done!')

				st.subheader('Raw data')
				st.write(data.tail())

				# Plot raw data
				def plot_raw_data():
					fig = go.Figure()
					fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="open_price"))
					fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="close_porice"))
					fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
					st.plotly_chart(fig)
					
				plot_raw_data()

				# Predict forecast with Prophet.
				df_train = data[['Date','Close']]
				df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

				m = Prophet()
				m.fit(df_train)
				future = m.make_future_dataframe(periods=period)
				forecast = m.predict(future)

				# Show and plot forecast
				st.subheader('Forecast data')
				st.write(forecast.tail())
					
				st.write(f'Forecast plot for {n_years} years')
				fig1 = plot_plotly(m, forecast)
				st.plotly_chart(fig1)

				st.write("Forecast components")
				fig2 = m.plot_components(forecast)
				st.write(fig2)
                
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
