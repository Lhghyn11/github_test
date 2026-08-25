import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split


from dataset import StudentDataset
from model import StudentModel



# ====================
# 固定随机种子
# ====================

torch.manual_seed(42)



# ====================
# 数据
# ====================

dataset = StudentDataset()


train_size = int(len(dataset)*0.75)

val_size = len(dataset)-train_size



train_dataset, val_dataset = random_split(
    dataset,
    [
        train_size,
        val_size
    ]
)



train_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=True
)



val_loader = DataLoader(
    val_dataset,
    batch_size=2,
    shuffle=False
)



print("训练集:",len(train_dataset))
print("验证集:",len(val_dataset))



# ====================
# 模型
# ====================

model = StudentModel()



# ====================
# loss
# ====================

loss_fn = nn.MSELoss()



# ====================
# optimizer
# ====================

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)



# ====================
# scheduler
# ====================

scheduler = torch.optim.lr_scheduler.StepLR(
    optimizer,    
    step_size=1000,
    gamma=0.1
)



# ====================
# best model
# ====================

best_val_loss = float("inf")



# ====================
# early stopping
# ====================

patience = 300

counter = 0



# ====================
# training
# ====================


for epoch in range(5000):


    # ----------
    # train
    # ----------

    model.train()


    train_loss = 0



    for x,y in train_loader:


        pred = model(x)


        loss = loss_fn(
            pred,
            y
        )


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()


        train_loss += loss.item()



    # ----------
    # validation
    # ----------

    model.eval()


    val_loss = 0



    with torch.no_grad():


        for x,y in val_loader:


            pred = model(x)


            loss = loss_fn(
                pred,
                y
            )


            val_loss += loss.item()



    # ----------
    # save best
    # ----------

    if val_loss < best_val_loss:


        best_val_loss = val_loss


        counter = 0

        #保存
        #torch.save(
        #    model.state_dict(),
        #    "best_model.pth"
        #)
        checkpoint = {

            "epoch": epoch,

            "model_state_dict":
                model.state_dict(),

            "optimizer_state_dict":
                optimizer.state_dict(),

            "scheduler_state_dict":
                scheduler.state_dict(),

            "best_val_loss":
                best_val_loss
        }


        torch.save(
            checkpoint,
            "checkpoint.pth"
        )


        print(
            "保存最佳模型"
        )


    else:

        counter += 1



    # ----------
    # early stopping
    # ----------

    if counter >= patience:

        print(
            "Early stopping"
        )

        break



    # ----------
    # scheduler
    # ----------

    #scheduler.step()



    if epoch % 100 == 0:


        print(
            epoch,
            "train loss:",
            train_loss,
            "val loss:",
            val_loss
        )



print("训练完成")

print(
    "best val loss:",
    best_val_loss
)


print(
    "模型保存完成"
)