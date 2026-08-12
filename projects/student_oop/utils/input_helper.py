def input_int(message):

    while True:

        try:

            value = int(input(message))

            return value#返回输入的数字

        except ValueError:#如果是abc，进入except，然后print，然后继续循环

            print("请输入数字")