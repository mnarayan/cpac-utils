import sys
import os
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import io
import pickle
from decimal import Decimal

OUTPUT_DIR = 'data/cpac/derivatives'


def load_timeseries_txt(filename=None, verbose=False, prefix=None):

    df = pd.read_csv(filename, sep='  ', header=None, prefix=prefix)
    df_dims = df.shape
    if verbose:
        print(df_dims)
    
    return df


def load_timeseries_csv(filename=None, verbose=False):

    df = pd.read_csv(filename)
    df_dims = df.shape
    
    row_str = df.values[0].all()
    col_names = row_str.split('\t')
    col_names.remove('#')
    for idx in np.arange(col_names.count('')):
        col_names.remove('')
    for idx,val in enumerate(col_names):
        col_names[idx] = val.replace('  ','')
        if verbose:
            print(col_names[idx])
    
    new_df = pd.DataFrame(columns=col_names)
    
    for idx in np.arange(1,int(df_dims[0]/2+1)):
        row_str = df.values[idx*2].all()
        row_str = row_str.replace('\t\t\t','')
        row_str = row_str.split('\t')
        if verbose:
            print(row_str)
        
        for jdx,val in enumerate(row_str):
            row_str[jdx] = val.replace('  ','')
        
        row_values = np.array(row_str,dtype='float')
        # for jdx,val in enumerate(row_values):
        #     row_values[jdx] = float(Decimal(val))
                
        new_df = new_df.append(
                    pd.DataFrame(row_values,index=col_names).transpose()
                    )

    return new_df
 
def main():
 # print command line arguments
    filepath = sys.argv[1]
    
    with open(filepath) as fp:
        for cnt, fname in enumerate(fp):
               fname = fname.replace('\n','')
               file_dirs = fname.split('/')
               
               if "pipeline" in file_dirs[-7]:
                   output_dir = os.path.join(OUTPUT_DIR,
                                file_dirs[-7])
               else:
                   output_dir = os.path.join(OUTPUT_DIR,
                                file_dirs[-8])
               if not os.path.exists(output_dir):
                       os.makedirs(output_dir)

               if "compcor" in file_dirs[-4]:         
                   output_dir = os.path.join(output_dir,
                                file_dirs[-4].replace('_compcor','compcor'))
               # else:
               #     output_dir = os.path.join(output_dir,
               #                  file_dirs[-7].replace('_compcor','compcor'))
               if not os.path.exists(output_dir):
                       os.makedirs(output_dir)

               if "sub-" in file_dirs[-7]:
                   output_dir = os.path.join(output_dir,
                                file_dirs[-7])
                   save_filename = os.path.join(output_dir,   
                                           "%s" % file_dirs[-7]
                                           )
               else:
                   output_dir = os.path.join(output_dir,
                                file_dirs[-6])
                   save_filename = os.path.join(output_dir,   
                                           "%s" % file_dirs[-6]
                                           )
               if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                
               if "scan" in file_dirs[-4]:               
                   save_filename = save_filename + \
                               "_" + file_dirs[-4].replace('_scan_','') + \
                               "_" +  file_dirs[-2].replace('_mask_','')
               else:
                   save_filename = save_filename + \
                               "_" + file_dirs[-5].replace('_scan_','') + \
                               "_" +  file_dirs[-2].replace('_mask_','')

               print("File {} is {}".format(cnt,fname))
               
               if '.csv' in fname:
                   ts = load_timeseries_csv(fname)
               else:
                   ts = load_timeseries_txt(fname)
                   
               pickle.dump({'X': ts.values, 
                               'columns': ts.columns, 
                               'filepath': file_dirs
                               }, 
                           open(save_filename + ".pickle", "wb")
                           )
               io.savemat(save_filename,
                               dict(X=ts.values,
                               columns=list(ts.columns),
                               filepath=file_dirs),
                               appendmat=True
                               )       
               print(save_filename)

               # if os.path.isfile(fname):
               #     print(save_filename)
               # else:
               #     print('File does not exist')

if __name__ == "__main__":
    main()
