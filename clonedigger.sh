#!/bin/sh
OUT=`clonedigger pyproject|egrep -o "\d+ clones were found"`
echo "${OUT}" | cut -d" " -f1 | xargs test 1 -gt
if [ $? -ne 0 ]; then
    echo "${OUT}" >&2
    exit 1
fi
