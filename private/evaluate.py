import torch
import csv
import sys
from sklearn.metrics import accuracy_score, f1_score

# -------------------------
# Paths (adjust if needed)
# -------------------------
GROUND_TRUTH_PATH = "ground_truth_client_labels.pt"
SUBMISSION_PATH = sys.argv[1]  # path to submission.csv

# -------------------------
# Load ground truth
# -------------------------
ground_truth = torch.load(GROUND_TRUTH_PATH)

# Convert to sorted lists
gt_labels = []
pred_labels = []

# -------------------------
# Load submission
# -------------------------
submission = {}

with open(SUBMISSION_PATH, "r") as f:
    reader = csv.DictReader(f)
    if "client_id" not in reader.fieldnames or "predicted_label" not in reader.fieldnames:
        raise ValueError("Submission must contain 'client_id' and 'predicted_label' columns.")

    for row in reader:
        client_id = int(row["client_id"])
        label = row["predicted_label"].strip().lower()

        if label not in {"honest", "malicious"}:
            raise ValueError(f"Invalid label '{label}' for client {client_id}")

        submission[client_id] = label

# -------------------------
# Match predictions to ground truth
# -------------------------
for client_id in sorted(ground_truth.keys()):
    if client_id not in submission:
        raise ValueError(f"Missing prediction for client_id {client_id}")

    gt_labels.append(ground_truth[client_id])
    pred_labels.append(submission[client_id])

# -------------------------
# Compute metrics
# -------------------------
accuracy = accuracy_score(gt_labels, pred_labels)
macro_f1 = f1_score(gt_labels, pred_labels, average="macro")

# -------------------------
# Output results
# -------------------------
print("Evaluation Results")
print("------------------")
print(f"Accuracy : {accuracy:.4f}")
print(f"Macro F1 : {macro_f1:.4f}")
