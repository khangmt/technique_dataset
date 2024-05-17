import os
os.environ["TFHUB_CACHE_DIR"] = "./data/tf_hub"
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from classes.managment import Manager
from multiprocessing import set_start_method
from classes.procedure import Procedure
from classes.finalizing import stat_Calculator
# from mitre_attack import MitreAttack
from modules import *

def main():
    pass

if __name__ == "__main__":
    try:
        set_start_method("spawn")
    except:
        print("context already set")
    Manager(campaign_from_0= False, procedure_from_0=False, technique_from_0= False,techniue_alignment_from_0=False,
            matching_from_0=False, context_similarity_from0=False, multiprocessing=False,do_procedure_deduplication=False)
