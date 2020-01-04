import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python36(host):
    python = host.package('rh-python36')
    assert python.is_installed


def test_docker(host):
    docker = host.package('docker')
    assert docker.is_installed


def test_git(host):
    git = host.package('git')
    assert git.is_installed
