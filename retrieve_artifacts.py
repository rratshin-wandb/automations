import os, sys, time
import wandb
wandb.require("core")

PROJECT_NAME="eval-llama-3.1-8b-fine-tune"
ENTITY="reviewco"

def main():

    time.sleep(180)
    print("[" + get_tstamp() + "] Artifacts retrieved.")

def get_tstamp():
    # get timestamp
    from datetime import datetime
    tstamp = datetime.now().strftime("%Y%m%d%H%M%S%f") # 20240910113645272981
    # tstamp = tstamp[:16]
    return tstamp

if __name__ == "__main__":
    main()

