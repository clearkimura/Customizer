#!/usr/bin/python2.7

import sys
import curses

tty_colors = 0
DEBUG = False

try:
    curses.setupterm()
    tty_colors = curses.tigetnum('colors')
except curses.error:
    pass

if tty_colors >= 8 and sys.stdout.isatty():
    cmarker = '\033[1;34m'
    cinfo = '\033[1;32m'
    cwarning = '\033[1;33m'
    ccritical = '\033[1;31m'
    cdebug = '\033[1;36m'
    cnormal = '\033[0m'
else:
    cmarker = ''
    cinfo = ''
    cwarning = ''
    ccritical = ''
    cdebug = ''
    cnormal = ''

    # http://stackoverflow.com/questions/107705/python-output-buffering
    class Unbuffered(object):
        ''' Override print behaviour '''
        def __init__(self, stream):
            self.stream = stream

        def write(self, data):
            ''' Write to stdout without buffering '''
            self.stream.write(data)
            self.stream.flush()

        def __getattr__(self, attr):
            return getattr(self.stream, attr)

    sys.stdout = Unbuffered(sys.stdout)


def info(msg, marker=None):
    ''' Print message with INFO status '''
    if not marker is None:
        print('{}* {}{}: {}{}{}'.format( \
            cmarker, cnormal, msg, cinfo, marker, cnormal))
    else:
        print('{}* {}{}'.format(cmarker, cnormal, msg))


def warning(msg, marker=None):
    ''' Print message with WARNING status '''
    if not marker is None:
        sys.stderr.write('{}* {}{}: {}{}{}\n'.format( \
            cwarning, cnormal, msg, cwarning, marker, cnormal))
    else:
        sys.stderr.write('{}* {}{}\n'.format(cwarning, cnormal, msg))


def critical(msg, marker=None):
    ''' Print message with CRITICAL status '''
    if not marker is None:
        sys.stderr.write('{}* {}{}: {}{}{}\n'.format( \
            ccritical, cnormal, msg, ccritical, marker, cnormal))
    else:
        sys.stderr.write('{}* {}{}\n'.format(ccritical, cnormal, msg))


def debug(msg, marker=None):
    ''' Print message with DEBUG status '''
    if DEBUG:
        if not marker is None:
            print('{}* {}{}: {}{}{}'.format( \
                cdebug, cnormal, msg, cdebug, marker, cnormal))
        else:
            print('{}* {}{}'.format(cdebug, cnormal, msg))


def sub_info(msg, marker=None):
    ''' Print sub-message with INFO status '''
    if not marker is None:
        print('{}  => {}{}: {}{}{}'.format( \
            cmarker, cnormal, msg, cinfo, marker, cnormal))
    else:
        print('{}  => {}{}'.format(cmarker, cnormal, msg))


def sub_warning(msg, marker=None):
    ''' Print sub-message with WARNING status '''
    if not marker is None:
        sys.stderr.write('{}  => {}{}: {}{}{}\n'.format( \
            cwarning, cnormal, msg, cwarning, marker, cnormal))
    else:
        sys.stderr.write('{}  => {}{}\n'.format(cwarning, cnormal, msg))


def sub_critical(msg, marker=None):
    ''' Print sub-message with CRITICAL status '''
    if not marker is None:
        sys.stderr.write('{}  => {}{}: {}{}{}\n'.format( \
            ccritical, cnormal, msg, ccritical, marker, cnormal))
    else:
        sys.stderr.write('{}  => {}{}\n'.format(ccritical, cnormal, msg))


def sub_debug(msg, marker=None):
    ''' Print sub-message with DEBUG status '''
    if DEBUG:
        if not marker is None:
            print('{}  => {}{}: {}{}{}'.format( \
			cdebug, cnormal, msg, cdebug, marker, cnormal))
        else:
            print('{}  => {}{}'.format(cdebug, cnormal, msg))

class exception(Exception):
    pass
