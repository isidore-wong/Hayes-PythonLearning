logging模块输入日志文件，可以替代print函数的功能，也能部分替代debug的功能

logging几个常用的功能：

logging.debug('debug message')

logging.info('info message')

logging.warning('warning message')

logging.error('error message')

logging.critical('critical message')

logging最简单的方法是logging.basicconfig([**kwargs])
该方法可用个参数有：

filename   
filemode   
fromat  
datefmt     
level       
stream
 

