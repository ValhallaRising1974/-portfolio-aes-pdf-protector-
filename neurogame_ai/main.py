from neural_network import NeuralNetwork
from utils import load_data

if __name__ == "__main__":
    print("🧠 Inicializando NeuroGame AI...")
    data = load_data()
    model = NeuralNetwork()
    model.train(data)
