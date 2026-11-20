import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("students.csv")

X = df[
    [
        "study_hours",
        "attendance",
        "previous_marks"
    ]
].values

y = df["passed"].values

# Split Data
X_train , X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

# Normalize Data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert into pytorch Tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(
    y_train, dtype=torch.float32
).view(-1,1)

y_test =torch.tensor(
    y_test,dtype=torch.float32
).view(-1,1)

class StudentModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(

            # Input layer: 3 features
            nn.Linear(3, 16),

            # Activation function
            nn.ReLU(),

            # Hidden layer
            nn.Linear(16, 8),

            nn.ReLU(),

            # Output layer
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.network(x)


# Create model
model = StudentModel()

print(model)

print("Model Ended")

print("Model Accuracy Started")

# Loss Function
criterion = nn.BCEWithLogitsLoss()

# Optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# Training loop
epochs = 100

for epoch in range(epochs):

    # Forward Pas
    output = model(X_train)

    # Calculate Loss
    loss= criterion(output, y_train)

    # Clear previous Gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update model weight
    optimizer.step()

    if( epoch +1 )%10 ==0:
        print(
            f"Epoch: [{epoch+1} / {epochs}], "
            f"Loss: [ {loss.item():.4f} ]"
        )

model.eval()

with torch.no_grad():
    predictions = model(X_test)

    probabilities = torch.sigmoid(predictions)

    predicted_classes = (
        probabilities >= 0.5
    ).float()

    accuracy = accuracy_score(
        y_test.numpy(),
        predicted_classes.numpy()
    )

    print("Model Accuracy", accuracy)

print("Model Accuracy Ended")

print("Model Saving Start")
# Save trained model weights
torch.save(
    model.state_dict(),
    "student_model.pth"
)
# Save preprocessing scaler
joblib.dump(
    scaler,
    "scaler.pkl"
)
print("Model Save Successfully")
print("Model ENDS!!!!!!!!!!!!")

    