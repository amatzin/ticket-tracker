"""Build the claude.ai artifact version of the app.

The artifact host supplies the document wrapper, so the output is just the page's
<title>, <style> and body content. Usage: python3 tools/build-artifact.py OUT.html
"""
import pathlib, re, sys

src = (pathlib.Path(__file__).parent.parent / 'index.html').read_text()
title = re.search(r'<title>.*?</title>', src, re.S).group(0)
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
pathlib.Path(sys.argv[1]).write_text(f'{title}\n{style}\n{body.strip()}\n')
