import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('D://1 Intern\Titanic.csv')
data['Age'].fillna(data['Age'].median() , inplace=True)
data.drop(columns=['Cabin'], inplace=True)
data.drop_duplicates(inplace=True)
#survival count fig 1
data['Survived'].value_counts().plot(kind='bar', title='Survival Count', color = ['red', 'green'])
plt.xlabel('Survived')
plt.ylabel('Counts')
plt.show()
#age distribution fig 2
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Ditribution Of Age')
plt.show()
#survived by gender fig 3
sns.countplot(x='Survived', hue='Sex', data=data)
plt.title('Survival Count by Gender')
plt.show()
#suvival rate by class fig 4
sns.barplot(x='Pclass', y='Survived', data=data)
plt.title('Survival Rate by Class')
plt.show()
#age vs fare survival fig 5
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=data)
plt.title('Age vs. Fare with Survival Status')
plt.show()