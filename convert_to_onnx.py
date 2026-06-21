import torch
import torch.nn as nn

class SentimentModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10,2)

    def forward(self,x):
        return self.fc(x)

model = SentimentModel()

dummy_input = torch.randn(1,10)

torch.onnx.export(
    model,
    dummy_input,
    "model/sentiment_model.onnx"
)

print("ONNX model created")