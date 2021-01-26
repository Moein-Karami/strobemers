import os,sys
import argparse

import random

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except (ImportError, RuntimeError):
    print("COULD not import matplotlib")

import seaborn as sns
import pandas as pd
from matplotlib import pyplot


def plot(input_csv, outfolder, acc):

    indata = pd.read_csv(input_csv)
    print(indata)
    g = sns.lineplot(data=indata, x="k", y="unique", hue="datastructure", palette = sns.color_palette()[:5])
    # axes = g.axes
    # g.set_ylabels("Count")
    # g.set_xlabels("Number of splice sites")
    # axes.set_xticks(np.arange(0, 70, step=5) )
    # axes.set_xlim(xlim=(0, 70))
    # g.set_xlim(0,70)
    # g.set_xticks(np.arange(0, 70, step=5))
    # ax.set_ylabel("Error rate %")

    plt.savefig(os.path.join(outfolder, "uniqueness_{0}.eps".format(acc)))
    plt.savefig(os.path.join(outfolder, "uniqueness_{0}.pdf".format(acc)))
    plt.close()




def main(args):

    plot(args.csv, args.outfolder, args.acc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calc identity", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('csv', type=str, help='Path to consensus fastq file(s)')
    parser.add_argument('outfolder', type=str,  help='A fasta file with transcripts that are shared between samples and have perfect illumina support.')
    parser.add_argument('acc', type=str,  help='A fasta file with transcripts that are shared between samples and have perfect illumina support.')
    # parser.add_argument('--pickled_subreads', type=str, help='Path to an already parsed subreads file in pickle format')
    # parser.set_defaults(which='main')
    args = parser.parse_args()



    if len(sys.argv)==1:
        parser.print_help()
        sys.exit()

    main(args)