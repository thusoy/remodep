import os
import tempfile

import remodep

try:
    import unittest.mock as mock
except ImportError:
    import mock


TEST_PROC_MODULES_OUTPUT = '''\
ext4 477942 1 - Live 0xffffffffa0888000
nouveau 1122508 5 - Live 0xffffffffa0647000
acpi_cpufreq 17218 1 - Live 0xffffffffa03a3000
video 18096 1 nouveau, Live 0xffffffffa03de000
processor 28221 1 acpi_cpufreq, Live 0xffffffffa0349000
ahci 33334 2 - Live 0xffffffffa0108000
libahci 27158 1 ahci, Live 0xffffffffa0134000
libata 177508 2 ahci,libahci, Live 0xffffffffa00db000
thermal 17559 0 - Live 0xffffffffa000d000
thermal_sys 27642 3 video,processor,thermal, Live 0xffffffffa0000000
'''


def test_get_module_dependencies():
    uut = lambda x: list(remodep.get_reverse_module_dependencies(x))
    temp_modules = tempfile.NamedTemporaryFile(delete=False)
    temp_modules.write(TEST_PROC_MODULES_OUTPUT)
    temp_modules.close()
    lsmod_mock = mock.Mock(return_value=temp_modules.name)

    with mock.patch('remodep.get_modules_file_path', lsmod_mock):
        assert uut('foobar') == []
        assert uut('ext4') == ['ext4']
        assert uut('thermal_sys') == ['nouveau', 'video', 'acpi_cpufreq', 'processor', 'thermal', 'thermal_sys']
        assert uut('libata') == ['ahci', 'libahci', 'libata']
        assert len(lsmod_mock.mock_calls) == 4

    os.remove(temp_modules.name)
