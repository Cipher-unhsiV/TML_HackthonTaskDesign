# Detecting Malicious Clients in Federated Learning

## Overview

Federated learning (FL) enables collaborative model training without sharing raw data. However, this setting is vulnerable to malicious or non-compliant clients that can poison training, submit low-quality updates, or free-ride on others’ computation.

In this task, participants act as security auditors and analyze a completed federated learning run to identify which clients behaved maliciously during training.

---

## Task Description

You are given artifacts from a federated learning system after training has completed.  
Some clients followed the protocol correctly, while others deviated from it.

Your goal is to **identify which clients were malicious**.

This is a **binary classification task** at the client level.

---

## What You Are Given

- The **final global model** produced by federated learning  
- Metadata describing the training setup (e.g., number of rounds, aggregation method, model architecture)  
- Optionally, anonymized or aggregated client-level statistics  

You are **not** given:
- Raw client data  
- Client behavior labels  
- Descriptions of malicious strategies  

---

## Your Objective

For each client, predict whether it is:
- `honest`
- `malicious`

---

## Submission Format

Submit a CSV file named `submission.csv` with the following format:

```csv
client_id,predicted_label
0,honest
1,malicious
2,honest
...
```

- ```client_id``` must match the provided client identifiers
- ```predicted_label``` must be either ```honest``` or ```malicious```

---

## Evaluation

Your submission will be evaluated against hidden ground-truth client behavior labels.

### Metrics

- **Primary metric:** Accuracy  
- **Secondary metric:** Macro F1-score (used as a tie-breaker)

Participants are ranked by accuracy, with Macro F1-score used to break ties.

---

## Rules and Constraints

- You may **not retrain** the provided model.
- Only the provided artifacts may be used.
- No access to raw client data is allowed.
- All computation must be performed offline.

---

## Ground Truth

Ground truth labels are defined by how each client was implemented in the federated learning simulation.  
Each client is unambiguously labeled as either **honest** or **malicious**.

---

## What This Task Is Not

- Not membership inference  
- Not memorization analysis  
- Not continuous score estimation  
- Not interpretability-only analysis  

---

## Goal

This task reflects a realistic and high-impact security challenge: **detecting malicious behavior in large-scale federated learning systems after training has completed**.



