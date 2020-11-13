#!/usr/bin/python3
import sys
import pdfgen
import asyncio

pdfgen.sync.from_url(sys.argv[1], sys.argv[2])
