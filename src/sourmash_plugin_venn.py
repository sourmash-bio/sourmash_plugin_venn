"Read/write sketches via plugin."
import pylab
from matplotlib_venn import venn2, venn3

import sourmash
from sourmash.logging import debug_literal
from sourmash.plugins import CommandLinePlugin


###

#
# CLI plugin - supports 'sourmash scripts venn'
#

class Command_Venn(CommandLinePlugin):
    command = 'venn'
    description = "makes a venn diagram of the overlap between two sketches"

    def __init__(self, subparser):
        super().__init__(subparser)
        # add argparse arguments here.
        debug_literal('RUNNING cmd venn __init__')
        subparser.add_argument('sketches', nargs='+')
        subparser.add_argument('-o', '--output', default=None)

    def main(self, args):
        # code that we actually run.
        super().main(args)
        print('RUNNING cmd', self, args)

        sketch_files = list(args.sketches)
        print(sketch_files)

        sketches = []
        for filename in sketch_files:
            x = list(sourmash.load_file_as_signatures(filename))
            sketches.extend(x)

        assert len(sketches) == 2

        hashes1 = set(sketches[0].minhash.hashes)
        hashes2 = set(sketches[1].minhash.hashes)

        label1 = sketches[0].name
        label2 = sketches[1].name

        venn2([hashes1, hashes2], set_labels=(label1, label2))
        if args.output:
            print(f"saving to '{args.output}'")
            pylab.savefig(args.output)
