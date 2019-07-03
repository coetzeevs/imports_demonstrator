import argparse
import importlib
import os

if __name__ == '__main__':
    print('Parse value from argument call...')
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True,
                        help="name of the job file without the .py extention e.g. solution_demo i.s.o. solution_demo.py")

    args = parser.parse_args()

    try:
        print('Import job module...')
        # this line imports the module specified in the ArgumentParser from the job-folder
        # and runs the __init__ commands that makes available the modules in the helpers file
        importlib.import_module(f'job.{args.job}')

    except:
        raise
