import torch
import joblib
import numpy as np

# Import model architecture
from train import StudentModel

# Load trained model
model = StudentModel()

model.load_state_dict(
    torch.load(
        "student_model.pth",
        map_location="cpu",
        weights_only=True
    )
)

model.eval()

# Load Scaler
scaler = joblib.load("scaler.pkl")

# New Student Information 
student = np.array([[7,85,65]])

# Process Input
student = scaler.transform(student)

student = torch.tensor(
    student, 
    dtype=torch.float32
)

# Predict

with torch.no_grad():
    output = model(student)
    probability = torch.sigmoid(output).item()

    if probability>= 0.5:
        print("Predictions: PASS")
    else:
        print("Predictions: FAIL")

    print("Pass Probability: ", probability)