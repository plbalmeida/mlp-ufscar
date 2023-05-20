from sklearn.model_selection import ParameterGrid
import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://load_balancer:5555")

    param_grid = {
        'n_estimators': [100, 200, 500],
        'max_features': ['sqrt', 'log2'],
        'max_depth': [4, 5, 6, 7, 8]
        }

    hyperparameters_sets = list(ParameterGrid(param_grid))

    for hyperparameters in hyperparameters_sets:
        socket.send_json(hyperparameters)


if __name__ == "__main__":
    main()
