# -*- coding: UTF-8 -*-

import optparse
import bbt_searchfile
from common.logging import MyLogging

Usage = "main_analyze.py -d yyyy-mm-dd  -p (path)"
Parser = optparse.OptionParser(usage=Usage)
mylog = MyLogging()


def usage():
	# Parser.add_option("-d", "--date", dest="date", default="\d+", help=r'yyyy-mm-dd 可当做一个通配使用')
	Parser.add_option("-y", "--year", dest="year", default="\d+", help=r'yyyy-mm-dd 可当做一个通配使用')
	Parser.add_option("-m", "--month", dest="month", default="\d+", help=r'yyyy-mm-dd 可当做一个通配使用')
	Parser.add_option("-d", "--day", dest="day", default="\d+", help=r'yyyy-mm-dd 可当做一个通配使用')
	Parser.add_option("-l", "--log-path", dest="path", help=r"Log file dir.")
	Parser.add_option("-a", "--app", dest="app", default="\d+", help=r"AppId 应用id.")
	Parser.add_option("-p", "--platform", dest="platform", default="\d+", help=r"Log file dir.")
	Parser.add_option("-t", "--channel-type", dest="channel_type", default="\d+", help=r"Log file dir.")
	Parser.add_option("-c", "--channel", dest="channel", default="\d+", help=r"Log file dir.")


if __name__ == '__main__':
	usage()
	(option, args) = Parser.parse_args()
	anal = bbt_searchfile.Analyze(option.year, option.month, option.day, option.path, option.platform, option.app,
								  option.channel_type, option.channel, mylog)
	anal.run()
