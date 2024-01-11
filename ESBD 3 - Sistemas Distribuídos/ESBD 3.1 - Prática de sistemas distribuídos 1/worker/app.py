import os

import boto3
import joblib
import logging
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import zmq


def main():
    logging.basicConfig(level=logging.INFO)

    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://load_balancer:5556")

    while True:
        hyperparameters = socket.recv_json()

        diabetes = load_diabetes()
        X = diabetes.data
        y = diabetes.target
        y = [1 if i > y.mean() else 0 for i in y]

        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        rf = RandomForestClassifier(
            n_estimators=hyperparameters['n_estimators'],
            max_features=hyperparameters['max_features'],
            max_depth=hyperparameters['max_depth']
            )

        message = 'model training'
        logging.info(f"Worker {os.getenv('WORKER_NAME')} received task: {message}")
        rf.fit(X_train, y_train)
        logging.info(f"Worker {os.getenv('WORKER_NAME')} completed task: {message}")

        local_path = '/tmp/model.joblib'
        joblib.dump(rf, local_path)

        s3_bucket = 'esbd-3-1'
        s3_key = f'n_estimators_{hyperparameters["n_estimators"]}_max_features{hyperparameters["max_features"]}_max_depth_{hyperparameters["max_depth"]}.joblib'

        s3 = boto3.client('s3')
        s3.upload_file(local_path, s3_bucket, s3_key)


if __name__ == "__main__":
    main()
