import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import efficientnet
import timm
import torchvision.models as models


class BaseModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=7, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.25)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)

        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout2(x)

        x = self.avgpool(x)
        x = x.view(-1, 128)
        return self.fc(x)

# Noise studey efficientnet_b4 custom module
class efficientnet_v2_s(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = efficientnet.efficientnet_v2_s(weights=True)
        self.fc = nn.Linear(in_features=1000, out_features=18)
    def forward(self, x):
        x = self.efficientnet(x)
        x = self.fc(x)

        return x


# Noise studey efficientnet_b5 custom module
class NsEfnB5(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model("tf_efficientnet_b5_ns", pretrained=True)
        self.efficientnet.classifier = nn.Sequential(
                                            nn.Linear(in_features=2048, out_features=1024, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=1024, out_features=512, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=512, out_features=256, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=256, out_features=num_classes),
                                            )
    def forward(self, x):
        x = self.efficientnet(x)

        return x


# Noise studey efficientnet_b7 custom module
class NsEfnB7(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model("tf_efficientnet_b7_ns", pretrained=True)
        self.efficientnet.classifier = nn.Sequential(
                                            nn.Linear(in_features=2560, out_features=1024, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=1024, out_features=512, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=512, out_features=256, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=256, out_features=num_classes),
                                            )
    def forward(self, x):
        x = self.efficientnet(x)

        return x




# Custom Model Template
class MyModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        """
        1. 위와 같이 생성자의 parameter 에 num_claases 를 포함해주세요.
        2. 나만의 모델 아키텍쳐를 디자인 해봅니다.
        3. 모델의 output_dimension 은 num_classes 로 설정해주세요.
        """

    def forward(self, x):
        """
        1. 위에서 정의한 모델 아키텍쳐를 forward propagation 을 진행해주세요
        2. 결과로 나온 output 을 return 해주세요
        """
        return x

# Noise studey efficientnet_b4 custom module
class NsEfnB4(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model("tf_efficientnet_b4_ns", pretrained=True)
        self.efficientnet.classifier = nn.Sequential(
                                            nn.Linear(in_features=1792, out_features=1024, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=1024, out_features=512, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=512, out_features=256, bias=True),
                                            nn.ReLU(),
                                            nn.Linear(in_features=256, out_features=num_classes),
                                            )
    def forward(self, x):
        x = self.efficientnet(x)

        return x

class efficientnet_v2_l(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = models.efficientnet_v2_l(pretrained=True)
        #self.backbone = models.efficientnet_b3(pretrained=True)
        #weight = 'EfficientNet_V2_L_Weights.IMAGENET1K_V1'
        #self.backbone = models.efficientnet_v2_l(weights='IMAGENET1K_V1')
        
        self.classifier = nn.Linear(1000, 18)
        #self.classifier = nn.Sequential(
            #nn.ReLU(),
            #nn.Dropout(0.2),
            #nn.Linear(1000, 18)
            #nn.ReLU(),
            #nn.Linear(512, 256),
            #nn.ReLU(),
            #nn.Linear(256,128),
            #nn.ReLU(),
            #nn.Linear(128,18)
            #)
        #512로 줄여서
        #batchnorm()
        #relu()
    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x

class efficientnet_v2_m(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = models.efficientnet_v2_m(pretrained=True)
        #self.backbone = models.efficientnet_b3(pretrained=True)
        #weight = 'EfficientNet_V2_L_Weights.IMAGENET1K_V1'
        #self.backbone = models.efficientnet_v2_l(weights='IMAGENET1K_V1')
        
        self.classifier = nn.Linear(1000, 18)
        #self.classifier = nn.Sequential(
            #nn.ReLU(),
            #nn.Dropout(0.2),
            #nn.Linear(1000, 18)
            #nn.ReLU(),
            #nn.Linear(512, 256),
            #nn.ReLU(),
            #nn.Linear(256,128),
            #nn.ReLU(),
            #nn.Linear(128,18)
            #)
        #512로 줄여서
        #batchnorm()
        #relu()
    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x
    
    
class vit_base_patch16_384(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = timm.create_model('vit_base_patch16_384', pretrained=True)

        
        self.classifier = nn.Linear(1000, 18)
        #self.classifier = nn.Sequential(
            #nn.ReLU(),
            #nn.Dropout(0.2),
            #nn.Linear(1000, 18)
            #nn.ReLU(),
            #nn.Linear(512, 256),
            #nn.ReLU(),
            #nn.Linear(256,128),
            #nn.ReLU(),
            #nn.Linear(128,18)
            #)
        #512로 줄여서
        #batchnorm()
        #relu()
    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x
    

class rexnet_200(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = timm.create_model('rexnet_200', pretrained=True)

        
        self.classifier = nn.Linear(1000, 18)
        #self.classifier = nn.Sequential(
            #nn.ReLU(),
            #nn.Dropout(0.2),
            #nn.Linear(1000, 18)
            #nn.ReLU(),
            #nn.Linear(512, 256),
            #nn.ReLU(),
            #nn.Linear(256,128),
            #nn.ReLU(),
            #nn.Linear(128,18)
            #)
        #512로 줄여서
        #batchnorm()
        #relu()
    def forward(self, x):
        x = self.backbone(x)
        x = self.classifier(x)
        return x