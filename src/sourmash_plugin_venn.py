"Create and write out a pairwise Venn diagram."
import sys

import pylab
from matplotlib_venn import venn2, venn3

import sourmash
from sourmash import sourmash_args
from sourmash.logging import debug_literal, error, notify
from sourmash.plugins import CommandLinePlugin
from sourmash.cli.utils import (add_ksize_arg, add_moltype_args)

###

#
# CLI plugin - supports 'sourmash scripts venn'
#

class Command_Venn(CommandLinePlugin):
    command = 'venn'
    description = "makes a venn diagram of the overlap between two or three sketches"

    def __init__(self, subparser):
        super().__init__(subparser)
        # add argparse arguments here.
        debug_literal('RUNNING cmd venn __init__')
        subparser.add_argument('sketches', nargs='+',
                               help="file(s) containing two or three sketches")
        subparser.add_argument('-o', '--output', default=None,
                               help="save Venn diagram image to this file",
                               required=True)
        subparser.add_argument('--name1', default=None,
                               help="override name for first sketch")
        subparser.add_argument('--name2', default=None,
                               help="override name for second sketch")
        subparser.add_argument('--name3', default=None,
                               help="override name for (optional) third sketch")
        add_ksize_arg(subparser)
        add_moltype_args(subparser)

    def main(self, args):
        # code that we actually run.
        super().main(args)
        moltype = sourmash_args.calculate_moltype(args)

        debug_literal(f'RUNNING cmd {self} {args}')

        sketch_files = list(args.sketches)

        sketches = []
        for filename in sketch_files:
            notify(f"Loading sketches from {filename}")
            x = list(sourmash.load_file_as_signatures(filename,
                                                      ksize=args.ksize,
                                                      select_moltype=moltype))
            notify(f"...loaded {len(x)} sketches from {filename}.")
            sketches.extend(x)

        if not len(sketches):
            error("ERROR: no sketches found. Must supply 2 or 3.")
            sys.exit(-1)
        elif len(sketches) == 1:
            error("ERROR: only found one sketch. Must supply 2 or 3.")
            sys.exit(-1)
        elif len(sketches) > 3:
            error("ERROR: found more than three sketches. Must supply 2 or 3.")
            sys.exit(-1)

        hashes1 = set(sketches[0].minhash.hashes)
        hashes2 = set(sketches[1].minhash.hashes)
            
        label1 = args.name1 or sketches[0].name
        label2 = args.name2 or sketches[1].name

        if len(sketches) == 2:
            venn2([hashes1, hashes2], set_labels=(label1, label2))

        elif len(sketches) == 3:
            hashes3 = set(sketches[2].minhash.hashes)
            label3 = args.name3 or sketches[2].name
            venn3([hashes1, hashes2,hashes3], set_labels=(label1, label2, label3))

        if args.output:
            print(f"saving to '{args.output}'")
            pylab.savefig(args.output)
