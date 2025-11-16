# Step E — Trust Score (Public Version)

## Overview

The **ATLP Trust Score** is a conceptual metric that represents how reliable,
compliant, and trustworthy an AI model or agent has been over time.

It does **not** judge “intelligence” or “quality” in a generic sense.  
Instead, it answers a focused question:

> “How consistently does this AI behave within its licensed rules and verification checks?”

The public documentation explains **what** influences the Trust Score and **how it is used**,  
but does **not** disclose internal scoring formulas or implementation details.

---

## Core Ideas

The Trust Score is:

- **History-aware** — it reflects past behavior, not just a single event  
- **Contextual** — it relates to the model’s license, use-case, and environment  
- **Action-linked** — it moves based on actual, verifiable events  
- **Enforcement-aware** — it is influenced by violations and penalties  

The goal is to make AI behavior:

- more predictable  
- more auditable  
- more accountable  

---

## What Can Affect the Trust Score?

At a high level, the Trust Score can be influenced by:

### ✅ Positive Factors (Increase Score)

- Passing verification checks consistently  
- Long periods of compliant behavior  
- Successfully serving requests within licensed boundaries  
- Transparent versioning and updates  
- Strong evidence history and clear logging  

### ❌ Negative Factors (Decrease Score)

- Violations of license terms  
- Repeated policy breaches  
- Attempts to bypass verification  
- Conflicts with governance rules  
- Evidence of misuse or unsafe behavior  

Exact scoring amounts, thresholds, and weighting remain internal.

---

## How the Trust Score Is Used (Conceptually)

The Trust Score can be used by:

- **Platforms** — to decide what an AI is allowed to do  
- **Developers** — to monitor their models and agents over time  
- **Governance bodies** — to evaluate risk and determine enforcement actions  
- **Users or integrators** — to prefer higher-trust models for sensitive tasks  

Examples of how the Trust Score might be used (conceptually):

- Minimum score required to operate autonomously  
- Certain features only enabled above a threshold  
- Stricter monitoring for low-trust models  
- Governance review if trust drops below a critical level  

---

## Public vs Internal View

This public version describes the Trust Score at a **conceptual level only**.

Public documentation includes:

- What the Trust Score represents  
- What can influence it  
- How it might be used in decisions  

Internal documentation (kept private) includes:

- Exact formulas and scoring functions  
- Detailed penalty/bonus values  
- Specific evidence integration rules  
- Storage, cryptographic, and audit mechanisms  
- Any sensitive or patent-relevant design details  

---

## Role of Trust in the ATLP Ecosystem

In ATLP, the Trust Score is not just a number — it’s a way to:

- Encourage responsible AI behavior  
- Provide a shared language for “how much can we rely on this model?”  
- Tie licensing, verification, and enforcement together in a coherent way  

It is one of the core levers that enables:

- **Governance** (Step G)  
- **Enforcement** (Step H)  
- **Licensing decisions** (Step B)  
- **Verification outcomes** (Step C)  

This document is meant to help developers and stakeholders understand the concept  
without exposing any of the internal mechanics that remain part of the private ATLP Master Specification.
