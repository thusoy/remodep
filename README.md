# remodep

List reverse kernel module dependencies for loaded modules.

Installation:

    $ pip install remodep

Usage:

    $ remodep pcspkr
    pcspkr

    $ remodep libata
    ahci
    libahci
    libata

Definitely unload a kernel module including the modules that use it:

    $ remodep scsi_mod | xargs rmmod


## Development

    $ ./configure
    $ ./test

To re-run tests on each change:

    $ ./tools/watch-and-run-tests.sh
