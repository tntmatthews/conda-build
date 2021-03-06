import os
import json
import glob
import sys


def main():
    prefix = os.environ['PREFIX']

    info_files = glob.glob(os.path.join(prefix, 'conda-meta',
                             'conda-build-test-python-xx-1.0-py34*0.json'))
    assert len(info_files) == 1
    info_file = info_files[0]
    with open(info_file, 'r') as fh:
        info = json.load(fh)

    # numpy with no version, python with no version, python with version pin
    depends = sorted(info['depends'])
    assert depends[0].startswith('python ')
    assert sys.version[:3] == ("3.4")


if __name__ == '__main__':
    main()
