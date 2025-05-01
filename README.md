# Portfolio Optimization using Markowitz Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A Python implementation of Modern Portfolio Theory (MPT) that helps investors find the optimal asset allocation to maximize returns for a given level of risk.

## Overview

This tool applies Harry Markowitz's Modern Portfolio Theory to find the optimal portfolio weights for a set of stocks. It:

1. Downloads historical stock data using Yahoo Finance
2. Calculates logarithmic returns
3. Generates thousands of random portfolios with different asset allocations
4. Visualizes the efficient frontier
5. Uses optimization techniques to find the portfolio with the maximum Sharpe ratio

## Features

- **Data Retrieval**: Seamlessly downloads historical stock data from Yahoo Finance
- **Portfolio Simulation**: Generates multiple random portfolios to visualize the risk-return relationship
- **Visualization**: Plots the efficient frontier with interactive charts
- **Optimization**: Identifies the optimal portfolio weights to maximize the Sharpe ratio
- **Performance Metrics**: Calculates expected returns, volatility, and Sharpe ratio

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/markowitz_model.git
cd markowitz_model

# Install required packages
pip install numpy pandas matplotlib yfinance scipy
```
## Usage

Run the script and follow the interactive prompts:

```bash
python MyMarkowitzModel.py
```

The program will ask you to:

1. Enter the number of stocks in your portfolio
2. Enter each stock's ticker symbol (e.g., AAPL, MSFT, GOOGL)
3. Specify start and end dates for historical data analysis

#### Example

```
Enter the number of stocks in portfolio: 6
Enter the ticker of stock 1: AAPL
Enter the ticker of stock 2: GE
Enter the ticker of stock 3: WMT
Enter the ticker of stock 4: AMZN
Enter the ticker of stock 5: TSLA
Enter the ticker of stock 6: DB
Enter the start date for analysis in the format YYYY-DD-MM: 2012-01-01
Enter the end date for analysis in the format YYYY-DD-MM: 2017-01-01
```

#### Example Output

<img width="600" alt="Image" src="https://github.com/user-attachments/assets/1b26abfc-d672-4778-badd-23937103be8c" />

<img width="600" alt="Image" src="https://github.com/user-attachments/assets/6c2235ed-b7cf-435d-8d5a-a88b3222f329" />

```
Optimal portfolio weights: 
AAPL : 13.94%
GE : 37.33%
WMT : 0.0%
AMZN : 32.13%
TSLA : 16.6%
DB : 0.0%

Portfolio returns in %:  23.46
Portfolio risk in %:  19.53
Portfolio Sharpe Ratio:  1.2014300985406978
```

The program will:

1. Display historical price charts
2. Calculate and display the optimal portfolio allocation
3. Show a final visualization with the optimal portfolio highlighted

## How It Works

### Theory

This implementation is based on Modern Portfolio Theory, which suggests that:

* Portfolio diversification can reduce risk without sacrificing returns
* There exists an "efficient frontier" of optimal portfolios
* The optimal portfolio maximizes the Sharpe ratio (excess return per unit of risk)

### Key Functions

* `download_data()`: Retrieves historical stock prices
* `calculate_returns()`: Computes logarithmic returns
* `portfolio_performance()`: Calculates expected return and volatility
* `generate_portfolios()`: Creates random portfolio weights
* `optimize_portfolio()`: Finds weights that maximize the Sharpe ratio

## Requirements

- Python 3.6+
- NumPy
- Pandas
- Matplotlib
- yfinance
- SciPy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Harry Markowitz for developing Modern Portfolio Theory
- Yahoo Finance for providing the historical stock data


## Acknowledgments

Harry Markowitz for developing Modern Portfolio Theory
Yahoo Finance for providing the historical stock data

