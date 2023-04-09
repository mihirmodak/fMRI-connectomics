##This script downloads the different FASTQ/FASTA files from the NIH Human Microbiome Project page. We were able to download tsv files that held the download links which we accessed via this script. We were also able to add the downloaded files to specific folders that were organized by subjects in order to keep track each subjects' individual sample
from urllib import request
import os
import pandas as pd

meta_data = pd.read_csv("sample_metadata.csv")
subject_ids = meta_data["Source Name"].to_numpy()
conditions = meta_data["Factor Value[diagnosis]"].to_numpy()


print(conditions)

base_path = r"sample_data" ###Change this

for  id, subject in enumerate(subject_ids):
    url_download = "https://s3.amazonaws.com/openneuro/ds000030/ds000030_R1.0.5/uncompressed/sub-{0}/func/sub-{0}_task-rest_bold.nii.gz".format(subject)
    
    condition = conditions[id]
    condition_path = os.path.join("sample_data",condition)

    if not os.path.exists(condition_path):
        os.makedirs(condition_path)
    
    final_path = os.path.join(condition_path, "{0}.nii.gz".format(subject))
    request.urlretrieve(url_download, final_path)

    