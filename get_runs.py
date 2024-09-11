import wandb
import wandb_workspaces.reports.v2 as wr
import os, sys
import time
wandb.require("core")

PROJECT_NAME="eval-llama-3.1-8b-fine-tune"
ENTITY="reviewco"

def main():

    api = wandb.Api()
    runs = api.runs(path=f"{ENTITY}/{PROJECT_NAME}")
    for run in runs:
        s_run_plus_state = run.displayName + "-" + run.state
        print(s_run_plus_state)

if __name__ == "__main__":
    main()

