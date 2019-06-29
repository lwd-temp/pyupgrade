# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import sys

import pytest

from pyupgrade import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        # Any number of zeros is considered a legal token
        '0', '00',
        # Don't modify non octal literals
        '1', '12345', '1.2345',
    ),
)
def test_noop_octal_literals(s):
    assert _fix_tokens(s, py3_plus=False) == s


@pytest.mark.xfail(sys.version_info >= (3,), reason='python2 "feature"')
@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('0755', '0o755'),
        ('05', '5'),
    ),
)
def test_fix_octal_literal(s, expected):
    assert _fix_tokens(s, py3_plus=False) == expected
