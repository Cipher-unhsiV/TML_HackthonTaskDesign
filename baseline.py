import json
import csv
import torch
import os

# Paths
METADATA_PATH = "metadata.json"
MODEL_PATH = "model/global_model.pt"
OUTPUT_PATH = "submission.csv"

def main():
    # Load metadata
    with open(METADATA_PATH, "r") as f:
        metadata = json.load(f)

    num_clients = metadata["federated_learning"]["num_clients"]

    # (Optional) Load model to show how it would be done
    # This baseline does NOT use the model for predictions
    try:
        state_dict = torch.load(MODEL_PATH, map_location="cpu")
        print("Loaded global_model.pt successfully.")
    except Exception as e:
        print("Warning: could not load model:", e)

    # Generate trivial predictions: all clients are honest
    predictions = []
    for client_id in range(num_clients):
        predictions.append((client_id, "honest"))

    # Write submission file
    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["client_id", "predicted_label"])
        writer.writerows(predictions)

    print(f"Baseline submission written to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
