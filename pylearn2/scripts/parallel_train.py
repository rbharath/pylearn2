"""
Script implementing logic for parallel training of pylearn2 models
on ICME GPU cluster.
"""
__authors__ = "Bharath Ramsundar"
__email__ = "bharath.ramsundar@gmail.com"

# Standard library imports
import argparse

class ParallelScheduler():
    """
    Spawns the desired number of jobs in parallel. Currently only designed
    for use with Stanford academic clusters.
    """
    def __init__(self, num_jobs, num_parallel, script_name, config):
        self.num_jobs = num_jobs
        self.num_parallel = num_parallel
        self.script_name = script_name
        self.config = config

    def schedule_jobs(self):
        with open(args.config, "r") as input_yaml:
            input_yaml_str = input_yaml.read()
        pass

def make_argument_parser():
    """
    Creates an ArgumentParser to read the options for this script from
    sys.argv
    """
    parser = argparse.ArgumentParser(
        description='Launch parallel experiments from '
                    'a YAML configuration file.',
        epilog='\n'.join(__doc__.strip().split('\n')[1:]).strip(),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--num-jobs', '-N', type=int,
                        help='The total number of parallel runs '
                             'for given yaml file')
    parser.add_argument('--num-parallel', '-P', type=int,
                        help='Max number of jobs that can be run '
                             'simultaneously in parallel')
    parser.add_argument('--script-name', action='store',
                        choices=None,
                        help='A python script that accepts a single '
                             'yaml file as argument.')
    parser.add_argument('config', action='store',
                        choices=None,
                        help='A YAML configuration file specifying the\n'
                             'training procedure. This yaml must have\n'
                             'string replace tokens in its save path')
    return parser

if __name__ == "__main__":
    """See module-level docstring for a description of the script."""
    parser = make_argument_parser()
    args = parser.parse_args()
    scheduler = ParallelScheduler(args.num_jobs, args.num_parallel,
                    args.script_name, args.config)
    scheduler.schedule_jobs()
