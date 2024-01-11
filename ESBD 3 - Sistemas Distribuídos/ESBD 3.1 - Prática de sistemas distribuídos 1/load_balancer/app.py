import zmq


def main():
    context = zmq.Context()

    frontend = context.socket(zmq.PULL)
    frontend.bind("tcp://*:5555")

    backend = context.socket(zmq.PUSH)
    backend.bind("tcp://*:5556")

    zmq.device(zmq.QUEUE, frontend, backend)


if __name__ == "__main__":
    main()
