#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import json
import os
import ConfigParser


def get_plugins():
    config = ConfigParser.RawConfigParser()
    abs_dir = os.path.abspath(os.path.dirname(__file__))
    config.read(os.path.join(abs_dir, "config.cfg"))
    plugin_str = config.get("plugins", "enabled")
    plugin_list = [x.strip() for x in plugin_str.split(",")]
    sys.path.append(os.path.join(abs_dir, "plugins"))

    plugin_methods = []

    for plugin in plugin_list:
        try:
            plugin_methods.append(__import__(plugin).return_json)
        except ImportError:
            #print("Warning: Could not import plugin %s" % plugin)
            pass
    return plugin_methods


def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()


def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()


def main():
    # initialize plugins
    plugins = get_plugins()

    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
                        line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        i = 0
        for plugin in plugins:
            j.insert(i, plugin())
            i += 1
        # and echo back new encoded json
        print_line(prefix + json.dumps(j))

if __name__ == "__main__":
    main()
