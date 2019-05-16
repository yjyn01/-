# optparse模块主要用来为脚本传递命令参数，采用预先定义好的选项来解析命令行参数。
# 实例化一个 OptionParser 对象(可以带参，也可以不带参数)，带参的话会把参数变量的内容作为帮助信息输出
import optparse

Usage = "main_analyze.py -d yyyy-mm-dd  -p (path)"
Parser = optparse.OptionParser(usage=Usage)

Parser.add_option("-d", "--date", dest="date", default="", help=r'yyyy-mm-dd 可当做一个通配使用')
Parser.add_option("-l", "--log-path", dest="path", help=r"Log file dir.")
Parser.add_option("-a", "--app", dest="app", default="\d+", help=r"AppId 应用id.")
Parser.add_option("-p", "--platform", dest="platform", default="\d+", help=r"Log file dir.")
Parser.add_option("-t", "--channel-type", dest="channel_type", default="\d+", help=r"Log file dir.")
Parser.add_option("-c", "--channel", dest="channel", default="\d+", help=r"Log file dir.")

(option, args) = Parser.parse_args()
print(option.date)
