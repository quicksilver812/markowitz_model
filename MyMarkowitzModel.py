# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import scipy.optimize as optimization

# Define Constants
NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000

# Download stock data
def download_data(stocks, start_date, end_date):
    stocks_data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        stocks_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pd.DataFrame(stocks_data)

# Visualise stock data
def show_data(data):
    data.plot(figsize = (12,8))
    plt.title("Historical Price Data")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend(loc='upper left')
    plt.show()

# Calculate Returns
def calculate_returns(data):
    log_returns = np.log(data/data.shift(1))
    return log_returns[1:]

# Portfolio Performance Calculator
def portfolio_performance(weights, returns):
    portfolio_returns = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
    portfolio_volatilities = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*NUM_TRADING_DAYS, weights)))

    return portfolio_returns, portfolio_volatilities

# Generate Random Portfolios
def generate_portfolios(returns):
    portfolio_weights = []
    portfolio_returns = []
    portfolio_volatilities = []
    portfolio_sharpe_ratios = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.rand(len(stock_names))
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_return, portfolio_volatility = portfolio_performance(w, returns)
        portfolio_returns.append(portfolio_return)
        portfolio_volatilities.append(portfolio_volatility)
        portfolio_sharpe_ratios.append(portfolio_return/portfolio_volatility)

    return np.array(portfolio_weights), np.array(portfolio_returns), np.array(portfolio_volatilities), np.array(portfolio_sharpe_ratios)

# Visualise performance of all portfolios
def show_portfolios(returns, volatilities, sharpe_ratios):
    plt.figure(figsize=(12,8))
    plt.scatter(volatilities, returns, c = sharpe_ratios, cmap = 'viridis', marker = 'o', alpha = 0.5)
    plt.title('Random Portfolio Performance')
    plt.xlabel("Risk in %")
    plt.ylabel("Returns in %")
    plt.colorbar(label="Sharpe Ratio")
    plt.grid(True)
    plt.show()

# Min Sharpe Ratio function
def min_function_sharpe(weights, returns):
    portfolio_return, portfolio_volatility = portfolio_performance(weights, returns)
    return -portfolio_return/portfolio_volatility

# Optimisation function
def optimize_portfolio(weights, returns):
    constraints = ({'type':'eq', 'fun':lambda x: np.sum(x)-1})
    bounds = tuple((0,1) for _ in range(len(stock_names)))
    initial_guess = weights[0]

    optimum = optimization.minimize(
        fun=min_function_sharpe,
        x0=initial_guess,
        args = (returns,),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    return optimum

# Print optimised portfolio results
def print_optimal_portfolio(optimum, returns):
    weights = optimum['x']
    print("\nOptimal portfolio weights: ")
    for i in range(len(stock_names)):
        print(f'{stock_names[i]} : {(weights[i]*100).round(2)}%')
    portfolio_return, portfolio_volatility = portfolio_performance(weights.round(4), returns)
    print("\nPortfolio returns in %: ", (portfolio_return*100).round(2))
    print("Portfolio risk in %: ", (portfolio_volatility*100).round(2))
    print("Portfolio Sharpe Ratio: ", portfolio_return/portfolio_volatility)

# Visualise all portfolios along with optimum portfolio
def show_portfolios_with_opt(returns, volatilities, sharpe_ratios, opt, log_returns):
    plt.figure(figsize=(12,8))
    plt.scatter(volatilities, returns, c = sharpe_ratios, cmap = 'viridis', marker = 'o', alpha = 0.5)
    plt.title('Random Portfolio Performance')
    plt.xlabel("Risk in %")
    plt.ylabel("Returns in %")
    plt.colorbar(label="Sharpe Ratio")
    plt.grid(True)

    weights = opt['x'].round(4)
    portfolio_returns, portfolio_volatility = portfolio_performance(weights, log_returns)
    plt.scatter(portfolio_volatility, portfolio_returns, color = "red", marker = "*", s=100, label = 'Optimum Portfolio')
    plt.show()

# Main method
if __name__ == '__main__':
    stock_names = []
    num_stocks = int(input('Enter the number of stocks in portfolio: '))
    for i in range(num_stocks):
        name = input(f'Enter the ticker of stock {i+1}: ')
        stock_names.append(name)
    start = input('Enter the start date for analysis in the format YYYY-DD-MM: ')
    end = input('Enter the end date for analysis in the format YYYY-DD-MM: ')
    dataset = download_data(stock_names, start, end)
    show_data(dataset)
    log_daily_returns = calculate_returns(dataset)
    p_weights, p_returns, p_volatilities, p_sharpe_ratios = generate_portfolios(log_daily_returns)
    optimal_portfolio = optimize_portfolio(p_weights, log_daily_returns)
    print_optimal_portfolio(optimal_portfolio, log_daily_returns)
    show_portfolios_with_opt(p_returns, p_volatilities, p_sharpe_ratios, optimal_portfolio, log_daily_returns)
