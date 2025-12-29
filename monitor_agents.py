#!/usr/bin/env python3
"""Monitor agent progress in real-time"""

import os
import glob

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'

print("=" * 70)
print("AGENT PROGRESS MONITOR")
print("=" * 70)

# Check for newly created batch files
print("\nNewly created individual language batches:")
pattern = os.path.join(ANALYTICS_DIR, "*-batch-*.json")
batch_files = sorted(glob.glob(pattern))

if batch_files:
    for filepath in batch_files:
        filename = os.path.basename(filepath)
        size = os.path.getsize(filepath)
        print(f"  {filename} ({size:,} bytes)")
else:
    print("  No individual batch files found yet")

# Check standard batch files
print("\nStandard batch files status:")
tools = ['datarobot', 'domo-ai', 'h2oai', 'microstrategy-ai', 'power-bi-copilot', 'qlik-sense-ai', 'sisense-ai', 'yellowfin-ai']

for tool in tools:
    print(f"\n{tool}:")
    for batch_num in [1, 2, 3]:
        filepath = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 100:
                print(f"  batch{batch_num}: {size:,} bytes")
            else:
                print(f"  batch{batch_num}: Empty ({size} bytes)")

print("\n" + "=" * 70)
