import os
import pandas as pd


def read_chrom_size(version):
    fn_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(fn_dir, 'bio_database/{}.chrom.size'.format(version))
    df = pd.read_csv(fn, sep='\t')
    return df.set_index('chrom')['size'].to_dict()
