# Linear Regression Salary Predictor

This project demonstrates the application of linear regression to predict salaries based on years of experience, test scores, and interview scores. The Python script utilizes pandas for data manipulation, matplotlib for plotting, and scikit-learn for performing the linear regression analysis. Additionally, the word2number library is used to convert textual numerical representations into their numeric forms.

## Features

- Data cleaning and preprocessing
- Conversion of textual numerical information into numeric form
- Linear regression model to predict salaries
- Visualization of the regression line over the data points

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pip (Python package installer)

## Installation

Install the necessary Python packages by running the following command:

```bash
pip install pandas matplotlib scikit-learn word2number
```

## Dataset

The dataset should be in a CSV file named `hiring.csv` with the following columns:

- `experience` (in years or textual format e.g., "two")
- `test_score(out of 10)`
- `interview_score(out of 10)`
- `salary($)` (the target variable)

## Usage

To run the script, navigate to the directory containing the script and dataset, then execute:

```bash
python main.py
```

Ensure that the `hiring.csv` file is in the same directory as the script.

## How It Works

1. **Data Preprocessing**: The script first cleans the data by filling missing values and converting textual numerical data into numeric form.
2. **Model Training**: It then trains a linear regression model using the cleaned data.
3. **Prediction and Visualization**: The script predicts salary for a given set of inputs and plots the regression line over the data points for visual analysis.

## Contributing

Contributions to the project are welcome. Please follow the standard fork-and-pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


Adjust the sections according to your project's actual details and requirements.