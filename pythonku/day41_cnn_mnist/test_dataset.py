from dataset import MNISTDataset


dataset = MNISTDataset()


image,label = dataset[0]


print(image.shape)
print(label)