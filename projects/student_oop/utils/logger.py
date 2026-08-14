import logging
import os


if not os.path.exists("logs"):#自动创建文件夹
    os.makedirs("logs")#不存在就创建

print("logs目录创建检查完成")
print("logs存在:", os.path.exists("logs"))
print("当前路径:", os.getcwd())


logging.basicConfig(
    filename="logs/app.log",#所有日志等于
    level=logging.INFO,#日志等级记录info warning error
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"#转换乱码
)


logger = logging.getLogger(__name__)