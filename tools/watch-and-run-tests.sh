#!/bin/sh

TEST_COMMAND="./test --exitfirst --failed-first"

$TEST_COMMAND

# TODO: Ideally we'd ignore the .git/ and venv/ dirs to prevent listening to
# a ton of files, but watchdog doesn't seem to support ignoring subdirectories
# for now.
./venv/bin/watchmedo shell-command \
    --patterns="*.py" \
    --recursive \
    --command "$TEST_COMMAND" \
    .
