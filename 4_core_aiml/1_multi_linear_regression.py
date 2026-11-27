import numpy as np

# lets consider 'n' features and '1' target each object is 'm' long
class LinearRegression:
    def __init__(self, seed:int=42, 
                 iterations:int=1000,
                 learning_rate:float=0.001):
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.random_number_gen = np.random.default_rng(seed=seed)

    def fit(self, X, y):
        m = X.shape[0]
        n = X.shape[1]
        print(f"[INFO] Shape of input data: {m} rows, {n} columns")
        
        # step 1: Initalise beta and compute initial predictions
        X_new = np.hstack([X, np.ones((m,1))])
        beta = (self.random_number_gen.random((1,n+1))).T

        y_pred_init = X_new @ beta
        y_actual = np.array(y).reshape(-1,1)

        # step 2: compute cost function
        errors = y_pred_init - y_actual
        cost = (0.5/m)*((y_pred_init - y_actual).T @ (y_pred_init - y_actual))

        # step 3: gradient descent to optimise beta
        Y = y_pred_init

        print("[INFO] Training started...")
        for _ in range(self.iterations):
            gradient = (X_new.T @ (X_new @ beta - y_actual)) / m
            beta = beta - self.learning_rate * gradient

        self.beta_trained = beta

        print("[INFO] Training complete!")


    def predict(self, X):
        y_pred = []
        X_new = np.hstack([X, np.ones((X.shape[0],1))])
        for sample in list(X_new):
            prediction = sample @ self.beta_trained
            y_pred.append(float(prediction[0]))

        return y_pred 




if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("../docs/salary.csv")
    
    X = data[["experience", "education"]].values
    y = data["salary"].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=10
    )

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train_scaled = sc.fit_transform(X_train)
    X_test_scaled = sc.transform(X_test)

    linreg_model = LinearRegression(iterations=20000, learning_rate=0.05)
    linreg_model.fit(X_train_scaled,y_train)

    y_pred = linreg_model.predict(X_test_scaled)

    from sklearn.metrics import r2_score 
    mse = r2_score(y_test, y_pred)
    print("R2 Score: ",mse)
