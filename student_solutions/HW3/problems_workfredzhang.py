import json
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

data_path = os.path.join(script_dir, 'hypothetical_scenario_data.json')
with open(data_path, 'r') as f:
    data = json.load(f)

# ---------------------------------------------------------
# PROBLEM 1: Agent Time Taken: Edited vs. Unedited
# ---------------------------------------------------------

time_by_type = defaultdict(lambda: {"edited": [], "unedited": []})

for record in data:
    inquiry_type = record["inquiry_type"]
    time = record["agent_time_taken_sec"]
    edited = record["agent_edit_distance_chars"] > 0
    key = "edited" if edited else "unedited"
    time_by_type[inquiry_type][key].append(time)

inquiry_types = sorted(time_by_type.keys())
unedited_means = [np.mean(time_by_type[t]["unedited"]) if time_by_type[t]["unedited"] else 0 for t in inquiry_types]
edited_means   = [np.mean(time_by_type[t]["edited"])   if time_by_type[t]["edited"]   else 0 for t in inquiry_types]

x = np.arange(len(inquiry_types))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width / 2, unedited_means, width, label="Unedited", color="steelblue")
ax.bar(x + width / 2, edited_means,   width, label="Edited",   color="coral")

ax.set_title("Mean Agent Time Taken: Edited vs. Unedited Drafts")
ax.set_xlabel("Inquiry Type")
ax.set_ylabel("Mean Agent Time Taken (sec)")
ax.set_xticks(x)
ax.set_xticklabels(inquiry_types, rotation=15, ha="right")
ax.legend()
fig.tight_layout()

plt.savefig(os.path.join(results_dir, "bar_grouped_time.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 2: Time vs. Satisfaction by Inquiry Type
# ---------------------------------------------------------

inquiry_type_set = sorted({r["inquiry_type"] for r in data})
color_map = plt.cm.get_cmap("tab10", len(inquiry_type_set))
type_to_color = {t: color_map(i) for i, t in enumerate(inquiry_type_set)}

fig, ax = plt.subplots(figsize=(10, 6))
for inquiry_type in inquiry_type_set:
    subset = [r for r in data if r["inquiry_type"] == inquiry_type]
    times  = [r["agent_time_taken_sec"]        for r in subset]
    csat   = [r["customer_satisfaction_score"] for r in subset]
    ax.scatter(times, csat, label=inquiry_type, color=type_to_color[inquiry_type], alpha=0.6, edgecolors="none")

ax.set_title("Agent Time Taken vs. Customer Satisfaction by Inquiry Type")
ax.set_xlabel("Agent Time Taken (sec)")
ax.set_ylabel("Customer Satisfaction Score")
ax.legend(title="Inquiry Type", bbox_to_anchor=(1.05, 1), loc="upper left")
fig.tight_layout()

plt.savefig(os.path.join(results_dir, "scatter_time_vs_csat.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 3: Time Distribution by AI Confidence Score
# ---------------------------------------------------------

high_conf = [r["agent_time_taken_sec"] for r in data if r["ai_confidence_score"] >= 0.8]
low_conf  = [r["agent_time_taken_sec"] for r in data if r["ai_confidence_score"] <  0.8]

fig, ax = plt.subplots(figsize=(10, 6))
bins = np.linspace(
    min(min(high_conf), min(low_conf)),
    max(max(high_conf), max(low_conf)),
    30
)
ax.hist(high_conf, bins=bins, alpha=0.6, label="High Confidence (≥ 0.8)", color="steelblue")
ax.hist(low_conf,  bins=bins, alpha=0.6, label="Low Confidence (< 0.8)",  color="coral")

ax.set_title("Agent Time Distribution by AI Confidence Score")
ax.set_xlabel("Agent Time Taken (sec)")
ax.set_ylabel("Frequency")
ax.legend()
fig.tight_layout()

plt.savefig(os.path.join(results_dir, "hist_overlaid_time.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 4: Satisfaction Trend with Variance Bounds
# ---------------------------------------------------------

scores = np.array([r["customer_satisfaction_score"] for r in data], dtype=float)
window = 20

# Rolling stats via a strided cumsum approach
rolling_mean = np.convolve(scores, np.ones(window) / window, mode="valid")
rolling_std  = np.array([scores[i:i + window].std() for i in range(len(scores) - window + 1)])

# Index aligned to the center of each window
index = np.arange(window - 1, len(scores))

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(index, rolling_mean, label="Rolling Mean (w=20)", color="steelblue", linewidth=2)
ax.fill_between(
    index,
    rolling_mean - rolling_std,
    rolling_mean + rolling_std,
    alpha=0.25,
    color="steelblue",
    label="± 1 Std Dev"
)

ax.set_title("Customer Satisfaction: Rolling Mean with Variance Bounds")
ax.set_xlabel("Interaction Index")
ax.set_ylabel("Customer Satisfaction Score")
ax.legend()
fig.tight_layout()

plt.savefig(os.path.join(results_dir, "line_rolling_satisfaction.png"))
plt.close()

print(f"All plots generated and saved in {results_dir}")

