from robot import run_cli

import sys
import os


runner_path = os.path.abspath(os.path.dirname(__file__))
driver_path = os.path.join(runner_path, 'webdrivers')
landing_page = 'https://www.desmos.com/fourfunction'
output_dir = os.path.join(runner_path, 'logs')

if driver_path not in os.environ['PATH']:
    os.environ['PATH'] += f';{driver_path}'


if __name__ == '__main__':
    default_args = [
        '-v', 'BROWSER:chrome',
        '-v', f'LANDING_PAGE:{landing_page}',
        '--outputdir', output_dir
    ]

    run_cli(default_args + sys.argv[1:])
