#!/bin/sh
webpage=skybucket/
pycodestyle $webpage
pydocstyle $webpage
pyflakes $webpage

