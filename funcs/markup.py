"""Cross-version inline color markup for the instruction texts.

The instruction CSVs (instructions/*.csv) author color in one canonical,
simple tag: <c=COLOR>...</c> (COLOR is anything PsychoPy accepts, e.g. a
name like 'red' or a hex code like '#ff0000'). Every text component in this
project currently falls back to plain text -- confirmed on-site that the
installed PsychoPy's TextBox2 does not parse rich-text markup at all (it
printed the raw [color=...] tag as literal text rather than either coloring
it or silently dropping it), so strip_tags() is what every routine's Text
field should actually use for now, e.g. in Builder: $strip_tags(text)

to_textbox2() is kept for later: TextBox2's own [color=...]...[/color]
BBCode-style tag is real (confirmed against PsychoPy's source), it just
isn't active in the currently installed version. If the lab machine's
PsychoPy is ever upgraded, swap strip_tags() for to_textbox2() in the
Builder Text field and inline color should start working with no CSV
changes needed.
"""
import re

_ANY_TAG = re.compile(r'<.*?>')
_OPEN_TAG = re.compile(r'<c=([^>]+)>')


def strip_tags(text):
    """<c=COLOR>...</c>  ->  ...  (plain text, for any version/component)."""
    return _ANY_TAG.sub('', text)


def to_textbox2(text):
    """<c=COLOR>...</c>  ->  [color=COLOR]...[/color]  (for TextBox2, once
    the installed PsychoPy actually renders it -- see module docstring).
    """
    text = _OPEN_TAG.sub(r'[color=\1]', text)
    text = text.replace('</c>', '[/color]')
    return text
