# code4BBS
## Technical trading is a difficult task for a beginner. How we can easily predict the prices of the crypto and make an investment decision in crypto easily

![image](https://user-images.githubusercontent.com/85974708/153758063-3c875af2-97e5-4e76-b816-575ef92dff3d.png)


# Aproach towards the problem statement
We have approached the problem through machine learning. Firstly, we had collected data from kaggle dataset but then we shifted to yfinance api for collecting the data. We used yfinance because of live data supply and low latency. We had trained LSTM model from scratch but we finally used fbprophet which is a pretrained model because it was giving better predictions. 

# Webapp description
We used streamlit (an open source app framework) for our webapp and have implemented the following features:
(i)   Home page
(ii)  Signup and login page: One needs to create an account and login to use the app.
(iii) One needs to select the coin from the dropdown list accourding to one's choice and set the number of years for which one wants to forecast.
(iV)  The raw data and time series data will be visible with a range slider (to set the time period for which one wants to view the changes in prices)
(v)   The blue line is the predicted price and the shaded region shows the amount by which the price can vary at a particular time.
(vi)  The black line is the actual price at a particular point.
(vii) The yearly, weekly and monthly trend is displayed at the bottom of the page.

![image](https://user-images.githubusercontent.com/85974708/153759233-10be6cbe-aacc-41f1-bad3-de492be5bb6c.png)
# website link :https://share.streamlit.io/sai-rohan-harshavardhan-vuppala/code4bbs/main/login.py
