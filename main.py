import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
import math

df = pd.read_csv('hiring.csv')
df.to_csv('hiring.csv', index=False)

experience = []
expierence = df['experience'].tolist()
test_scores = df['test_score(out of 10)'].tolist()
interview_scores = df['interview_score(out of 10)'].tolist()

def make_num():
    df['experience'] = df['experience'].fillna(0) # replace NaN with 0
    df['experience'] = df['experience'].apply(lambda x: w2n.word_to_num(x) if isinstance(x, str) else x) # replace words with numbers
    return df['experience']

df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(math.floor(df['test_score(out of 10)'].mean()))

def get_average():
    sum = 0
    for i in range(len(expierence)):
        sum += expierence[i]
    return sum / len(expierence)

make_num()

reg = linear_model.LinearRegression()
print(df)

reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])

prediction = reg.predict([[2, 10, 10]])
rounded_prediction = round(prediction[0])
print(rounded_prediction)

x = df['experience'].tolist()
y = df['salary($)'].tolist()

# Plot the scatter points
plt.scatter(x, y)

# Generate predicted values for the range of experience values
x_pred = pd.DataFrame({'experience': range(int(df['experience'].min()), int(df['experience'].max()) + 1)})
x_pred['test_score(out of 10)'] = df['test_score(out of 10)'].mean()
x_pred['interview_score(out of 10)'] = df['interview_score(out of 10)'].mean()
y_pred = reg.predict(x_pred)

# Plot the line of best fit
plt.plot(x_pred['experience'], y_pred, color='red')

plt.xlabel('Experience')
plt.ylabel('Salary($)')
plt.title('Experience vs. Salary')
plt.show()