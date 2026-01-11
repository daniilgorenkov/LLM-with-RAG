**==> picture [93 x 23] intentionally omitted <==**

Received 14 December 2022, accepted 13 January 2023, date of publication 27 January 2023, date of current version 13 February 2023. _Digital Object Identifier 10.1109/ACCESS.2023.3240167_ 

# State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels: A Comprehensive Review 

## MUHAMMAD ZAKIR SHAIKH 1, ZEESHAN AHMED 1, BHAWANI SHANKAR CHOWDHRY 1, (Senior Member, IEEE), ENRIQUE NAVA BARO 2, TANWEER HUSSAIN 1, (Member, IEEE), MUHAMMAD ASLAM UQAILI 1, SANAULLAH MEHRAN 1, DILEEP KUMAR 1,3, AND ALI AKBER SHAH 1 

1National Center of Robotics and Automation-Condition Monitoring Systems Laboratory, Mehran University of Engineering and Technology (MUET), Jamshoro 76062, Pakistan 

2Departamento de Ingeniería de Comunicaciones, Campus de Teatinos, Universidad de Malaga, 29016 Málaga, Spain 

3Department of Electronic Engineering, Polytechnic University of Catalonia, 08034 Barcelona, Spain 

Corresponding author: Muhammad Zakir Shaikh (zakir.shaikh@faculty.muet.edu.pk) 

This research is supported in part by National Center of Robotics and Automation-Condition Monitoring Systems Laboratory, Mehran University of Engineering and Technology and in part by the Junta de Andalucía, Grupo de investigación TIC128, Universidad de Malaga, Spain. 


- **ABSTRACT** In recent decades, there has been a constant demand for faster, longer, and safer railway networks. This also brings challenges for condition monitoring systems in modern railway vehicles. More specifically, critical parts of railway vehicles like wheels degrade over time due to various operational and environmental reasons. Different dynamic effects such as skidding/sliding over the track and the presence of contamination between wheel-rail cause various wheel defects. Faulty wheels ultimately lead to the derailment of railway vehicles. To avoid worst situations like railway derailments, various research has been conducted for developing efficient condition monitoring systems for railway wheels. In addition, there has been some commercial condition monitoring products that can be deployed with railway vehicles. These systems incorporate various sensors such as strain gauges and vision sensors to collect data for diagnosis and prognosis. Various methods have been explored but yet there is a broad research gap in terms of developing advanced onboard condition monitoring systems. With the progress in technology, advanced systems with Machine Learning/Deep Learning methods can provide more efficient and robust condition monitoring of dynamic railway systems. Considering the need for advancement in condition monitoring systems for railway vehicles, a comprehensive review of existing condition monitoring systems for railway wheels is conducted in this paper. The review is aimed at understanding the feasibility and potential of new methods for modern railways. This paper provides a detailed overview of studies on the existing wayside systems and reports their advantages and disadvantages concerning its recently emerging counterpart on-board monitoring systems. Data acquisition systems and analysis methods are critically reviewed which could assist in developing more efficient and reliable condition monitoring systems for railway wheels. This article also reviews the current progress of wayside systems and their limitations. The article is targeted at the researchers and engineers working in this domain, who can pave the way for developing advanced and cost-effective condition monitoring systems for railway wheels using modern technologies. 

**INDEX TERMS** Railway wheels, fault diagnosis, condition monitoring, sensors, dynamic systems. 

The associate editor coordinating the review of this manuscript and approving it for publication was Mehrdad Saif . 

**I. INTRODUCTION** 

Wheels are very critical components of the railway system which requires continuous monitoring for safe and 

VOLUME 11, 2023 This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

13257 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

sustained operation. Wheels degrade due to various environmental and operational reasons. Rough environments and operating conditions cause various faults such as cracks, fatigue, shelling, spalls, flats, cavities, and indentations [1], [2]. The continuous wheel degradation in the shape of different faults ultimately lead to the major damages and accidents. Thus, continuous or periodic condition monitoring is essential to minimize the risk. Additionally, faults such as wheel flats are also a source of great discomfort for the residents living along the railway line and passengers onboard the vehicle. Deployment of Condition Monitoring Systems (CMS) results in process optimization, high reliability, reduced risk of failure, and financial loss. These reasons have made CMS an integral part of the railway for uninterrupted operation [3]. For predictive maintenance and restoration operation, a modern-day railway system relies on advanced monitoring systems. Sensors and their point of installation in CMS are decided based on the intended application of the system. The point of the installation could be either on the rolling stock or track mounted. Track-mounted sensors are usually used to detect wheel faults and on-board sensors are used for infrastructure monitoring [4], [5]. Railway infrastructure management is driven by data acquired via inspection devices. Predictive models use this data to better predict potential faults in the future and suggest maintenance strategies. 

With the progress in the railway transportation field [6], [7] various research has been conducted to explore methods of condition monitoring and effective fault diagnosis of railway wheels. Currently adopted methods of wheel inspection can be broadly categorized into two types: online inspection and offline inspection. In online inspection, the vehicle is examined while running. On the other hand, offline inspection requires putting the vehicle out of operation or it could be taken to a maintenance workshop for a thorough inspection. The online inspection could be further categorized into onboard and trackside inspection. Onboard inspection implies that the inspection system is mounted on the wheelset. Whereas, trackside systems are on-ground systems, that monitor wheels while the vehicle is running [8] The categorization of wheelset inspection is shown in Figure 1. 

**==> picture [153 x 103] intentionally omitted <==**

**FIGURE 1.** Inspection methods. 

Each approach has its pros and cons which are taken into consideration for condition monitoring of wheels depending 

on inspection duration and fault severity level [9]. Among these, wayside wheel CMSs are considered the most effective method in terms of safety, cost optimization, and preventive maintenance solutions [3]. These methods could be further classified based on types of measurements such as strain, vibration, and Acoustic Emissions (AE). These measurements are analyzed to detect wheel tread and profile. The development of onboard CMS has been an active field of research and multiple methods of signal processing and estimation techniques such as the Kalman filter and its variants are commonly used for estimating the parameters such as adhesion and conicity. 

With the technological advancement in the fields of sensor design, information-processing techniques such as the emergence of Artificial Intelligence (AI) and better processing hardware have significantly contributed towards the design and development of more efficient CMS. In this direction, AI and computer vision based techniques have also been investigated for condition monitoring of railway wheels, which are widely exploited for different tasks [10]. Multiple pieces of research have been conducted for wheel fault diagnosis using Deep Learning (DL) algorithms owing to advantages such as high accuracy, end-to-end implementation, handcrafted features, adaptability to withstand noise, and upgradability. 

In the past, several reviews have been published for condition monitoring techniques discussing automated inspection systems, data acquisition techniques, maintenance strategies, and visual inspection techniques. Ngigi et al. [11] endeavoured to compare and critically assess the modern methods and review the number of present monitoring methods to perform fault detection in railways. For Condition monitoring of railway assets, a generalized overview of the model-based techniques, signal based techniques are discussed. Practical applications of the developed vehicle-based or track-based systems are also reviewed. For saving cost and time, the adoption of condition-based maintenance by several wayside monitoring devices is encouraged. However, several new methods and techniques have been reported in the literature which need to be reviewed to assess their applicability in modern railway systems. 

Further, Kundu et al. [3] presented a comprehensive overview of the sensors available for health monitoring of the wheel and bearing in railway vehicles. Comparative analyses of different sensing technologies were performed in the domain of onboard and wayside to understand their functionality for estimating a specific fault in rolling stock. In addition, several diagnostic tools were used to identify faults in the bearing and a wheel. Case studies are incorporated that demonstrate the utility of condition monitoring technologies for identifying railway faults. It was found that trackside sensing technology is more economically suitable in contrast to onboard sensing technology. 

Alemi et al. [12] reviewed and categorized wheel defect detection methods. Basic categorization of present methods into in-service and in-workshop is done. Different types of 

13258 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

sensing techniques used to collect information are also discussed in detail with respect to the intended wheel’s fault detection. It is emphasized to research further on depreciating the time spent on numerous inspections and improvement in accuracy. To overcome the discontinued data problem due to inspection at the interval in wayside systems, further work on wayside system development using advanced techniques is suggested. However, this review does not cover the applicability and limitations of various commercial wayside systems currently in use around the globe. 

Considering the importance of sensing systems, Falamarzi et al. [13] presented a detailed introduction to the type of sensors and devices used in the CMS for railway inspection. A thorough investigation of the non-destructive testing (NDT) sensors such as accelerometer transducers, optical lasers, cameras, and mechanical sensors is presented. Correspondingly, the capabilities of CMS, trolleys, Track Recording Vehicles (TRV), and hi-rail vehicles, which are among vital inspection devices, are also studied. Future prospects regarding the deployment of smartphones as compact devices for inspection are discussed. Smartphones are equipped with an Inertial Measurement Unit (IMU) and a camera. They have been used as data acquisition devices for passenger coaches for track comfort analysis. However, a smartphone’s usage as a sensor probe has many limitations for fault detection purposes, especially for wheel fault diagnosis. Since the wayside installation of smartphones for acquiring fault data via IMUs is impractical. However, smart AI apps could be developed to classify faults in a workshop setting. On the other hand, the usage of drones has also been explored as a track monitoring device. 

More recently, Liu et al. [14] reviewed applications of visual inspection techniques and systems in the railway industry. Various applications of image processing and machine vision for the inspection of railway tracks, rolling stock, and other static infrastructure such as pantograph-catenary networks are reviewed in detail. The importance of further development of machine vision-based systems for inspection, especially for rolling stock is stressed. 

As observed from the aforementioned literature, the wayside CMS provides an economical way of inspection and fault diagnosis. Researchers and developers working in this domain require precise information and guidelines for wayside systems to get promptly acquainted and furnish their ideas for new developments. Considering the importance of wayside monitoring for railway wheels, this paper critically reviews the techniques extensively used for effective wheel fault diagnosis. It reports and discusses the current trends aimed at improving the performance of railway systems. It also describes future trends and challenges in this field and how advancements in methods can benefit railway systems. In addition, a comprehensive survey of the commercially available devices for wayside inspection is presented. The survey of the commercial devices could assist researchers to design and develop better products for railway applications. 

**==> picture [78 x 14] intentionally omitted <==**

Compared to the existing reviews, this paper particularly reviews the wayside systems used for the condition monitoring of wheels, as the flowchart for the wayside condition monitoring system is shown in Figure 2. It depicts the generalized sequential flow for an automated inspection system of railway wheel faults. First the different NDT sensors are installed on trackside to capture the data which is later categorized into several railway wheel faults. These faults data are preprocessed before any condition monitoring algorithms are applied. Finally, an automated CMS is implemented to identify and assess the different types of railway wheel defects, their severity level, and predictive maintenance. The output of a CMS could be used in a variety of ways. Defect identification leads to the identification of the cause of defect occurrence and can help minimize the risk of defects occurring in the future. Moreover, CMSs help develop predictive maintenance strategies by providing a timely quantitative assessment of the rolling stock behavior. Additionally, it could be used to drive further intuition to perform a quantitative assessment to gain useful insights and suggest maintenance actions. 

**==> picture [243 x 182] intentionally omitted <==**

**FIGURE 2.** Flowchart for wayside CMS. 

To the best of the authors’ knowledge, such a comprehensive review of wayside monitoring of railway wheels does not exist in the literature. This review aims to provide a concise overview of the state-of-the-art techniques in wayside wheel CMS research and provide a roadmap guide for further research. The following are the core contributions of this review paper: 

1. It discusses the challenges associated with using each sensor type from a system design point of view such as deployment, installation, sensitivity, range of the sensors, and sophistication of processing techniques. 

2. For system designers and researchers, it provides a glimpse of the industrial systems in operation to provide a baseline for performance evaluation of new wayside systems. 

13259 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

## _A. TYPES OF FAULTS_ 

Railway wheels fail owing to various types of faults [15]. These faults are categorized more precisely into four groups: polygonization defects (periodic/non-periodic nonroundness), surface defects (scaled wheels, spalling, wheel flats, and cracks), sub-surface defects (Hardening, cracks, residual stress, shelling, and contamination), and profile defects (High flange, thin flange, wide flange, small flange angle, hollow wear, wheel diameter variation). Some defects are shown in Figure 3. These defects are the major source of damage to railway wheels, which are needed to be inspected. 

There are various causes for multiple types of wheel defect formation, which results in the derailment and catastrophic failure. Based on various causes, the mechanisms of forming recurrent wheel polygonization faults are mainly categorized into three groups: (1) thermoelastic instability, (2) occurrence of congenital vibration in vehicle and track system, and (3) initial defects of wheels [16]. 

**==> picture [242 x 182] intentionally omitted <==**

**FIGURE 3.** Different wheel defects; (a) polygonization defect; OOR, (b) surface defect, (c) sub-surface defect and (d) profile defect. 

The wheel undulation due to braking of the tread signifies the thermoelastic instability between the wheel tread and the cast iron blocks. The natural vibration induced in the wheelrail system including :(1) sliding vibration of the wheel-rail system, (2) lower bending of the wheelset, (3) P2 resonance, (4) self-excited frictional vibration of the wheel-rail interaction system, etc., reuslts in wheel polygonization formation. The initial defects of the wheel, such as wheel reprofiling, static and dynamic inequities, and inhomogeneous properties of the wheel material, are crucial factors affecting the origin and development of the Out-of-Round (OOR) wheel. The appearance of surface defects can occur mainly when sliding on the tracks in case wheels are seized. In railway applications, this phenomenon can lead to the formation of martensite at the edges of induced shells and happens due to rolling contact fatigue. Also, stress cycling at the crack tip is caused by multiple passes of rolling contact and extends the crack in a way perpendicular to surface creep [17]. In subsurface defects, fatigue failure of rolling contact is one of the major 

faults in railway wheels, caused by recurrent rolling contact with tracks. This fatigue failure is induced by internal defects such as non-metallic inclusions or blisters in the wheels. Nonmetallic inclusions in the metal are found on the surface of the rolling stock after peeling or abrasion [18]. Profile variations in the wheel are the result of the winding motion of the wheels on a straight path and the passage of the vehicle in curves on the track. 

The remainder of the paper is organized as follows: Section II reviews and classifies different types of wayside condition monitoring systems in terms of sensing methods. Section III reports and discusses various commercial CMS, and their architecture with monitoring capabilities. Section IV summarizes the limitations and challenges of existing condition monitoring and presents prospects for developing more efficient and robust way-side CMS for modern railways. 

## **II. SENSING SYSTEM** 

For the detection of railway wheel defects, NDT sensors are preferred to utilize such as mechanical sensors, accelerometer sensors, optical sensors, cameras, and other sensors. To evaluate the mechanical properties of a system or a component without giving rise to damage, NDT sensing comes in as an inspection technique of a wide group that is applied in industry. In railway system, different techniques and sensors are utilized, which includes Alternate Current Field Measurement (ACFM), radiography, Electro Magnetic Acoustic Transducers (EMATs), AE, Magnetic Flux Leakage (MFL), Eddy Current (EC), Ultrasonic Testing (UT), etc. [19]. These sensors can detect a wide range of faults, discussed in section I-A. Additionally, for predicting the lifespan of railway wheels and future failures, the data acquisition, and its prognosis can play a vital role in the railway system. Based on this, unexpected failures are detected by the condition monitoring approach. Wheels maintenance plan and its optimization by this approach can be more efficient for the prognosis of possible future failures. It has been established that 99% of all failures are the result of the degradation of a system expressed by certain indicators [20]. Hence, for processing and measuring these features, suitable types of sensors are essential. Parameters that cause failure or the effects of the resultant failure, both can be measured by a data acquisition system. For monitoring railway wheels, the presence of abnormalities and cracks are accessed by some sensors that are used directly on the wheels, and the output is obtained from the interaction of faulty wheels with the rail [21]. 

In the following sections, different types of sensors used in research for wayside detection of faulty wheels are described along with their capabilities and drawbacks: 

## _A. ULTRASONIC_ 

In the field of NDT methods, ultrasonic sensing is widely implemented. For conventional ultrasonic methods, the major disadvantage is that the overall check-up of rail-wheels 

13260 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

requires disassembling each part of the train by putting it outof-service, which is expensive and time-consuming. 

Nowadays, for wheel flats detection on-line techniques are commonly used, which include ultrasonic sensing. Brizuela et al. [22] presented and designed an innovative ultrasound method to quantify and detect flats formed on the surface of rolling railway wheels. To achieve this, Rayleigh waves are transmitted over a measuring rail, and variations in the Round-Trip-Time of Flights (RTOF) concerning ultrasound pulse and the contact point of the railway wheel allow quantifying, detecting, and analyzing the wheel flats. Comprehensive theoretical validation and experimental results on a test bench consisting of two-wheel flats of size 40 mm and 26 mm in length are presented. The drawback of this technique, regarding the measuring accuracy was influenced by the distance measurements, therefore it was challenging to detect the wheel-flats of the entire circumference of the rolling wheel accurately. 

Montinaro et al. [23] proposed a non-conventional approach for the inspection of train wheels using noncontact laser ultrasonic sensing. For the generation end, a pulsed IR Nd:YAG laser is used for the generation of wideband ultrasonic waves. On the receiving end, a noncontact ultrasonic wave is received by a laser interferometer, as can be visualized in Figure 4. This measured the distance between the inspected surface and interferometer (surface out-of-plane displacements) with the help of receiving system while overcoming the issues related to encumbrance. To assess the accuracy and reliability of their method and its validation, experimental investigation on detecting standardreproduced defects is conducted. It is shown that in comparison with the laser-based techniques their method has the advantage of being non-contact, avoiding the use of coupling techniques, and solving the accessibility and adaptability issues. 

Diagnosing wheel faults of electrical multiple units (EMU) presents a difficult challenge due to various noise interference caused by internal hazard defects of the rail. In this regard, Sun and Lu [24] developed an automated method of wheel fault detection, as shown in Figure 5, which is aided by a denoising algorithm to perform data quality enhancement. This technique consists of an efficient sine-type processing threshold function, which gives better results as compared to the classical wavelet hard/soft threshold function. Slowvariation compression processing is adopted to characterize this improved function. For a smooth transition from the soft to the hard threshold, there is a continuous decrease in the compression amount when wavelet coefficients increase continuously, and no compression processing is performed when the wavelet coefficients exceeded a certain value. The outcomes obtained from their experiment showed that in the ultrasonic echo data, noise can be suppressed by utilizing an improved threshold function. The method shows good accuracy, improves the signal-to-noise ratio, and for defect signal its waveform characteristics are retained which is 

**==> picture [78 x 14] intentionally omitted <==**

**==> picture [203 x 215] intentionally omitted <==**

**FIGURE 4.** (a) Schematic representation of the experimental setup, (b) laboratory setup [23]. 

**==> picture [222 x 274] intentionally omitted <==**

**FIGURE 5.** Effect comparison of noise reduction. (a) soft threshold denoising. (b) hard threshold denoising. (c) improved threshold denoising. (d) and complete flowchart for denoising algorithm [24]. 

conducive to identifying defects. However, the developed method focuses on sub-surface defect detection and ignores surface faults. The summarized techniques for ultrasonic sensing are shown in Table 1. 

13261 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 1.** Summarized reviews on ultrasonic sensing. 

**==> picture [308 x 45] intentionally omitted <==**

**==> picture [119 x 70] intentionally omitted <==**

**==> picture [489 x 52] intentionally omitted <==**

**==> picture [118 x 61] intentionally omitted <==**

## _B. STRAIN GAUGES_ 

For railway track and train components, wheel defects are harmful, and an important source of damage to the railway rolling stock and infrastructure. Because of this vibration, emissions and noise can also be generated and mitigating these are costly. Detection of wheels defect is achieved by utilizing a commercial wheel impact load detector (WILD) [25] based on CMS, which comprises a series of strain gauges. 

**==> picture [228 x 204] intentionally omitted <==**

**FIGURE 6.** The configuration of six sensors installed under the rail [26]. 

In this regard, Alemi et al. [26] proposed and validated the fusion technique with the help of lab tests to examine its applicability to detect wheel flats and non-roundness. This method 

**==> picture [242 x 128] intentionally omitted <==**

**FIGURE 7.** Multiple vertical wheel force measurements of a train wheel by the four sensors of one measurement bar [27]. 

gathered data from multiple sensors to re-create a new informative pattern, which provides an inclusive description of the condition of the wheels. Therefore, a testing rig consisting of a wheel, a circular rail, and a rotating arm is developed. Under the rail, six strain sensors have been installed symmetrically with 60-degree intervals over the rail circle to measure the rail strain by their system, as shown in Figure 6. Detection of several defects of the wheel including the out-of-round and flat wheels have been tested and validated with the results of fusion technique by providing informative patterns. 

To detect and classify defects of wheel automatically, Krummenacher et al. [27] proposed two machine learning techniques, based on the data collected with the aid of wheel load checkpoints (WLC). It measured the vertical force of the wheel by a sensor system installed permanently on the railway network. Four measurement bars 1m long with four 

13262 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**==> picture [488 x 242] intentionally omitted <==**

**FIGURE 8.** Schematic of a vehicle containing the damaged wheel [29]. 

strain gauges are attached per measurement bars in each WLC, as shown in Figure 7. Since two measurement bars on each side with the installation of 4 sensors, were estimated eight times at different wheel parts when each wheel passes over the WLC. Their method learns wheel defects of different types automatically and during normal operation, and predicts whether the wheel is defective or not. The first technique used a support vector machine algorithm for classifying time series data with novel features. The second technique utilized DL-based convolutional neural networks to learn features automatically from a 2-dimensional data representation or from time series data. Multiple datasets were constructed to evaluate the performance of their method for the defect types such as non-roundness, shelling, and flat spot. The performance on detecting wheel faults related to non-roundness and flat spot wheels is improved by employing a neural network approach and measurement system by modelling multi-sensor structure based on shift invariant networks and multiple instances learning. Further, their method lacks in predicting severity scores for the wheel defects and optimization for precision in the neural network model. 

Zhou et al. [28] designed a technique based on multisensor fusion for precise positioning and recognition of wheel flats. The spatial distribution of rail strain characteristics was simulated under different conditions of wheel flats which were analyzed by the use of the numerical method. Based on this, their method utilized a multi-sensor arrays layout scheme which is more efficient and effective in capturing the wheel flats response. For algorithm validation, wheel profiles that were inspected offline were fed into the numerical model to simulate multi-sensor array output data, and 

identification of the defective wheels was also conducted by this algorithm. The results of their offline inspection demonstrated that during railway wheel passage the algorithm can locate and detect the wheel flats accurately under complex conditions. 

Mosleh et al. [29] developed a multi-sensory layout scheme to detect the occurrence of wheel flats on freight and passenger train. It relies on the dynamic response of the train track with the aid of 3D numerical simulation for wheel flats detection. To assess the layout schemes’ sensitivity with respect to the type of sensors (accelerometer and strain gauge) and their installation position, defined acceleration, and shear measurement points. For input, 19 positions of the track are evaluated by considering the accelerations and shear values, as shown in Figure 8, and by envelop spectrum approach using the analysis of spectral kurtosis the wheel flats were identified. The accuracy of the system based on the detection of wheel flats with the influence of the sensors type and their position is analyzed. 

The summary of the techniques for strain gauge sensing is provided in Table 2. 

## _C. FIBER BRAGG GRATING_ 

For high-speed rail, defects that occur in wheel tread are very critical and challenging, as a deviation of a small radius in wheel defects may give rise to damage [30]. 

For monitoring the condition of the railway infrastructure, fiber optics cables play an important role, which is installed alongside the railway tracks. 

In this study, Liu and Ni [31] developed a method for track-side monitoring of wheel conditions based on Fiber 

13263 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 2.** Summarized reviews on strain gauge sensing. 

**==> picture [490 x 250] intentionally omitted <==**

Bragg Gratings (FBG). On the rail foot, two FBG strain gauge arrays are mounted for the way-side sensing system. These sensors at the paired rails get excited by-passing wheelsets and accordingly measure the dynamic strains. Each FBG array is 3 m in length to make sure of full coverage i.e., a little longer than the circumference of the wheel, for the detection of potential defects of the wheel tread. This detection algorithm is divided into three steps: 1. preprocessing of strain data with the help of a method for smoothing the data to eliminate the trends; 2. examining novel responses for the normalized data by outlier analysis; 3. identification of local defects on the extracted novel responses in step 2 with the aid of refined analysis. Liu et al. [32] in another study, investigated that the minor defects of the wheel can produce anomalies with lower amplitude in contrast with the effect of wheel load. Therefore, it is needed to extract the features based on defect-sensitive data by using advanced signal processing techniques. Keeping this in mind, the Bayesian blind source separation (BSS) technique is explored in which the response signal of rail is decomposed to get the components that have defect-sensitive features. Consequently, by analyzing anomalies based on Chauvenet’s criterion the potential defects are detected. Different speeds occupied by trains on a sensor-based rail track to monitor the condition of wheels, the deployment of FBG-based sensor array is shown in Figure 9. Their technique achieved adequate and acceptable accuracy results in the detection of wheel defects when the train occupied higher speed i.e., greater than 30 kph. Their algorithm also detects a small defect having a depth (radius deviation) of 0.05 mm or 0.06 mm successfully. 

**==> picture [242 x 161] intentionally omitted <==**

**FIGURE 9.** Deployment of FBG sensor array and configuration of the online monitoring system [31], [32]. 

For detecting and quantifying online dynamic wheel flats when trains reached high speed, Gao et al. [33] demonstrated and developed a novel detection system for wheel flats based on the reflective optical position sensor. Their system contains two sensors that are attached along each rail to estimate the impact of the wheel-rail force of the whole circumference with the help of detecting the collimated laser spot displacement, as shown in Figure 10. To establish a relationship quantitatively between the length of the wheel flat and the sensor signal, a vehicle-track coupling dynamics analysis model is developed. The multi-body dynamic method and element method are coupled together to achieve this. The effects of 

13264 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 3.** Summarized reviews on fiber bragg grating sensing. 

**==> picture [472 x 45] intentionally omitted <==**

**==> picture [482 x 54] intentionally omitted <==**

**==> picture [61 x 36] intentionally omitted <==**

**==> picture [400 x 36] intentionally omitted <==**

wheel flat lengths, load, train speed, as well as impact forces position were evaluated and simulated. The assessment of the system has been carried out through laboratory investigation, simulation, and field tests. 

Recently, Ni and Zhang [34] developed a Bayesian probabilistic technique for quantitative as well as online assessment of conditions of railway wheels with the use of wayside distributed FBG strain-monitoring data. Their technique is a non-parametric and fully data-driven approach. Strain sensors with distributed FBG are mounted densely along rail length providing ease in the detection of minor defects of the wheel. In this implementation, each array of the sensor comprises 21 evenly spaced FBG gauges at intervals of 0.15 m on each single-track rail foot. To enable the rolling action sensing of the whole wheel tread circumference, the instrument covered the total range of 0.3 m. For the acquisition and processing of data, FBG sensors are linked via optical cables to an optical interrogator of high speed which is computer controlled. The responses of the dynamic strain of the rail track are measured during the train’s passage and are processed to obtain the values of the normalized cumulative distribution function. Later, a model of probabilistic reference about the sparse Bayesian learning technique is constructed. An innovative Bayesian null hypothesis significance testing with regards to intrinsic Bayes factor having scale-invariant data is performed. This approach is independent of the Jeffreys-Lindley paradox and is followed by newly monitored data gathered from possible 

defective wheels to detect faults in the wheel and to assess the condition of the wheel quantitatively. 

The summarized techniques for fiber optic sensing are given in Table 3. 

## _D. LASER AND CAMERA_ 

For the safe operation of railway vehicles, the geometric parameter of wheel diameter plays a significant role, which needs to be dynamically measured. The allowable error for dynamic measurement of wheel diameter is 0.3 mm [35]. The majority of the existing systems and methods based on dynamic measurements do not satisfy this requirement for high-speed vehicles. Considering this, Zheng et al. [35] for the first time developed a simplified method for measuring the diameter of train wheels precisely and dynamically by utilizing three one-dimensional laser displacement transducers (1D-LDTs) depicted in Figure 11. Factors affecting the accuracy of measurement were analyzed. As a key factor, rail deformation caused by the wheel-rail interaction force at low-speed (20 km/h) and high speed (300 km/h) was determined using a combination of finite element methods and multi-body dynamics. Moreover, field experiments are performed to confirm the performance of the enhanced measuring system. It is shown that repetitive error and system error measurement are both less than 0.3 mm. 

Pan et al. [36] developed a measurement system based on the fusion of multiple sensory data, as shown in Figure 12. 

13265 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**==> picture [227 x 275] intentionally omitted <==**

**FIGURE 10.** The schematic diagram of the installed sensor modules and the rail vertical deformation: (a) The installation location of the sensor; (b) The schematic diagram of the sensor; (c) The rail vertical deformation [33]. 

**==> picture [226 x 253] intentionally omitted <==**

**FIGURE 11.** Schematic of the measurement method using three 1D-LDTs: (a) setup; (b) schematic diagram [35]. 

Laser sensors acquire the cross profile of wheels when the measuring wheel passes over the rail. Measured profiles are divided into two groups. Later, measured wheel profiles are reconstructed with respect to one another for an entire 

profile-parameterized segment. Furthermore, to overcome the missing data in wheel profiles, the rigid alignment and multi-sensor data fusion technique is adopted. However, the measurement accuracy is improved by resisting the induced data related to error noise. With an entire cross profile of the wheel, accurate and reliable parameters of wheel size are gained. In addition, the feasibility and robustness of this approach are evaluated by real-time experiments, meeting the requirements of the railway industry. The actual experimental tests showed the strength and measurement accuracy dynamically. 

**==> picture [239 x 165] intentionally omitted <==**

**FIGURE 12.** Wheel size measurement system: (a) Schematic diagram of wheel section profile acquisition; (b) Schematic diagram of wheel profile diagnosis system [36]. 

Amu et al. [37] implemented the ML method to anticipate flaws in the wheel of the railway vehicle by utilizing the R-CNN algorithm. For detection, an algorithm based on a selective search method is used, which estimates the hierarchical assemblage of similar regions rapidly with high recall based on the size, texture, color, and shape compatibility of the wheel image. Image segmentation is performed to extract regions of interest (ROI). Later, ROIs are fed into a convolutional neural network (CNN) for classification. CNN identifies different defect types (type 1: thermal cracking defect, type 2: inherent defect, type 3: rolling contact fatigue cracks, and type 4: shattered rim defect) in railway wheels. Moreover, the precise location of the defects on the wheel tread is also determined. To evaluate the effectiveness of this process, multiple data sets are established by utilizing the train and test wheel images with 2D representations. 

For revolving structures like railway wheels, Sun et al. [38] proposed a framework for reconstructing symmetrical 3D revolving structures by making use of a pose-unconstrained profile of a normal section. The profile of a normal section with the aid of general 3D profiles of the section was obtained by a multi-line structured light-vision sensor. Firstly, a model is developed to evaluate the revolving axis that measures the profile of the normal section using relative points. After that, the model is embedded into an algorithm based on an iterative 

13266 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**==> picture [500 x 187] intentionally omitted <==**

**FIGURE 13.** Overview of their framework. (a) Acquiring general section profiles at different viewpoints. (b) Iterative optimization algorithm for each viewpoint: estimating the axis with corresponding points and calculating normal section profile with the axis. (c) Registering multiple partial normal section profiles to get a complete normal section profile [38]. 

scheme to improve the corresponding points and measure the profile of a normal section accurately. Simulation results showed that their algorithm is suitable for various shapes of 3D revolving structures and is vigorous against defects of local surfaces. Moreover, authors conducted real experiments to reconstruct the profile of the normal section with respect to the 3D wheel, as shown in Figure 13. The algorithm outcomes demonstrated the 0.065 mm of mean precision and 0.007 mm of repeatability with respect to standard deviation, which concludes the robustness of the sensor towards the position and poses. 

To measure the geometrical parameters of wheel tread dynamically and precisely in a complex environment, Ran et al. [39] developed a measurement system based on a line-structured light vision sensor. In this measurement system, skeleton extraction based on a sub-pixel extraction of the laser-stripe center is illustrated. Crucially decreasing the complex environmental lightning interference in the field and enhancing the accuracy of extraction. For further improving the stability and accuracy of measurements, the dynamic effect of anomaly error due to the measurement on the outcomes is analyzed. Field tests are conducted to verify the system’s performance. The outcomes showed that the stability and accuracy of measurements are enhanced after the correction of anomaly error, mainly for the value of flange slope and flange height. 

In railway vehicles, in-situ measurement of shaft diameter is considered to be an important factor. For this purpose, Tan et al. [40] established a shaft diameter-based measurement model by the formation of an ellipse through the intersection of the surface of the measured shaft and the light plane. Ellipse center coordinates and the normal vector of the light plane are acquired with respect to the coordinate system of the camera. Later, the oblique elliptic cone equation is established by getting the camera’s optical center and ellipse 

at the top and bottom respectively. Further, the shaft diameter measurement model is obtained through the established equation of the image plane and oblique elliptic cone, as illustrated in Figure 14. Lastly, with a lathe and the checkerboard calibration plate, the accuracy of the shaft diameter measurement model is tested. The model demonstrated accurate test results for instance when the diameter of the shaft is 36.162 mm, it reaches 1250 r/min of speed, with 0.019 mm of maximum average measured error. 

Emoto et al. [41] proposed an automated system for inspecting and monitoring the wheels’ condition by utilizing laser sensors and cameras for image data, as depicted in Figure 15. To simulate the actual condition of the wheel, experiments were performed on a 20% scaled wheel model. Firstly, for measuring profile, original CAD data was compared with respect to measured data. However, it was found that due to the laser beam reflection, obtaining the profile measurement entirely was difficult. Subsequently, computer vision was used for detecting the defect of the surface. Instead of segmentation or DL techniques, their scheme focused on the image processing method based on ROI extraction, and for reducing lighting effects, Contrast Limited Adaptive Histogram Equalization (CLAHE) filter was chosen to handle the issues such as inequalities of orbital reflectance and illumination. The relationship between the rate of detection and values of the accumulator confirmed its effectiveness for detecting surface defects on testing data of known defects. This development of the whole system brought the advancement in existing monitoring processes and accurate measurements which were done manually. 

For an accurate knowledge of the geometry profile feature of the tread wheel, a mechanism based on on-machine measurement by utilizing a 1D laser sensor is investigated by Liu et al. [42]. With the combination of specific tread profile morphology and laser sensor measurement model, the 

13267 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 4.** Summarized reviews on laser and camera sensing. 

**==> picture [489 x 287] intentionally omitted <==**

**==> picture [239 x 147] intentionally omitted <==**

**FIGURE 14.** Diameter measurement with the line structured light vision [40]. 

**==> picture [239 x 149] intentionally omitted <==**

**FIGURE 15.** Laser and vision sensors based automated inspection system [41]. 

correspondent on-machine measurement model of the wheel tread profile was developed. This measurement model was designed in accordance with the characteristics of curved and inclined profiles. Adaptive error correction was studied to enhance the complex profile measurement and to suppress the laser sensors measurement error. In the calibration and 

test experiments, more than 30% of the error was suppressed by this method. Finally, the laser-based measurement method was applied practically to the wheel tread profile measurement on a wheel-set lathe lying underfloor. These experiments not only enhance the accuracy of wheel geometry measurements but also improve the mechanical strength of 

13268 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

the machine tool, which is essential for railway vehicles to operate safely. 

The summarized techniques for laser and camera sensing are provided in Table 4. 

## _E. ACOUSTIC EMISSION_ 

The railway industry is concentrated on improving maintenance and remote condition monitoring of the rolling stock to lower the chances of failure. High operating speeds of trains may deteriorate an axle bearing leading to consequential derailments, loss of life, and serious disruption to network operations. For wayside fault diagnosis and condition monitoring of the wheelset bearing of a high-speed train, AE technology is appropriate to utilize because of its high sensitivity and high frequency [43], [44], [45]. 

In this direction, Amini et al. [46] discussed the consequences of measurements concerning wayside highfrequency AE, as shown diagrammatically in Figure 16, by producing artificial damage in the axle bearing of freight rolling stock in Long Marston, UK. Time spectral kurtosis (TSK) was used in the data analysis of AE. Also, the wheelset position identification is considered to lower the influence of ambient noise and ambiguity in the acquired results. Differentiating the signal from faulty bearings and non-Gaussian noises proved to be challenging for the data gathered from a real train. Conventional methods of analysis such as moving kurtosis and moving RMS, although have the capability of distinguishing the defects of axle bearing, are not ideally good when there is a low signal-to-noise ratio. Unnecessary noises occurred in the braking system, leading to an increase in kurtosis slightly and raising the RMS value, which results in incorrect fault identification. TSK, using time and frequency domains including kurtosis values for each frequency band, has been shown to increase the ability to identify the defects of bearing in such cases. Moreover, another source of noise that rises the amplitude of AE in the raw data is engine noise, which is eliminated by applying the threshold-based method to increase the ability to diagnose. From the obtained results, it is found that the time spectral kurtosis can distinguish the faults of axle bearing from the randomly generated noises by various sources which include the interaction of wheel-rail, braking, and variation in the speed of the train. 

Further, Aktas et al. [47] proposed a novel system based on Parametric-Constraint Optimization techniques for the detection of wheel flats, and this approach can be adapted by several CMS remotely. A novel ‘‘defect-score curve’’ was introduced to detect the wheel flats with an effective technique and efficient computation. The condition of the defect was recognized with the comparison of the estimated defectscore curve and threshold-curve interpreted by the false alarm rates and desired detection. Set a 100% false alarm rate, for good system performance but with a cost of increasing computational complexity and training time due to a large number of points in the defect-score curve. To evaluate the effectiveness of their method, numerous field tests at the 

**==> picture [78 x 14] intentionally omitted <==**

TCDD rail network were conducted on various train speeds and conditions of wheel flats and achieved an accuracy of up to 90 %. 

**==> picture [235 x 159] intentionally omitted <==**

**FIGURE 16.** Simplified outline of wayside installation configuration [46]. 

Furthermore, the interference of the wheel-rail rolling mechanism crucially affects the detection accuracy of wheel faults. To solve the aforementioned problem, Chang et al. [48] proposed a novel method of detection, as illustrated in Figure 17, which includes an Improved Synthesize Health Index (ISHI) with a Time-Adaptive Threshold (time-ATH). To acquire the information regarding faults from wheelgenerated signals, a complete set of features containing multiple types of features was extracted from AE signals. It calculates time-ATH for detecting the faulty wheel signals and lowers the impact of interference of wheel-rail rolling. Their method was fully validated in real datasets, and the outcomes determined that their method carry out a surpassed detection accuracy and detection rate. The summary of the techniques for AE sensing is given in Table 5. 

Moreover, reviewing several sensing systems shows the ongoing research activities in a particular domain, as depicted in Figure 18. 

## **III. COMMERCIAL WAYSIDE SYSTEMS FOR WHEEL FAULT DIAGNOSIS** 

The installation of sensors on the track for condition monitoring is intended to ensure the smooth operation of the rolling stock and eliminate the chances of sudden disruption of the railway track. However, there is less reliability in these systems, and in most cases, railway vehicles are checked at the depot before they go into service. Such inspections are prone to human error and are time-consuming. For many years, these techniques have been utilized, but the rise in damaged wheelsets caused by heavier loads, higher speeds, and altered operating conditions has led railway stakeholders to re-assess these inspection approaches. Considering the importance of efficient automated systems, Brickle et al. [49] reported on current and prospective automated systems that include rail-based sensors for wheel-set condition monitoring (WCM). Research authorized by the Rail Safety and Standard 

13269 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 5.** Summarized reviews on ae sensing. 

**==> picture [490 x 99] intentionally omitted <==**

**==> picture [212 x 238] intentionally omitted <==**

**FIGURE 17.** Experiment condition (a) system structure of AE experiment, (b) experiment equipment, (c) receiving sensor and mechanical clamp, and (d) pre-amplifier [48]. 

Board (RSSB) UK recognized the practical categories of automated WCM inspection systems as followed; wheel profile detectors, bogie performance detectors, wheel impact detectors, wheel tread condition monitoring detectors, acoustic bearing defect detectors, hot axle bearing and hot/cold wheel detectors, automatic vehicle identification systems, and brake disc condition detectors. 

Nowadays, real-time CMS is crucially required in railway inspection system that mainly comprises of intelligent sensing devices with the help of video cameras, lasers, etc. For WCM, several companies are working in this domain and have developed various commercial products, as shown in Figure 19, such inspection system products are: 

**==> picture [151 x 52] intentionally omitted <==**

**==> picture [223 x 208] intentionally omitted <==**

**FIGURE 18.** Research in several sensing systems. 

1. Trimble TreadView system [50] utilizes state-of-the-art 3D laser scanning and digital imaging technology to automatically scan the flange, wheel tread, and areas where the plate surface across the whole wheel circumference at mainline operating speed. Also, this system is designed to work in all weather and ambient light. 

2. For the wayside system, Trimble Wheel-View [51] provides wheel profile measurement information for dynamic trains automatically. It is an efficient and fastpaced program for improving the maintenance of wheel procedures and skipping/removing derailments due to worn-out wheels. It enhances the maintenance efficiency of the wheel by recognizing rapid maintenance procedures based on the use of wheel-wear standards and early detection of wheel damage. 

3. PSI Technics Automated Train Inspection System [52] provides an effective intelligent solution by the use of robotics and AI for the automatic inspection and 

13270 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 6.** Wayside inspection system. 

**==> picture [488 x 629] intentionally omitted <==**

13271 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 6.** _(Continued.)_ Wayside inspection system. 

**==> picture [443 x 632] intentionally omitted <==**

13272 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**TABLE 6.** _(Continued.)_ Wayside inspection system. 

**==> picture [451 x 632] intentionally omitted <==**

13273 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

**==> picture [237 x 316] intentionally omitted <==**

**FIGURE 19.** Inspection systems; (a) Trimble WheelView system [51], (b) Trimble TreadView system [50], (c) Track IQ [53], (d) MERMEC Train Monitoring Systems [54], (e) PSI Technics Automated Train Inspection System [52]. 

 - monitoring of trains quickly. The product includes the portals of the sensor which comprises image processing pipelines to document and record anomalies, damage, or wear to the train’s sides, roof, and structure of the train underbody. 

4. Track-IQ [53] has a reputation for being a professional supplier, manufacturer, and operator of wayside equipment for condition monitoring and data management systems in the railway industry. Products for Track IQ’s rolling stock monitoring include WCM, Bearing Acoustic Monitor (Rail-BAM), Bogie Geometry Monitor (BGM), and the vision-based systems for monitoring and evaluating the surface condition and wheel profile, components of the bogie, wagon sides, brakes, couplers, and trailer. Rail-BAM is a prognostic tool and can predict bearing faults even months before the actual occurrence. BGM uses proximity or position sensors to determine any anomalous kinematic behavior. 

5. MERMEC Train Monitoring Systems [54] majorly provide a wayside real-time solution for measuring wheel profile and diameter, brake inspection and measurement, pantograph inspection and measurement, and wheel surface defects detection. Different sensors are installed on the trackside for measur- 

ing essential wheel parameters. The sensing system includes lasers, video cameras, and an ad-hoc illuminating system. The system installation is feasible and can be installed on any railway infrastructure. It gives robust identification of defective components and provides the least track out-of-service for easiness. 

These inspection systems automatically inspect and monitor bogie brakes, bogie components, undercarriage parts, wagon sides, couplers, wheel profile, and surface condition for the prevention of derailment, maintenance scheduling, preventative maintenance, and to reduce rail and track damage caused by overly worn railway wheels. Inspection and measurement features of some commercialization devices for automated inspection and safety operation for railway management systems are given in Table 6. 

## **IV. SUMMARY AND FUTURE DIRECTIONS** 

The design process of wayside systems is generally driven by the fault that it is intended to detect. The choice of sensors and communication between the wayside system and to control room, data processing techniques, and real-time inferencing, depends on the fault type being identified. In this paper, the wayside research is categorized based on its sensing end. However, other distinctions could be made in terms of algorithmic techniques for defect identification and gathering further insights to predict the effects of identified faults on railway operations. Strain gauge based systems such as WILD, and WLC in earlier years of their development used signal processing and estimation theory techniques to detect tread surface deformities. However, recently data fusion and ML-based techniques are being used for more coherent pattern recognition of different faults and have resulted in comparatively better results. On the other hand, ultrasonic and AE still use signal processing and estimation theory techniques such as advanced versions of wavelet transform and Bayesian probabilistic estimation techniques to identify a pattern in the time series data. Similarly, FBG-based research which is a rather new sensing paradigm is going in the same direction. Imaging sensors-based research in terms of algorithmic techniques could be further divided into wheel tread fault detection and wheel profile variations. Wheel tread fault detection techniques is using ML and DL-based systems. Profile measurement along with help from a laser input (due to the need for depth information) and 3D characteristics. For this, the required high operating speeds are kept simple on the algorithmic level and vary from system to system. 

Recently, DL has revolutionized the field of pattern recognition and information processing in general. Better time series and sequential data processing techniques such as gradient boosters [63] Long Short Term Memory (LSTM) [64] and Auto-Regressive models [65] could be used for more accurate feature extraction from ultrasound, strain gauge, FBG, and acoustic sensors’ data. On the other hand, there are several options available for fault identification from image data. Algorithms such as You Only Look Once (YOLO) provide fast and accurate real-time predictions and the effort 

13274 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

needed for their on-edge synthesis has been greatly reduced due to the presence of large, automated tools and software frameworks. DL examples present in the wayside research are very premature and other venues need to be explored for better fault detection results. For the wheel profile estimation, 3D information extraction from 2D data is a progressing field [66] which may replace the usage of an additional component such as lasers for aiding in the 3D information extraction. 

## **V. CHALLENGES** 

## _A. ECONOMIC VIABILITY_ 

Deployment of wayside systems greatly reduces componentrelated failure incidents [67] Report published by the Federal Railroad Administration (FRA) US determined that increased deployment of wayside detectors greatly reduced the number of component-related failure issues 

According to the FRA of the USA, every equipmentrelated railway accident cost financial damages of around 18300 USD on average. It is suggested in studies [68] that automated wayside systems will only fail to detect faults 5 in 100 times. 

For setting a rough reference point, consider the case example of Pakistan railways. Pakistan railways, from Aug 2018 to June 2019 reported 54 Accidents. Out of which 39 were equipment failure-related derailments [69]. This value may vary but it is safe to say that about 72% of accidents were due to equipment. From Aug 2018 to Dec 2019 Pakistan Railway lost 410 million in railway accidents [70]. 

If 72% of this cost (295.2 million) is due to equipmentrelated failure, then deployment of automated wayside inspection systems could have saved 95% (280 million) in just one and half years and the lives of 110 people who were unfortunate victims of these accidents. 

However, there is a need for region-based case studies to establish if wayside systems are economically viable to deploy for railway industries. 

## _B. DESIGN CHALLENGES FOR EARLY DIAGNOSIS_ 

## 1) SENSING END CHALLENGES 

Wayside systems are equipped with different types of sensors. WILD and Wheel Profile Measurement Systems (WPMS) are examples of such systems. Strain gauges, FBG sensors, and high-speed cameras equipped with laser sensors are typically used sensors in these systems [13]. However, vision sensors have a clear advantage over the other counterparts as strain gauges or FBG sensors need to be laid below the track. Hence, once installed these systems do not provide portability [14]. Vision sensor systems can be relocated from one position to another depending on the traffic flow and provide ease of monitoring. However, these systems need proper calibration before functioning. A single vision sensor based track-side system installed on a junction can monitor all the trains coming on different tracks [14]. 

Strain gauges are the commonly used sensors in wheel defect CMS. These sensors monitor the impacts of faulty 

**==> picture [78 x 14] intentionally omitted <==**

wheels over the rail and if the strain is above a certain threshold, then the wheel is dissembled and taken for an in-workshop assessment. However, strain gauges can only detect defects when they have become severe enough to cause impacts on the wheel and have already caused damage to rail infrastructure [71]. Hence, early detection is not possible with these sensors. Fiber-based sensing technology is a rather new sensing paradigm being adapted for wheel condition monitoring [31]. However, these sensors similar to strain gauges need to be laid under the rails and cannot be moved once installed. Ultrasonic and AE sensors are other types of sensors used in wayside inspection. However, the response speed is very slow and the vehicle needs to be slowed down to get more precise data [24]. On the other hand, high-speed cameras aided by laser sensors provide reliable, fast, and accurate information from the wayside about wheel profile and wheel tread defects. In addition to that, it also provides flexibility in terms of the portability of wayside systems [24], [38], [39], [72]. These sensors with proper calibration and aided by powerful algorithmic techniques such as DL could be deployed alone for early detection of wheel tread defects and variations in wheel profile. 

## 2) PROCESSING TECHNIQUES CHALLENGES 

In previous sections, it has already been discussed that vision sensors have a clear advantage including portability and early detection capability. However, defect identification from a moving target (wheel) is a challenging task in itself. It is hard to classify the naturally occurring faults from the image data since most of the time surface defects appear in conjunction with each other and it’s hard to visually distinguish them from one another. Since fault classification leads to the cause of the fault for the development of the prognostic system, it is necessary to distinctly identify fault types. Another challenge is the greatly varying light conditions in the surrounding environment. Visual inspection systems (VIS) for wheels need to have reflection, shadow, and motion blur tolerance for efficient functioning. VIS should also be able to capture the entire circumference of the wheel and needs to have the required field of view, frames per second, and working distance. Processing techniques should also satisfy the memory, latency, and throughput requirements under operational conditions. Apart from DL, advanced signal processing techniques such as Wavelet transform and Kalman filtering could be used as a preprocessing step to get more coherent data and deeper insights into the performance of vehicle operation. 

## _C. PROBLEMS, KNOWLEDGE GAPS, AND FUTURE SUGGESTIONS_ 

Traditional wayside systems for online condition monitoring of wheel profile and tread such as WILD are equipped with strain gauges [26], [27], [29]. These systems help identify faults when they are severe enough to put stress on the rails. However early detection of the faults is not possible through these systems. Additionally, these systems do not offer portability and are harder to deploy onsite. However, WILD is 

13275 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**

also one of the most deployed wayside system, and further research into using advanced signal processing and DL techniques for getting the most out of the current pool of deployed systems could be explored. This will help the industry upgrade its fault detection systems without bearing the infrastructural cost of new systems. FBG sensors are a new type of optical sensor recently being explored by researchers for wheel condition monitoring [28], [31], [32]. These sensors provide more resolution and sensitivity and enable the detection of faults early. However, similar to strain gauges these sensors also need to be laid under the rails and cannot be moved once installed. Further research could be potentially aimed toward the manufacturing of portable versions of FBG sensors to ease the installation process of these systems. Additionally, considering the high fidelity of data acquired by FBG sensors, further methods of estimating the useful life of the rolling equipment, and derailment risk factor could be developed. Vision sensors are very useful for the early detection of wheel tread faults coupled with machine vision and image processing [36], [72], [73]. Advanced algorithmic techniques for ROI segmentation, data quality enhancement and profile estimation are yet to be explored. DL techniques have revolutionized the field of pattern recognition in recent years and help extract useful features even from noisy or cluttered data. Another knowledge gap is the simultaneous consideration of wheel tread faults and geometric profile parameters. Since these are closely associated with one another, a more synergetic approach is needed to get more precise information about the wheel condition. 

## **CREDIT AUTHORSHIP CONTRIBUTION STATEMENT** 

Muhammad Zakir Sheih: data curation, conceptualization, methodology, validation, writing—original draft. Zeeshan Ahmed: data curation, methodology, writing— original draft. Bhawani Shankar Chowdhry: methodology, conceptualization, review, funding acquisition, supervision. Enrique Nava: manuscript improvement and revision, validation, and supervision. Tanweer Hussain: methodology, conceptualization, review, funding acquisition, supervision. Muhammad Aslam Uqaili: review, funding acquisition, supervision. Sanaullah Mehran: editing, visualization, data collection, proofread, validation. Dileep Kumar: editing, visualization, data collection, validation. Ali Akbar Shah: proofread, data collection. 

## **CONFLICT OF INTEREST** 

The authors declare that they have no conflict of interest or known competing financial interests or personal relationships that could have appeared to influence the work reported in this article. 

## **REFERENCES** 


- [1] T. A. Zucarelli, M. A. Vieira, L. A. M. Filho, D. A. P. Reis, and L. Reis, ‘‘Failure analysis in railway wheels,’’ _Proc. Struct. Integrity_ , vol. 1, pp. 212–217, Jan. 2016, doi: 10.1016/j.prostr.2016.02.029. 


- [2] G. Zhang and R. Ren, ‘‘Study on typical failure forms and causes of high-speed railway wheels,’’ _Eng. Failure Anal._ , vol. 105, pp. 1287–1295, Nov. 2019, doi: 10.1016/j.engfailanal.2019.07.063. 


- [3] P. Kundu, A. Darpe, and S. P. Singh, ‘‘A review on condition monitoring technologies for railway rolling stock,’’ in _Proc. 4th Eur. Conf. Progn. Heal. Manag. Soc._ , vol. 4, no. 1, 2018, pp. 1–15. [Online]. Available: https://papers.phmsociety.org/index.php/phme/article/view/250 


- [4] E. Bernal, M. Spiryagin, and C. Cole, ‘‘Onboard condition monitoring sensors, systems and techniques for freight railway vehicles: A review,’’ _IEEE Sensors J._ , vol. 19, no. 1, pp. 4–24, Jan. 2019, doi: 10.1109/JSEN.2018.2875160. 


- [5] K. Mal, I. Hussain, T. D. Memon, D. Kumar, and B. S. Chowdhry, ‘‘Modern condition monitoring systems for railway wheel set dynamics: Performance analysis and limitations of existing techniques,’’ _Sir Syed Univ. Res. J. Eng. Technol._ , vol. 12, no. 1, pp. 31–41, Mar. 2022, doi: 10.33317/ssurj.419. 


- [6] N. Bešinović, ‘‘Resilience in railway transport systems: A literature review and research agenda,’’ _Transp. Rev._ , vol. 40, no. 4, pp. 457–478, 2020, doi: 10.1080/01441647.2020.1728419. 


- [7] A. Jaraš¯unien˙e, G. Sinkevičius, and A. Mikalauskait˙e, ‘‘Analysis of application management theories and methods for developing railway transport,’’ _Proc. Eng._ , vol. 187, pp. 173–184, Jan. 2017, doi: 10.1016/j.proeng.2017.04.363. 


- [8] M. Asplund, ‘‘Wayside condition monitoring system for railway wheel profiles: Applications and performance assessment,’’ Ph.D. dissertation, Dept. Civil, Envirment. Natural Resour. Eng., Operation, Maintenance Acoust., Luleå Univ. Technol., Luleå, Sweden, 2016. [Online]. Available: https://www.diva-portal.org/smash/record.jsf?pid= diva2%3A1044611&dswid=-6084 


- [9] M. R. M. Asplund and S. Famurewa, ‘‘Condition monitoring and e- maintenance solution of railway wheels,’’ _J. Qual. Maint. Eng. Artic. Inf._ , vol. 20, no. 3, p. 16, 2014. 


- [10] Y. Zang, W. Shangguan, B. Cai, H. Wang, and M. G. Pecht, ‘‘Methods for fault diagnosis of high-speed railways: A review,’’ _Proc. Inst. Mech. Eng., O, J. Risk Rel._ , vol. 233, no. 5, pp. 908–922, Oct. 2019, doi: 10.1177/1748006X18823932. 


- [11] R. W. Ngigi, C. Pislaru, A. Ball, and F. Gu, ‘‘Modern techniques for condition monitoring of railway vehicle dynamics,’’ _J. Phys., Conf. Ser._ , vol. 364, May 2012, Art. no. 012016, doi: 10.1088/1742-6596/364/1/012016. 


- [12] A. Alemi, F. Corman, and G. Lodewijks, ‘‘Condition monitoring approaches for the detection of railway wheel defects,’’ _Proc. Inst. Mech. Eng., F, J. Rail Rapid Transit_ , vol. 231, no. 8, pp. 961–981, Sep. 2017, doi: 10.1177/0954409716656218. 


- [13] A. Falamarzi, S. Moridpour, and M. Nazem, ‘‘A review on existing sensors and devices for inspecting railway infrastructure,’’ _J. Kejuruter._ , vol. 31, no. 1, pp. 1–10, 2019. [Online]. Available: http://journalarticle.ukm.my/14293/ 


- [14] S. Liu, Q. Wang, and Y. Luo, ‘‘A review of applications of visual inspection technology based on image processing in the railway industry,’’ _Transp. Saf. Environ._ , vol. 1, no. 3, pp. 185–204, 2019, doi: 10.1093/tse/tdz007. 


- [15] M. Asplund, M. Palo, S. Famurewa, and M. Rantatalo, ‘‘A study of railway wheel profile parameters used as indicators of an increased risk of wheel defects,’’ _Proc. Inst. Mech. Eng., F, J. Rail Rapid Transit_ , vol. 230, no. 2, pp. 323–334, 2014, doi: 10.1177/0954409714541953. 


- [16] G. Tao, Z. Wen, X. Jin, and X. Yang, ‘‘Polygonisation of railway wheels: A critical review,’’ _Railway Eng. Sci._ , vol. 28, no. 4, pp. 317–345, Dec. 2020, doi: 10.1007/s40534-020-00222-x. 


- [17] E. Magel and J. Kalousek, ‘‘Identifying and interpreting wheel defects,’’ in _Proc. IHHA Conf._ , 1996, pp. 5.8–5.21. 


- [18] T. Kato, T. Fujimura, S. Hiramatsu, and Y. Yamamoto, ‘‘Subsurface crack propagation from internal defect in rolling contact fatigue of railway wheel steel,’’ _Mater. Trans._ , vol. 62, no. 2, pp. 185–190, Feb. 2021, doi: 10.2320/matertrans.Z-M2020860. 


- [19] M. Gupta, M. A. Khan, R. Butola, and R. M. Singari, ‘‘Advances in applications of non-destructive testing (NDT): A review,’’ _Adv. Mater. Process. Technolog._ , vol. 8, no. 2, pp. 2286–2307, 2021, doi: 10.1080/2374068X.2021.1909332. 


- [20] R. Ahmad and S. Kamaruddin, ‘‘An overview of time-based and conditionbased maintenance in industrial application,’’ _Comput. Ind. Eng._ , vol. 63, no. 1, pp. 135–149, Aug. 2012, doi: 10.1016/j.cie.2012.02.002. 


- [21] J. Veldman, H. Wortmann, and W. Klingenberg, ‘‘Typology of condition based maintenance,’’ _J. Quality Maintenance Eng._ , vol. 17, no. 2, pp. 183–202, May 2011, doi: 10.1108/13552511111134600. 


- [22] J. Brizuela, C. Fritsch, and A. Ibáñez, ‘‘Railway wheel-flat detection and measurement by ultrasound,’’ _Transp. Res. C, Emerg. Technol._ , vol. 19, no. 6, pp. 975–984, Dec. 2011, doi: 10.1016/j.trc.2011.04.004. 

13276 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 


- [23] N. Montinaro, G. Epasto, D. Cerniglia, and E. Guglielmino, ‘‘Laser ultrasonics inspection for defect evaluation on train wheel,’’ _NDT E Int._ , vol. 107, Oct. 2019, Art. no. 102145, doi: 10.1016/j.ndteint.2019.102145. 


- [24] Z. Sun and J. Lu, ‘‘An ultrasonic signal denoising method for EMU wheel trackside fault diagnosis system based on improved threshold function,’’ _IEEE Access_ , vol. 9, pp. 96244–96256, 2021, doi: 10.1109/ACCESS.2021.3093482. 


- [25] O. Lunys, S. Dailydka, S. Steiš¯unas, and G. Bureika, ‘‘Analysis of freight wagon wheel failure detection in Lithuanian railways,’’ _Proc. Eng._ , vol. 134, pp. 64–71, Jan. 2016, doi: 10.1016/j.proeng.2016.01.040. 


- [26] A. Alemi, Y. Pang, and G. Lodewijks, ‘‘Experimental validation of multisensor data fusion model for railway wheel defect identification,’’ in _Proc. 4th Eur. Conf. Prognostics Health Manage. Soc._ , 2018, pp. 2–7. 


- [27] G. Krummenacher, C. S. Ong, S. Koller, S. Kobayashi, and J. M. Buhmann, ‘‘Wheel defect detection with machine learning,’’ _IEEE Trans. Intell. Transp. Syst._ , vol. 19, no. 4, pp. 1176–1187, Apr. 2018, doi: 10.1109/TITS.2017.2720721. 


- [28] C. Zhou, L. Gao, H. Xiao, and B. Hou, ‘‘Railway wheel flat recognition and precise positioning method based on multisensor arrays,’’ _Appl. Sci._ , vol. 10, no. 4, p. 1297, Feb. 2020, doi: 10.3390/app10041297. 


- [29] A. Mosleh, P. A. Montenegro, P. A. Costa, and R. Calçada, ‘‘Railway vehicle wheel flat detection with multiple records using spectral kurtosis analysis,’’ _Appl. Sci._ , vol. 11, no. 9, p. 4002, Apr. 2021, doi: 10.3390/app11094002. 


- [30] X. Z. Liu, _Development of Online Wheel Defect Detection Methods for High-Speed Trains_ . Hong Kong: Hong Kong Polytechnic Univ., 2018. 


- [31] X. Z. Liu and Y. Q. Ni, ‘‘Wheel tread defect detection for high-speed trains using FBG-based online monitoring techniques,’’ _Smart Struct. Syst._ , vol. 21, no. 5, pp. 687–694, 2018, doi: 10.12989/sss.2018.21.5.687. 


- [32] X.-Z. Liu, C. Xu, and Y.-Q. Ni, ‘‘Wayside detection of wheel minor defects in high-speed trains by a Bayesian blind source separation method,’’ _Sensors_ , vol. 19, no. 18, p. 3981, Sep. 2019, doi: 10.3390/s19183981. 


- [33] R. Gao, Q. He, Q. Feng, and J. Cui, ‘‘In-service detection and quantification of railway wheel flat by the reflective optical position sensor,’’ _Sensors_ , vol. 20, no. 17, pp. 1–18, 2020, doi: 10.3390/s20174969. 


- [34] Y.-Q. Ni and Q.-H. Zhang, ‘‘A Bayesian machine learning approach for online detection of railway wheel defects using track-side monitoring,’’ _Struct. Health Monitor._ , vol. 20, no. 4, pp. 1536–1550, Jul. 2021, doi: 10.1177/1475921720921772. 


- [35] F. Zheng, B. Zhang, R. Gao, and Q. Feng, ‘‘A high-precision method for dynamically measuring train wheel diameter using three laser displacement transducers,’’ _Sensors_ , vol. 19, no. 19, p. 4148, Sep. 2019, doi: 10.3390/s19194148. 


- [36] X. Pan, Z. Liu, and G. Zhang, ‘‘On-site reliable wheel size measurement based on multisensor data fusion,’’ _IEEE Trans. Instrum. Meas._ , vol. 68, no. 11, pp. 4575–4589, Nov. 2019, doi: 10.1109/TIM.2018.2890328. 


- [37] D. Amu, P. Sushma, A. Sandhiya, and S. Shahena, ‘‘Detection of wheel discoloration using R-CNN,’’ _Int. Res. J. Eng. Technol._ , vol. 7, no. 8, pp. 4877–4884, 2020, https://d1wqtxts1xzle7.cloudfront.net/64738874/ IRJET_V7I8837-libre.pdf?1603347965=&response-content-disposition= inline%3B+filename%3DIRJET_Detection_of_Wheel_Discoloration_u. pdf&Expires=1662367455& Signature=gnUGslOdxS3H398~k76J5zdAC gkeEMJCAST5ltPdlcLY~DlY 


- [38] J. Sun, Z. Zhang, and J. Zhang, ‘‘Reconstructing normal section profiles of 3-D revolving structures via pose-unconstrained multiline structuredlight vision,’’ _IEEE Trans. Instrum. Meas._ , vol. 70, pp. 1–12, 2021, doi: 10.1109/TIM.2020.3024339. 


- [39] Y. Ran, Q. He, Q. Feng, and J. Cui, ‘‘High-accuracy on-site measurement of wheel tread geometric parameters by line-structured light vision sensor,’’ _IEEE Access_ , vol. 9, pp. 52590–52600, 2021, doi: 10.1109/ACCESS.2021.3070018. 


- [40] Q. Tan, Y. Kou, J. Miao, S. Liu, and B. Chai, ‘‘A model of diameter measurement based on the machine vision,’’ _Symmetry_ , vol. 13, no. 2, pp. 1–15, 2021, doi: 10.3390/sym13020187. 


- [41] T. Emoto, A. A. Ravankar, A. Ravankar, T. Emaru, and Y. Kobayashi, ‘‘Automatic inspection of railcar wheels using laser and image sensor,’’ in _Proc. 60th Annu. Conf. Soc. Instrum. Control Eng. Jpn., (SICE)_ , 2021, pp. 1282–1287. 


- [42] F. Liu, L. Liang, C. Hou, G. Xu, D. Liu, B. Zhang, L. Wang, X. Chen, and H. Du, ‘‘On-machine measurement of wheel tread profile with the 1-D laser sensor,’’ _IEEE Trans. Instrum. Meas._ , vol. 70, pp. 1–11, 2021, doi: 10.1109/TIM.2021.3122186. 

**==> picture [78 x 14] intentionally omitted <==**


- [43] A. Anastasopoulos, K. Bollas, D. Papasalouros, and D. Kourousis, ‘‘Acoustic emission on-line inspection of rail wheels,’’ _Proc. 29th Eur. Conf. Acoust. Emiss. Test._ , vol. 28, 2010, pp. 1–8. 


- [44] G. Xu, D. Hou, H. Qi, and L. Bo, ‘‘High-speed train wheel set bearing fault diagnosis and prognostics: A new prognostic model based on extendable useful life,’’ _Mech. Syst. Signal Process._ , vol. 146, Jan. 2021, Art. no. 107050, doi: 10.1016/j.ymssp.2020.107050. 


- [45] D. Hou, H. Qi, C. Wang, and D. Han, ‘‘High-speed train wheel set bearing fault diagnosis and prognostics: Fingerprint feature recognition method based on acoustic emission,’’ _Mech. Syst. Signal Process._ , vol. 171, May 2022, Art. no. 108947, doi: 10.1016/j.ymssp.2022.108947. 


- [46] A. Amini, M. Entezami, Z. Huang, H. Rowshandel, and M. Papaelias, ‘‘Wayside detection of faults in railway axle bearings using time spectral kurtosis analysis on high-frequency acoustic emission signals,’’ _Adv. Mech. Eng._ , vol. 8, no. 11, pp. 1–9, 2016, doi: 10.1177/1687814016676000. 


- [47] M. Aktas, E. H. Gunel, P. Yilmazer, and T. Akgun, ‘‘Detection of wheel flatten defect on the moving train with acoustic emission sensor,’’ in _Proc. IEEE 29th Annu. Int. Symp. Pers., Indoor Mobile Radio Commun. (PIMRC)_ , Sep. 2018, pp. 386–390, doi: 10.1109/PIMRC.2018.8580762. 


- [48] Y. Chang, X. Zhang, C. Lin, J. Liu, and Y. Shen, ‘‘An efficient method for wheel-flattened defects detection based on acoustic emission technique,’’ _IEEE Trans. Ultrason., Ferroelectr., Freq. Control_ , vol. 69, no. 2, pp. 843–853, Feb. 2022, doi: 10.1109/TUFFC.2021.3138197. 


- [49] C. P. Barrie Brickle, R. Morgan, E. Smith, and J. Brosseau. (2008). _Identification of Existing and New Technologies for Wheelset Condition Monitoring. Report for the Rail Safety and Standards Board (RSSB). Report no. T607_ . [Online]. Available: http://www.rssb.co.uk 


- [50] (2018). _Trimble Treadview System_ . [Online]. Available: https://rail. trimble.com/treadview/ 


- [51] (2018). _Trimble WheelView System_ . [Online]. Available: https://rail.trimble.com/event/wheelview/ 


- [52] _PSI Technics Automated Train Inspection System_ . Accessed: Aug. 16, 2022. [Online]. Available: https://www.psi-technics.com/EN/ServicesProducts/Automated-TrainInspection/automated-train-inspectioninspect.php 


- [53] _Track IQ RailBAM Wayside Condition Monitoring System_ . [Online]. Available: https://www.trackiq.net/ 


- [54] _Train Monitoring Systems—MERMEC_ . Accessed: Jan. 14, 2020. [Online]. Available: https://www.mermecgroup.com/measuring-trains-br-andsystems/train-monitoring/87/wheel-parameters.php 


- [55] _Apna Technolo-Gies & Solutions (ApnaTech)_ . Accessed: Sep. 10, 2022. [Online]. Available: https://apnatech.com/ 


- [56] _Hegenscheidt MFD—Diagnostic System for Wheelsets ARGUS_[®] _II_ . Accessed: Sep. 10, 2022. [Online]. Available: https://www.hegenscheidtmfd.com/en/railway-technology/argus-ii-wheelset-diagnostics-system/ 


- [57] _TBOGI-HD: Bogie Condition Monitor and Hunting Detector for Freight and Heavy Haul Railways | WID_ . Accessed: Sep. 10, 2022. [Online]. Available: https://www.wid.ca/tbogi-hd 


- [58] _Nagory Foster Private Limited—Hunting Truck Detector_ . Accessed: Sep. 10, 2022. [Online]. Available: http://www.nagoryfoster.com/ Hunting_Truck_Detector.asp 


- [59] _Transportation Technological Center, Inc. (TTCI)—TADS_[®] _Trackside Acoustic Detection System_ . Accessed: Sep. 10, 2022. [Online]. Available: https://www.ttci.tech/ 


- [60] (2014). _Ibérica Tecnológica En Sistemas De Seguridad Ferroviarios, Sl, (ITSS) Pegasus Hot Wheel Detector_ . [Online]. Available: https://www.itss.tech/pegasus-habd-hwd 


- [61] _Voestalpine Railway Systems—PHOENIX HBD/HWD Hot Box and Hot Wheel Detection_ . Accessed: Sep. 10, 2022. [Online]. Available: https://www.voestalpine.com/railway-systems/en/products/phoenixmds-hbd-hwd-hot-box-detection-and-hot-wheel-detection/ 


- [62] _Southern Technologies Corporation—SMARTSCAN NG_ . Accessed: Sep. 10, 2022. [Online]. Available: https://www.southern-tech.com/ products/item/smartscan-ng 


- [63] C. Bentéjac, A. Csörgő, and G. Martínez-Muñoz, ‘‘A comparative analysis of gradient boosting algorithms,’’ _Artif. Intell. Rev._ , vol. 54, no. 3, pp. 1937–1967, 2020. 


- [64] Y. Yu, X. Si, C. Hu, and Z. Jianxun, ‘‘A review of recurrent neural networks: LSTM cells and network architectures,’’ _Neural Comput._ , vol. 31, no. 7, pp. 1235–1270, Jul. 2019. 


- [65] S. Bond-Taylor, A. Leach, Y. Long, and C. G. Willcocks, ‘‘Deep generative modelling: A comparative review of VAEs, GANs, normalizing flows, energy-based and autoregressive models,’’ 2021, _arXiv:2103.04922_ . 

13277 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

**==> picture [78 x 14] intentionally omitted <==**


- [66] X. Zhao, F. Ma, D. Güera, Z. Ren, A. G. Schwing, and A. Colburn, ‘‘Generative multiplane images: Making a 2D GAN 3D-aware,’’ in _Proc. Eur. Conf. Comput. Vis._ , 2022, pp. 18–35. 


- [67] S. P. Singh, ‘‘Effectiveness of wayside detector technologies on train operation safety,’’ FRA, Washington, DC, USA, Tech. Rep. DOT/ FRA/ORD-22/19, 2022. Accessed: Sep. 10. 2022. [Online]. Available: https://railroads.dot.gov/elibrary/effectiveness-wayside-detectortechnologies-train-operation-safety 


- [68] B. W. Schlake, C. P. L. Barkan, and J. R. Edwards, ‘‘Impact of automated inspection technology on unit train performance,’’ in _Proc. Joint Rail Conf._ , Jan. 2010, pp. 281–288, doi: 10.1115/JRC2010-36258. 


- [69] (2019). _Pakistan Train Fire: Are Accidents at a Record High BBC News_ . [Online]. Available: https://www.bbc.com/news/world-asia-50252409 


- [70] (2020). _Railways Suffers Rs410m Loss in Train Accidents_ . [Online]. Available: https://www.bbc.com/news/world-asia-50252409 


- [71] M. de Almeida Costa, J. P. de Azevedo Peixoto Braga, and A. R. Andrade, ‘‘Assessing the performance of different devices in railway wheelset inspection,’’ _Measurement_ , vol. 165, Dec. 2020, Art. no. 108145, doi: 10.1016/j.measurement.2020.108145. 


- [72] A. Trilla, J. Bob-Manuel, B. Lamoureux, and X. Vilasis-Cardona, ‘‘Integrated multiple-defect detection and evaluation of rail wheel tread images using convolutional neural networks,’’ _Int. J. Prognostics Health Manage._ , vol. 12, no. 1, pp. 1–19, May 2021, doi: 10.36001/ijphm.2021.v12i1.2906. 


- [73] W. Zhang, Y. Zhang, J. Li, X. Gao, and L. Wang, ‘‘The defects recognition of wheel tread based on linear CCD,’’ in _Proc. IEEE Far East Forum Nondestruct. Eval./Testing_ , Jun. 2014, pp. 302–307, doi: 10.1109/FENDT.2014.6928285. 

MUHAMMAD ZAKIR SHAIKH received the bachelor’s degree in electronics and the master’s degree in electronic systems engineering from the Mehran University of Engineering and Technology, Jamshoro, in 2013 and 2015, respectively. He is currently pursuing the Ph.D. degree, with a focus on fault diagnosis of rail wheel profile via deep learning. He is also working as a Lecturer and Business Development Manager with the National Center for Robotics and Automation-Condition Monitoring Systems Laboratory, Mehran University of Engineering and Technology. He is also working as the President of QS World Merit Pakistan to implement sustainable development goals. He has represented Pakistan and Mehran University at United Nation’s HQ, New York, and has won the International Competition ‘‘I am a Mover, Shaker and Change-Maker.’’ Besides that, he has already worked as a Research Associate on a project titled ‘‘Design and Implementation of Intelligent Energy Efficient Industrial Process Control System Using Conveyor Belts via Robotic Arm,’’ a fully funded project of Pakistan Science Foundation. He has been declared as the 2011 Star Laureate for the outstanding achievements in the field of science and technology by South Asian Publications. He has broken historic record by getting two gold medals in the 27th IEEEP All Pakistan Students Seminar, by getting the first position in one research paper and the second position in another paper. 

ZEESHAN AHMED received the B.E. degree (Hons.) in electronics engineering from the Mehran University of Engineering and Technology, Jamshoro. He did many projects during his bachelor’s program. He led his group in the final year project. During his bachelor’s degree, he has six months of Trainee Engineer experience under the Program ‘‘Benazir Bhutto Shaheed Human Resources Research and Development Board (SBSHRRDB).’’ He also worked as a Junior Data Scientist at Covolv.ai, for six months, where he developed different python-based tools for monitoring employees activities, and his responsibilities included 3D point cloud data annotation, data analysis, and predictive modeling of complex 3D LiDAR data. He is currently a Research Assistant with the National Center for Robotics and Automation-Condition Monitoring Systems Laboratory, Mehran UET. He has authored or coauthored multiple international and national research publications. His research interests include artificial intelligence, machine learning, deep learning, and computer vision. He is a member of QS World Merit Pakistan for implementing sustainable development goals. 

BHAWANI SHANKAR CHOWDHRY (Senior Member, IEEE) is currently a Distinguished National Professor and the Former Dean of the Faculty of Electrical Electronics and Computer Engineering, Mehran University of Engineering and Technology, Jamshoro, Pakistan. His list of research publications crosses more than 60 in national and international journals, such as IEEE and ACM proceedings, in the areas of intelligent instrumentation, WSN, embedded systems, simulation and modeling, internet technologies, and smart civil structures. He is a member of various professional bodies, including the immediate past Chairperson IEEE Karachi Section, Region10 Asia/Pacific; a fellow of IEP and IEEEP; and a Senior Member of ACM Inc., USA. He organized several international conferences, including IMTIC 2008, IMTIC 2012, IMTIC 2013, IMTIC 2015, IMTIC 2018, WSN4DC 2013, IEEE SCONEST, and IEEE PSGWC 2013. He was the Track Chair of the Global Wireless Summit (GWS 2014). He was the Chief Organizer and the Co-Chair of GCWOC 2016 and GCWOC 2017, Malaga, Spain. In 2015, he also organized a twoweek ICTP/UNESCO Regional Workshop on ‘‘FPGA Based Instrumentation Systems,’’ fully funded by the Abdus Salam ICTP/ UNESCO for the first time in Pakistan, in which scientists from 27 regional countries were invited for participation. 

ENRIQUE NAVA BARO received the Ingeniero de Telecomunicación (B.S. and M.S.) degrees and the Ph.D. degree in engineering from the Universidad Politécnica de Madrid (UPM), Madrid, Spain, in 1988 and 1992, respectively. From 1990 to 1994, he was an Assistant Professor at the Universidad de Málaga (UMA), Spain, where he has been an Associate Professor, since 1994. He was a Visiting Professor at The University of Chicago, Chicago, IL, USA, in 2000; RWTH Aachen, Germany, in 2011 and 2014; UNSW@ADFA Canberra, Australia, in 2012; and LAPIUPB Romania (many one-week short stays). He is currently the Head of the Multidisciplinary Research Group on Medical Image Processing Techniques. He has participated as a Researcher in two Marine Science Campaigns, onboard the Miguel Oliver Oceanographic Ship, in 2015. He is promoting and contributing to a closer collaboration between UMA and many universities and institutions in Asian countries, with special focus in Pakistan, where he was appointed as a member of the Pakistan Engineering Council International Advisory Board (PEC-IAB), from 2020 to 2022. His research interests include applied signal and image processing, and numerical methods, working in multidisciplinary teams with researchers from others fields, such as radiology, human physiology, analytical chemistry, mechanical engineering, phonetics, acoustics, entomology, and marine science. He is a member of the Institute for Ocean Engineering (IIO). 

13278 

VOLUME 11, 2023 

M. Z. Shaikh et al.: State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels 

TANWEER HUSSAIN (Member, IEEE) received the B.Eng. degree in mechanical engineering and the Postgraduate Diploma degree in manufacturing engineering from the Mehran UET, Jamshoro, and the Ph.D. degree in mechanical engineering from the University of Nottingham, U.K., in 2012. During his Ph.D. degree, he was involved in research projects, in collaboration with Rolls Royce, U.K., for aero-engine assembly design. During the start of his career, he joined as a Maintenance Engineer at Dewan Sugar Mills (Polypropylene Division). Later, he joined as a Lead Engineer in Total Waste Management Alliance (a contractor of ENI) at Bhit Gas Field, Jamshoro. He also possesses rich teaching and research experience in one of the leading engineering university of Pakistan. He has vast field and research experience. He has served in national and multinational industries, including polypropylene, oil and gas, and jet-engine manufacturer industries. He is currently a Professor with the Department of Mechanical Engineering, Mehran University of Engineering and Technology. He is also a specialist in design, modeling and analysis of mechanical assemblies, stochastic, and uncertainty analysis of mechanical systems. He has more than three dozen research publication in high-repute research journals and conferences. His research interests include renewable energy, controlling variation propagations in aero-engine assembly, and probabilistic/stochastic analysis of assembly tolerances. 

MUHAMMAD ASLAM UQAILI received the bachelor’s, master’s, and Ph.D. degrees in electrical engineering and the master’s degree in economics. He is currently working as the Vice Chancellor with MUET, Jamshoro. Previously, he held positions of the Pro-Vice-Chancellor, a Registrar, and the Dean of Quality Enhancement Cell (QEC), MUET. He is also an Engineer, an Academician, an Economist, and a Development Professional. He has held other positions in different statutory forums of MUET. He facilitated the linkage of Mehran University with national and international public and private institutions, including universities in USA, U.K., China, Japan, Malaysia, and Turkey. Recognizing the contribution to higher education, he has been nominated on several academic forums in the country. He is recognized as a leading academician in Pakistan and abroad. During his tenure, MUET was ranked by HEC, Islamabad, as the second best public engineering university in the country and number one public sector engineering university in the province, in 2015. He has supervised 11 doctoral and 24 master’s students. He has written 13 chapters in international books, 75 research papers in national and international research journals, and presented 56 research papers in national and international conferences. He has also edited four international books. He is a member of the editorial board of several research journals. 

SANAULLAH MEHRAN received the B.E. degree in electronics and the M.E. degree in mechatronics from MUET, Jamshoro. He has nine national and international publications to his credit. His research interests include machine vision, machine learning/deep learning, estimation theory, nature inspired computing, and deep generative models. 

**==> picture [79 x 105] intentionally omitted <==**

**==> picture [78 x 14] intentionally omitted <==**

DILEEP KUMAR received the bachelor’s degree (Hons.) in electronic engineering and the master’s degree in mechatronics from Mehran UET, Jamshoro, Pakistan. He is currently pursuing the Ph.D. degree with the University of Politecnica de Catalunya (UPC), Barcelona, Spain. During his bachelor’s degree, he was awarded with the Prime Minister’s National ICT Scholarship for four years. He completed the B.E. degree with good grades and achievements. His final year project titled ‘‘IoT-Based Remote Monitoring and Controlling of Agricultural Growth Chamber’’ was highly appreciated and funded by the Ministry of Information, Communication and Technologies, Pakistan. Besides his master’s degree, he also worked as a Teaching Assistant at the Department of Mechatronics Engineering, for a year. After completing his master’s degree with some good research publications, he worked as a Research Assistant/Programmer at the NCRA-Condition Monitoring System Laboratory at his Alma Mater. He got promoted to the position of a Design Engineer after one and a half years, owing to his dedication and competence. He has been working on applications of machine learning/deep learning algorithms for condition monitoring. Recently, he got selected for one of the top Spanish Government Ph.D. Scholarship, namely FI-SDUR, owing to his strong research profile and academic achievements. During the last four years, he has authored or coauthored 19 publications in different research journals. 

ALI AKBER SHAH received the B.E. degree in electronics engineering and the M.E. degree in mechatronics engineering from the Mehran University of Engineering and Technology, Jamshoro. He is currently pursuing the Ph.D. degree in electronics engineering, with a focus on railway track condition monitoring. He is also working as a Research Associate/Design Engineer with the National Center for Robotics and Automation-Condition Monitoring Systems Laboratory, Mehran University of Engineering and Technology. He has represented Pakistan and Mehran University in several national and international platforms. Besides that, he has already worked as a Lecturer with the Computer Science Department, SZABIST, Hyderabad. He has over 22 publications and nine of those publications are related to railway track condition monitoring. His latest publication published in (9.95 Impact Factor) IEEE INTERNET OF THINGS JOURNAL. He is in the process of filing two patents in his domain of specialization. His research interests include railway track surface monitoring, rolling stock condition monitoring, road condition monitoring, CAD designing, robotics and automation, and bridge condition monitoring. He is also working as a member of UIC’s Harmotrack Project to Implement Standards of International Railway Association in Pakistan and the European Union’s Central Project. He is also a Student Advisor of IEEE Instrumentation and Measurement Society Student Branch. 

13279 

VOLUME 11, 2023