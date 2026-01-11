**==> picture [51 x 59] intentionally omitted <==**

Available online at www.sciencedirect.com 

# **ScienceDirect** 

Transportation Research Procedia 72 (2023) 4199–4206 

# Transport Research Arena (TRA) Conference 

# Machine learning approach for wheel flat detection of railway train 

wheels 

Araliya Mosleh[a] *, Andreia Meixedo[a] , Diogo Ribeiro[b] , Pedro Montenegro[a] , Rui Calçada[a] 

_aCONSTRUCT – LESE, Faculty of Engineering (FEUP), University of Porto, Portugal_ 

_bCONSTRUCT – LESE, School of Engineering, Polytechnic of Porto, Porto, Portugal_ 

## **Abstract** 

## 

Nowadays, monitoring the condition of railway infrastructure has become necessary and led railway companies to take advantage of artificial intelligence (AI) technologies to improve safety and reduce operating costs. This paper aims to present an unsupervised methodology to detect railway wheel flats. The automatic damage detection algorithm is based on the acceleration evaluated on the rails for the passage of traffic loads. The results of this research study show that only one sensor is enough to detect wheel flat automatically, which enables the development of a low-cost monitoring system that can be easily implemented in actual operating conditions. 

© 2023 The Authors. Published by ELSEVIER B.V. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer-review under responsibility of the scientific committee of the Transport Research Arena (TRA) Conference 

_Keywords:_ Machine learning; wheel flat detection; autoregressive model; principal component analysis; outlier analysis. 

## **1. Introduction** 

Defective wheels in railway wagons are identified as one of the most significant sources of damage to railway infrastructure and vehicles. Damage to the railway tracks can be caused by wheel defects, resulting in considerable maintenance costs for railway administrations as well as rolling stock operators. Regardless of the vehicle type, a wheel flat occurs when a wheel locks and slides over the rail (Li et al., 2016). The impact load caused by a defective 

* Corresponding author. Tel.: +351-225081901 

_E-mail address:_ amosleh@fe.up.pt 

2352-1465 © 2023 The Authors. Published by ELSEVIER B.V. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer-review under responsibility of the scientific committee of the Transport Research Arena (TRA) Conference 10.1016/j.trpro.2023.11.354 

4200 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

wheel, which depends on the depth and length of the flat, can be several times higher than the static load of the wheel (Mosleh, Montenegro, et al., 2020). Therefore, early detection of defective wheels prevents significant damage that may cause service interruption or derailment. 

Researchers have proposed onboard and wayside measurement methods for detecting wheel defects in the last decade. Onboard damage detection services require the installation of sensors on wheels to make a comprehensive diagnosis of the damage and to effectively manage the wheels condition. Due to the high costs and maintenance issues, this method is rarely used. In addition, onboard detection techniques are commonly used to monitor the track condition rather than the wheel condition. However, wayside measurement systems continue to provide the best way to identify wheel defects, since the condition of all wheels is assessed during the passage of trains in service. 

In previous studies, advanced signal processing methods were used to eliminate signal interference to diagnose faulty signal patterns of wheel flats (Amini et al., 2016; Jiang & Lin, 2018; Mosleh et al., 2021). While widespread research has been conducted on the detection of infrastructure defects (Defossez et al., 2015; Mohammadi et al., 2022; Mosleh, Costa, et al., 2020a; Yonas et al., 2015), particularly on railways (Pimentel et al., 2021; Pintão et al., 2022), a limited amount of literature has been published on automatic wheel flat identification. Therefore, artificial intelligence (AI) can be used to detect a defective wheel at an early stage and improve safety and reduce operating costs. 

Many researchers (Atamuradov et al., 2019; Do et al., 2019; Gibert et al., 2015; Meixedo et al., 2016; Meixedo et al., 2021; Nenov et al., 2011) used several machine learning algorithms to analyze the data, implement a learning scheme, and apply intelligent decisions regarding the presence of wheel flats, including artificial neural networks (ANN), principal component analysis (PCA), and support vector machines (SVM). 

Although a number of publications have been published about railway defect detection, there is limited literature on automatic early wheel flat detection to the best of the authors' knowledge. According to most wheel flat detection schemes, there is no indicator that can automatically differentiate a defective from a healthy wheel. Additionally, in all the above studies, multiple sensors are required to distinguish a defective wheel from a healthy one. Consequently, one of the goals of this research is to develop an unsupervised machine learning algorithm that can automatically detect a wheel flat, using only one sensor installed on the rail. The goal of this paper is to develop a 3D numerical dynamic model of vehicle-track coupling system and to develop an indicator for automatically detecting healthy wheels from defective ones. The acceleration measurement points are strategically defined in order to examine the sensitivity of the proposed methodology, to the position where they are installed. 

## **2. Train-track dynamic interaction** 

An in-house software program, VSI-Vehicle-Structure Interaction Analysis, is used for numerical train-track dynamic interaction simulations that have been validated and described in detail in a previous publication (Montenegro et al., 2015). In this model, the train is coupled to the track via a 3D wheel-rail contact model that uses Hertzian theory (Hertz, 1882) to compute the normal contact forces and USETAB routine (Kalker, 1996) to compute the tangential forces that arise from rolling friction creep. MATLAB® (MATLAB®, 2018) is used to implement the numerical tool, which imports structural matrices modeled in a finite element (FE) package for both the vehicle and the track. In this work, the track is modeled in the computer software program ANSYS® (ANSYS®, 2018) using beam elements for the rails and sleepers, spring-dashpot elements to simulate the behavior of the flexible layers, such as the ballast and fasteners, and mass point elements for taking into account the mass of the ballast. Train has been modeled in ANSYS® (ANSYS®, 2018) through a multibody formulation, using spring-dashpot elements to simulate the flexibility of the primary and secondary suspension, rigid beams to consider rigid body movements, and mass point elements located at the center of gravity of each body, namely carbodies, bogies, and wheelsets, to simulate their mass and inertial effects. The authors' previous publications describe both track and train models in detail (Mosleh et al., 2021; Mosleh, Montenegro, et al., 2020). 

## **3. A model-based approach** 

A virtual simulation of baseline (undamaged) and damaged wheel scenarios is accomplished to test and validate the automatic wheel flat detection approach presented in this study. Three intervals are defined for a damaged wheel 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

4201 

due to different wheel flat lengths (𝐿𝐿) and nominated as L1, L2 and L3. The uniform distributions U (10, 20) [mm], U (25, 50) [mm] and U (55,100) [mm] define the lower and upper limits of the wheel flat length for each interval L1, L2 and L3 respectively. In which 𝑅 is the radius of the wheel. The vertical profile deviation of the wheel flat (Z) is defined as follows: 

**==> picture [362 x 28] intentionally omitted <==**

where H represents the Heaviside function. The acceleration of the rail is evaluated for the 19 sensors shown in Figure 1, including several scenarios, for both baseline (undamaged) and damaged conditions to test the proposed methodology. Table 1 summarizes the 100 simulations of the undamaged scenarios that aim at reproducing the responses of the rail considering several speeds, loading schemes and unevenness profiles of the rail. 

**==> picture [329 x 64] intentionally omitted <==**

Fig.1. Virtual wayside monitoring system. 

The selected unevenness profiles of the rail are measured on the Northern Line of the Portuguese Railway Network according to the details provided by Mosleh et al. (Mosleh, Costa, et al., 2020b). The dynamic analyses are carried out for one passing vehicle of the Alfa Pendular (AP) passenger train (Ribeiro et al., 2013). Moreover, 150 simulations are performed for the damaged scenarios considering several combinations of flat properties for defective wheels circulating at 60 m/s. 

Table 1. Damaged and undamaged scenarios. 

|Train|Undamaged scenarios<br>Alfa Pendular|Damaged scenarios<br>Alfa Pendular| |---|---|---| |Number of Loading schemes|3 types|1 type| |Unevenness profile|10 profiles|1 profile| |Speeds|20-60 m/s|60 m/s| |Noise ratio|5%|5%| |Flat characteristics|-|Flat lengths: 10-20(L1),25-50(L2),55-100(L3)mm| |Total analysis|100|150|



## **4. Automatic wheel flat detection** 

## _4.1. Overview_ 

The methodology developed and implemented in this work aims to automatically detect wheel flats through the following five steps (Meixedo et al., 2021): (i) data acquisition, (ii) features extraction from acquired responses using an autoregressive (AR) model, (iii) feature normalization to remove the environmental and operational variations (EOVs) by applying a latent-variable method named principal component analysis (PCA), (iv) data fusion, through the implementation of a Mahalanobis distance, to merge the features from each sensor and enhance sensitivity to detect wheel defects, and (v) unsupervised feature classification through outlier analyses (Meixedo et al., 2022). 

4202 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

## _4.2. Feature extraction with AR approach_ 

In this study, individual AR (30) parameters are used to fit each accelerometer's time series, and their parameters are used as damage-sensitive features. Therefore, the outcome of applying the AR model to the 250 scenarios for each of the 19 measurements presented in Fig.1 is a three-dimensional feature matrix of 250 by 30 by 19. Fig.2 shows 4 features out of 30 for all 250 scenarios for the accelerations measured on position 1. Due to the condition of the train's wheel, the features are divided into two major categories, namely baseline scenarios (first 100 passages) and damaged scenarios (150 subsequent passages). For damaged scenarios, simulations 101 to 150 consider the passage of a vehicle with a wheel flat length between 10 and 20 mm (L1), while simulations 151 to 200 consider a wheel flat length between 25 and 50 mm (L2). Afterward, the range of 55 to 100 mm (L3) is considered for the wheel flat length corresponding to simulations 201 to 250. As presented in this figure, the AR parameters for damaged scenarios exhibit a higher fluctuation than a range of baseline scenarios. 

**==> picture [285 x 296] intentionally omitted <==**

**==> picture [85 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig.2. Feature extraction.<br>**----- End of picture text -----**<br>


## _4.3. Feature normalization with PCA approach_ 

Performing PCA modeling on AR parameters resulted in a 19-by-30 matrix that has PCA-based features for every vehicle passage. Since the cumulative percentage of variance for the first component is greater than 80%, it is discarded during model development (i.e., p = 1). For the accelerations measured on position 1, Fig.3 shows four PCA features out of 30 for all 250 baseline and damaged scenarios. As presented in this figure, although suppression of the changes generated by EOVs, the differences between healthy wheels and damaged ones are not sufficient to detect a defective wheel. Therefore, a data fusion is performed and discussed in the next section. 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

4203 

**==> picture [285 x 307] intentionally omitted <==**

**==> picture [96 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig.3. Feature normalization.<br>**----- End of picture text -----**<br>


## _4.4. Data fusion_ 

The Mahalanobis distance transforms the 30 AR-PCA-based parameters into one single damage-sensitive feature for each sensor and vehicle passage. For each of the 19 sensors, this procedure yields a 250-by-1 vector of distances. Fig.4 shows a noticeable improvement in sensitivity for the various sensors. 

4204 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

**==> picture [285 x 202] intentionally omitted <==**

Fig.4. Damage index (DI) for all 250 train passages. 

## _4.5. Automatic wheel flat detection based on a statistical approach_ 

Fig.5 allows observing different damage behaviours between three intervals, namely L1, L2 and L3, corresponding to low, median and severe wheel flat lengths. From the results presented in this figure, it is possible to infer that the methodology can effectively detect all the damage scenarios without any false positives or false negatives. One of the main advantages of the proposed methodology is that it is not necessary to install a series of sensors on the rail. Only one sensor is adequate to detect a defective wheel. Therefore, the proposed methodology has the advantage of minimizing the cost of the installation system, as well as allowing a more automatic and straightforward implementation. Such results clearly show the great potential of this innovative application of data mining in the railway industry. 

**==> picture [173 x 203] intentionally omitted <==**

Fig.5. Automatic wheel flat detection. 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

4205 

## **5. Conclusion** 

This paper aims to develop an unsupervised damage detection methodology capable of automatically detecting a defective train wheel at an early stage. One of the main advantages of the proposed methodology compared to the previous ones (Krummenacher et al., 2018; Ni & Zhang, 2020) is that no require the installation of many sensors on the rail. A defective wheel can only be detected by only one sensor. Due to this, the proposed methodology has the advantage of requiring only one sensor and therefore minimizing the cost of the installation system, as well as allowing a more automatic and straightforward implementation process. 

Future work includes a field trial to evaluate further the usefulness of the technology developed. Moreover, for the final development of the proposed methodology, it is imperative to develop an automatic indicator to distinguish a wheel flat from other types of wheel defects, i.e., polygonization or out of roundness. 

## **Acknowledgments** 

This work was financially supported by Base Funding-UIDB/04708/2020 and Programmatic Funding-UIDP/04708/2020 of the CONSTRUCT - Instituto de Estruturas e Construções, funded by national funds through the FCT/MCTES (PIDDAC). Moreover, the first author acknowledges Grant no. 2021.04272.CEECIND from the Stimulus of Scientific Employment, Individual Support (CEECIND) - 4rd Edition provided by ‘‘FCT – Fundação para a Ciência e Tecnologia’’. The paper reflects research developed in the ambit of the project Way4SafeRail, NORTE-01-0247-FEDER-069595, founded by Agência Nacional de Inovação S.A., program P2020|COMPETE – Projetos em Copromoção. This work is a result of the project "FERROVIA 4.0", with reference POCI-01-0247-FEDER- 046111, co-funded by the European Regional Development Fund (ERDF), through the Operational Programme for Competitiveness and Internationalization (COMPETE 2020) and the Lisbon Regional Operational Programme (LISBOA 2020), under the PORTUGAL 2020 Partnership Agreement". 

## **References** 

Amini, A., Entezami, M., Huang, Z., Rowshandel, H., & Papaelias, M. (2016). Wayside detection of faults in railway axle bearings using time spectral kurtosis analysis on high-frequency acoustic emission signals. _Advances in Mechanical Engineering_ , _8_ (11). https://doi.org/10.1177/1687814016676000 ANSYS®. (2018). Academic Research, Release 19.2, ANSYS Inc. Atamuradov, V., Medjaher, K., Camci, F., Dersin, P., & Zerhouni, N. (2019). Railway Point Machine Prognostics Based on Feature Fusion and Health State Assessment. _IEEE Transactions on Instrumentation and Measurement_ , _68_ (8), 2691 - 2704. https://doi.org/10.1109/TIM.2018.2869193 Defossez, F., Pislaru, C., Ulianov, C., Carter, E., Rantaldo, M., Larsson, D., & Blacktop, K. (2015). _The sustainable freight railway: Designing the freight vehicle – track system for higher delivered tonnage with improved availability at reduced cost, wp4 - Track based monitoring and limits for imposed loads_ ( 


- Do, L., Vu, H., Vo, B., Liu, Z., & Phung, D. (2019). An effective spatial-temporal attention based neural network for traffic flow prediction. _Transportation Research Part C: Emerging Technologies_ , _108_ , 12-28. https://doi.org/10.1016/j.trc.2019.09.008 


- Gibert, X., Patel, V., & Chellappa, R. (2015). Deep Multitask Learning for Railway Track Inspection. _IEEE Transactions on Intelligent Transportation Systems_ , _18_ (1), 153 - 164. https://doi.org/10.1109/TITS.2016.2568758 


- Hertz, H. (1882). Ueber die Berührung fester elastischer Körper [On the contact of elastic solids]. _Journal für die reine und angewandte Mathematik_ , _92_ , 156-171. 


- Jiang, H., & Lin, J. (2018). Fault diagnosis of wheel flat using empirical mode decomposition-Hilbert envelope spectrum. _Mathematical Problems in Engineering_ , _2018_ , 1-16. https://doi.org/10.1155/2018/8909031 


- Kalker, J. J. (1996). Book of tables for the Hertzian creep-force law. (Ed.),^(Eds.). 2nd Mini Conference on Contact Mechanics and Wear of Wheel/Rail Systems, Budapest, Hungary. 


- Krummenacher, G., Ong, S., Koller, S., Kobayashi, S., & Buhmann, J. M. (2018). Wheel Defect Detection With Machine Learning. _IEEE Transactions on Intelligent Transportation Systems_ , _19_ (9), 1176 - 1187. https://doi.org/1110.1109/TITS.2017.2720721 


- Li, Y., Liu, J., & Wang, Y. (2016). Railway Wheel Flat Detection Based on Improved Empirical Mode Decomposition. _Shock and Vibration_ (Article ID 4879283). https://doi.org/10.1155/2016/4879283 


- MATLAB[®] . (2018). Release R2018a, The MathWorks Inc. 


- Meixedo, A., Alves, V., Ribeiro, D., Cury, A., & Calçada, R. (2016). Damage identification of a railway bridge based on genetic algorithms. (Ed.),^(Eds.). Proceedings of the 8th International Conference on Bridge Maintenance, Safety and Management, IABMAS Foz do Iguacu, 

4206 

_Araliya Mosleh et al. / Transportation Research Procedia 72 (2023) 4199–4206_ 

## 

Brazil. 


- Meixedo, A., Santos, J., Ribeiro, D., Calçada, R., & Todd, M. (2021). Damage detection in railway bridges using traffic-induced dynamic responses. _Engineering Structures_ , _238_ , 112189, doi:112110.111016/j.engstruct.112021.112189. https://doi.org/10.1016/j.engstruct.2021.112189 


- Meixedo, A., Santos, J., Ribeiro, D., Calçada, R., & Todd, M. (2022). Online unsupervised detection of structural changes using train–induced dynamic responses. _Mechanical Systems and Signal Processing_ , _165_ , 108268, doi:108210.101016/j.ymssp.102021.108268. https://doi.org/10.1016/j.ymssp.2021.108268 


- Mohammadi, M., Mosleh, A., Razzaghi, M., Costa, P., & Calçada, R. (2022). Stochastic analysis of railway embankment with uncertain soil parameters using polynomial chaos expansion. _Structure and Infrastructure Engineering_ (doi: 10.1080/15732479.2022.2033277). 


- Montenegro, P. A., Neves, S. G. M., Calçada, R., Tanabe, M., & Sogabe, M. (2015). Wheel-rail contact formulation for analyzing the lateral trainstructure dynamic interaction. _Computers & Structures_ , _152_ , 200-214. https://doi.org/10.1016/j.compstruc.2015.01.004 


- Mosleh, A., Costa, P., & Calçada, R. (2020a). Development of a Low-Cost Trackside System for Weighing in Motion and Wheel Defects Detection. _International Journal of Railway Research_ , _7_ (1), 1-9, doi:10.22068/IJRARE.22067.22061.22061. https://doi.org/10.22068/IJRARE.7.1.1 


- Mosleh, A., Costa, P., & Calçada, R. (2020b). A new strategy to estimate static loads for the dynamic weighing in motion of railway vehicles. _Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit_ , _234_ (2), 183-200, doi: 110.1177/0954409719838115. https://doi.org/10.1177/0954409719838115 


- Mosleh, A., Montenegro, P., Costa, P., & Caçada, R. (2021). Railway Vehicle Wheel Flat Detection with Multiple Records Using Spectral Kurtosis Analysis. _Applied Sciences_ , _11_ (9), doi: 10.3390/app11094002. https://doi.org/10.3390/app11094002 


- Mosleh, A., Montenegro, P. A., Costa, P., & Calçada, R. (2020). An approach for wheel flat detection of railway train wheels using envelope spectrum analysis. _Structure and Infrastructure Engineering_ , 1-20, doi: 10.1080/15732479.15732020.11832536. https://doi.org/10.1080/15732479.2020.1832536 


- Nenov, N., Dimitrov, E., Vasilev, V., & Piskulev, P. (2011). Sensor system of detecting defects in wheels of railway vehicles running at operational speed. _Proc. 34th Int. Spring Seminar on Electron. Technol. (ISSE)_ , 577–582. 


- Ni, Y., & Zhang, Q. (2020). A Bayesian machine learning approach for online detection of railway wheel defects using track-side monitoring. _Structural Health Monitoring_ , _20_ (4), 1-15. https://doi.org/10.1177/1475921720921772 


- Pimentel, R., Ribeiro, D., Matos, L., Mosleh, A., & Calçada, R. (2021). Bridge Weigh-in-Motion system for the identification of train loads using fiber-optic technology. _Structures_ , _30_ , 1056-1070, doi: 1010.1016/j.istruc.2021.1001.1070. https://doi.org/10.1016/j.istruc.2021.01.070 


- Pintão, B., Mosleh, A., Vale, C., PA., M., & Costa, P. (2022). Development and Validation of a Weigh-in-Motion Methodology for Railway Tracks. _Sensors_ , _22_ (5), 1976, doi: 1910.3390/s22051976. https://doi.org/10.3390/s22051976 


- Ribeiro, D., Calçada, R., R., D., Brehm, M., & Zabel, V. (2013). Finite-element model calibration of a railway vehicle based on experimental modal parameters. _Vehicle System Dynamics_ , _51_ (6), 821-856. 


- Yonas, L., Matthias, A., & Matti, R. (2015). Investigation of the Top-of-Rail Friction by Field Measurements on Swedish Iron Ore Line. _International Journal of COMADEM_ , _18_ (2), 17-20.