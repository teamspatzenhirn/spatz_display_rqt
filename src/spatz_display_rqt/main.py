import sys

from rqt_gui.main import Main


def main():
    plugin = 'spatz_display_rqt.display.Display'
    main = Main(filename=plugin)
    sys.exit(main.main(standalone=plugin))  # , plugin_argument_provider=Display.add_arguments))


if __name__ == '__main__':
    main()
