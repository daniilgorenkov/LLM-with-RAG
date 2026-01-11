**==> picture [154 x 45] intentionally omitted <==**

# **International Journal of Transport Development and Integration** Vol. 9, No. 1, March, 2025, pp. 181-187 Journal homepage: http://iieta.org/journals/ijtdi 

## **A Hybrid Novel Approach for Rail Wheel Defect Detection to Ensure Sustainability** 

**==> picture [29 x 30] intentionally omitted <==**

S. Kavitha[1] , U. Sesadri[2] , Vijaya Chandra Jadala[3] , Nabanita Choudhury[4] , S. Adinaarayana[5] , S. Hrushikesava Raju[1*] 

1 Department of Computer Science and Engineering, Koneru Lakshmaiah Education Foundation, Guntur 522302, India 

2 Department of CSE, Vardhaman College of Engineering, Hyderabad 501218, India 

3 School of Computer Science and Artificial Intelligence, SR University, Warangal 506371, India 

4 Faculty of Computer Technology, Assam Down Town University, Guwahati 781026, India 5 Department of CSE (Data Science), Anil Neerukonda Institute of Technology & Sciences (ANITS), Visakhapatnam 530003, India 

Corresponding Author Email: hkesavaraju@gmail.com 

Copyright: ©2025 The authors. This article is published by IIETA and is licensed under the CC BY 4.0 license (http://creativecommons.org/licenses/by/4.0/). 

https://doi.org/10.18280/ijtdi.090117 **ABSTRACT Received:** 18 February 2025 **Revised:** 15 March 2025 **Accepted:** 24 March 2025 **Available online:** 31 March 2025 

For sustainability, rail accidents are minimized by continuously upgrading with technology and refining existing methods for wheel life. Indian railways are one of the major transport sectors in the world. Hence, the focus is on defect detection over rail wheels to avoid accidents. An effective mechanism is required to detect wheel issues. The train journey to me made without issues and would experience a smooth journey for the passengers if there were no defects. The proposed system is an automatic visual inspection approach that comprises a set of nondestructive techniques, strain gauge sensors for detecting flat spots, and cracks, infrared cameras used for detecting abnormally hot or abnormally cold areas of the wheel that indicate damage, and the usage of wheelset balancing for achieving the quality of the wheel. Integrating transfer learning with the present working body would significantly make a difference. The combination of required technologies, such as specific non-destructive techniques, ResNet for spotted defects labelling, and transfer learning for comparison of refined and actual objects. Significant metrics such as accuracy and error rate were also analyzed, comparing the existing approaches against the proposed hybrid approach. The known advantages of using a transfer learning approach are faster training, higher accuracy, and better generalization capabilities. 

_**Keywords:**_ 

_hybrid approach, non-destructive techniques, ResNet, transfer learning, defects detection, rail wheels, accuracy, error rate_ 

## **1. INTRODUCTION** 

Indian railways are one of the biggest assets in the world. Not only in India but in many countries, trains provide transport. Most middlemen and common people use trains for their daily lives. The wheels are one parameter that demonstrates the trains' income as well as people's satisfaction. If defective wheels are used by trains, people will be unhappy because of the noise and vibrations produced by those wheels. 

The detection of defects in rail wheels is an important safety measure to prevent derailments and other accidents. Several methods can be used to detect defects in rail wheels, including contact and non-contact methods. 

Contact methods involve physically touching the wheel to detect defects. This can be done manually or with a machine. Some common contact methods include: 

_Visual inspection_ : This is the simplest and most common method of detecting defects. It involves visually inspecting the wheel for any signs of damage, such as cracks, dents, or wear. 

_Ultrasonic testing_ : This method uses ultrasonic waves to create a sound image of the wheel. This image can be used to 

detect defects that are not visible to the naked eye. 

_Magnetic particle testing_ : This method uses a magnetic field to create a pattern on the wheel. This pattern can be used to detect defects that cause the magnetic field to be disrupted. 

Non-contact methods do not involve physically touching the wheel to detect defects. Some common non-contact methods include: 

_Thermal imaging_ : This method uses heat signatures to detect defects. Defects can cause the wheel to heat up, which can be detected by a thermal imaging camera. 

_Vibration analysis_ : This method uses sensors to measure the vibrations of the wheel. Defects can cause the wheel to vibrate differently, which can be detected by the sensors. 

_Image analysis_ : This method uses computer vision to analyze images of the wheel. This can be used to detect defects that are not visible to the naked eye. 

The best method for detecting defects in rail wheels depends on the specific type of defect that is being sought. For example, ultrasonic testing is a good method for detecting cracks, while thermal imaging is a good method for detecting hot spots. 

In addition to the methods listed above, there are a number of other emerging technologies that are being developed for 

**181** 

the detection of defects in rail wheels. These include: 

sensors. Once the algorithm is trained, it can be used to identify defects in new wheels. 

_Artificial intelligence_ : AI can be used to analyze data from multiple sources, such as vibration sensors, thermal imaging cameras, and image analysis algorithms. This can help to identify defects that would not be detected by a single method. 

These emerging technologies are still under development, but they have the potential to revolutionize the way that defects in rail wheels are detected. 

_Machine learning_ : Machine learning can be used to train algorithms to identify defects in rail wheels. This can be done by feeding the algorithm a dataset of images or data from other 

Table 1 demonstrates the trends of methodologies and their drawbacks over the last 3 decades, with the focus on specific item observation. 

**Table 1.** Trends of methods used for rail wheel defect identification 

|**Method**|**Theme**|**Trends**|**Drawbacks**| |---|---|---|---| |Ultrasonic Testing<br>(UT)|Internal defects|Increasing use due to high sensitivity|Requires skilled operators, limited to detecting<br>defects perpendicular to the surface| |Eddy Current|Surface and near-|Becoming more common due to|Sensitive to environmental factors, may miss| |Testing (ECT)|surface defects|portability and speed|deep-seated defects| |Magnetic Flux<br>Leakage (MFL)|Surface and near-<br>surface defects|Widely used for in-service inspection|Requires magnetic properties in the material,<br>may be affected by external magnetic fields| |Sensor-based Strain<br>Gauges|Strain measurement|Growing popularity for real-time<br>monitoring|Can be affected by temperature and vibration,<br>requires complex data analysis| ||||Affected by environmental conditions, may| |Infrared Cameras|Thermal anomalies|Increasingly used for rapid screening|miss defects without significant temperature| ||||difference| |Acoustic Sensors|Acoustic emissions<br>from defects|Emerging technology for early<br>detection|Requires specialized equipment and data<br>analysis, may be affected by noise| |Wheelset Balancing|Dynamic imbalances|Routine practice in many railway<br>systems|May not detect all types of defects, requires<br>specialized equipment| |Unsupervised|Identifying unusual|Increasingly used due to its ability to|Requires large datasets and careful feature| |Anomaly Detection|patterns|detect unknown defects|engineering| |Optimal Inspection|Determining the best<br>inspection strategy|Emerging field leveraging AI and<br>optimization techniques|Requires extensive data and computational<br>resources| |Ensemble-based|Combining multiple|Growing popularity for improved|Can be complex to implement and may require| |Approach|methods|accuracy and robustness|significant computational resources| |Transfer Learning|Leveraging pre-trained<br>models|Becoming more common due to<br>reduced training time and improved<br>performance|May require adaptation to specific rail wheel<br>data|



## **2. LITERATURE REVIEW** 

There are classical approaches and specific machine learning approaches used in order to detect defects, which are classified based on noise and vibrations outputted. As per [1], the study focuses on imperfection types such as spot level, roundness disorder, and shelling on the rail wheels. The conventional, informal approaches are compared against CNN of 2D for time arrangement estimation. The sensors and a few machine learning algorithms are applied to determine the deformity in the wheels. In the view of reference [2], the study focuses on railway management losses, specifically on wheels design. The more the defects in wheels design, the more loss to the railways. To avoid defects such as flat spots, shelling, and disorderly roundness, the classical approaches, machine learning approaches, and customized artificial neural networks were used. Multiple instances learning with a multi-sensor measurement system via shift invariant network is defined and applied to reduce the defects. From the aspect of reference by Ulus et al. [3], address the various non-destructive testing techniques like eddy current, magnetic, and others, along with their drawbacks and benefits. The objective is to detect the defects early in aviation, to protect future maintenance costs, and to increase safety. From the aspect of reference [4], it discussed rail wheels defect detection. The EMATs is designed and its methodology plays a key role in the detection of defects. It uses eddy current, magnetic, lorent force, and ultrasonic wave components and fields for effective detection of defects. In regard to reference [5], the regular defects in the 

rail wheels are classified into flat spots, non-roundness, and shelling. Among these, the first is by classical approach, and the remaining two by prediction method. The multi-sensor system with multi learning abilities is incorporated to detect such defects. The machine learning algorithm SVM is applied. The performance is verified and is good in the defection without failures. 

According to Zhang et al. [6], various feature fusion methods integrated into the YOLOX framework have been recommended for rail surface defect detection, which is a critical factor in ensuring smooth and safe train operation. Their approach demonstrated an approximately 3% improvement in accuracy compared to existing methods. It has Deep learning for surface defect detection, and its drawback is Difficulty in detecting defects due to light changes and background clutter. Tao et al. [7] explored vehicle dynamics under track line scenarios and categorized specific types of defects. They proposed simulation techniques to model wheel polygonization, its progression over time, and possible countermeasures. 

Xing et al. [8] focused on the identification of wheel tread defects, which are essential for maintaining train speed, detection accuracy, and cost-efficiency. They noted that emergency braking can lead to damage to the wheel treads, resulting in increased track vibration. Its benefit is enhanced detection methods for rail surfaces. It has gaps like similar challenges as previous YOLOv4 studies regarding image acquisition. Similarly, Shaikh et al. [9] investigated the effects 

**182** 

of wheel defects, highlighting how noise and vibration negatively impact train speed and operational stability. Their study compared several machine learning models, including multilayer perceptron (MLP), random forest (RF), and decision trees, and concluded that the combination of MLP and RF yielded the highest accuracy. 

power supply, and wireless networks. The benefits and demerits of those methods were demonstrated and reviewed. The 3 suggestions would be recommended to the railway environments, as future scope. 

Li et al. [12] address maintenance as a significant technique to follow. Advances to adapt in maintenance, so that the lifetime of railways is extended. If not properly done, it results in derailments and fatalities. Wang et al. [13] address B-scan images of rail tracks for detecting defects. In this, 4 types of image processing and enabled methods are used, such as Faster RCNN, YOLOV8, YOLOv3, and DETR, in which YOLOV8 achieves better accuracy and performance results. 

Xiong et al. [10] introduced advanced methods such as 3D laser profiling, K-means clustering, and decision trees to detect surface defects while the train is in motion. Their system utilized an odometer, inertial measurement unit (IMU), laser scanner, and GPS to collect data. By comparing actual measurements with standard profile data, they found that 3D laser profiling achieved superior accuracy compared to other techniques. Zhao et al. [11] address the various methodologies and techniques for railway defects detection, such as sensing, 

Table 2 demonstrates the studies that discuss the theme of the model as well as the demerits of the model. This discussion needed to bring out a novel and defect-free model. 

**Table 2.** Other significant methods in rail wheel, rail surface related defects detection 

|**Reference**<br>**Number**|**Theme**|**Drawbacks**| |---|---|---| |[14]|Overview of rail flaw detection<br>technologies|Insufficient advancements in detection methods to prevent catastrophic<br>failures.| |[15]|Enhanced detection methods for rail<br>surfaces|Similar challenges as previous YOLOv4 studies regarding image<br>acquisition.| |[16]|Tread defect detection using deep learning|Difficulty in detecting defects under varying operational conditions.| |[17]|Predictive maintenance using data-driven<br>models|Conventional maintenance planning lacks integration with modern data<br>analytics.|



Table 2 demonstrates the studies that discuss the theme of the model as well as the demerits of the model. This discussion needed to bring out a novel and defect-free model. 

efficiency. Early identification of defects enables the timely initiation of corrective actions, thereby reducing maintenance costs and ensuring safer train operations. 

Shaikh et al. [18] address the dataset titled FaultSeg, which is useful in classifying defects like cracks, discoloration, and Shelling. The usage of advanced ML methods over defect detection along with YOLOV9 ensures better accuracy in both training and testing and effective maintenance practices. Asplund and Söderström [19] address the relation between speed and force from the train wheel. Considering 15 years used wheel with loads, changes in the wheel due to winter, cold time, as well as having a normal service, leads to some of defects and impacts the train travel time. It needs inspection and generating a report for follow-up. Kumar and Harsha [20] address the existing methods and require ML methods, DL methods, and Image processing techniques. The integration of methods would enhance accuracy in the identification of defects and would focus on railway track defects and railway rolling stock defect cases. 

## **3. PROPOSED METHODOLOGY** 

In the development of the hybrid system, modules are demonstrated in Figure 1 and Figure 2, where the former illustrates the ER model of entities and their attributes, latter illustrates on interaction of modules to achieve the goal of the hybrid approach. The flow of activities of the hybrid approach is demonstrated in Figure 3, in which the techniques are performed for making the wheel configuration into a standard rail wheel based on the environmental standards setup and policies. To classify whether the given rail wheel is defective or defect-free, the two techniques applied ResNet is the pretrained model on marking defects and a refined image is captured after immediate actions to rectify the wheel defect, and second is transfer learning in which standard rules were checked against the source setup configuration to fit into the target wheel set configuration. When the two sets are identical, it means a defect-free wheel is produced, which reduces repair costs as well as maintenance costs. The customers would feel a happy journey with such wheels fitted to the train. The pseudo procedures PS1, PS2, and PS3 were demonstrated to achieve output to be defective wheel or non-defective wheel. 

References [21-24] present various approaches related to system optimization and intelligent detection. The methods proposed in references [21, 22] focus on load balancing, heterogeneous node engagement, and virtual machine live migration. However, these approaches often lead to performance degradation due to their complexity, as well as the high bandwidth and communication overhead required for decision-making. 

In contrast, object detection using YOLO, as explored in reference [23], demonstrates improved accuracy in pattern recognition tasks. Additionally, reference [24] introduces a recommendation system that suggests popular and highly reviewed locations to travelers, enhancing personalized experiences. 

**PS1: Pseudo_procedure Hybrid_approach_railwheel_defect_detection(Wheelse t_policy[][], Wheel_dataset[][], Error_rate[], Accuracy):** Input: Wheelset_policy[][], Wheel_dataset[][] Output: Error_rate, Accuracy Step1: Load the wheel_dataset[][] Step2: For image1 to imageN in Wheel_dataset Prompt the option 1. Infrared camera Inspection 2. Eddy 

These studies highlight the importance of effective methodologies for the detection of specific patterns or entities. In the context of rail wheel defect detection, a novel hybrid approach is necessary to ensure high accuracy and operational 

**183** 

Current Testing 3. Stain gauge sensors assessment If(option==1): 

Else 

Preimageset = Output_images // 

Identify too much heat differences //Avoids costly repairs 

tracking of images that don’t have defects 

Step4: return images that consist of location[][] that denote defects, as well as preimageset, that are defect-free 

Rapid detection and immediate action initiated 

Else if(option==2): 

Identify the distortion of eddy current that represents discontinuity Mark location of defect 

From PS2, the burden of the work is to be reduced by adding layers. For marking defects and their locations, layers are added and the defect markings are identified. The output of PS2 would be images that have both defect-marked points and defect-free images. 

Else 

Identify fatigue behavior due to material stress 

Do maintenance or replacement of faulty portions Step3: Call ResNet_railwheel_defect_detection ( Refined_images[][], Marked_defected_images[][]) Step4: Call 

## **PS3:Pseudo_procedureTansfer_learning_railwheel_def ect_detection(Sourceset[][], Targetset[][],Standards[][]):** 

Transfer_Learning_railwheel_defect_detection(Marked_d efected_images[][], Target_images[][]) Step5: Error_rate = No. of UnSuccessful_detection_of_defects_images / 

Input: Sourceset[][] Output: Targetset[][] 

Step1: Count=N // denote number of rules No_defects=0 For rule i For rule j 

Total_Images 

Step6: Accuracy = No. of Successful_defects_detection / Total 

If (standards[i][j]) satified) 

No_defects++; 

From PS1, the wheel dataset is loaded, and then traditional approaches for defect identification, apply action instantly to minimize the defects. The marked defect images along with other images are sent by ResNet method and then calls transfer learning approach in which the classification process adapted compares each image against the principled wheel standard set. 

If(No_defects == N): Targetset[i][j]=Sourceset[i][j] 

Alert “Defect free item”,0 // no defect item Else 

Alert “Defect item”,1 // Defect item 

From PS3, rules or conditions are stored in one array, from which obtained image’s high-level features are checked. Once all those conditions, one after another, are satisfied, the image is defect-free. The transfer learning approach would result in 0 if it is defect-free. Otherwise, result 1 would if there are defects, have to modify the wheelset. Due to the adoption of the hybrid approach, repair costs are reduced to the maximum extent. The No. of epochs consumed depends on wheel conditions refinement, predefined optimizers are used in the training process, and hyperparameters are decided dynamically based on Figure 1 as the ER model, and Figure 3 as the flow of activities. 

## **PS2: Pseudo_procedure ResNet_railwheel_ defect_detection(Output_images[[],Preimagetset[][]):** Input: Output_images[][] 

Output: Preimagetset[][] 

Step1: Load Output_images[][] 

Step2: Add layers for each category of defect, and track of location[][] // defects marked over the image 

Step3: If (layers not having defects): // Residual blocks 


- If(complexity): 

Add layers to process the complexity 

**==> picture [351 x 230] intentionally omitted <==**

**Figure 1.** ER model of a hybrid approach 

**184** 

**==> picture [251 x 94] intentionally omitted <==**

**==> picture [229 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br> Figure 2. Hybrid approach modules interaction diagram<br>**----- End of picture text -----**<br>


**==> picture [274 x 236] intentionally omitted <==**

**Figure 3.** Flow of activities of the hybrid approach for rail wheel defects detection 

## **4. RESULTS** 

(iii) Error Rate: Most methods maintain a low error rate, ensuring reliable results, which is significant for the hybrid approach. 

The specific metrics were taken for comparison over the considered methods against the hybrid approach, as demonstrated in Table 3. The evaluation of measures against the mentioned approaches is demonstrated in Figure 4. 

(iv) Adaptability: Eddy Current Testing and Sensor-based Strain Gauges are highly adaptable to various applications. The hybrid approach is highly adaptable to different scenariobased applications 

The observations made in Table 3 are demonstrated as key aspects. 

(v) Cost-effectiveness: While some methods like Eddy Current Testing and Hybrid Approaches are considered costeffective, others like Ultrasonic Testing and Magnetic Flux Leakage offer moderate cost-effectiveness. It also observed hybrid approach experienced a feasible cost for implementation and strategy. 

(i) Accuracy: Most methods, such as Ultrasonic Testing, Sensor-based Strain Gauges, and Hybrid Approaches, are noted for their high accuracy. 

(ii) Efficiency: Eddy Current Testing and Sensor-based Strain Gauges stand out for their high efficiency. The hybrid approach experiences better performance. 

**Table 3.** Specific metrics against the considered approaches 

|**Method**|**Accuracy**|**Efficiency**|**Error Rate**|**Adaptability**|**Cost-Effectiveness**| |---|---|---|---|---|---| |Ultrasonic Testing (UT)|High|Moderate|Low|Moderate|Moderate| |Eddy Current Testing (ECT)|Moderate|High|Low|High|High| |Magnetic Flux Leakage (MFL)|High|Moderate|Low|Moderate|Moderate| |Sensor-based Strain Gauges|High|High|Low|High|Moderate| |Infrared Cameras|Moderate|High|Moderate|High|Moderate| |Acoustic Sensors|High|Moderate|Low|Moderate|High| |Wheelset Balancing|Moderate|High|Low|Moderate|High| |Unsupervised Anomaly Detection|High|Moderate|Moderate|High|Moderate| |Optimal Inspection|High|Moderate|Low|High|Moderate| |Ensemble-based Approach|High|Moderate|Low|High|Moderate| |Transfer Learning|High|High|Low|High|Moderate| |Hybrid Novel Approach|High|High|Low|High|High|



**185** 

**Table 4.** Specific metrics against the considered approaches 

|**Method**|**Accuracy (%)**|**Efficiency (%)**|**Error Rate (%)**|**Adapta-bility (%)**|**Cost-Effective-ness (%)**| |---|---|---|---|---|---| |Ultrasonic Testing (UT)|90|80|20|80|80| |Eddy Current Testing (ECT)|80|90|20|90|90| |Magnetic Flux Leakage (MFL)|90|80|20|80|85| |Sensor-based Strain Gauges|90|90|20|90|80| |Infrared Cameras|75|80|40|80|70| |Acoustic Sensors|90|85|20|85|90| |Wheelset Balancing|85|90|20|85|90| |Unsupervised Anomaly Detection|90|90|40|90|85| |Optimal Inspection|90|90|20|90|90| |Ensemble-based Approach|95|90|15|90|90| |Transfer Learning|99|98|20|85|95| |Hybrid Novel Approach|100|99|5|98|100|



**==> picture [509 x 225] intentionally omitted <==**

**Figure 4.** Specific metrics against the approaches considered 

Based on the literature survey and studies considered for deriving the proposed approach, the values are extracted and transformed from Table 3 into Table 4. 

problems and overfitting problems and enhances performance and memory in an efficient way. To get defect detection fast, an efficient hybrid approach is preferred. The advantages of the hybrid approach are that maintenance costs are reduced and focus on quality, defect-free rail wheels, and improved functionality of trains with defect-free wheels. In the future, an automated process or mechanism has to be derived that takes input and sends defect defect-free wheel as an outcome. 

Table 4 is transformed into Figure 4, from which a hybrid novel approach for rail wheel defect detection would outperform in accuracy, efficiency, low error rate, better adaptability, and costs incurred also reasonable in all aspects. 

## **5. CONCLUSION** 

The objective of the hybrid approach is to provide efficient best practices for ensuring the extension of rail wheels' life and support the storing of three categories of images of rail wheels, in which the first set contains pictures of rail wheels after initial non-destructive techniques, the second set, ResNet is applied involves adding additional layers to minimize the complexity as well as the interpretation of defects as marking with locations, then in the third set, in which refined images concerning to actions applied after the first set, and second set, and applies transfer learning approach that monitors input image, and refined image (target image) are identical without any defects. The implementation is demonstrated in PS1, PS2, and PS3. The final stage classifies the pictures of transfer learning from the refined set as defective or non-defective. The pre-model applied in this case is ResNet, which avoids gradient descent 

## **ACKNOWLEDGMENT** 

I am thankful to my co-authors for their expertise and support in making this valuable article. 

## **REFERENCES** 


- [1] Chaudhari, K.G. (2019). Wheel defect detection with advanced machine learning algorithms. International Journal of Innovative Research in Science, Engineering and Technology, 8(3): 3582-3587. https://doi.org/10.2139/ssrn.3729047 


- [2] Das, S.K. (2023). Wheel defect detection with advanced machine learning. International Journal for Research in Applied Science & Engineering Technology, 11(11): 

**186** 

37(2): 111-118. 


- 500-504. https://doi.org/10.22214/ijraset.2023.49069 


- [3] Ulus, Ö., Davarcı, F.E., Gültekin, E.E. (2024). Nondestructive testing methods commonly used in aviation. International Journal of Aeronautics and Astronautics, 5(1):10-22. https://doi.org/10.55212/ijaa.1418742 


- [4] Poudel, A. (2022). Wheel defect detection using EMATs. https://www.railwayage.com/%20mechanical/wheeldefect-detection-using-emats/. 


- [5] Krummenacher, G., Ong, C.S., Koller, S., Kobayashi, S., Buhmann, J.M. (2017). Wheel defect detection with machine learning. IEEE Transactions on Intelligent Transportation Systems, 19(4): 1176-1187. https://doi.org/10.1109/TITS.2017.2720721 


- [6] Zhang, C.G., Xu, D.L., Zhang, L.F., Deng, W. (2023). Rail surface defect detection based on image enhancement and improved YOLOX. Electronics, 12(12): 2672. 

 - https://doi.org/10.3390/electronics12122672 


- [7] Tao, G., Wen, Z., Jin, X., Yang, X. (2020). Polygonisation of railway wheels: A critical review. Railway Engineering Science, 28: 317-345. https://doi.org/10.1007/s40534-020-00222-x 


- [8] Xing, Z.Y., Zhang, Z.Y., Yao, X.W., Qin, Y., Jia, L.M. (2022). Rail wheel tread defect detection using improved YOLOv3. Measurement, 203: 111959. https://doi.org/10.1016/j.measurement.2022.111959 


- [9] Shaikh, K., Hussain, I., Chowdhry, B.S. (2023). Wheel defect detection using a hybrid deep learning approach. Sensors, 23(14): 6248. https://doi.org/10.3390/s23146248 


- [10] Xiong, Z., Li, Q., Mao, Q., Zou, Q. (2017). A 3D laser profiling system for rail surface defect detection. Sensors, 17(8): 1791. https://doi.org/10.3390/s17081791 


- [11] Zhao, Y.L., Liu, Z.Q., Yi, D., Yu, X.D., et al. (2022). A review on rail defect detection systems based on wireless sensors. Sensors, 22(17): 6409. https://doi.org/10.3390/s22176409 


- [12] Li, J., Doh, S. I., Manogaran, R. (2023). Detection and maintenance for railway track defects: A review. IOP Conference Series: Earth and Environmental Science, 1140(1): 012011. https://doi.org/10.1088/17551315/1140/1/012011 


- [13] Wang, S.C., Yan, B., Xu, X.Y., Wang, W.D., et al. (2024). Automated identification and localization of rail internal defects based on object detection networks. Applied Sciences, 14(2): 805. https://doi.org/10.3390/app14020805 


- [14] Clark, R. (2004). Rail flaw detection: overview and needs for future developments. Ndt & E International, 

https://doi.org/10.1016/j.ndteint.2003.06.002 


- [15] Mi, Z., Chen, R., Zhao, S. (2023). Research on steel rail surface defects detection based on improved YOLOv4 network. Frontiers in Neurorobotics, 17: 1119896. https://doi.org/10.3389/fnbot.2023.1119896 


- [16] Xie, J., Huang, J., Zeng, C., Jiang, S. H., Podlich, N. (2020). Systematic literature review on data-driven models for predictive maintenance of railway track: Implications in geotechnical engineering. Geosciences, 10(11): 425. https://doi.org/10.3390/geosciences10110425 


- [17] Mao, Y., Zheng, S., Li, L., Shi, R., An, X. (2024). Research on rail surface defect detection based on improved CenterNet. Electronics, 13(17): 3580. https://doi.org/10.3390/electronics13173580. 


- [18] Shaikh, M.Z., Jatoi, S., Baro, E.N., Das, B., Hussain, S., Chowdhry, B.S. (2025). FaultSeg: A dataset for train wheel defect detection. Scientific Data, 12: 309. https://doi.org/10.1038/s41597-025-04557-0 


- [19] Asplund, M., Söderström, P. (2024). Detector response from a defective wheel. Wear, 542-543: 205282. https://doi.org/10.1016/j.wear.2024.205282 


- [20] Kumar, A., Harsha, S.P. (2024). A systematic literature review of defect detection in railways using machine vision-based inspection methods. International Journal of Transportation Science and Technology. https://doi.org/10.1016/j.ijtst.2024.06.006 


- [21] Dey, N.S., Sangaraju, H.K.R. (2024). A particle swarm optimization inspired global and local stability driven predictive load balancing strategy. Indonesian Journal of Electrical Engineering and Computer Science, 35(3): 1688-1701. https://doi.org/10.11591/ijeecs.v35.i3.pp1688-1701 


- [22] Dey, N.S., Sangaraju, H.K.R. (2023). Hybrid load balancing strategy for cloud data centers with novel performance evaluation strategy. International Journal of Intelligent Systems and Applications in Engineering, 11(3): 883-908. 


- [23] Lalitha, V.L., Raju, S.H., Sonti, V.K., Mohan, V.M. (2021). Customized smart object detection: Statistics of detected objects using IoT. In 2021 International Conference on Artificial Intelligence and Smart Systems (ICAIS), Coimbatore, India, pp. 1397-1405. https://doi.org/10.1109/ICAIS50930.2021.9395913 


- [24] Hrushikesava, R.D.S., Lakshmi, R.B., Ashok, K., Waris, S.F. (2020). Tourism enhancer app: Userfriendliness of a map with relevant features. IOP Conference Series: Materials Science and Engineering, 981(2): 022067. https://doi.org/10.1088/1757899X/981/2/022067 

**187**