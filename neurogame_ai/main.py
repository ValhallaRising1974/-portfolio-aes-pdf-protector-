# main.py
from neural_network import GameNeuralNet
from utils import load_data, evaluate_performance

def main():
    print("Initializing NeuroGame AI...")

    # Load training data
    training_data, validation_data = load_data()

    # Initialize model
    model = GameNeuralNet(input_size=100, hidden_size=64, output_size=5)
    print("Model initialized.")

    # Train the model
    model.train(training_data, epochs=50, learning_rate=0.001)

    # Evaluate the model
    accuracy = evaluate_performance(model, validation_data)
    print(f"Validation accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()from neural_network import NeuralNetwork
from utils import load_data

if __name__ == "__main__":
    print("🧠 Inicializando NeuroGame AI...")
    data = load_data()
    model = NeuralNetwork()
    model.train(data)
