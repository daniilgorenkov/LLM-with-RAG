 WG-line JJ-line ZX-line
4 5
2
2
0 0 0
 Left rail
-2
-2
-4 -5
0 500 1000 0 500 1000 0 500 1000
4 5
2
2
 Right rail 0 0 0
-2
-2
-4 -5
0 500 1000 0 500 1000 0 500 1000
4 5
2 5
 Left rail 0 0 0
-2 -5
-4 -5
0 500 1000 0 500 1000 0 500 1000
5 5
5
 Right rail 0 0 0
-5
-5 -5
0 500 1000 0 500 1000 0 500 1000
Distance (m) Distance (m) Distance (m)
 Three measured track irregularities on WG-line, JJ-line, and ZX-line
(a) 20 (b)
S1002CN 1.  After running 15,000 km
After running 15,000 km After running 42,000 km
After running 42,000 km After running 75,000 km
10 After running 75,000 km 1 After running 95,000 km
After running 95,000 km After running 170,000 km
After running 170,000 km After running 190,000 km
After running 190,000 km 0.8
0
0.6
-10
0.4
-20 0.2
0
-30
-60 -40 -20 0 20 40 60 -60 -40 -20 0 20 40 60
Y (mm) Y (mm)
Lateral track irregularity (mm)
Vertical track irregularity (mm)
(mm) (mm)
Z w
Z
**----- End of picture text -----**However, for 1D time-series data, such as the acceleration data used in this paper, 1DCNN is usually a more ideal choice . Figure 4 shows the difference between the 2DCNN and 1DCNN, where applying 2DCNN to a 2D image will generate a 2D image, whereas applying 1DCNN to a 1D image will generate a 1D image. The convolutional filter of the 1DCNN is one-dimensional, which enables it to detect the interdependencies in 1D data.## 3.1.  The Architecture of the designed 1DCNNThe architecture of the 1DCNN model designed in our work is shown in Fig. 5. The proposed model includes 7 main blocks, the first 5 blocks are designed for feature extraction, among which each block consists of a 1DCNN layer, an advanced activation function (AAF) layer, and a max-pooling layer. The last two blocks are designed for**----- Start of picture text -----**
 104 Y. Ye et al.
Width Sequence data
Sequence data
Height
2D 1D
convolution convolution
Input: 3D tensor Output: 3D tensor Input: 2D tensor Output: 2D tensor
(a) (b)
**----- End of picture text -----**classification, where each includes a fully connected layer and an activation layer.For the design of the 1DCNN layer, existing studies  have shown that the feature maps should change from wide and shallow to narrow and deep from the input layer to the output layer. This rule has proven to be very effective in many successful CNN models, such as the classic AlexNet  and VGGNet . This article, therefore, follows this rule to adjust the number of the convolution kernels in the CNN layer part, i.e., the number of CNN convolution kernels in each subsequent layer is twice that of the previous layer. This strategy can increase the depth of the feature maps from the first block to the last block. In our model, the number of convolution kernels in the first CNN layer (block 1) is set to 32, and the number of convolution kernels in the last CNN layer (block 5) is 512.For the selection of the activation function, most studies on CNN models use the rectified linear unit (ReLU) function . This function, however, has a disadvantage, that is, a too-large learning rate or gradients could easily lead to the ‘‘death’’ of neurons, and the ReLU function often cannot perform well when the nonlinear relationship of the input dataset is very complicated . The vehicle suspension system is a highly nonlinear system. For signals from such systems, this activation function is obviously not an ideal choice. Therefore, an advanced activation function, parametric rectified linear unit (PReLU) proposed in , is used in our work, and the expression is given:**----- Start of picture text -----**
 1DCNN part: feature extraction Fully-connected layer part: classification
Depth
64 neurons
4 neurons
Normal
LDF
YDF
512 Y&LDF
157×1×128 79×1×256 40×1×512 Block 7
Width×Height×Depth= 1250×1×32625×1×32 625×1×64313×1×64313×1×128 157×1×256Block 4 79×1×512Block 5
1250×1×1 Block 2 Block 3
Block 1
Block 6
Input layer 1DCNN layer or Activation function layer Max-pooling layer Global average pooling layer Output layer
Width
Softmax
Height
... Advanced activation function
 Data acquisition GWN-strategy
Normal LDF
5 5
0 0
-5 -5
0 2 4 0 2 4
Time (s) Time (s)
YDF Y&LDF
10 10
0 0
-10 -10
Accelemeter position 0 2 4 0 2 4
Time (s) Time (s)
EST-strategy Upper envelope
5 Normal LDF
5 5
0
0 0
-5
-5 -5
-10 0 2 4 0 2 4
Time (s) Time (s)
-15
YDF Y&LDF
-20 10 10
S1002CN 0 0
-25
S1002CN-W190K -10 -10
-30
0 2 4 0 2 4
-60 -40 -20 0 20 40 60
Y (mm) Time (s) Time (s)
1DCNN Andrews curve
ID
convolution
Input: 2D tensor Output: 2D tensor
t
2)
Pahse I
Data preprocessing Acceleration (m/s
2)
 (mm)
Pahse II Z
Acceleration (m/s
Traning dataset selection
yit
Pahse III
lassification and visualization
C
**----- End of picture text -----**Case III (Sect. 4.1.3), respectively, demonstrate that the GWN-strategy can overcome the interference caused by track irregularities, and the EST-strategy can overcome the interference caused by wheel wear. Through the multivariate analysis method, Case IV (Sect. 4.1.4)demonstrates that the GWN-EST-1DCNN method is not disturbed by simultaneous changes in track irregularities and wheel wear.## 4.  Case I (same line and same wheel profile)A vehicle model, with S1002CN wheel profiles, running on the WG line is taken as an example to illustrate the feasibility of using the 1DCNN method for train suspension systems in the case of the same railway line and the same wheel profile. The training dataset and testing dataset are, respectively, composed of 3,456 samples and 1,408 different samples, respectively . The length of each sample is t ¼ 5 s. According to the designed network of the 1DCNN described in Sect. 3.1, the final results,including the convergence rate, confusion matrix, and visualization features, are shown in Fig. 9. Figure 9a indicates that the designed 1DCNN method with 30 epochs is convergent. The confusion matrix for the testing samples is shown in Fig. 9b, and it can be seen that all the states can be totally distinguished by the 1DCNN method (100%). To visualize the classification and clustering results, Andrews plot is presented in Fig. 9c, which shows that the four states can be completely separated and the clustering result is excellent. Overall, Fig.  indicates that the designed**----- Start of picture text -----**
 (a)
Training accuracy
Validation accuracy
Epoch
(b) Normal LDF YDF Y&LDF (c)
Normal
LDF
YDF
Y&LDF
t
Accuracy
yit
**----- End of picture text -----****----- Start of picture text -----**
 Recognition result Andrews curve
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
yit
Without GWN-strategy
ZX-line
yit
With GWN-strategy
yit
Without GWN-strategy
JJ-line
yit
With GWN-strategy
**----- End of picture text -----****----- Start of picture text -----**
 110 Y. Ye et al.
Recognition result Andrews curve
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
yit
Without EST-strategy
S1002CN-W95K
yit
With EST-strategy
**----- End of picture text -----**experiment proves that the GWN-strategy can improve the robustness against track irregularities.## 4.  Case II (same wheel profile, and different railway lines)## 4.  Case III (same railway line, and different wheel profiles)To demonstrate that the GWN-strategy can improve the robustness of the diagnostic method against track irregularities, three measured track irregularities plotted in Fig.  are introduced here. The wheel profile used here is S1002CN. The training dataset and testing dataset are composed of 3,456 samples and 4,992 different samples, respectively . Finally, the results are shown in Fig. 10. It can be clearly seen that the LDF state cannot be well distinguished without the GWN-strategy. On the ZXline, 47.9% of the LDF state was incorrectly identified as the normal state, and the corresponding incorrect recognition rate is 11.6% on the JJ-line. However, with the GWNstrategy, the corresponding incorrect recognition rates decrease from 47% and 11.6% to 16% and 4%, respectively; and the classification and clustering effect become better since it can be clearly seen that for the case of ZXline and Without GWN-strategy, the Andrew curve cannot show the LDF state (blue curve) at all. The simulationTo demonstrate that the EST-strategy can improve the robustness of the diagnostic method against wheel wear, a new S1002CN wheel profile, the most worn wheel profile (S1002CN-W190K), and a wheel profile with a degree of wear between the two profiles (S1002CN-W95K) are introduced here . The rail line used here is the WG-line. The training dataset and testing dataset are composed of 3,456 samples and 1,480 different samples, respectively . Note that when using the ESTstrategy, the samples of the training dataset are randomly selected from the dataset corresponding to the S1002CN wheel profile and the dataset corresponding to the S1002CN-W190K wheel profile, while without the ESTstrategy, the training dataset is only the dataset corresponding to the S1002CN wheel profile; the testing dataset is the dataset corresponding the S1002CN-W95K. Figure 11 shows the recognition results obtained by these two methods. It can be seen that, without the EST-strategy, 29.9% of the normal state is incorrectly identified as LDF,**----- Start of picture text -----**
 Recognition result Andrews curve
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
Normal LDF YDF Y&LDF
Normal
LDF
YDF
Y&LDF
t
yit
Without GWN-strategy Without EST-strategy
ZX-line
yit
With GWN-strategy With EST-strategy
yit
Without GWN-strategy Without EST-strategy
JJ-line
yit
With GWN-strategy With EST-strategy
**----- End of picture text -----****----- Start of picture text -----**
 (b)
(a)
(c)
200
100
0
-100
Accelermeter position 0 500 1000 1500 2000 2500
Time (s)
10
0
Abnormal Normal
-10
0 500 1000 1500 2000 2500
Time (s)
Speed (km/h)
2)Acceleration (m/s
**----- End of picture text -----**and all the Y&LDF samples are incorrectly recognized as YDF. By contrast, when using the EST-strategy, the accuracy is significantly improved. Besides, the Andrews curve also shows that when the EST strategy is applied, the difference in the curve distribution of these four faults becomes obvious. The simulation experiment proves that the EST-strategy can improve the robustness against wheel wear.## 4.  Case IV (different railway lines, and different wheel profiles)In this subsection, we test the fault states under different track irregularities and different wheel profiles, and the training dataset and testing dataset are composed of 3,456 samples and 4,992 different samples, respectively . According to the technique route of the GWNEST-1DCNN method described in Sect. 3.3, the final results in Fig.  show that, compared with simply using the 1DCNN method, the GWN-EST-1DCNN method can classify fault states regardless of whether the profile changes or the railway line changes except for a slightly worse prediction of the LDF samples on the ZX-line. Overall, it can be concluded that the recognition result is greatly improved.## 4.  DiscussionThe advantages of the proposed GWN-EST-1DCNN method mainly arise from the following two aspects:- (1) Track irregularities affect the bogie accelerations required for train suspension fault diagnosis. Under different track irregularities, there are some different relatively high-frequency and low amplitude impact components in these acceleration signals. The strategy of adding Gaussian white noise (GWN-strategy) to the original acceleration signals can improve the immunity of the diagnostic method to track irregularities since this strategy reduces the sensitivity of diagnostic methods to changes in track spectrum.- (2) The wheel profile will change as the train running mileage increases. As the mileage increases, the amplitude of the bogie acceleration also increases. Therefore, using the dataset trained under the new wheel profile to identify the dataset under the worn wheel profiles may cause misidentification, i.e., the fault diagnostic method may incorrectly attribute the change in the bogie acceleration to a failure of the vehicle suspension system. The EST-strategy can improve the immunity of the diagnostic method to wheel wear mainly due to two reasons: (I) The training dataset of the diagnostic method covers a wider range of samples, which can identify the testing dataset to a certain extent more accurately. (II)- Training the diagnostic method with the datasets corresponding to the new wheel profile and the most worn wheel profile makes the method immune to the changes in the acceleration amplitude caused by wheel wear to a certain extent.## 5 5. Experimental verification## 5.  Experiment setupThe actual operating conditions of railway vehicles are more complicated. To verify the performance of the 1DCNN method in real-life conditions, the field tracking data of a CRH3 train running on a high-speed railway line are applied. More information concerning the monitoring system can be found in . The acceleration was measured through a tri-axial accelerometer mounted on the bogie frame , and the original sampling frequency was equal to 2 kHz. In our work, the lateral acceleration signal from the tri-axial accelerometer with a resampling frequency 250Hz is used.When processing the tracking data, it was found that the acceleration signal of front bogie at the third car was abnormally vibrating, and its amplitude, for most of the time, was usually greater than that of the acceleration signal of other front bogies. Upon inspection, it was found that a hydraulic cylinder of the secondary lateral damper at the front bogie of the third car was short of oil . Figure 13c shows the vehicle speed, the lateral acceleration of the front bogie at the third car (abnormal), and the lateral acceleration of the front bogie at the second car (normal).## 5.  Fault diagnosisThree states, including the normal (normal), the lateral damper failure at the speed of 80–100 km/h (LDF80–100), and the lateral damper failure at the speed of 180–200 km/ h (LDF180–200), are selected for analysis. The training dataset and testing dataset are, respectively, composed of 2,560 samples (normal: 1000; LDF80–100: 780; LDF180– 200: 780) and 1024 samples (normal: 500; LDF80–100: 262; LDF180–200: 262), and the length of each sample is t ¼ 5 s. The designed 1DCNN method described in Sect. 3.  is applied to these signals, and the final results, including the convergence rate, confusion matrix, and Andrews curve, are shown in Fig. 14. Figure 14a indicates that the proposed 1DCNN method with 30 epochs is convergent. The confusion matrix for the testing samples is provided in Fig. 14b, and it can be seen that all the states can be totally distinguished (100%). Andrews plot**----- Start of picture text -----**
 (a)
Training accuracy
Validation accuracy
Epoch
(b) Normal LDF80–100 LDF180–200
Normal
LDF80–100
LDF180–200
(c)
–
–
t
Accuracy
yit
**----- End of picture text -----**presented in Fig. 14c shows that the three states can be completely separated and the clustering result is excellent. The experiment results obtained using the field tracking data further verify that the proposed 1DCNN-based method can accurately identify the faults of the vehicle suspension systems at different speeds.Due to the limitation of experimental resources, this paper only verified the method of 1DCNN to identify the secondary lateral damper failure using the field tracking data.## 6 ConclusionTrack irregularities and wheel wear will affect the vibration signals used for condition monitoring of railway vehicles. The developed fault diagnosis method for train suspension systems, therefore, must be guaranteed to be immune to changes resulting from the track irregularities and wheel wear before being put into use. Aiming at solving this issue, a GWN-EST-1DCNN-based method for high-speed train suspension systems is proposed. This method consists of three phases. In the first phase (data preprocessing), a strategy of adding Gaussian white noise (GWN-strategy) is applied to the original signal, making the diagnostic method be immune to the interference caused by track irregularities. In the second phase (training dataset establishment), an EST-strategy is proposed to improve the robustness of the diagnostic network against wheel wear. In the third phase (training and recognition), a 1DCNN-based fault diagnostic network of high-speed train suspension systems is built. Simulation experiments show the superiority and correctness of the proposed method. In addition, the field tracking data of a CRH3 train running on a highspeed railway line are used to further verify the effectiveness of the 1DCNN method. The test results show that the method has the potential to be applied in the field of railway engineering.This paper ends with the following notes. (1) It should be noted that the trained DL algorithm is extremely sensitive to the vehicle speed because the axlebox acceleration caused by different suspension faults varies at different vehicle speeds. Therefore, during on-board monitoring, the suspension status can be determined by obtaining the axlebox acceleration at a constant speed (e.g., 200 km/h or 250 km/h). However, to achieve real-time monitoring, more velocity conditions need to be further analyzed. (2) In the simulation experiments, only the complete damage of the dampers in the secondary suspension system is simulated. The degradation of suspension systems, including dampers, will be studied in the following-up work. (3) In the field experimental part, due to the limitation of experimental resources, this paper only verified the method of 1DCNN to identify the secondary lateral damper failure using the field tracking data.