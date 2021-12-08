---
layout: post
title: Tracking指标
slug: Tracking指标
date: 2021-12-4
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 实验
---



## 评价标准

True positives（TP，真正） : 预测为正，实际为正

True negatives（TN，真负）：预测为负，实际为负

False positives（FP，假正）: 预测为正，实际为负

False negatives（FN，假负）：预测为负，实际为正

![img](https://pic1.zhimg.com/80/v2-ede11a19f93d09e20039bb77a0a9cf90_720w.jpg)



**TPR、FPR和TNR**

**TPR**（true positive rate，真正类率，灵敏度，Sensitivity）

TPR = TP/(TP+FN)

真正类率TPR代表分类器预测的正类中实际正实例占所有正实例的比例。

**FPR**（false positive rate，假正类率）

FPR = FP/(FP+TN)

假正类率FPR代表分类器预测的正类中实际负实例占所有负实例的比例。

**TNR**（ture negative rate，真负类率，特异度，Specificity）

TNR = TN/(FP+TN)
TNR = 1 - FPR

真负类率TNR代表分类器预测的负类中实际负实例占所有负实例的比例。

**Recall** = TPR（召回率）

Recall = TP/（TP+FN）

即当前被分到正样本类别中，真实的正样本占所有正样本的比例，即召回率（召回了多少正样本比例）；**（召回率表示真正预测为正样本的样本数占实际正样本的样本数的比率）**

**Precision**（精确率）

Pre = TP/（TP+FP）

当前预测为正样本类别中，被正确分类的比例（即正式正样本所占比例），就是我们一般理解意义上所关心的正样本的分类精确率确率；**（精确率表示真正预测为正样本的样本数占所有预测为正样本的样本数的比例）** 通俗说：预测为正样本中正确的占的比例

**Accuracy**（准确率，ACC）

ACC = (TP+TN)/(TP+TN+FN+FP)

表示预测正确的样本占所有样本的比率

**F-Score**

F-Score 是精确率Precision和召回率Recall的加权调和平均值。该值是为了综合衡量Precision和Recall而设定的。

![img](https://pic4.zhimg.com/80/v2-0f76e89f7b9b09e1666655ff0553c5cb_720w.jpg)



当a=1时，

![img](https://pic3.zhimg.com/80/v2-e0e13bd5e4f486fda7562cc836b96676_720w.jpg)



这时，Precision和Recall都很重要，权重相同。

当有些情况下，我们认为Precision更重要，那就调整a的值小于1；如果我们认为Recall更加重要，那就调整a的值大于1。

一般来说，当F-Score或F1-score较高时，说明结果较理想。

### ROC

![img](https://pic1.zhimg.com/80/v2-4dbeb108d5d8349a9e4ab062ca926d74_720w.jpg)



横轴FPR:1-TNR,1-Specificity，FPR越大，预测正类中实际负类越多。

[纵轴TPR](https://www.zhihu.com/search?q=纵轴TPR&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})：Sensitivity(正类覆盖率),TPR越大，预测正类中实际正类越多。

理想目标：TPR=1，FPR=0,即图中(0,1)点，故ROC曲线越靠拢(0,1)点，越偏离45度[对角线](https://www.zhihu.com/search?q=对角线&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})越好，Sensitivity、Specificity越大效果越好。

### ROC绘制

ROC本质上就是在设定某一阈值之后，计算出该阈值对应的TPR & FPR，便可以绘制出ROC上对应的一个点，当设定若干个阈值之后，便可以连成ROC曲线，因此可以想见，当所采样的阈值越多，ROC Curve越平滑。

### 如何画[roc曲线](https://www.zhihu.com/search?q=roc曲线&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})

假设已经得出一系列样本被划分为正类的概率，然后按照大小排序，下图是一个示例，图中共有20个测试样本，“Class”一栏表示每个测试样本真正的标签（p表示正样本，n表示负样本），“Score”表示每个测试样本属于正样本的概率。

![img](https://pic4.zhimg.com/80/v2-2e7ccbea8660960971fe9fcb27eb4e47_720w.jpg)



接下来，我们从高到低，依次将“Score”值作为阈值threshold，当测试样本属于正样本的概率大于或等于这个threshold时，我们认为它为正样本，否则为负样本。举例来说，对于图中的第4个样本，其“Score”值为0.6，那么样本1，2，3，4都被认为是正样本，因为它们的“Score”值都大于等于0.6，而其他样本则都认为是负样本。每次选取一个不同的threshold，我们就可以得到一组FPR和TPR，即ROC曲线上的一点。这样一来，我们一共得到了20组FPR和TPR的值，将它们画在ROC曲线的结果如下图：

![img](https://pic2.zhimg.com/80/v2-6dfd4a7c5a0a185ebf91727dbccad86d_720w.jpg)



AUC(Area under Curve)：Roc曲线下的面积，介于0.1和1之间。Auc作为数值可以直观的评价分类器的好坏，值越大越好。

### AUC

AUC 即ROC曲线下的面积，计算方式即为ROC Curve的微积分值，其物理意义可以表示为：随机给定一正一负两个样本，将正样本排在负样本之前的概率，因此AUC越大，说明正样本越有可能被排在负样本之前，即分类额结果越好。

AUC(Area under Curve)：Roc曲线下的面积，介于0.1和1之间。Auc作为数值可以直观的评价分类器的好坏，值越大越好。

### 为什么使用Roc和Auc评价分类器

ROC曲线有个很好的特性：当测试集中的正负样本的分布变换的时候，ROC曲线能够保持不变。在实际的数据集中经常会出现样本类不平衡，即正负样本比例差距较大，而且测试数据中的正负样本也可能随着时间变化。下图是ROC曲线和[Presision-Recall曲线](https://www.zhihu.com/search?q=Presision-Recall曲线&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})的对比：

![img](https://pic2.zhimg.com/80/v2-abf8d5303be1e91aa968432ad5d40d5d_720w.jpg)



在上图中，(a)和(c)为[Roc曲线](https://www.zhihu.com/search?q=Roc曲线&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})，(b)和(d)为Precision-Recall曲线。

(a)和(b)展示的是分类其在原始测试集([正负样本](https://www.zhihu.com/search?q=正负样本&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})分布平衡)的结果，(c)(d)是将测试集中负样本的数量增加到原来的10倍后，分类器的结果，可以明显的看出，ROC曲线基本保持原貌，而Precision-Recall曲线变化较大。

**解读**：**ROC曲线围成的面积 (即AUC)可以解读为：从所有正例中随机选取一个样本A，再从所有负例中随机选取一个样本B，分类器将A判为正例的概率比将B判为正例的概率大的可能性。可以看到位于随机线上方的点(如图中的A点)被认为好于随机猜测。在这样的点上TPR总大于FPR，意为正例被判为正例的概率大于负例被判为正例的概率**。

从另一个角度看，由于画ROC曲线时都是先将所有样本按分类器的预测概率排序，所以AUC反映的是分类器对样本的排序能力，依照上面的例子就是A排在B前面的概率。AUC越大，自然排序能力越好，即分类器将越多的正例排在负例之前。

### ROC的相关总结

1） ROC 可以反映二分类器的总体分类性能，但是无法直接从图中识别出分类最好的阈值，事实上最好的阈值也是视具体的场景所定；

2）ROC Curve 对应的AUC越大（或者说对于连续凸函数的ROC曲线越接近(0,1) )说明分类性能越好;

3）ROC曲线一定是需要在 y = x之上的，否则就是一个不理想的分类器；

### ROC曲线的优点

放一张混淆矩阵图可能看得更清楚一点 :

![img](https://pic4.zhimg.com/80/v2-e76f65e7a0a42f51b4dcc0169157660f_720w.jpg)



兼顾[正例](https://www.zhihu.com/search?q=正例&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})和负例的权衡。因为TPR聚焦于正例，FPR聚焦于与负例，使其成为一个比较均衡的评估方法。

ROC曲线选用的两个指标，TPR=TPP=TPTP+[FNTPR=TPP=TPTP+FN](https://www.zhihu.com/search?q=FNTPR%3DTPP%3DTPTP%2BFN&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})，FPR=FPN=FPFP+TNFPR=FPN=FPFP+TN，都**不依赖于具体的类别分布**。

注意TPR用到的TP和FN同属P列，FPR用到的FP和TN同属N列，所以即使P或N的整体数量发生了改变，也不会影响到另一列。也就是说，**即使正例与负例的比例发生了很大变化，ROC曲线也不会产生大的变化，而像Precision使用的TP和FP就分属两列，则易受类别分布改变的影响**。

参考文献 [1] 中举了个例子，负例增加了10倍，ROC曲线没有改变，而PR曲线则变了很多。作者认为这是ROC曲线的优点，即具有[鲁棒性](https://www.zhihu.com/search?q=鲁棒性&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A87768945})，在类别分布发生明显改变的情况下依然能客观地识别出较好的分类器。

![img](https://pic2.zhimg.com/80/v2-1315348b974d74f468cccee1a6452765_720w.jpg)



### ROC曲线的缺点

**上文提到ROC曲线的优点是不会随着类别分布的改变而改变，但这在某种程度上也是其缺点**。因为负例N增加了很多，而曲线却没变，这等于产生了大量FP。像信息检索中如果主要关心正例的预测准确性的话，这就不可接受了。

在类别不平衡的背景下，负例的数目众多致使FPR的增长不明显，导致ROC曲线呈现一个过分乐观的效果估计。ROC曲线的横轴采用FPR，根据FPR =FPNFPN=FPFP+TNFPFP+TN，**当负例N的数量远超正例P时，FP的大幅增长只能换来FPR的微小改变。结果是虽然大量负例被错判成正例，在ROC曲线上却无法直观地看出来**。（当然也可以只分析ROC曲线左边一小段） 举个例子，假设一个数据集有正例20，负例10000，开始时有20个负例被错判，FPR=2020+9980=0.002FPR=2020+9980=0.002，接着又有20个负例错判，FPR2=4040+9960=0.004FPR2=4040+9960=0.004，在ROC曲线上这个变化是很细微的。而与此同时Precision则从原来的0.5下降到了0.33，在PR曲线上将会是一个大幅下降。

### PR曲线

在PR曲线中，以Recall（貌似翻译为召回率或者查全率）为x轴，Precision为y轴。

![img](https://pic4.zhimg.com/80/v2-331a4faabbfccdb904b44b3fd20dbf93_720w.jpg)



绘制ROC曲线和PR曲线都是选定不同阈值，从而得到不同的x轴和y轴的值，画出曲线。

### PR (Precision Recall) 曲线

PR曲线展示的是Precision vs Recall的曲线，PR曲线与ROC曲线的相同点是都采用了TPR (Recall)，都可以用AUC来衡量分类器的效果。不同点是ROC曲线使用了FPR，而PR曲线使用了Precision，因此PR曲线的两个指标都聚焦于正例。类别不平衡问题中由于主要关心正例，所以在此情况下PR曲线被广泛认为优于ROC曲线。

### 使用场景

ROC曲线由于兼顾正例与负例，所以适用于评估分类器的整体性能，相比而言PR曲线完全聚焦于正例。

如**果有多份数据且存在不同的类别分布**，比如信用卡欺诈问题中每个月正例和负例的比例可能都不相同，**这时候如果只想单纯地比较分类器的性能且剔除类别分布改变的影响，则ROC曲线比较适合**，因为类别分布改变可能使得PR曲线发生变化时好时坏，这种时候难以进行模型比较；反之，如果想测试相同类别分布下对分类器的性能的影响，则PR曲线比较适合。

如果想要评估在**相同的类别分布下正例的预测情况，则宜选PR曲线**。

类别不平衡问题中，ROC曲线通常会给出一个乐观的效果估计，所以大部分时候还是PR曲线更好。

最后可以根据具体的应用，在曲线上找到最优的点，得到相对应的precision，recall，f1 score等指标，去调整模型的阈值，从而得到一个符合具体应用的模型。

### IoU

IoU这一值，可以理解为系统预测出来的框与原来图片中标记的框的重合程度。

计算方法即检测结果Detection Result与 Ground Truth 的交集比上它们的并集，即为检测的准确率：



![img](https://pic3.zhimg.com/80/v2-53fd9c13a7e5e4c65bd48ece17a60632_720w.jpg)





![img](https://pic2.zhimg.com/80/v2-44ef24919ccbecd843290d80d6a94b3d_720w.jpg)



如下图所示：
蓝色的框是：GroundTruth
黄色的框是：DetectionResult
绿色的框是：DetectionResult ⋂ GroundTruth
红色的框是：DetectionResult ⋃ GroundTruth

![img](https://pic2.zhimg.com/80/v2-5a0e66ccee3063dbe4b7efba889f21c9_720w.jpg)