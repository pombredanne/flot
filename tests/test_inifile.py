import pathlib

import pytest

from flit.inifile import read_pkg_ini, ConfigError

samples_dir = pathlib.Path(__file__).parent / 'samples'

def test_invalid_classifier():
    with pytest.raises(ConfigError):
        read_pkg_ini(samples_dir / 'invalid_classifier.ini')
