''' Tools for formatting JSON
'''
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


def json_obj_fmt(json_obj, compact=False):
    if compact:
        return json.dumps(json_obj, separators=(',', ':'))
    return json.dumps(
        json_obj, sort_keys=True, indent=4, separators=(',', ': '))


def json_str_fmt(json_str, compact=False):
    json_obj = json.loads(json_str)
    return json_obj_fmt(json_obj, compact)


def display_json_str_color(json_str):
    lexer = JsonLexer()
    formatter = TerminalFormatter()
    print(highlight(json_str, lexer, formatter))


def main():
    json_str = '{"Street": "123 Main St", "City": "Anytown"}'
    json_out1 = json_str_fmt(json_str, compact=True)
    json_out2 = json_str_fmt(json_str, compact=False)
    print(json_out1)
    print(json_out2)
    display_json_str_color(json_out2)


if __name__ == '__main__':
    main()
