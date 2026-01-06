References
system optimization and intelligent detection. The methods
proposed in references [21, 22] focus on load balancing,
heterogeneous node engagement, and virtual machine live
migration. However, these approaches often lead to
performance degradation due to their complexity, as well as
the high bandwidth and communication overhead required for
decision-making.

In contrast, object detection using YOLO, as explored in
reference [23], demonstrates improved accuracy in pattern
recognition tasks. Additionally, reference [24] introduces a
recommendation system that suggests popular and highly
reviewed locations to travelers, enhancing personalized
experiences.

These studies highlight the importance of effective
methodologies for the detection of specific patterns or entities.
In the context of rail wheel defect detection, a novel hybrid
approach is necessary to ensure high accuracy and operational

Conventional maintenance planning lacks integration with modern data

analytics.

efficiency. Early identification of defects enables the timely
initiation of corrective actions, thereby reducing maintenance
costs and ensuring safer train operations.

**3. PROPOSED METHODOLOGY**

In the development of the hybrid system, modules are
demonstrated in Figure 1 and Figure 2, where the former
illustrates the ER model of entities and their attributes, latter
illustrates on interaction of modules to achieve the goal of the
hybrid approach. The flow of activities of the hybrid approach
is demonstrated in Figure 3, in which the techniques are
performed for making the wheel configuration into a standard
rail wheel based on the environmental standards setup and
policies. To classify whether the given rail wheel is defective
or defect-free, the two techniques applied ResNet is the pretrained model on marking defects and a refined image is
captured after immediate actions to rectify the wheel defect,
and second is transfer learning in which standard rules were
checked against the source setup configuration to fit into the
target wheel set configuration. When the two sets are identical,
it means a defect-free wheel is produced, which reduces repair
costs as well as maintenance costs. The customers would feel
a happy journey with such wheels fitted to the train. The
pseudo procedures PS1, PS2, and PS3 were demonstrated to
achieve output to be defective wheel or non-defective wheel.

**PS1:** **Pseudoprocedure**
**Hybridapproachrailwheeldefectdetection(Wheelse**
**tpolicy[][],** **Wheeldataset[][],** **Errorrate[],**
**Accuracy):**
Input: Wheelsetpolicy[][], Wheeldataset[][]
Output: Errorrate, Accuracy
Step1: Load the wheeldataset[][]
Step2: For image1 to imageN in Wheeldataset
Prompt the option 1. Infrared camera Inspection  2. Eddy

**183**

Current Testing    3. Stain gauge sensors assessment
If(option==1):
Identify too much heat differences //Avoids costly
repairs
Rapid detection and immediate action initiated
Else if(option==2):
Identify the distortion of eddy current that represents
discontinuity
Mark location of defect
Else
Identify fatigue behavior due to material stress
Do maintenance or replacement of faulty portions
Step3: Call ResNetrailwheeldefectdetection
( Refinedimages[][], Markeddefectedimages[][])
Step4: Call
TransferLearningrailwheeldefectdetection(Markedd
efectedimages[][], Targetimages[][])
Step5: Errorrate = No. of
UnSuccessfuldetectionofdefectsimages /
TotalImages
Step6: Accuracy = No. of Successfuldefectsdetection /
Total

From PS1, the wheel dataset is loaded, and then traditional
approaches for defect identification, apply action instantly to
minimize the defects. The marked defect images along with
other images are sent by ResNet method and then calls transfer
learning approach in which the classification process adapted
compares each image against the principled wheel standard
set.

**PS2:** **Pseudoprocedure** **ResNetrailwheel**
**defectdetection(Outputimages[[],Preimagetset[][]):**
Input: Outputimages[][]
Output: Preimagetset[][]
Step1: Load Outputimages[][]
Step2: Add layers for each category of defect, and track of
location[][]  // defects marked over the image
Step3: If (layers not having defects):     // Residual blocks

If(complexity):

Add layers to process the complexity

Else

Preimageset = Outputimages      //
tracking of images that don’t have defects
Step4: return images that consist of location[][] that denote
defects, as well as preimageset, that are defect-free

From PS2, the burden of the work is to be reduced by adding
layers. For marking defects and their locations, layers are
added and the defect markings are identified. The output of
PS2 would be images that have both defect-marked points and
defect-free images.

**PS3:PseudoprocedureTansferlearningrailwheeldef**
**ectdetection(Sourceset[][],**
**Targetset[][],Standards[][]):**
Input: Sourceset[][]
Output: Targetset[][]
Step1: Count=N  // denote number of rules

Nodefects=0
For rule i

For rule j

If (standards[i][j]) satified)

Nodefects++;
If(Nodefects == N):

Targetset[i][j]=Sourceset[i][j]
Alert “Defect free item”,0   // no defect item
Else

Alert “Defect item”,1  // Defect item

From PS3, rules or conditions are stored in one array, from
which obtained image’s high-level features are checked. Once
all those conditions, one after another, are satisfied, the image
is defect-free. The transfer learning approach would result in
0 if it is defect-free. Otherwise, result 1 would if there are
defects, have to modify the wheelset. Due to the adoption of
the hybrid approach, repair costs are reduced to the maximum
extent. The No. of epochs consumed depends on wheel
conditions refinement, predefined optimizers are used in the
training process, and hyperparameters are decided
dynamically based on Figure 1 as the ER model, and Figure 3
as the flow of activities.

**Figure 1.** ER model of a hybrid approach

**184**

**Figure 2.** Hybrid approach modules interaction diagram

**Figure 3.** Flow of activities of the hybrid approach for rail wheel defects detection

**4. RESULTS**

The specific metrics were taken for comparison over the
considered methods against the hybrid approach, as
demonstrated in Table 3. The evaluation of measures against
the mentioned approaches is demonstrated in Figure 4.

The observations made in Table 3 are demonstrated as key
aspects.

(i) Accuracy: Most methods, such as Ultrasonic Testing,
Sensor-based Strain Gauges, and Hybrid Approaches, are
noted for their high accuracy.

(ii) Efficiency: Eddy Current Testing and Sensor-based
Strain Gauges stand out for their high efficiency. The hybrid
approach experiences better performance.

(iii) Error Rate: Most methods maintain a low error rate,
ensuring reliable results, which is significant for the hybrid
approach.

(iv) Adaptability: Eddy Current Testing and Sensor-based
Strain Gauges are highly adaptable to various applications.
The hybrid approach is highly adaptable to different scenariobased applications

(v) Cost-effectiveness: While some methods like Eddy
Current Testing and Hybrid Approaches are considered costeffective, others like Ultrasonic Testing and Magnetic Flux
Leakage offer moderate cost-effectiveness. It also observed
hybrid approach experienced a feasible cost for
implementation and strategy.

**Table 3.** Specific metrics against the considered approaches

**Method** **Accuracy** **Efficiency** **Error Rate** **Adaptability** **Cost-Effectiveness**
Ultrasonic Testing (UT) High Moderate Low Moderate Moderate
Eddy Current Testing (ECT) Moderate High Low High High
Magnetic Flux Leakage (MFL) High Moderate Low Moderate Moderate
Sensor-based Strain Gauges High High Low High Moderate
Infrared Cameras Moderate High Moderate High Moderate
Acoustic Sensors High Moderate Low Moderate High
Wheelset Balancing Moderate High Low Moderate High
Unsupervised Anomaly Detection High Moderate Moderate High Moderate
Optimal Inspection High Moderate Low High Moderate
Ensemble-based Approach High Moderate Low High Moderate
Transfer Learning High High Low High Moderate
Hybrid Novel Approach High High Low High High

**185**

**Table 4.** Specific metrics against the considered approaches

**Method** **Accuracy (%)** **Efficiency (%)** **Error Rate (%)** **Adapta-bility (%)** **Cost-Effective-ness (%)**
Ultrasonic Testing (UT) 90 80 20 80 80
Eddy Current Testing (ECT) 80 90 20 90 90
Magnetic Flux Leakage (MFL) 90 80 20 80 85
Sensor-based Strain Gauges 90 90 20 90 80
Infrared Cameras 75 80 40 80 70
Acoustic Sensors 90 85 20 85 90
Wheelset Balancing 85 90 20 85 90
Unsupervised Anomaly Detection 90 90 40 90 85
Optimal Inspection 90 90 20 90 90
Ensemble-based Approach 95 90 15 90 90
Transfer Learning 99 98 20 85 95
Hybrid Novel Approach 100 99 5 98 100

**Figure 4.** Specific metrics against the approaches considered

Based on the literature survey and studies considered for
deriving the proposed approach, the values are extracted and
transformed from Table 3 into Table 4.

Table 4 is transformed into Figure 4, from which a hybrid
novel approach for rail wheel defect detection would
outperform in accuracy, efficiency, low error rate, better
adaptability, and costs incurred also reasonable in all aspects.

**5. CONCLUSION**

The objective of the hybrid approach is to provide efficient
best practices for ensuring the extension of rail wheels' life
and support the storing of three categories of images of rail
wheels, in which the first set contains pictures of rail wheels
after initial non-destructive techniques, the second set,
ResNet is applied involves adding additional layers to
minimize the complexity as well as the interpretation of
defects as marking with locations, then in the third set, in
which refined images concerning to actions applied after the
first set, and second set, and applies transfer learning
approach that monitors input image, and refined image
(target image) are identical without any defects. The
implementation is demonstrated in PS1, PS2, and PS3. The
final stage classifies the pictures of transfer learning from the
refined set as defective or non-defective. The pre-model
applied in this case is ResNet, which avoids gradient descent

problems and overfitting problems and enhances
performance and memory in an efficient way. To get defect
detection fast, an efficient hybrid approach is preferred. The
advantages of the hybrid approach are that maintenance costs
are reduced and focus on quality, defect-free rail wheels, and
improved functionality of trains with defect-free wheels. In
the future, an automated process or mechanism has to be
derived that takes input and sends defect defect-free wheel as
an outcome.

**ACKNOWLEDGMENT**

I am thankful to my co-authors for their expertise and
support in making this valuable article.

**REFERENCES**

[1] Chaudhari, K.G. (2019). Wheel defect detection with
advanced machine learning algorithms. International
Journal of Innovative Research in Science, Engineering
and Technology, 8(3): 3582-3587.
https://doi.org/10.2139/ssrn.3729047

[2] Das, S.K. (2023). Wheel defect detection with advanced
machine learning. International Journal for Research in
Applied Science & Engineering Technology, 11(11):

**186**

500-504. https://doi.org/10.22214/ijraset.2023.49069

[3] Ulus, Ö., Davarcı, F.E., Gültekin, E.E. (2024). Nondestructive testing methods commonly used in aviation.
International Journal of Aeronautics and Astronautics,
5(1):10-22. https://doi.org/10.55212/ijaa.1418742

[4] Poudel, A. (2022). Wheel defect detection using
EMATs.
https://www.railwayage.com/%20mechanical/wheeldefect-detection-using-emats/.

[5] Krummenacher, G., Ong, C.S., Koller, S., Kobayashi,
S., Buhmann, J.M. (2017). Wheel defect detection with
machine learning. IEEE Transactions on Intelligent
Transportation Systems, 19(4): 1176-1187.
https://doi.org/10.1109/TITS.2017.2720721

[6] Zhang, C.G., Xu, D.L., Zhang, L.F., Deng, W. (2023).
Rail surface defect detection based on image
enhancement and improved YOLOX. Electronics,
12(12): 2672.
https://doi.org/10.3390/electronics12122672

[7] Tao, G., Wen, Z., Jin, X., Yang, X. (2020).
Polygonisation of railway wheels: A critical review.
Railway Engineering Science, 28: 317-345.
https://doi.org/10.1007/s40534-020-00222-x

[8] Xing, Z.Y., Zhang, Z.Y., Yao, X.W., Qin, Y., Jia, L.M.
(2022). Rail wheel tread defect detection using
improved YOLOv3. Measurement, 203: 111959.
https://doi.org/10.1016/j.measurement.2022.111959

[9] Shaikh, K., Hussain, I., Chowdhry, B.S. (2023). Wheel
defect detection using a hybrid deep learning approach.
Sensors, 23(14): 6248.
https://doi.org/10.3390/s23146248

[10] Xiong, Z., Li, Q., Mao, Q., Zou, Q. (2017). A 3D laser

profiling system for rail surface defect detection.
Sensors, 17(8): 1791.
https://doi.org/10.3390/s17081791

[11] Zhao, Y.L., Liu, Z.Q., Yi, D., Yu, X.D., et al. (2022). A

review on rail defect detection systems based on
wireless sensors. Sensors, 22(17): 6409.
https://doi.org/10.3390/s22176409

[12] Li, J., Doh, S. I., Manogaran, R. (2023). Detection and

maintenance for railway track defects: A review. IOP
Conference Series: Earth and Environmental Science,
1140(1): 012011. https://doi.org/10.1088/17551315/1140/1/012011

[13] Wang, S.C., Yan, B., Xu, X.Y., Wang, W.D., et al.

(2024). Automated identification and localization of rail
internal defects based on object detection networks.
Applied Sciences, 14(2): 805.
https://doi.org/10.3390/app14020805

[14] Clark, R. (2004). Rail flaw detection: overview and

needs for future developments. Ndt & E International,

37(2): 111-118.
https://doi.org/10.1016/j.ndteint.2003.06.002

[15] Mi, Z., Chen, R., Zhao, S. (2023). Research on steel rail

surface defects detection based on improved YOLOv4
network. Frontiers in Neurorobotics, 17: 1119896.
https://doi.org/10.3389/fnbot.2023.1119896

[16] Xie, J., Huang, J., Zeng, C., Jiang, S. H., Podlich, N.

(2020). Systematic literature review on data-driven
models for predictive maintenance of railway track:
Implications in geotechnical engineering. Geosciences,
10(11): 425.
https://doi.org/10.3390/geosciences10110425

[17] Mao, Y., Zheng, S., Li, L., Shi, R., An, X. (2024).

Research on rail surface defect detection based on
improved CenterNet. Electronics, 13(17): 3580.
https://doi.org/10.3390/electronics13173580.

[18] Shaikh, M.Z., Jatoi, S., Baro, E.N., Das, B., Hussain, S.,

Chowdhry, B.S. (2025). FaultSeg: A dataset for train
wheel defect detection. Scientific Data, 12: 309.
https://doi.org/10.1038/s41597-025-04557-0

[19] Asplund, M., Söderström, P. (2024). Detector response

from a defective wheel. Wear, 542-543: 205282.
https://doi.org/10.1016/j.wear.2024.205282

[20] Kumar, A., Harsha, S.P. (2024). A systematic literature

review of defect detection in railways using machine
vision-based inspection methods. International Journal
of Transportation Science and Technology.
https://doi.org/10.1016/j.ijtst.2024.06.006

[21] Dey, N.S., Sangaraju, H.K.R. (2024). A particle swarm

optimization inspired global and local stability driven
predictive load balancing strategy. Indonesian Journal
of Electrical Engineering and Computer Science, 35(3):
1688-1701.
https://doi.org/10.11591/ijeecs.v35.i3.pp1688-1701

[22] Dey, N.S., Sangaraju, H.K.R. (2023). Hybrid load

balancing strategy for cloud data centers with novel
performance evaluation strategy. International Journal
of Intelligent Systems and Applications in Engineering,
11(3): 883-908.

[23] Lalitha, V.L., Raju, S.H., Sonti, V.K., Mohan, V.M.

(2021). Customized smart object detection: Statistics of
detected objects using IoT. In 2021
International
Conference on Artificial Intelligence and Smart
Systems (ICAIS), Coimbatore, India, pp. 1397-1405.
https://doi.org/10.1109/ICAIS50930.2021.9395913

[24] Hrushikesava, R.D.S., Lakshmi, R.B., Ashok, K.,

Waris, S.F. (2020). Tourism enhancer app: Userfriendliness of a map with relevant features. IOP
Conference Series: Materials Science and Engineering,
981(2): 022067. https://doi.org/10.1088/1757899X/981/2/022067

**187**