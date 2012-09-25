#!/usr/bin/env python

import sys
import Tkinter, tkMessageBox

def main():
    window = Tkinter.Tk()
    window.wm_withdraw()
    tkMessageBox.showinfo(title='Hi', message='Hello world!')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
