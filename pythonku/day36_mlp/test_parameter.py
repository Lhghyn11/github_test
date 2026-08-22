from model import StudentModel


model = StudentModel()


for name,param in model.named_parameters():

    print(name)

    print(param.shape)

    print("----------------")