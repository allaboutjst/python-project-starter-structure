# -*- coding: utf-8 -*-

import sys
from os import environ
from os.path import dirname, join, pardir, abspath, exists
import subprocess

import nose

def fetch_demo_repo():
    # user is manually setting YAML dir, don't tamper with it
    if 'TEST_DEMO_YAML_DIR' in environ:
        return

    repo_path = environ.get(
        'TEST_ES_REPO',
        abspath(join(dirname(__file__), pardir, pardir, 'demo'))
    )

    # no repo
    if not exists(repo_path) or not exists(join(repo_path, '.git')):
        print('No demo repo found...')
        # set YAML DIR to empty to skip yaml tests
        environ['TEST_DEMO_YAML_DIR'] = ''
        return

    # set YAML test dir
    environ['TEST_DEMO_YAML_DIR'] = join(repo_path, 'rest-api-spec', 'src', 'main', 'resources', 'rest-api-spec', 'test')

    # fetching of yaml tests disabled, we'll run with what's there
    if environ.get('TEST_ES_NOFETCH', False):
        return


def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down....\n')

    # fetch yaml tests
    fetch_demo_repo()

    # always insert coverage when running tests
    if argv is None:
        argv = [
            'nosetests', '--with-xunit',
            '--with-xcoverage', '--cover-package=demo', '--cover-erase',
            '--logging-filter=demo', '--logging-level=DEBUG',
            '--verbose',
        ]

    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__))
    )

if __name__ == '__main__':
    run_all(sys.argv)