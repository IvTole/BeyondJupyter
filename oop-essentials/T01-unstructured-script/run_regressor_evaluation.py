from sklearn import linear_model, metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np


def main():

    # data import and dummy variables
    include_columns = ['popularity','genre', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
                   'acousticness','instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms',
                   'time_signature']

    df = pd.read_csv("../data/spotify_data_sample.csv", usecols=include_columns)

    #df = df.sample(frac=0.1, replace=False, random_state=42)
    #df.to_csv("../data/spotify_data_sample.csv")

    numeric_data = df.select_dtypes(include=[np.number])
    categorical_data = df.select_dtypes(exclude=[np.number])

    # to dummies
    for category in categorical_data:
        dummy_df = pd.get_dummies(df[category])
        df = df.join(dummy_df)
    df.drop(categorical_data, inplace=True, axis=1)

    target = 'popularity'
    independent_variables = [var for var in df.columns.to_list() if var!=target]
    X = df[independent_variables]
    y = df[target]
    print("Stage1 = Data Load")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3, shuffle=True)
    print("Stage2 = Split")


    log_reg = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000)
    log_reg.fit(X_train, y_train)
    y_pred = log_reg.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    print(f"LogisticRegression: MAE={mae:.1f}")

    knn = KNeighborsRegressor(n_neighbors=1)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    print(f"KNeighborsRegressor: MAE={mae:.1f}")

    rforest = RandomForestRegressor(n_estimators=100)
    rforest.fit(X_train, y_train)
    y_pred = rforest.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    print(f"RandomForestRegressor: MAE={mae:.1f}")

    d_tree = DecisionTreeRegressor(random_state=42, max_depth=2)
    d_tree.fit(X_train, y_train)
    y_pred = d_tree.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    print(f"DecisionTreeRegressor: MAE={mae:.1f}")


if __name__ == '__main__':
    main()
