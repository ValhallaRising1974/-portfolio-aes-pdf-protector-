# neural_network.py
import torch
import torch.nn as nn
import torch.optim as optim

class GameNeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GameNeuralNet, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, output_size),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.model(x)

    def train(self, data, epochs=20, learning_rate=0.001):
        optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        loss_fn = nn.CrossEntropyLoss()

        for epoch in range(epochs):
            total_loss = 0
            for x_batch, y_batch in data:
                x_batch = torch.tensor(x_batch, dtype=torch.float32)
                y_batch = torch.tensor(y_batch, dtype=torch.long)

                optimizer.zero_grad()
                output = self.forward(x_batch)
                loss = loss_fn(output, y_batch)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            print(f"Epoch {epoch + 1}/{epochs} - Loss: {total_loss:.4f}")class NeuralNetwork:
    def __init__(self):
        print("Rede Neural criada.")

    def train(self, data):
        print(f"Treinando com dados: {data}")
