**Jurnal Dinamika Vokasional Teknik Mesin** Vol. 09, No. 1, April 2024, pp. 10-25 https://journal.uny.ac.id/index.php/dynamika/issue/view/72682 ISSN: 2548-7590, DOI: 10.21831/dinamika.v9i1.72682 

# **Train Wheel Out-Of-Roundness (OOR) and Machine Learning-Vibration Based Fault Diagnosis: A Review** 

**Yasser Yusran[1] , I Wayan Suweca[2] , Yunendar Aryo Handoko[3]** 

1,2,3Mechanical Engineering Department, Faculty of Mechanical and Aerospace Engineering, Institut Teknologi Bandung Jalan Ganesa No. 10, Bandung 40132, Indonesia 

## **ABSTRACT** 

## **Article Info** 

_**Article history:**_ This article aims to give a complete review of previous and current research on numerous types of out-of-roundness (OOR) failures in Received April 21, 2024 train wheels, as well as diagnostic approaches based on machine Revised April 28, 2024 learning and vibration data. The study provides a comprehensive Accepted April 30, 2024 overview of the current state of research by categorizing reviews into Published April 30, 2024 three primary domains: (1) types of OOR failures in train wheels, (2) fault diagnosis methodologies, and (3) the use of machine learning and _**Keywords:**_ vibration data to diagnose train wheel OOR failures. Initially, the study investigates the characteristics, causes, and consequences of Fault diagnosis railway wheel OOR failures, including their impact on vibrations. It Machine learning then dives further into diagnostic methods, comparing the Train wheel out-of-roundness effectiveness of statistical methods to machine learning-based Vibration methods for diagnosing failures. Furthermore, the study addresses current advances in machine learning and vibration-based diagnostic methods to diagnose train wheel OOR failures, providing information on their applications and results. This article highlights that by utilizing machine learning methods with vibration data offers a promising way for accurately diagnosing OOR faults in train wheels and predicting their potential failure and remaining useful life, resulting to enhanced maintenance efficiency and less downtime. 

## _**Corresponding Author:**_ 

Yasser Yusran Mechanical Engineering Department, Faculty of Mechanical and Aerospace Engineering Institut Teknologi Bandung 40132 Bandung, Jawa Barat, Indonesia Email: 23122028@mahasiswa.itb.ac.id 

## **INTRODUCTION** 

Train wheel has a vital role in the safe and reliable operation of railways. It is responsible for supporting the weight of the train, transmitting traction, ensuring stability and guidance on the tracks. One of the most common problems with train wheels is out-of-roundness (OOR), which can result in rail damage and sleeper cracking, as well as high-cycle fatigue of wheels and other vehicle components (X. Z. Liu, 2019). Currently, railway operators mostly depend on visual inspections that are performed by experienced staff to identify train wheel OOR faults. Furthermore, they may find faults based on passenger complaints or reports of excessive vibration by drivers. In addition, frequent scheduled reprofiling of wheels based on engineering methods is conducted, even when no faults are specifically 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 11 

identified. Although these methods may be working in specific situations, but they are essentially incapable of providing a quick and accurate fault diagnosis method for train wheel OOR faults. 

Wheel OOR is dangerous because it can cause intense vibration and has the potential to impose damage to both track and vehicle components. It may further increase the likelihood of derailment and deteriorate ride comfort (X.-Z. Liu, 2019). In 2018, PT Kereta Api Indonesia (Persero), a leading railway operator in Indonesia, experienced a derailment, with wheelset OOR being one of the causes (Komite Nasional Keselamatan Transportasi Republik Indonesia, 2018). In 2019, _Havelländische Eisenbahn AG_ (HVLE), one of the rail operators in Germany, collected the wheelset failure data and found that wheel OOR had the highest failure rate compared to another type of wheelset failure (Chi et al., 2020). Wheel OOR anomalies also had been often recorded in China high-speed railway operations over 10 years, from 2012 to 2022 (Chi et al., 2020). 

Damage to the surface of the train wheel can be identified by analysing the wheel condition with some measurements such as ultrasonic testing (Pau, 2005), infrared camera (Verkhoglyad et al., 2008), acoustic emission (Thakkar et al., 2006), magnetic method (Zurek, 2006) and vibration (Li, 2022). Wheel OOR defects have a high correlation in impact vibration (Jing et al., 2021). Wheel OOR would result in impact loadings on operating railway vehicles and these impact loadings on vehicles may result in a series of abnormal vibrations, causing train performance to degrade and perhaps risking train operation safety. As speed and capacity of train increase, the impact loadings become higher, and railway vehicle impacts vibration problems from wheel OOR become more significant. In addition, the vibration-based condition monitoring could be done using wayside monitoring method (Ye et al., 2022). It could be done by installing sensors at one or several track sections, to monitor the wheel condition of all approaching wheel by analysing the rail vibration (Jelila & Pamuła, 2022)(Guedes et al., 2023). The wayside monitoring method will reduce the maintenance cost for train wheel monitoring because the number of sensors will be less than the on-board method that need one sensor for each train wheelset (Shaikh et al., 2023). 

The manual diagnosis of vibration data which is done by the operator would be time-consuming and human-dependent (Ye et al., 2022). Besides that, the fault diagnosis results between one operator to each operator might be different. To ensure operational safety and service quality, it is imperative to establish fault diagnosis techniques that enable prompt detection of wheel out-of-round (OOR) faults. The use of artificial intelligence techniques such as machine learning to diagnose equipment faults has tested positive in the manufacturing industry (Lee et al., 2019). It has a high accuracy value in diagnosing equipment faults. In addition, the machine learning technique also could predict equipment failures and calculate the remaining useful of equipment life (Çinar et al., 2020). Thus, using vibration data and machine learning to diagnose wheel OOR faults could improve the efficiency and effectiveness of railway operation and maintenance. 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 12 

The purpose of this literature review is to collect, collate and review the important published research work in the implementation of machine learning for diagnosing train wheel OOR faults basedon vibration data. Starting with understanding the characteristics, causes, and consequences of OOR problems is critical for providing the safety and efficiency of railway operations. A complete study of previous and current studies can provide significant knowledge into the factors that influence OOR faults and their impact on train wheel performance. Furthermore, by comparing various fault diagnosis methods, including machine learning-based approaches, this review can assist identify the most effective techniques for accurately diagnosing and predicting the OOR failures. In addition, this review will be highly valuable for railway industry in establishing predictive maintenance strategies to mitigate the risk of train wheel OOR failures. The article will be presented in the following order: (1) type of train wheel OOR faults, (2) classification of fault diagnosis methods, and (3) machine learning algorithms to diagnose equipment faults based on vibration data. 

## **TRAIN WHEEL OUT-OF-ROUNDNESS (OOR) FAULTS** 

During rail vehicle operation, the train exhibits two types of wear (Braghin et al., 2009): changes in the transversal profile, known as regular wear, and the formation of periodic wear patterns in the circumferential direction, known as irregular wear or wheel out-of-roundness (OOR). Regular wear is caused by modest fluctuations in contact forces and creepages caused by the wheelset's longitudinal and lateral motion on the track. On the other hand, wheel OOR is caused by rapid fluctuations in wheel-rail contact conditions, which could be caused by train-track interaction. 

The various types of irregular wear or wheel out-of-round (OOR) faults (J. C. O. Nielsen & Johansson, 2000) are compiled in Figure 1. Train wheel wear can cause changes in both the transverse and circumferential profiles of the wheel. The transverse profile change is commonly known as regular wear, which refers to the deterioration mechanisms that cause a change in the profile across the wheel. The circumferential profile change is usually known as irregular wear or out-of-roundness (OOR). The wheel OOR is could be presented as circular irregularity of the wheel circumference or discrete tread defects (J. Nielsen, 2009). 

The circular irregularity can be further divided into periodic and stochastic irregularities based on the dominant wavelengths present. If there are limited dominant wavelengths, it is considered periodic irregularity, and if there are many, it is referred to as stochastic irregularity (Peng, 2020). Periodic irregularity can be subdivided into eccentricity, wheel polygonization, and wheel roughness. Eccentricity is a 1-order problem in circular irregularity, while wheel polygonization and roughness have multiple orders. Wheel polygonization typically has longer wavelengths and higher amplitudes, while wheel roughness features shorter wavelengths and smaller amplitudes (Peng, 2020). Discrete tread defects include wheel tread flats, wheel tread spalling, and wheel tread shelling. For detailed explanation, Figure 2 shows the types of OOR faults in pictures or illustrations and Table 1 explains the 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 13 

differences between each type faults based on its characteristics, causes, and effects (including the effects on the vibration generated). 

**==> picture [400 x 212] intentionally omitted <==**

Figure 1. Classification of OOR faults (Peng, 2020) 

**==> picture [294 x 262] intentionally omitted <==**

Figure 2. The pictures of OOR faults classification (a) Eccentricity (Kang et al., 2022), (b) Stochastic non-roundness (Jing et al., 2022), (c) Wheel polygonization (Peng, 2020), (d) Wheel roughness (Chiello et al., 2019), (e)Wheel tread flat (J. C. O. Nielsen et al., 2015), (f)(g) Wheel tread spalling (C. Liu et al., 2022)(Chong et al., 2010), (h)(i) Wheel tread shelling (Chong et al., 2010)(Papaelias et al., 2016) 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 14 

Table 1. Differences of OOR faults based on characteristics, causes, and effects. 

|**OOR faults**<br>Eccentricity|**Characteristics**<br>- Occurs when the wheelset's rotation|**Causes**<br> <br>- Improper machining, inaccurate assembly,|**Effects**<br>- Produces vertical vibrations with amplitudes that increase as the train speed increases,| |---|---|---|---| ||center deviates from its mass center or|poor material quality (Kang et al., 2022)|while normal wheel is approximately zero (Lv et al., 2017)| ||geometric center (Kang et al., 2022)|- Incorrect wheel fixation during profiling or|- At a certain speed, the frequency of eccentricity vibration will approach the natural| |||reprofiling (J. C. O. Nielsen & Johansson,|frequency of the vehicle, causing resonance in the car body and increasing the vertical| |||2000)|vibration significantly (Lv et al., 2017)| |Wheel|- Circular tread defects with periodic large|<br>- Fixed-frequency mechanisms such as vehicle|- The root mean square (RMS) value of the vertical acceleration with a polygonal wheel is| |polygonization|<br>deviation (Sun et al., 2021)|speed, wheelset and local rail flexibility,|4-8 times higher than a normal wheel (Sun et al., 2021)| ||- Defect properties for wavelength is from|<br>wheelset imbalance, material hardness, self-|- The vertical load spectrum on the railway vehicle's suspension and structural components| ||140 mm to entire circle and amplitude is|<br>induced vibration, and wheel flat(Peng, 2020)|is increased by polygonized wheel which effect the components break more quickly and| ||larger than 0.2mm (Peng, 2020)|- Various suspension, material, machining or|prematurely (Fröhling et al., 2019)| |||track factors(Fröhlinget al.,2019)|- In high-speed, the vehicle's safety potentially be jeopardized (Xiaoyiet al.,2018)| |Wheel|- Circular tread defect of periodic small|<br>- During tread braking, hot spots arise in some|- The energy (covariance) of vertical acceleration signals of corrugation wheel is 2-5 times| |roughness|deviation (Bracciali & Cascini, 1997)|regions. When the cooling phase, it will|higher than normal wheel (Bracciali & Cascini, 1997)| |(corrugation)|- Defect properties for wavelength is from|<br>generate valleys and corrugation pattern (J.|- The movement of a corrugated wheel along the track generates acoustic waves as a result| ||30 -80 mm and amplitude is around 10|Nielsen, 2009)|of the vibration caused by the ridges and valleys on the tread (Bracciali & Cascini, 1997)| ||µm(Peng,2020)||- Increasing dynamicload and produce wavymotion invertical(Srivastava et al.,2016).| |Stochastic|- Circular tread defects with non-periodic|<br>- Irregular wear or damage to the wheel tread,|- Effects two parameters in vertical displacement irregularity which are increasing the| |(non-periodic)|intervals (Peng, 2020)|manufacturing defects, and uneven loading or|amplitude of wheel OOR until 200 times compared to periodic non-roundness and creating| |non-roundness||braking forces on the wheel (Jing et al., 2022)|random (non-constant) value for phase angel (Jing et al., 2022)| ||||- It can cause the train to vibrate and produce excessive noise (Jing et al., 2022)| ||||- The uneven loading and contact between the non-round wheel and the track can cause| ||||increased wear and tear on both the wheel and the track (Jing et al., 2022)| |Wheel tread|A discrete defect that happens when a|Excessive braking force in comparison to|- It causes impact vibration, which produces a spike that is approximately 4 times larger in| |flats|piece of the wheel tread flattens (J. C. O.|<br>available wheel/rail friction [16]. It could be|peak-to-peak value than normal vertical acceleration (Ye et al., 2020)| ||Nielsen & Johansson, 2000)|because the brakes are incorrectly set, frozen,|- The impact vibration can be harmful to both passengers and vehicle-track systems.| |||malfunctioning or areas where wheel/rail|Passengers may experience less comfort as result of the high-frequency vibrations and| |||friction is accidentallylow(Ye et al.,2020)|increased noise (Jing et al., 2021)| |Wheel tread|- Localized degradation of wheel tread to|- Cracking developed due phase transformation|- The RMS and maximum amplitude (peak) value of vertical vibration will increase with the| |spalling|cracks, leaving behind rough, pitted on|stress from the martensite formation of surface|severity of the spalling defect. The RMS and peak values are about 2-3 times higher than| ||wheel surface (J. Nielsen, 2009)|material (Srivastava et al., 2016)|the value of the normal wheel (G. Xu et al., 2021) (Yan et al., 2021)| ||- The crack forms perpendicular and|<br>- It can be caused by rolling contact fatigue (J.|- It produces impact vibration that reduces the life of vehicle-track components and has an| ||parallel to the wheel surface (Srivastava|<br>Nielsen, 2009), and by wheel/rail relative|impact on railway safety and passenger comfort (Wang et al., 2013)| ||et al., 2016)|sliding (W. Liu et al., 2015)|| |Wheel tread|- Indicated as the loss of relatively large|- Caused by excessive normal contact and shear|- The RMS value of vertical vibration is about 2-3 times higher than the value of the normal| |shelling|(greater than 5 mm) metal from the|<br>stress, which leads fatigue cracks (Chong et al.,|wheel and followed by large maximum peak value in high frequency (Papaelias et al., 2016)| ||wheel tread [35].|2010)|- It may cause irregularities on the rail-wheel surface, increase dynamic load, degrade riding| ||- Occurs below the plastically worked|- Happens as a result of subsurface fatigue due to|quality, increase vibration, and trigger derailments(Srivastava et al., 2016)| ||layer (Srivastava et al., 2016) and forms|<br>excessive contact stress or the presence of non-|| ||sharp angle to the surface (Moyar &|<br>metallic impurities within the rail or wheel|| ||Stone,1991)|surface (Srivastava et al.,2016)||



_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 15 

## **FAULT DIAGNOSIS METHODS** 

In the train wheel out-of-roundness (OOR) fault section , it was explained that all OOR defects in the train wheel will result in certain changes in vertical vibration. After the OOR defects are detected through vertical vibration, the fault diagnosis is then carried out in order to identify the specific type and location of the OOR defect. There are three main methods of fault diagnosis in dynamic system which are model based fault diagnosis, knowledge based fault diagnosis and data-driven based fault diagnosis. These methods are gathered in Figure 3. 

**==> picture [307 x 269] intentionally omitted <==**

Figure 3. Fault diagnosis methods classification (Escobet et al., 2019) 

## **Model based Fault Diagnosis** 

The model based fault diagnosis compares a measured signal, the actual plant output, and its estimation computed in terms of an explicit mathematical model of the system under normal operational conditions (Escobet et al., 2019). Figure 4 describes the stages of model-based fault diagnosis. 

**==> picture [455 x 131] intentionally omitted <==**

Figure 4. Block diagram of model based fault diagnosis (Escobet et al., 2019) 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 16 

The difference between measured and estimated output is known as the residual or error; these residuals should be zero when the system is operating normally and should vary from zero when a malfunction develops. As a result, the faults are discovered by applying a (fixed or variable) threshold to the residual. When a fault is identified, the fault signal is compared to a fault signature database to appropriately diagnose the fault. Observers, Kalman filters, parity equations, and parameter estimates are the four techniques used in model-based fault diagnostics (Escobet et al., 2019). The observer technique generates a set of residuals to detect and uniquely identify various faults (Venkatasubramanian, Rengaswamy, Kavuri, et al., 2003). Kalman Filter’s prediction error can be employed as a fault detection residual; its mean is zero if no faults exist and becomes nonzero if faults exist (Escobet et al., 2019). Parity equations are obtained by rearranging or direct manipulation of the state space or the input–output model of the system (Escobet et al., 2019). Parameter estimation, which involves applying identification methods to identify a linear or nonlinear model of the system (Venkatasubramanian, Rengaswamy, Kavuri, et al., 2003). 

## **Knowledge based Fault Diagnosis** 

Knowledge based fault diagnosis is also known as qualitative model-based fault diagnosis because the input-output relationships are stated in terms of qualitative functions focusing on different units in a system (Venkatasubramanian, Rengaswamy, & Kavuri, 2003). The knowledge based fault diagnosis relies on a large volume of historical data available to extract a to extract a knowledge base, explicitly representing the dependency of system variables (Fadzail et al., 2022). Figure 5 depicts a knowledge-based block diagram for diagnosing the type of fault condition in the system. 

**==> picture [396 x 130] intentionally omitted <==**

Figure 5. Block diagram of knowledge based fault diagnosis (Fadzail et al., 2022) 

According to Figure 5, it begins with historical training and learning data to build the knowledge base before moving on to the classifier. Simultaneously, the system model will process the inputs and faults to produce the output. Finally, the consistency of the system's input and output will be evaluated against the knowledge base to decide the diagnosis. This method employs two main techniques: expert systems and causal models (Escobet et al., 2019). Expert systems are knowledge-based procedures that are more similar to human problem-solving in style, and they are used to replicate the reasoning of 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 17 

human experts when diagnosing faults (Escobet et al., 2019). Another knowledge-based technique is the use of causal models in the modelling of fault-symptom relationships, such as signed direct graph (digraphs) and fault tree analysis (FTA) (Escobet et al., 2019). 

## **Data-driven based Fault Diagnosis** 

The data-driven based fault diagnosis uses information gathered by sensors and actuators in a dynamic system to extract valuable knowledge. The growth of technology, such as the Internet of Things (IoT), has increased the importance of this method. Data obtained may be used to analyse component degradation or to develop behavioural models from data, diagnose the faults and estimate its remaining useful lifetime (RUL) (P. Nunes, J. Santos, 2023). Figure 6 illustrates the schematic of data-driven based fault diagnosis. 

**==> picture [394 x 120] intentionally omitted <==**

Figure 6. Block diagram of data-driven based fault diagnosis (Gonzalez-Jimenez et al., 2021) 

Following Figure 6, the data obtained from sensors and actuators becomes a collection of big data that will be extracted into some data features. These features are analysed by using a computational model, either statistical model or machine learning (ML) model, to find a hidden pattern that presents information about the system condition, including failure diagnosis information. Statistical approaches focus on identifying faults based on the distribution of variables during the working process, whereas ML is a subfield of artificial intelligent (AI) that provides methodologies for dealing with highdimensional data and extracting hidden relationships between data in non-linear and complex systems (Carvalho et al., 2019). 

Table 2 compares the advantages and limitations of three fault diagnostic methods: model based, knowledge based, and data-driven based. Table 2 shows that data-driven fault diagnosis offers several advantages over model- or knowledge-based methodologies. In addition, section of this paper also indicating OOR faults in train wheel are highly connected to vertical vibration data. Furthermore, the following section of this review will investigate vibration data-driven based fault diagnosis, with a focus on machine learning techniques, which are one of the approaches used in the application of data-based failure diagnosis. 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 18 

Table 2. Advantages and limitations of fault diagnosis methods 

|**Fault Diagnosis**|**Advantages**|**Limitations**| |---|---|---| |**Method**||| |Model based|- Highly effective and accurate (Ran et al.,|- Real-case system is often too stochastic and| ||2019)|complex to model (Ran et al., 2019)| ||- Models can be reused (Ran et al., 2019)|- Many mathematics assumptions must be evaluated| ||- Have some control over the behaviour of|(Ran et al., 2019)| ||the<br>residuals<br>(Venkatasubramanian,|- Several physical parameters must be determined| ||Rengaswamy, Kavuri, et al., 2003)|(Ran et al., 2019)| |||- The model can be influenced by changes in| |||structural dynamics and operational conditions (Ran| |||et al., 2019)| |||- Noises and disruptions in measurement can lead to| |||incorrect fault diagnosis (Escobet et al., 2019)| |||- Inability to detect a new fault that has not been| |||specificallymodelled (Escobet et al.,2019)| |Knowledge based|- Reduce the diffculties on exact numeric|- Time-consuming and costly for large-scale systems| ||information (Ran et al., 2019)|(Ran et al., 2019)| ||- Able to<br>capture<br>human<br>diagnostic|- There is not available knowledge from new faults| ||associations that are not readily translated|(Escobet et al., 2019)| ||into mathematical models (Escobet et al.,|- Acquire complete knowledge to build a reliable| ||2019)|knowledge based system (Ran et al., 2019)| ||- Ability to yield partial conclusions from|| ||incomplete and uncertain knowledge of|| ||the<br>process<br>(Venkatasubramanian,|| ||Rengaswamy, & Kavuri, 2003)|| |Data-driven based|- There is no need to model the system|- The statistical technique relies on the assumption| ||(Escobet et al., 2019)|that parameters have a known distribution, which| ||- Can learn the overall system's behaviour|may approximate the true behaviour (Gao et al.,| ||with only a few datasets (Escobet et al.,|2015)| ||2019)|- A large volume of data is necessary (Gonzalez-| ||- It is possible to detect new issues or faults|Jimenez et al., 2021)| ||with insufficient data (Escobet et al.,|- Platform for data storage is required (Gonzalez-| ||2019)|Jimenez et al., 2021)| ||- The updated and corrected diagnostic can|- High computational resources (Gonzalez-Jimenez| ||provide more reliable information for|et al., 2021)| ||maintenance decision-making in the|| ||future<br>(Venkatasubramanian,|| ||Rengaswamy, Yin, et al., 2003)|| ||- The ML approach can describe very|| ||complex and non-linear systems with|| ||great accuracy in defect identification|| ||(Venkatasubramanian,<br>Rengaswamy,|| ||Yin, et al., 2003)|| ||- The<br>ML<br>approach<br>is<br>capable<br>of|| ||diagnosing,<br>predicting<br>failure,<br>and|| ||calculating the lifetime of equipment|| ||(Dalzochio et al., 2020)||



## **MACHINE LEARNING-VIBRATION BASED OOR FAULT DIAGNOSIS** 

The data-driven based fault diagnosis is divided into two types of analytical techniques: statistical and machine learning techniques. A statistical method is used by initially building an empirical model of the normal behaviour of components, followed by some variable ranking test (such as e.g. data variance, Pearson correlation coefficient, relief algorithm, fisher score, class separability, chi-squared or χ[2] , information gain and gain ratio (Zhang et al., 2011)) are used to determine if the data under consideration corresponds to equipment condition classification (P. Nunes, J. Santos, 2023). A machine learning (ML) method is used to create a normal behaviour model utilizing data from an output 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 19 

monitoring sensor (Krummenacher et al., 2018). To determine maintenance activities, ML approaches could model very complex systems with multiclassification of equipment state and compare the predicted sensor value with the actual sensor value (P. Nunes, J. Santos, 2023). Table 3 compares the advantages and limits of statistical and machine learning methods. 

Table 3. Advantages and limitations of statistical and machine learning methods 

|**Data-driven Based Fault**|**Advantages**|**Limitations**|| |---|---|---|---| |**Diagnosis**|||| |Statistical methods|- Easy<br>to<br>understand<br>(noncomplex|- Relies on the assumption|that parameters| ||calculation) (Zhang et al., 2011)|have a known distribution, which may|| ||- Lower computational cost (Zhang et al.,|approximate the true behaviour.|| ||2011)|- Does not consider the non-linearity of the|| |||data (Guedes et al., 2023)|| |||- Time invariant, while most of the real|| |||processes<br>are|time-varying| |||(Venkatasubramanian,|Rengaswamy,| |||Yin, et al., 2003)|| |Machine learning methods|- Possible to detect new issues or faults with|- A large volume of training data is|| ||insufficient data (Escobet et al., 2019)|necessary for some ML methods (Gao et|| ||- Can describe very complex and non-linear|al., 2015)|| ||systems with great accuracy in defect|- High computational resources (Gonzalez-|| ||identification<br>(Venkatasubramanian,|Jimenez et al., 2021)|| ||Rengaswamy, Yin, et al., 2003)||| ||- Capable of diagnosing, predicting failure,||| ||and calculating the lifetime of equipment||| ||(Dalzochio et al.,2020)|||



As listed in Table 3, the machine learning method has more benefits than the statistical method. In addition, in the era of Industry 4.0, artificial intelligence such as machine learning methods could help humans in decision making and make the job more efficient with high accuracy result. So, we will study the machine learning approach in better detail. 

## **Machine Learning Techniques** 

Machine learning (ML) approaches are data-driven learning methods that employ historical data to train software to make generalized predictions. These models may automatically learn how to solve problems of many types and dimensionalities, ranging from hundreds to only a few input features (Nacchia et al., 2021). ML is classified into four types in data-driven fault diagnostics (Achouch et al., 2022), which are supervised learning, unsupervised learning, reinforcement learning, and deep learning. The types of supervised and unsupervised learning intended to predict or describe existing relationships in a dataset are said to be supervised when the dependent variable is available and unsupervised when it is not. Whereas reinforcement learning is a computational approach that learns from the interaction with the environment, which means determining how the agents in a system can perform actions in their environment to maximize the cumulative rewards. Deep learning (DL) is a type of artificial neural network (ANN). It is a broad category of approaches that may be applied to both supervised and unsupervised learning. ANN is inspired by brain activity, and its major purpose is to learn from unstructured or unlabelled data by employing one or more layers to extract higher-level characteristics 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 20 

from raw input step by step. Deep learning techniques may be used on industrial equipment in a variety of contexts, including fault diagnosis, failure prediction, and so on. There are a lot of ML algorithms that could be used to several stages of predictive maintenance, such as diagnosis, prognosis, and estimation of useful life. Figure 7 shows the taxonomy of machine learning algorithms that gathered from some literatures (Achouch et al., 2022)(Sohail et al., 2023)(Tiboni et al., 2022)(Abid et al., 2021). The taxonomy highlights the connection among classes of algorithms. 

**==> picture [462 x 216] intentionally omitted <==**

Figure 7. Taxonomy of machine learning algorithms 

## **Machine Learning-Vibration based OOR Fault Diagnosis** 

OOR faults in train wheel, as discussed in section 2, are strongly related to the vertical vibration of the wheelset dynamic system. Additionally, vibration data is the most frequently utilized type of data in mechanical equipment condition monitoring, including rotating equipment (Tiboni et al., 2022). Analysis of vibration data using traditional statistical methods often requires a significant amount of time and computational complexity. One solution to this problem is to use machine learning approaches for processing vibration data, such as when diagnosing and even predicting the OOR faults. There has been some research in recent years on the application of machine learning to analyse vibration data in the diagnosis of OOR defects, which is summarized in Table 4. 

Table 4 shows that most of the research was focused on the application of machine learning to identify a single type of defect with a vibration based OOR fault. Diagnosing multiple failures is more challenging than a single failure, as all OOR failures will influence vertical vibration, so an effective ML algorithm is needed to identify the differences in vibration resulting from different OOR failures, for resulting an accurate diagnosis fault. According to Table 4, not all researchers utilized vibration data that acquired from acceleration measurements; instead, some researchers used data from displacement and impact loads measurements to analyse vertical vibration caused by OOR failures. These data were 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 21 

acquired from field observations, test-rig experiments, and multibody-dynamic software simulation. In addition, the machine learning algorithms used are quite varied even though the SVM and DNN algorithms were used in more than one study. Most of the use of ML algorithms was in the failure diagnosis stage only, although there was one study for estimating the remaining useful life (RUL). 

Table 4. Summary of ML application for vibration based OOR fault diagnosis. 

|**OOR Faults**|**Measured signal**||**Source**|**ML**<br>**Algorithm**|**ML Task**|**Ref.**| |---|---|---|---|---|---|---| |General defect|Impact load|Field||SVM<br>and|Fault detection|(Wang et al., 2018)| |||||SVR|and RUL|| ||||||estimation|| |Spalling|Acceleration|Field|(depot)|kNN-GBDT|Fault diagnosis|(Kou et al.,2018)| |Flat, shelling, non-|- Impact load|- Field||SVM, DNN|Fault diagnosis|(Krummenacher et| |roundness|- Wheel profile|- Maintenance||||al., 2018)| |||history data||||| |General defect|Displacement|Field||BL|Fault detection|(Ni & Zhang, 2021)| |Polygonization|Acceleration|Field||GMPSO-|Fault diagnosis|(Xie et al., 2022)| |||||MKELM||| |Axle crack, wheel|- Acceleration|- Simulation||Light-GBM|Fault diagnosis|(Xiong et al., 2022)| |flat, non-roundness,||- Test-rig||||| |and multi-defects||||||| |General defect|Impact load|Field||LAD|Fault detection|(Osman & Yacout,| |||||||2022)| |Polygonization|Acceleration|- Simulation||QPSO-SVM|Fault diagnosis|(M. Xu & Yao,| |||- Test-rig||||2023)| |Flat, spalling|Displacement|Field||NMF, MLP-|Fault diagnosis|(Wan et al., 2023)| |||||AE||| |Flat|Acceleration|Field||DNN|Fault diagnosis|(Ye et al., 2023)|



## **CONCLUSION** 

This paper conducted and addressed extensive evaluations of previous and current research work on wheel OOR faults and machine learning-vibration based fault diagnostics. The characteristics, factors influencing, and operation effects (including vibration features) caused by wheel OOR faults were given and examined in depth. The fault diagnosis methods, namely model-based, knowledgebased, and data-driven techniques was also described and deliberated. In-depth surveys of machine learning approaches for diagnosing equipment failure were also provided. Machine learning-based fault diagnosis is more capable, reliable, and accurate than other fault diagnosis methods such as statisticalbased fault diagnosis, perhaps even the best when compared to model- and knowledge-based fault diagnosis. ML-based fault diagnosis could be used in complex and nonlinear systems and it is much simpler and easier to implement as it does not require system modelling. ML-based fault diagnosis is used to analyse data from equipment monitoring results. Whereas, wheel OOR faults have a significant relationship to vertical vibration in railway vehicle operation. So, by integrating machine learning techniques and vibration data, it is feasible to diagnose OOR faults in train wheel better and more accurately. Furthermore, the use of ML and vibration data may predict the failure and remaining useful life of the train wheel. Current research for machine learning and vibration-based train wheel OOR 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 22 

failure diagnosis is still not well established, and more research needs to be done. The requirement for a large amount of data to create machine learning models is a challenge, because in the actual world, fault data from sensor monitoring will almost likely be less than normal condition monitoring data (unbalanced data). Furthermore, research into the application of machine learning-vibration techniques to identify several train wheel OOR faults is required to determine the optimal machine learning method. This type of study can also include railway operator industries, increasing train wheel maintenance strategies more effective and efficient. 

## **REFERENCES** 


- Abid, A., Khan, M. T., & Iqbal, J. (2021). A review on fault detection and diagnosis techniques: basics and beyond. _Artificial Intelligence Review_ , _54_ (5), 3639–3664. https://doi.org/10.1007/s10462020-09934-2 


- Achouch, M., Dimitrova, M., Ziane, K., Sattarpanah Karganroudi, S., Dhouib, R., Ibrahim, H., & Adda, M. (2022). On Predictive Maintenance in Industry 4.0: Overview, Models, and Challenges. _Applied Sciences (Switzerland)_ , _12_ (16). https://doi.org/10.3390/app12168081 


- Bracciali, A., & Cascini, G. (1997). Detection of corrugation and wheelflats of railway wheels using energy and cepstrum analysis of rail acceleration. _Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit_ , _211_ (2), 109–116. https://doi.org/10.1243/0954409971530950 


- Braghin, F., Bruni, S., & Lewis, R. (2009). 6 - Railway wheel wear. In R. Lewis & U. Olofsson (Eds.), _Wheel–Rail Interface Handbook_ (pp. 172–210). Woodhead Publishing. https://doi.org/https://doi.org/10.1533/9781845696788.1.172 


- Carvalho, T. P., Soares, F. A. A. M. N., Vita, R., Francisco, R. da P., Basto, J. P., & Alcalá, S. G. S. (2019). A systematic literature review of machine learning methods applied to predictive maintenance. _Computers and Industrial Engineering_ , _137_ (September), 106024. https://doi.org/10.1016/j.cie.2019.106024 


- Chi, Z., Lin, J., Chen, R., & Huang, S. (2020). Data-driven approach to study the polygonization of high-speed railway train wheel-sets using field data of China’s HSR train. _Measurement: Journal of the International Measurement Confederation_ , _149_ , 107022. https://doi.org/10.1016/j.measurement.2019.107022 


- Chiello, O., Le Bellec, A., Pallas, M. A., Munoz, P., & Janillon, V. (2019). Characterisation of wheel/rail roughness and track decay rates on a tram network. _INTER-NOISE 2019 MADRID - 48th International Congress and Exhibition on Noise Control Engineering_ . https://doi.org/https://hal.science/hal-02305430 


- Chong, S. Y., Lee, J. R., & Shin, H. J. (2010). A review of health and operation monitoring technologies for trains. _Smart Structures and Systems_ , _6_ (9), 1079–1105. https://doi.org/10.12989/sss.2010.6.9.1079 


- Çinar, Z. M., Nuhu, A. A., Zeeshan, Q., Korhan, O., Asmael, M., & Safaei, B. (2020). Machine learning in predictive maintenance towards sustainable smart manufacturing in industry 4.0. _Sustainability (Switzerland)_ , _12_ (19). https://doi.org/10.3390/su12198211 


- Dalzochio, J., Kunst, R., Pignaton, E., Binotto, A., Sanyal, S., Favilla, J., & Barbosa, J. (2020). Machine learning and reasoning for predictive maintenance in Industry 4.0: Current status and challenges. _Computers in Industry_ , _123_ , 103298. https://doi.org/10.1016/j.compind.2020.103298 


- Escobet, T., Bregon, A., Pulido, B., & Puig, V. (2019). Fault Diagnosis of Dynamic Systems: Quantitative and Qualitative Approaches. In _Fault Diagnosis of Dynamic Systems: Quantitative and Qualitative Approaches_ . https://doi.org/10.1007/978-3-030-17728-7 


- Fadzail, N. F., Mat Zali, S., Mid, E. C., & Jailani, R. (2022). Application of Automated Machine Learning (AutoML) Method in Wind Turbine Fault Detection. _Journal of Physics: Conference_ 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 23 

_Series_ , _2312_ (1). https://doi.org/10.1088/1742-6596/2312/1/012074 


- Fröhling, R., Spangenberg, U., & Reitmann, E. (2019). Root cause analysis of locomotive wheel tread polygonisation. _Wear_ , _432_ – _433_ (April). https://doi.org/10.1016/j.wear.2019.05.026 


- Gao, R., Wang, L., Teti, R., Dornfeld, D., Kumara, S., Mori, M., & Helu, M. (2015). Cloud-enabled prognosis for manufacturing. _CIRP Annals - Manufacturing Technology_ , _64_ (2), 749–772. https://doi.org/http://dx.doi.org/10.1016/j.cirp.2015.05.011 


- Gonzalez-Jimenez, D., Del-Olmo, J., Poza, J., Garramiola, F., & Madina, P. (2021). Data-driven fault diagnosis for electric drives: A review. _Sensors_ , _21_ (12). https://doi.org/10.3390/s21124024 


- Guedes, A., Silva, R., Ribeiro, D., Vale, C., Mosleh, A., Montenegro, P., & Meixedo, A. (2023). Detection of Wheel Polygonization Based on Wayside Monitoring and Artificial Intelligence. _Sensors_ , _23_ (4). https://doi.org/10.3390/s23042188 


- Jelila, Y. D., & Pamuła, W. (2022). Detection of Tram Wheel Faults Using MEMS-Based Sensors. _Sensors_ , _22_ (17). https://doi.org/10.3390/s22176373 


- Jing, L., Liu, Z., & Liu, K. (2022). A mathematically-based study of the random wheel-rail contact irregularity by wheel out-of-roundness. _Vehicle System Dynamics_ , _60_ (1), 335–370. https://doi.org/10.1080/00423114.2020.1815809 


- Jing, L., Wang, K., & Zhai, W. (2021). Impact vibration behavior of railway vehicles: a state-of-the-art overview. _Acta Mechanica Sinica/Lixue Xuebao_ , _37_ (8), 1193–1221. https://doi.org/10.1007/s10409-021-01140-9 


- Kang, X., Chen, G., Song, Q., Dong, B., Zhang, Y., & Dai, H. (2022). Effect of wheelset eccentricity on the out-of-round wheel of high-speed trains. _Engineering Failure Analysis_ , _131_ (August 2021), 105816. https://doi.org/10.1016/j.engfailanal.2021.105816 


- Komite Nasional Keselamatan Transportasi Republik Indonesia. (2018). Laporan Akhir KNKT.18.03.05.02. In _Laporan Investigasi Kecelakaan Perkeretaapian_ . https://knkt.go.id/Repo/Files/Laporan/Perkeretaapian/2018/KNKT.18.03.05.02.pdf 


- Kou, L., Qin, Y., & Zhao, X. (2018). An Integrated Model of kNN and GBDT for Fault Diagnosis of Wheel on Railway Vehicle. _Proceedings - 2018 Prognostics and System Health Management Conference, PHM-Chongqing 2018_ , 432–436. https://doi.org/10.1109/PHMChongqing.2018.00080 


- Krummenacher, G., Ong, C. S., Koller, S., Kobayashi, S., & Buhmann, J. M. (2018). Wheel Defect Detection with Machine Learning. _IEEE Transactions on Intelligent Transportation Systems_ , _19_ (4), 1176–1187. https://doi.org/10.1109/TITS.2017.2720721 


- Lee, W. J., Wu, H., Yun, H., Kim, H., Jun, M. B. G., & Sutherland, J. W. (2019). Predictive maintenance of machine tool systems using artificial intelligence techniques applied to machine condition data. _Procedia CIRP_ , _80_ , 506–511. https://doi.org/10.1016/j.procir.2018.12.019 


- Li, C. (2022). Wheel Polygon Detection Based on Vibration-Impact Analyses of Bogie Components. _ICRT 2021 - Proceedings of the 2nd International Conference on Rail Transportation_ , 267–275. https://doi.org/10.1061/9780784483886.030 


- Liu, C., Xu, J., Wang, K., Liao, T., & Wang, P. (2022). Numerical investigation on wheel-rail impact contact solutions excited by rail spalling failure. _Engineering Failure Analysis_ , _135_ (February), 106116. https://doi.org/10.1016/j.engfailanal.2022.106116 


- Liu, W., Ma, W., Luo, S., Zhu, S., & Wei, C. (2015). Research into the problem of wheel tread spalling caused by wheelset longitudinal vibration. _Vehicle System Dynamics_ , _53_ (4), 546–567. https://doi.org/10.1080/00423114.2015.1008015 


- Liu, X.-Z. (2019). Railway Wheel Out-of-Roundness and Its Effects on Vehicle–Track Dynamics: A Review. _Data Mining in Structural Dynamic Analysis_ , 41–64. https://doi.org/10.1007/978-981-150501-0_3 


- Liu, X. Z. (2019). Railway Wheel Out-of-Roundness and Its Effects on Vehicle-Track Dynamics: A Review. _Data Mining in Structural Dynamic Analysis: A Signal Processing Perspective_ , 41–64. https://doi.org/10.1007/978-981-15-0501-0_3 


- Lv, K., Wang, K., Chen, Z., Cai, C., & Guo, L. (2017). Influence of Wheel Eccentricity on Vertical Vibration of Suspended Monorail Vehicle : Experiment and Simulation. _Shock and Vibration_ . https://doi.org/https://doi.org/10.1155/2017/1367683 


- Moyar, G. J., & Stone, D. H. (1991). An analysis of the thermal contributions to railway wheel shelling. 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 24 

_Wear_ , _144_ (1–2), 117–138. https://doi.org/10.1016/0043-1648(91)90010-R 


- Nacchia, M., Fruggiero, F., Lambiase, A., & Bruton, K. (2021). A systematic mapping of the advancing use of machine learning techniques for predictive maintenance in the manufacturing sector. _Applied Sciences (Switzerland)_ , _11_ (6), 1–34. https://doi.org/10.3390/app11062546 


- Ni, Y. Q., & Zhang, Q. H. (2021). A Bayesian machine learning approach for online detection of railway wheel defects using track-side monitoring. _Structural Health Monitoring_ , _20_ (4), 1536–1550. https://doi.org/10.1177/1475921720921772 


- Nielsen, J. (2009). 8 - Out-of-round railway wheels. In R. Lewis & U. Olofsson (Eds.), _Wheel–Rail Interface Handbook_ (pp. 245–279). Woodhead Publishing. https://doi.org/https://doi.org/10.1533/9781845696788.1.245 


- Nielsen, J. C. O., & Johansson, A. (2000). Out-of-round railway wheels-a literature survey. _Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit_ , _214_ (2), 79– 91. https://doi.org/10.1243/0954409001531351 


- Nielsen, J. C. O., Lombaert, G., & François, S. (2015). A hybrid model for prediction of ground-borne vibration due to discrete wheel/rail irregularities. _Journal of Sound and Vibration_ , _345_ , 103–120. https://doi.org/10.1016/j.jsv.2015.01.021 


- Osman, H., & Yacout, S. (2022). Condition-based monitoring of the rail wheel using logical analysis of data and ant colony optimization. _Journal of Quality in Maintenance Engineering_ , _29_ (2), 377–400. https://doi.org/10.1108/JQME-01-2022-0004 


- P. Nunes, J. Santos, E. R. (2023). Challenges in predictive maintenance – A review. _CIRP Journal of Manufacturing Science and Technology_ , _40_ , 53–67. https://doi.org/https://doi.org/10.1016/j.cirpj.2022.11.004 


- Papaelias, M., Amini, A., Huang, Z., Vallely, P., Dias, D. C., & Kerkyras, S. (2016). Online condition monitoring of rolling stock wheels and axle bearings. _Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit_ , _230_ (3), 709–723. https://doi.org/10.1177/0954409714559758 


- Pau, M. (2005). Ultrasonic waves for effective assessment of wheel-rail contact anomalies. _Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit_ , _219_ (2), 79– 90. https://doi.org/10.1243/095440905X8808 


- Peng, B. (2020). _Mechanisms of railway wheel polygonization_ . University of Huddersfield. 


- Ran, Y., Zhou, X., Lin, P., Wen, Y., & Deng, R. (2019). _A Survey of Predictive Maintenance: Systems, Purposes and Approaches_ . _XX_ (Xx), 1–36. http://arxiv.org/abs/1912.07383 


- Shaikh, M. Z., Ahmed, Z., Chowdhry, B. S., Baro, E. N., Hussain, T., Uqaili, M. A., Mehran, S., Kumar, D., & Shah, A. A. (2023). State-of-the-Art Wayside Condition Monitoring Systems for Railway Wheels: A Comprehensive Review. _IEEE Access_ , _11_ (December 2022), 13257–13279. https://doi.org/10.1109/ACCESS.2023.3240167 


- Sohail, A., Cheema, M. A., Ali, M. E., Toosi, A. N., & Rakha, H. A. (2023). Data-driven approaches for road safety: A comprehensive systematic literature review. _Safety Science_ , _158_ (August 2022). https://doi.org/10.1016/j.ssci.2022.105949 


- Srivastava, J. P., Sarkar, P. K., & Ranjan, V. (2016). Effects of thermal load on wheel–rail contacts: A review. _Journal of Thermal Stresses_ , _39_ (11), 1389–1418. https://doi.org/10.1080/01495739.2016.1216060 


- Sun, Q., Chen, C., Kemp, A. H., & Brooks, P. (2021). An on-board detection framework for polygon wear of railway wheel based on vibration acceleration of axle-box. _Mechanical Systems and Signal Processing_ , _153_ , 107540. https://doi.org/10.1016/j.ymssp.2020.107540 


- Thakkar, N. A., Steel, J. A., Reuben, R. L., Knabe, G., Dixon, D., & Shanks, R. L. (2006). Monitoring of rail-wheel interaction using Acoustic Emission (AE). _Advanced Materials Research_ , _13_ – _14_ , 161–168. https://doi.org/10.4028/0-87849-420-0.161 


- Tiboni, M., Remino, C., Bussola, R., & Amici, C. (2022). A Review on Vibration-Based Condition Monitoring of Rotating Machinery. _Applied Sciences (Switzerland)_ , _12_ (3). https://doi.org/10.3390/app12030972 


- Venkatasubramanian, V., Rengaswamy, R., & Kavuri, S. N. (2003). A review of process fault detection and diagnosis. Part II: Qualitative models and search strategies. _Computers & Chemical Engineering_ , _27_ (3), 313–326. https://doi.org/10.1016/s0098-1354(02)00161-8 

_Jurnal Dinamika Vokasional Teknik Mesin, Volume.09 No.1, April 2024 |_ 25 


- Venkatasubramanian, V., Rengaswamy, R., Kavuri, S. N., & Yin, K. (2003). A review of process fault detection and diagnosis. Part I: Quantitative model-based methods. _Computers & Chemical Engineering_ , _27_ (3), 327–346. https://doi.org/10.1016/s0098-1354(02)00162-x 


- Venkatasubramanian, V., Rengaswamy, R., Yin, K., & Kavuri, S. N. (2003). A review of process fault detection and diagnosis. Part III: Process history based methods. _Computers and Chemical Engineering_ , _27_ , 327–346. www.elsevier.com/locate/compchemeng 


- Verkhoglyad, A. G., Kuropyatnik, I. N., Bazovkin, V. M., & Kuryshev, G. L. (2008). Infrared diagnostics of cracks in railway carriage wheels. _Russian Journal of Nondestructive Testing_ , _44_ (10), 664–668. https://doi.org/10.1134/S1061830908100021 


- Wan, T. H., Tsang, C. W., Hui, K., & Chung, E. (2023). Anomaly detection of train wheels utilizing short-time Fourier transform and unsupervised learning algorithms. _Engineering Applications of Artificial Intelligence_ , _122_ (February). https://doi.org/10.1016/j.engappai.2023.106037 


- Wang, W., Guo, J., & Liu, Q. (2013). Experimental study on wear and spalling behaviors of railway wheel. _Chinese Journal of Mechanical Engineering (English Edition)_ , _26_ (6), 1243–1249. https://doi.org/10.3901/CJME.2013.06.1243 


- Wang, W., He, Q., Cui, Y., & Li, Z. (2018). Joint Prediction of Remaining Useful Life and Failure Type of Train Wheelsets: Multitask Learning Approach. _Journal of Transportation Engineering, Part A: Systems_ , _144_ (6). https://doi.org/10.1061/jtepbs.0000113 


- Xiaoyi, H., Haoran, Z., Zhikun, S., Yinqing, H., & Lan, L. (2018). Study on influence of high-order wheel polygon wear on dynamic performance of high-speed EMU vehicle. _11th International Conference on Contact Mechanics and Wear of Rail/Wheel Systems, Delft, The Netherlands_ . 


- Xie, B., Chen, S., Xu, M., Yang, Y., & Wang, K. (2022). Polygonal Wear Identification of Wheels Based on Optimized Multiple Kernel Extreme Learning Machine. _Lixue Xuebao/Chinese Journal of Theoretical and Applied Mechanics_ , _54_ (7), 1797–1806. https://doi.org/10.6052/0459-1879-22083 


- Xiong, L., Lv, L., Jiang, Y., Hua, C., & Dong, D. (2022). Multi-fault Classification of Train Wheelset System. _Journal of Physics: Conference Series_ , _2184_ (1). https://doi.org/10.1088/17426596/2184/1/012020 


- Xu, G., Hou, D., Qi, H., & Bo, L. (2021). High-speed train wheel set bearing fault diagnosis and prognostics: A new prognostic model based on extendable useful life. _Mechanical Systems and Signal Processing_ , _146_ . https://doi.org/10.1016/j.ymssp.2020.107050 


- Xu, M., & Yao, H. (2023). Fault diagnosis method of wheelset based on EEMD-MPE and support vector machine optimized by quantum-behaved particle swarm algorithm. _Measurement: Journal of the International Measurement Confederation_ , _216_ (March). https://doi.org/10.1016/j.measurement.2023.112923 


- Yan, B., Ma, X., Huang, G., & Zhao, Y. (2021). Two-stage physics-based Wiener process models for online RUL prediction in field vibration data. _Mechanical Systems and Signal Processing_ , _152_ , 107378. https://doi.org/10.1016/j.ymssp.2020.107378 


- Ye, Y., Huang, C., Zeng, J., Zhou, Y., & Li, F. (2023). Shock detection of rotating machinery based on activated time-domain images and deep learning: An application to railway wheel flat detection. _Mechanical Systems and Signal Processing_ , _186_ (May 2022). https://doi.org/10.1016/j.ymssp.2022.109856 


- Ye, Y., Shi, D., Krause, P., Tian, Q., & Hecht, M. (2020). Wheel flat can cause or exacerbate wheel polygonization. _Vehicle System Dynamics_ , _58_ (10), 1575–1604. https://doi.org/10.1080/00423114.2019.1636098 


- Ye, Y., Zhu, B., Huang, P., & Peng, B. (2022). OORNet: A deep learning model for on-board condition monitoring and fault diagnosis of out-of-round wheels of high-speed trains. _Measurement: Journal of the International Measurement Confederation_ , _199_ (February), 111268. https://doi.org/10.1016/j.measurement.2022.111268 


- Zhang, K., Li, Y., Scarf, P., & Ball, A. (2011). Feature selection for high-dimensional machinery fault diagnosis data using multiple models and Radial Basis Function networks. _Neurocomputing_ , _74_ (17), 2941–2952. https://doi.org/10.1016/j.neucom.2011.03.043 


- Zurek, Z. H. (2006). Magnetic monitoring of the fatigue process of the rim material of railway wheel sets. _NDT and E International_ , _39_ (8), 675–679. https://doi.org/10.1016/j.ndteint.2005.12.004