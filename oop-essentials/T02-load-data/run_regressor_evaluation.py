from sklearn import linear_model, metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from songpop.data import *


def main():
    dataset = Dataset(10000)
    X, y = dataset.load_xy_projected_scaled()

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3, shuffle=True)

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
