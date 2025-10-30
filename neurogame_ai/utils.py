# utils.py
import random

def load_data():
    # Simulated dataset for training and validation
    def generate_sample():
        x = [random.random() for _ in range(100)]
        y = random.randint(0, 4)
        return x, y

    training_data = [generate_sample() for _ in range(200)]
    validation_data = [generate_sample() for _ in range(50)]

    return training_data, validation_data

def evaluate_performance(model, data):
    correct = 0
    total = len(data)
    for x, y in data:
        input_tensor = torch.tensor([x], dtype=torch.float32)
        output = model(input_tensor)
        predicted = output.argmax(dim=1).item()
        if predicted == y:
            correct += 1
    return (correct / total) * 100def load_data():
    print("🔍 Carregando dados simulados...")
    return [1, 2, 3, 4, 5]
