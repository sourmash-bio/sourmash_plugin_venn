"""
Tests for sourmash_plugin_venn.
"""
import os
import pytest

import sourmash
import sourmash_tst_utils as utils
from sourmash_tst_utils import SourmashCommandFailed


def test_run_sourmash(runtmp):
    with pytest.raises(SourmashCommandFailed):
        runtmp.sourmash('', fail_ok=True)

    print(runtmp.last_result.out)
    print(runtmp.last_result.err)
    assert runtmp.last_result.status != 0                    # no args provided, ok ;)


def test_run_venn2(runtmp):
    a = utils.get_test_data('a.sig.gz')
    b = utils.get_test_data('b.sig.gz')

    output = runtmp.output('ab.png')
    runtmp.sourmash('scripts', 'venn', a, b, '-o', output)

    print(runtmp.last_result.out)
    print(runtmp.last_result.err)
    assert runtmp.last_result.status == 0

    assert "found two sketches - outputting a 2-part Venn diagram." in runtmp.last_result.err

    assert os.path.exists(output)


def test_run_venn3(runtmp):
    a = utils.get_test_data('a.sig.gz')
    b = utils.get_test_data('b.sig.gz')
    c = utils.get_test_data('c.sig.gz')

    output = runtmp.output('abc.png')
    runtmp.sourmash('scripts', 'venn', a, b, c, '-o', output)

    print(runtmp.last_result.out)
    print(runtmp.last_result.err)
    assert runtmp.last_result.status == 0

    assert "found three sketches - outputting a 3-part Venn diagram." in runtmp.last_result.err

    assert os.path.exists(output)
