## 

Wheel-bearing Fault Diagnosis of Trains using Empirical Wavelet Transform 

Hongrui Cao, Fei Fan, Kai Zhou, Zhengjia He 

|PII:|S0263-2241(16)00037-3| |---|---| |DOI:|http://dx.doi.org/10.1016/j.measurement.2016.01.023| |Reference:|MEASUR 3766| |To appear in:|Measurement| |Received Date:|4 May 2015| |Revised Date:|5 December 2015| |Accepted Date:|9 January 2016|



**==> picture [134 x 185] intentionally omitted <==**

Please cite this article as: H. Cao, F. Fan, K. Zhou, Z. He, Wheel-bearing Fault Diagnosis of Trains using Empirical Wavelet Transform, Measurement (2016), doi: http://dx.doi.org/10.1016/j.measurement.2016.01.023 

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. 

# **Wheel-bearing Fault Diagnosis of Trains using Empirical Wavelet Transform** 

## Hongrui Cao, Fei Fan, Kai Zhou, Zhengjia He 

State Key Laboratory for Manufacturing and Systems Engineering, 

Xi’an Jiaotong University, Xi’an 710049, PR China 

**Abstract:** Rolling bearings are used widely as wheel bearing in trains. Fault detection of the wheel-bearing is of great significance to maintain the safety and comfort of train. Vibration signal analysis is the most popular technique that is used for rolling element bearing monitoring, however, the application of vibration signal analysis for wheel bearings is quite limited in practice. In this paper, a novel method called empirical wavelet transform (EWT) is used for the vibration signal analysis and fault diagnosis of wheel-bearing. The EWT method combines the classic wavelet with the empirical mode decomposition, which is suitable for the non-stationary vibration signals. The effectiveness of the method is validated using both simulated signals and the real wheel-bearing vibration signals. The results show that the EWT provides a good performance in the detection of outer race fault, roller fault, and the compound fault of outer race and roller. 

**Key words:** wheel-bearing; vibration signal; empirical wavelet transform; faults diagnosis 

## **1. Introduction** 

With the rapid development of the national economy, railway traffic plays a more and more crucial role in the transport system. It is an important mission to guarantee the trains for passengers and freight transportation to operate safely and stably. Wheel-bearings are essential mechanical component of trains. Rolling bearings are used widely as wheel bearing in trains. The heavy-load and long-term alternating stress operating conditions can easily lead to all kinds of roller bearing failure, such as pitting, spalling, and axle burn off [1-3]. According to the statistics, bearing failure is one of the most common failure modes of railroad trains [2-3]. Therefore, it is of great importance to detect defects, to maintain the safety, the stability and the comfort, especially for the rapid development of trains’ speed in recent years [4]. 

For bearing fault diagnosis, there exist various kinds of technologies. They include on board condition monitors, base station monitoring systems and wayside detecting systems, such as oil monitoring/ferrographic monitoring, hot-box detectors, acoustic emission (AE) and vibration signal analysis. 

Oil monitoring includes physical and chemical analysis, ferrographic analysis, infrared spectra analysis, spectroscopy analysis, contamination analysis [5-7]. Oil monitoring is to extract the oil sample of lubricant used in train bearings to get the operation information through measuring its degradation degree, analyzing the wear position, the failure modes as well as the degree of the wear. Oil monitoring has been proven in many instances to be a both predictive and proactive tool to identify the incipient fatigue and wear modes. However, the main limitation is that it is just suitable for oil lubrication bearings and time-consuming. Besides, it is difficult to apply oil analysis to on-board monitoring [7]. 

In addition, some other inspection techniques have been developed to identify defective bearings prior to failure. The hot-box detection method is common used in practice [1, 3, 8, 9-10]. The method is to monitor the condition of bearing through detecting the temperature of bearing box. There are two kinds of 

detection systems. One is real-time on-board system with temperature sensors mounted on the bearings in each carriage. The other on is wayside system, such as HBD system (Hot Bearing Detector). The systems issue an alarm if the bearing operating temperature exceeds the user preset threshold. But the temperature doesn’t raise much in early failure. The catastrophic failure of roller bearing happens very quickly and may result in axle burn-off, which can lead to derailment and break down. This is dangerous for the safety of trains. 

In order to detect early bearing failure, acoustic emission technology is applied to monitoring rotating machinery [2, 11-12], for example, rolling bearings. Acoustic emission technology is to measure transient elastic waves generated from the interaction because of the damage on the bearing elements [13]. Although acoustic emission technology is proved to be useful, the successful application of acoustic emission to bearing fault diagnosis is very limited. The main drawback is that the attenuation of the signal is very severe. Hence, the acoustic emission sensors need to be close to the train bearings and to be placed on the non-rotating parts of wheel-bearing, which may be inconvenient to the complicated monitoring system. However, how to process, interpret and classify the information from the acquired data is also a big difficulty that baffles the researchers [14-17]. 

Vibration signal analysis is probably the most important and popular technique that is used for rolling element bearing monitoring [16]. The signal generated by bearing vibration is full of rich information and is sensitive to different fault types. There has been proved that this method has the ability to detect early fault and offer reliable results. The diagnosis based on vibration signals has attracted wide attention in recent years [18-19]. Lots of research work about rolling element bearings based on the vibration methods has been reported. These methods can be classified into three categories according to the feature, named time-domain method, frequency-domain method, and time-frequency domain method. The time-domain method is to measure the statistical parameters from the time domain signal, for example, variance, peak to peak value, and kurtosis. Frequency-domain methods, including the Fourier transform, fast Fourier transform and power spectrum and so on, are able to lock the certain frequency range that we are interested in [20-22]. Time-domain and frequency-domain method may lead to false results when applied to non-stationary signals, because these methods are based on the assumption that the process generating the signals is stationary and linear [23]. In recent years, many advanced time-frequency domain signal processing methods, such as short time Fourier transform(STFT) [24], Wigner-Ville distribution [25], wavelet transform [26-27], local mean decomposition(LMD) [28-29] and empirical mode decomposition(EMD) [30-31], have been utilized to deal with non-stationary signals for fault diagnosis of rotating machinery. Empirical mode decomposition, proposed by Huang et al., is one of the most powerful time-frequency methods to deal with non-stationary data [32]. It is based on the local characteristic in time domain waveform of the signal. The empirical mode decomposition method can decompose any signals into some members called intrinsic mode function (IMF) and a final residue. The IMFs indicate the natural oscillatory mode imbedded in the signal and work as the basis functions without pre-established. Since EMD was presented in 1998, it has drawn wide attention and been extensively studied in various fields, for example, medicine and biology [33], crack-induced response analysis [34], image processing [35], fault diagnosis [30]. Wu and Huang applied EMD to white noise and found empirically that EMD was effectively a dyadic filter [36]. Flandrin et al. showed that EMD was equivalent to filter banks on signals from stochastic processes [37]. Kopsinis and McLaughlin put forward EMD denoising method which was similar to wavelet denoising methods after studying wavelet thresholding [38]. In last few years, some researchers try to build EMD mathematical model. Daubechies et al. proposed a mode and built a function to represent the signal. Then they could use the function to detect 

different modes in signals [39]. Inspired by the EMD and compressed sensing, Hou et al. raised the idea to look for the sparest representation from the AM-FM formalism, then to retrieve the modes by error analysis under certain assumptions [40]. Jerome Gilles combined the wavelet transforms and EMD creatively. The author try to put the adaptability of dividing the signal spectrum in EMD method into wavelet transform. This can change the traditional spectrum division of binary wavelet. Based on this idea, they proposed a method called empirical wavelet transform (EWT) [41]. It has proved that this method can separate different modes and offer more reliable results compared with EMD. 

In this paper, we will introduce the empirical wavelet transform into fault diagnosis field. This method is verified by simulated signal and the results are compared with EMD. Then this method with Hilbert transform demodulation analysis is applied to practical vibration signals under different fault conditions, because the vibration signals are accompanied by modulation phenomenon in the practical engineering. Both the results show the effectiveness of this new method. 

The remainder of this paper is organized as follows. A brief introduction of EMD and a description of the empirical wavelet transform are given in section 2. In section 3, two simulated signals are used to validate the EWT, compared with the results of EMD .In section 4, the method is applied to wheel bearing of train for passengers. 

**==> picture [37 x 36] intentionally omitted <==**

## **2. Empirical Wavelet Transform** 

## 2.1. Overview of empirical mode decomposition 

Huang et al. introduced the use of empirical mode decomposition [32]. This method is able to decompose a multi-component signal into some IMFs. According to the definition, a function is an IMF if it satisfies the following two conditions: (1) the number of extrema and the number of zero crossings are equal or differ at most by one, and (2) the mean of the envelope defined by local maxima(upper envelope) and the envelope defined by local minima(lower envelope) is zero. The algorithm of the EMD is implemented through three steps as follows: 

Step 1: extract all the local maxima and local minima and connect the extrema using cubic spline as the upper and lower envelope respectively. 

Step 2: Get the component _[h]_ 1[ by taking the difference between the original signal][ ( )] _x t_ and the mean of the two envelopes. 

Step 3: Treat _[h]_ 1[ as the original signal and repeat step1and 2 until the component satisfies the ] 

definition of IMF. Then the final component is named as _[c]_ 1[ , which represent an IMF. After that, the ] 

residue between ( ) _x t_ and the _[c]_ 1[ is repeated step 1 and 2 until the residue is a monotonic function or a ] constant. 

After the decomposition, we get a number of IMFs _[c i] i_ (  1,2, , ) _n_ and a residue _nr_ , which is the _n_ mean trend of ( ) _x t_ . Then the original signal ( ) _x t_ can be formulated as _x t_ ( )   _c ti_ ( )  _rn_ . The IMF _i_  1 

components, such as _[c]_ 1[ ,] _[c]_[ , represent the frequency bands from high to low. A more detailed about the ] 2 

EMD algorithm can be found in Ref. [32]. 

**==> picture [34 x 34] intentionally omitted <==**

## 2.2. Empirical wavelet transform 

Empirical wavelet transform is a newly proposed method to detect the different members called modes adaptively [41]. In the view of Fourier domain, empirical wavelets means to build a set of wavelets to process the signal which is equivalent to build a set of band-pass filters. Adaptability is reflected in detecting the filters’ supports according to the information located in the original signal inspired by the empirical mode decomposition. The modes are AM-FM components that have compact support Fourier spectrum [39]. So detecting the different modes is similar to divide the Fourier spectrum and to apply filtering according to the support. 

First, we need to divide the Fourier. The segmentation of Fourier axis depends on where the information in the spectrum of the original signal, which reflects the adaptability. Segmentation of Fourier axis aims to divide the different portions which correspond to different modes which are centered around a specific frequency and compact support like IMF. Assume that we want to segment the Fourier spectrum into N continuous segments. In this case, we need to find (N-1) largest local maxima in the Fourier spectrum. 0 and  are always used in this method (the Fourier is normalized). For this set of maxima, we define that  _n_ is the limits between each segments, where  0 0 and  _N_   . Each segment is 

denoted as  _n_ [  _n_  1,  _n_ ], then _Nn_  1[] _n_ [0, ]  , see Fig.1. 

**==> picture [452 x 114] intentionally omitted <==**

## Fig.1. Segmentation of the Fourier axis 

Centered on each  _n_ , we define a transition phase _[T] n_[ with width][ 2]  _n_ and  _n_  _n_ .  is properly 

chose to get a tight frame and is given in Eq.(1). 

**==> picture [453 x 48] intentionally omitted <==**

Next, a series of empirical wavelets are constructed based on the idea used in the construction of Little-wood-Paley and Meyer’s wavelets [42]. For  _n_ 0 , the empirical scaling function and the empirical wavelet function can be defined by the following expressions, respectively: 

**==> picture [460 x 95] intentionally omitted <==**

and 

**==> picture [453 x 136] intentionally omitted <==**

The function,  ( ) _x_  _x_ 4(35 84  _x_  70 _x_ 2  20 _x_ 3) , which is the most common used [42]. So, for  _n_ 0 , equation (1) and (2) can be simplified to (4) and (5) as follows: 

**==> picture [453 x 95] intentionally omitted <==**

**==> picture [453 x 126] intentionally omitted <==**

The Empirical Wavelet Transform (EWT) is defined in the similar way with the classic wavelet transform. The detailed coefficients _Wf_  ( , ) _n t_ are given in Eq. (6), by the inner products with the empirical wavelets: 

**==> picture [453 x 32] intentionally omitted <==**

And the approximation coefficients _Wf_  (0, ) _t_ is given in Eq.(5), also by the inner products with the scaling function: 

**==> picture [453 x 32] intentionally omitted <==**

Then the reconstruction signal and the empirical mode are given in Eq.(8),(9) and (10). 

**==> picture [460 x 125] intentionally omitted <==**

## **3. Simulation validation** 

To verify the effectiveness of EWT, two simulation signals are considered in this section. When the faults of the rotating machinery such as rolling element bearing occur, the signal is often comprised of different harmonic components and impulses. First we consider the synthesized signal which is composed of cyclical impulses and white noise. This is used to validate if EWT is robust to noise. The mixed signal is established as 

**==> picture [435 x 32] intentionally omitted <==**

where _wn_  1500, _j_  0.035 . The time waveforms of the original signal _x t_ 0[( )] , the white noise ( ) _n t_ and the mixed signal ( ) _x t_ are given in Fig.2. 

**==> picture [434 x 203] intentionally omitted <==**

**----- Start of picture text -----**<br> 1<br>0<br>-1<br>0 0.02 0.04 0.06 0.08 0.1<br>2<br>0<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>2<br>0<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>Time (s)<br>(t)<br>x0<br>n(t)<br>x(t)<br>**----- End of picture text -----**<br>


**==> picture [37 x 36] intentionally omitted <==**

Fig.2.The time domain waveforms of _x t_ 0[( )] , ( ) _n t_ and the mixed signal ( ) _x t_ 

For the purpose of comparison, the EWT and EMD are all employed to decompose the synthesized signal. The components obtained by EWT and EMD are given in Figs.3-4 respectively, where IMF stands for intrinsic mode function. From Figs.3-5, it can be found that EWT has performed well and the component mode 2 is in agreement with the real impulse component. EMD decomposes the signal into 12 IMFs from high frequency to low frequency in order. Fig.4. just shows the former 4 IMFs. Due to the noise interference, EMD yielded false components without physical meanings. 

**==> picture [460 x 454] intentionally omitted <==**

**----- Start of picture text -----**<br> 0.25 2<br>0<br>0.2<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>0.15 2<br>0<br>0.1 -2<br>0 0.02 0.04 0.06 0.08 0.1<br>5<br>0.05<br>0<br>0 -5<br>0 1000 2000 3000 4000 5000 6000 7000 0 0.02 0.04 0.06 0.08 0.1<br>Frequency (Hz) Time (s)<br>(a) (b)<br>Fig.3 (a) The segmentation of the frequency spectrum; (b) EWT results of the mixed signal<br>2<br>0<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>2<br>0<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>2<br>0<br>-2<br>0 0.02 0.04 0.06 0.08 0.1<br>1<br>0<br>-1<br>0 0.02 0.04 0.06 0.08 0.1<br>Time (s)<br>Amplitude<br>mode 1<br>mode 2<br>mode 3<br>IMF 1<br>IMF 2<br>IMF 3<br>IMF 4<br>**----- End of picture text -----**<br>


Fig.4. EMD results of the mixed signal 

In sum, the analysis results indicate that EWT is more robust to the noise and gets more accurate components, compared with the EMD. The EWT has a well performance in dealing with multi-component signal and can distinguish the different members. 

## **4. Fault diagnosis for wheel-bearing of train** 

The wheel bearing is one of the most important parts in the train. So the research of the fault detection for wheel bearing is of great importance. Once the outer race, the inner race or the rolling element occur typical fault, the vibration signal often shows unilateral oscillation attenuation waveform. When the compound faults exist, the traditional methods used in fault diagnosis are often unavailable. In this section, the effectiveness of the proposed method is validated by the vibration signals collected from real wheel-bearings. 

Fault types of testing bearings in electric locomotives include outer race fault, ball fault, outer race and ball composite fault, respectively. The bearing type is 552732QT and detailed geometric parameters of the rolling bearings are listed in the following Table 1. Acceleration sensors are used to collect 

vibration signals at the sampling frequency 12.8 kHz. 

Once defects occur, the bearing generates a series of periodic vibrations when the rolling elements passing over the defects and the vibrations appear at a certain frequency which is related to the rotational speed, geometric parameters and the locations of the defects [15]. For a given bearing, the defective frequencies are as follows: 

||**Table 1 Thegeometricparameters of the bearing**| |---|---| ||Outer race diameter<br>290mm<br>Inner race diameter<br>160mm<br>Rolling element diameter<br>34 mm<br>Contact angle<br>0o<br>Roller number<br>17| ||Defective frequency of the outer race<br>_of_:|



**==> picture [453 x 69] intentionally omitted <==**

**==> picture [453 x 79] intentionally omitted <==**

Defective frequency of the rolling element _[f]_[ : ] _r_ 

**==> picture [453 x 48] intentionally omitted <==**

Where _[f]_[ means the shaft rotation frequency,] _s_[][means the contact angle,] _[ z]_[ means the number of the ] rolling elements, _d_ and _D_ mean the rolling element diameter and pitch diameter, respectively. 

4.1. **Case 1: outer ring fault** 

Fig.5 shows the rolling bearing with a slight rub fault in the outer race. Fig.6 (a) and (b) are the time-domain signal and its corresponding frequency spectrum at speed of 460r/min. Based on the geometrical parameters of the bearing and rotating speed, characteristic frequency of the outer race is calculated at 55.29Hz. It is obvious that impulse features are buried in the background noise and are difficult to be distinguished in Fig.6 (a).In addition, it could be found that the intermediate and high frequency components occupy a large proportion in Fig.6 (b). Characteristic frequency 55.29Hz is submerged in the environmental noise. 

With the purpose of detecting the feature related to the failure, the EWT method is used to analyze the signal in Fig.6 (a). The segmentation of the frequency spectrum and the EWT results are shown in Fig.7. The whole spectrum is divided into four regions and 4 different modes are obtained in total. As is 

shown in Fig.7 (b), periodic impulses are obvious in mode 1 and mode 2, therefore we apply Hilbert transform to these two modes. 

**==> picture [460 x 633] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig.5 Slight rub in the outer race<br>(a) (b)<br>Fig.6 (a) The time-domain signal; (b) The frequency spectrum<br>(a) (b)<br>Fig.7 (a) The segmentation of the frequency spectrum; (b) The EWT results<br>**----- End of picture text -----**<br>


**==> picture [485 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br> (a) (b)<br>**----- End of picture text -----**<br>


Fig.8 (a) The Hilbert envelope spectrum of mode 1; (b) The Hilbert envelope spectrum of mode 2 

As is shown in Fig.8 (a) and (b)，both 54.69Hz and its harmonics can be found in the Hilbert envelope spectrum of mode 1 and mode 2. What's more, the frequency component 54.69 Hz is close to the characteristic frequency of the outer race fault 55.29 Hz, which indicates that fault occurs on the outer race of rolling element bearing and the effectiveness of EWT to extract the fault feature. 

4.2. **Case 2: rolling element fault** 

Fig.9 Rub fault in the roller. 

Fig.9 shows the rolling bearing with roller rub fault. Fig.10 (a) and (b) are the time-domain signal and its corresponding frequency spectrum at speed of 530r/min. Based on the geometrical parameters of the bearing and rotating speed, characteristic frequency of the outer race is calculated at 28.56Hz.According to Fig.10 (b), it could be found that the intermediate and high frequency components occupy a large proportion in Fig.6 (b). Characteristic frequency 28.56Hz is submerged in the environmental noise. 

In order to detect the potential fault characteristic frequency, we apply the EWT method to analyze the signal in Fig.10 (a). The segmentation of the frequency spectrum and the EWT results are shown in 

Fig.11. The whole spectrum is divided into three regions and three different modes are obtained in total. It is obvious that mode 2 and mode 3 contains more abundant impulse information. Therefore, Hilbert envelope analysis is applied to mode 2 and mode 3. Both the frequency component 27.08Hz closing to the fault characteristic frequency 28.56Hz of the rolling elements and its second harmonic frequency could be found in the Hilbert envelope spectrum of mode 2 and mode 3, which reveals the existence of fault on the rolling element. With the EWT method, we diagnose the roller rub fault successfully. 

**==> picture [463 x 438] intentionally omitted <==**

**----- Start of picture text -----**<br> (a) (b)<br>Fig.10 (a) The time-domain signal; (b) The frequency spectrum<br>(a) (b)<br>**----- End of picture text -----**<br>


Fig.11 (a) The segmentation of the frequency spectrum; (b) The EWT results 

**==> picture [460 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br> (a) (b)<br>**----- End of picture text -----**<br>


Fig.12 (a) The Hilbert envelope spectrum of mode 2; (b) The Hilbert envelope spectrum of mode 3 

## 4.3. **Case3: compound fault (outer race + rolling element)** 

Fig.13 The outer race and roller compound fault 

Fig.13 shows the rolling bearing with outer-race and roller composite fault. Time-domain signal and 

its corresponding frequency spectrum at speed of 515r/min are presented in Fig.14 (a) and (b). As is shown in Fig.14 (a), vibration signal component is complex and useful fault diagnosis information is buried in strong background noise, leading to impulse features information about the fault is hard to be recognized. From Fig.14 (b), we can see the high frequency components occupy a large proportion and it is hard to distinguish fault characteristic frequency directly. 

To extract all the information about the failure, the EWT method is applied to analyze the vibration signal. The segmentation and decomposition result are shown in Fig.14 and Fig.15 (a) and (b). There are no obvious differences among the three modes. Therefore, we apply the Hilbert envelope transform to all the modes, respectively. Fig.16 (a), (b) and (c) are the Hilbert envelope spectrum of the three modes. 

From Fig.16 (a), we couldn’t find any fault characteristic frequency. In Fig.16 (b), we could find frequency components 27.78Hz closing to outer race fault characteristic frequency 27.8 Hz and 62.5 Hz closing to ball fault characteristic frequency 61.9 Hz. However, we could merely find the frequency components 62.5 Hz closing to ball fault characteristic frequency 61.9 Hz. Combining the analytical 

results of mode 2 and mode 3, we can infer the existence of outer-race and roller composite fault. Although EWT can’t separate these two faults into different modes completely, the results also indicate that the feature of compound faults can be extracted, which means that the compound faults of the wheel-bearing are diagnosed successfully. 

**==> picture [459 x 461] intentionally omitted <==**

**----- Start of picture text -----**<br> (a) (b)<br>Fig.14 (a) The time-domain signal; (b) The frequency spectrum<br>(a) (b)<br>Fig.15 (a) The segmentation of the frequency spectrum; (b) The EWT results<br>**----- End of picture text -----**<br>


**==> picture [460 x 189] intentionally omitted <==**

**==> picture [452 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br> (a)<br>**----- End of picture text -----**<br>


**==> picture [452 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br> (b) (c)<br>**----- End of picture text -----**<br>


Fig.16 (a) The Hilbert envelope spectrum of mode 1; (b) The Hilbert envelope spectrum of mode 2; (c) The Hilbert envelope spectrum of mode 3 

## **5. Conclusions** 

Various techniques have been proposed in the early articles for wheel-bearing of freight train or regular train. In this paper, a new defect detection method called empirical wavelet transform was investigated for wheel-bearing of train. Real vibration signals were collected from the wheel-bearings in maintenance workshop. To verify the effectiveness of the EWT method, this paper also provides the analysis results in different fault cases (i.e., outer race fault, roller fault, and the compound fault of outer race and roller). Moreover, some problems also exist in the empirical wavelet transform. For example, how to segment the spectrum adaptively is still needed to be studied. More investigations focused on the EWT methods and the application in fault diagnosis would be carried out in the future. 

## **Acknowledgment** 

The author would like to express heartfelt appreciation to Dr. Gilles for his research. This work was supported by National Natural Science Foundation of China (No. 51421004， 

51575423), Natural Science Basic Research Plan in Shaanxi Province of China (No. S2013JC9908) and the Fundamental Research Funds for the Central University. 

## **References** 

[1] Howard C. Choe, Yulun Wan, Andrew K. Chan. Neural pattern identification of railroad wheel-bearing faults from audible acoustic signals: comparison of FFT, CWT, and DWT features. Proceedings of SPIE-The International Society for Optical Engineering, 1997, pp. 480-496 

[2] James.E.Cline, James R. Bilodeau, Richard L.Smith. Acoustic wayside identification of freight car roller bearing defects. Proceedings of the 1998 ASME/IEEE Joint Railroad Conference, Philadelphia, 1998, pp. 79-83. 

[3] John DonelsonIII, Ronald L. Dicus. Bearing defect detection using on-board accelerometer measurements. Proceedings of the 2002 ASME/IEEE Joint Rail Conference, Washington, 2002, pp.95-102 

[4] J.S. Sakellariou, K.A. Petsounis, S.D. Fassois. On board fault detection and identification in railway vehicle suspensions via a Functional Model Based Method. Proceedings of the 2002 International Conference on Noise and Vibration Engineering, Leuven, 2002, pp. 1323-1332 

[5] B.J. Roylance. Ferrography-then and now.Tribology International. 2005, 38, 857-862 

[6] X.P. Yan, C.H. Zhao, Z.Y. Lu, X.C. Zhou, H.L. Xiao. A study of information technology used in oil monitoring.Tribology International. 2005, 38, 879-886 

[7] Z. Peng, N.J. Kessissoglou, M. Cox. A study of the effect of contaminant particles in lubricants using wear debris and vibration condition monitoring techniques. WEAR. 2005, 258, 1651-1662 

[8] William H. Sneed, Richard L. Smith. On-board real-time railroad bearing defect detection and monitoring. Proceedings of the 1998 ASME/IEEE Joint Rail Conference, Philadelphia, 1998, pp.149-153 

[9] Wei Zhou, Thomas G. Habetler, Ronald G. Harley. Bearing condition monitoring methods for electric machines: a general review. Proceedings of IEEE International Symposium on Diagnostics for Electric Machines, Power Electronics and Drives, Cracow, 2007, pp. 3-6 

[10] Yu-Jiang Zhang, ENSCO, Inc, Springfield, VA. Rail vehicle bearing defects detection. Transportation Research Board of the National Academies Safety Innovations Deserving Exploratory Analysis(IDEA) Final Report for Safety IDEA Project 16. 2012 

[11] C. James Li, S.Y.Li. Acoustic emission analysis for bearing condition monitoring. WEAR. 1995, 185, pp. 67-74 

[12] Qingbo He, Jun Wang, Fei Hu, Fanrang Kong. Wayside acoustic diagnosis of defective train bearings based on signal resampling and information enhancement. Journal of Sound and Vibration. 2013, 332, pp. 5635-5649 

[13] Southern Carolyne, Rennison David, KopkeUwe. RailBAM-An advanced bearing acoustic monitor: initial operational performance results. Proceedings of Conference on Railway Engineering, Darwin, 2004, pp. 23.01-23.07 

[14] D. Mba, Raj B.K.N. Rao. Development of acoustic emission technology for condition monitoring and diagnosis of rotating machines; bearings, pumps, gearboxes, engines and rotating structures.The Shock and Vibration Digest. 2006, 38, pp. 3-16 

[15] N. Tandon, A. Choudhury. A review of vibration and acoustic measurement methods for the detection of defects in rolling element bearing.Tribology International. 1999, 32, pp. 469-480 

[16] Abdullah M. Al-Ghamd, David Mba. A comparative experimental study on the use of acoustic emission and vibration analysis for bearing defect identification and estimation of defect size.Mechanical Systems and Signal Processing. 2006, 20, pp. 1537-1571 

[17] F. Hemmati, W. Orfali, M.S. Gadala. Rolling element bearing condition monitoring using acoustic emission technique. Proceedings of the 2012 International Conference on Noise and Vibration Engineering, Leuven, 2012, pp. 699-713 

[18] Andrew K.S. Jardine, Daming Lin, DraganBanjevic. A review on machinery diagnostics and prognostics implementing condition-based maintenance.Mechanical Systems and Signal Processing. 2006, 20, pp. 1483-1510 

[19] Jinglong Chen, YanyangZi, Zhengjia He, Jing Yuan. Compound faults detection of rotating machinery using improved adaptive redundant lifting multiwavelet. Mechanical Systems and Signal Processing. 2013, 38, pp. 36-54 

[20] Bin Chen, Zhaoli Yan, Wei Chen. Defect detection for wheel-bearing with time-spectral kurtosis and entropy. Entropy. 2014, 16, 607-626 

[21] Som P. Singh, SrinivasChitti, S.K. Punwani, Monique F. Stewart. On-board detection of derailed wheel and wheel defects.Proceedings of the 2007 ASME/IEEE Joint Rail Conference and Internal Combustion Engine Spring Technical Conference. Pueblo, 2007, pp. 143-150 

[22] Robert B. Randall, Jerome Antoni. Rolling element bearing diagnostics- A tutorial.Mechanical Systems and Signal Processing. 2011, 25, pp. 485-520 

[23] G. Meltzer, Nguyen PhongDien. Fault diagnosis in gears operating under non-stationary rotational speed using polar wavelet amplitude maps. Mechanical Systems and Signal Processing. 2004, 18, pp. 985-992 

[24] NeelamMehala, RatnaDahiya. A comparative study of FFT, STFT and wavelet techniques for induction machine fault diagnostic analysis. Proceedings of the 7[th] WSEAS international conference on Computational intelligence, man-machine systems and cybernetics, Stevens Point, 2008, pp. 203-208 

[25] NaimBaydar, Andrew Ball. A comparative study of acoustic and vibration signals in detection of gear failures using Winger-Ville distribution. Mechanical Systems and Signal Processing. 2001, 15, pp. 1091-1107 

[26] Z.K. Peng, F.L. Chu. Application of the wavelet transform in machine condition monitoring and fault diagnostics: a review with bibliography. Mechanical Systems and Signal Processing. 2004, 18, pp. 199-221 

[27] Yu Bo, Yun Lifen. Trains trouble shooting based on wavelet analysis and joint selection feature classifier. Journal of Multimedia. 2014, 9, pp. 207-215 

[28] Baojia Chen, Zhengjia He, Xuefeng Chen, Hongrui Cao, GaigaiCai, YanyangZi. A demodulating 

approach based on local mean decomposition and its applications in mechanical fault diagnosis. 

Measurement Science and Technology. 2011, 22, 055704 

[29] Yanxue Wang, Zhengjia He, YanyangZi. A demodulation method based on improved local mean 

decomposition and its application in rub-impace fault diagnosis. Measurement Science and Technology. 2009, 20, 025704 

[30] Yaguo Lei, Jing Lin, Zhengjia He, Ming J. Zuo. A review on empirical mode decomposition in fault diagnosis of rotating machinery.Mechanical Systems and Signal Processing. 2013, 35, pp. 108-126 

[31] Z.K. Peng, Peter W. Tse, F.L. Chu. An improved Hilbert-Huang transform and its application in vibration signal analysis. Journal of Sound and Vibration. 2005, 286, pp. 187-205 

[32] Norden E. Huang, ZhengShen, et al. The empirical mode decomposition and the Hilbert spectrum for nonlinear and non-stationary time series analysis.Proceedings of the Royal Society of London Series A-Mathematical Physical and Engineering Sciences. 1998, 454, pp. 903-995 

[33] Charleston-Villalobos S, Gonzalez-Camarena R, et al. Crackle sounds analysis by empirical mode 

decomposition. Engineering in Medicine and Biology Magazine, IEEE. 2007, 26, pp. 40-47 

[34] Baozhong Yang, C. Steve Suh. Interpretation of crack-induced rotor non-linear response using instantaneous frequency.Mechanical Systems and Signal Processing. 2004, 18, pp. 491-513 

[35] Min-Hung Yeh. The complex bidimensional empirical mode decomposition.Signal Processing. 2012, 92, pp. 523-541 

[36] Zhaohua Wu, Norden E. Huang. A study of the characteristics of white noise using the empirical mode decomposition method.Proceedings of the Royal Society of London Series A-Mathematical Physical and Engineering Sciences. 2004, 460, pp. 1597-1611 

[37] Patrick Flandrin, Gabriel Rilling, Paulo Goncalves. Empirical mode decomposition as a filter bank. Signal Processing Letters, IEEE. 2004, 11, pp. 112-114 

[38] YannisKopsinis, Stephen McLaughlin. Development of emd-based denoising methods inspired by wavelet thresholding.Signal Processing, IEEE Transactions on. 2009, 57, pp. 1351-1362 

[39] Ingrid Daubechies, Jianfeng Lu, Hau-Tieng Wu. Synchrosqueezed wavelet transforms: An empirical mode decomposition – like tool. Applied and Computational Harmonic Analysis. 2011, 30, pp. 243-261 

[40] Tomas Y. Hou, Zuoqiang Shi. Data-driven time-frequency analysis.Applied and Computational Harmonic Analysis. 2013, 35, pp. 284-308 

[41] Jerome Gilles. Empirical Wavelet Transform.Signal Processing, IEEE Transactions on. 2013, 61, pp. 3999-4010 

[42] Ingrid Daubechies. Ten Lectures on Wavelets.CBMS-NSF Regional Conference Series in Applied Mathematics.Philadelphia, 1992. 

**==> picture [462 x 225] intentionally omitted <==**

1. A novel method is employed for the diagnosis of wheel bearings fault. 

2. Empirical Wavelet Transform (EWT) is an adaptive analysis method. 

3. EWT provides a good performance in the detection of wheel-bearing fault.