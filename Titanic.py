import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')

# 데이터 정보 출력
print(df.info())
print(df.head())
print(df.describe())

# 결측치 확인
print(df.isnull().sum())

# 결측치 처리: Age의 결측치를 평균값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Embarked의 결측치를 최빈값으로 대체
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 결측치 재확인
print(df.isnull().sum())

# 새로운 열 추가: 가족 수(FamilySize)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df.head())

# 성별에 따른 생존자 비율 시각화
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# 클래스에 따른 생존자 비율 시각화
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

# 나이에 따른 생존자 비율 시각화
plt.figure(figsize=(10, 6))
sns.histplot(df[df['Survived'] == 1]['Age'], bins=30, label='Survived', kde=False, color='green')
sns.histplot(df[df['Survived'] == 0]['Age'], bins=30, label='Not Survived', kde=False, color='red')
plt.legend()
plt.title('Survival Rate by Age')
plt.show()

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

import matplotlib.pyplot as plt # matplotlib.pyplot 함수를 plt로 줄여서 사용

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#k-최근접 이웃
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

#2차원 리스트 만들기
fish_data = [[l, w] for l, w in zip(length, weight)]
print(fish_data)

fish_target = [1] * 35 + [0] * 14
print(fish_target)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
kn.score(fish_data, fish_target)
kn.score(fish_data, fish_target)