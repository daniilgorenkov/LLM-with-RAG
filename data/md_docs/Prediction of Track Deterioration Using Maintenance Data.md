# Prediction of Track Deterioration Using Maintenance Data and Machine Learning Schemes 

Jun S. Lee, Ph.D.[1] ; Sung Ho Hwang, Ph.D.[2] ; Il Yoon Choi, Ph.D.[3] ; and In Kyum Kim[4] 

Abstract: The maintenance and renewal of ballasted track can be optimized in terms of time and cost if a proper statistical model of track deterioration is derived from previous maintenance history and measurement data. In this regard, quite a few models with simplified assumptions on the parameters have been suggested for the deterioration of ballasted track. Meanwhile, data driven models such as the artificial neural network (ANN) and support vector regression (SVR), which are basic ingredients of machine learning (ML) technology, were introduced in this study to better represent the deterioration phenomena of track segments so that the results can be directly plugged into the optimization schemes. For this purpose, the influential parameters of track deterioration have been selected based on the maintenance history, and two ML models have been studied to find the best combination of input parameters. Through numerical experiments, it was found that at least 2 years of maintenance data were needed in our case to obtain a stable prediction of track deterioration. DOI: 10.1061/ JTEPBS.0000173. © 2018 American Society of Civil Engineers. 

Author keywords: Track maintenance; Machine learning; Artificial neural networks; Support vector regression; Track quality index; Decision support system. 

## Introduction 

Apart from the ballastless concrete track, the maintenance of ballasted tracks is one of the main tasks of infrastructure managers (IM) because track conditions should satisfy the requirements of maintenance manuals so that uninterrupted service during commercial hours is provided and the comfort level of passengers is beyond the threshold value. Maintaining track quality within a certain level is costly (UIC 1992) and, therefore, the proper prediction of track deterioration and an optimal schedule of tamping and renewal are essential to guarantee the operability of the track and to reduce the total maintenance cost (Guler 2016). During tamping, a multipletie-tamper is used to align the vertical and horizontal geometry of the ballasted track, and both the regulator and the stabilizer are used to improve the quality of the track. Meanwhile, the ballast is completely replaced by a new one when the renewal is planned in the field. In this regard, a theoretical approach to the optimization of both the maintenance cost and the number of interventions has been proposed in Lee et al. (2018) based on statistical modeling of track deterioration. However, the conditions of a ballasted track are not 

1Research Fellow, Dept. of High-Speed Railroad, Korea Railroad Research Institute, Euiwang Si, Kyunggi Province 16105, Republic of Korea (corresponding author). ORCID: https://orcid.org/0000-0003-1930 -2618. Email: jslee@krri.re.kr 

2Senior Researcher, Dept. of High-Speed Railroad, Korea Railroad Research Institute, Euiwang Si, Kyunggi Province 16105, Republic of Korea. Email: forever7@krri.re.kr 

3Principal Researcher, Dept. of High-Speed Railroad, Korea Railroad Research Institute, Euiwang Si, Kyunggi Province 16105, Republic of Korea. Email: iychoi@krri.re.kr 

4Research Assistant, Dept. of High-Speed Railroad, Korea Railroad Research Institute, Euiwang Si, Kyunggi Province 16105, Republic of Korea. Email: kiminkyum@krri.re.kr 

Note. This manuscript was submitted on October 22, 2017; approved on March 20, 2018; published online on June 20, 2018. Discussion period open until November 20, 2018; separate discussions must be submitted for individual papers. This paper is part of the Journal of Transportation Engineering, Part A: Systems, © ASCE, ISSN 2473-2907. 

uniform along the route, and various parameters such as vertical and horizontal curves, passing tonnages, and velocity, among others, influence the deterioration rate of the track. These aforementioned parameters are normally categorized along the track segments within the framework of an enterprise resource planning (ERP) or enterprise asset management (EAM) solution, where a typical length of the track segment is 200 m, unless a dynamic segmentation scheme (Jovanovic 2006) is used. The track quality index (TQI) is accordingly evaluated as a standard deviation of the measured data at each segment. 

A data-driven deterioration model can be introduced once the segment information and measurement data from the track measurement vehicle (TMV) are available. One of the main advantages of the data-driven model is that it predicts track conditions without requiring a sophisticated statistical model (Karlaftis and Vlahogianni 2011), and several track related parameters previously mentioned can be included to model track deterioration. Typical data-driven models that have been applied in the field of railway engineering, including track maintenance and prediction of track deterioration, are the artificial neural network (ANN) and support vector machine (SVM) algorithms (Fuqing 2011). 

In the following sections, important influential factors on track irregularities will be highlighted based on statistical data of the track geometry including the number of tampings as well as regression results of TQI as a function of passing tonnages. A machine learning procedure specializing in ANN and SVR will be subsequently introduced, and the applicability of the models to the track geometry will be investigated. A few numerical examples of the proposed models will be analyzed and parametric studies will also be carried out. For these objectives, a commercial statistical package as well as a public domain library called LIBSVM (Chang and Lin 2011) will be adopted and the prediction results will be. The proposed models based on machine learning can be imported into the decision support system (DSS) within the framework of ERP or EAM (Lovett 2017), and future work will be concentrated on the combination of DSS with TMV and Internet of Things (IoT) data. 

© ASCE 

04018045-1 

J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

## Literature Review 

Earlier applications of data-driven models to predict track deterioration can be found in Shafahi et al. (2008). They considered six parameters of track geometry, such as track record index, traffic load, speed, and radius, for which each parameter was classified into one of two to seven classes. The classification error between the predicted and observed data was estimated using the ANN with three hidden layers of neurons. A more detailed modeling of track deterioration using the ANN was proposed by Sadeghi and Askarinejad (2012). They combined various TQI values of gauge, profile, alignment, and twist in the neural networks and derived the deterioration rates of rail, sleeper, ballast, and fastener. They applied one hidden layer in the model and studied the best combination of number of neurons as well as TQI parameters. Guler (2013) considered eight mechanical inputs related to the track geometry and four environmental inputs to model the track deterioration rate. Two hidden layers together with a hyperbolic tangent transfer function were used in the ANN, and the model has been applied to field data obtained from commercial lines. Meanwhile, Li et al. (2006) investigated the relationship between track geometry and vehicle response using ANN with a cascading learning scheme so that the optimum number of neurons can be determined. The ANN model has also been applied to pavement maintenance (Sollazzo et al. 2017) and estimation of annual maintenance cost (Woldemariam et al. 2016). 

Another application of the data driven model to track deterioration can be found in Hu and Liu (2016). They originally adopted the SVM concept to classify measurement data into warning and action levels through a supervised learning process and track parameters such as traffic volumes, track class, and inspection intervals. A more detailed application of the SVM to predict track faults 1 month in advance was investigated by Bergmeir et al. (2013). They used the acceleration data of the bogie, axle boxes, and car body together with location, speed, and event date. As the prediction of the event is based on various input parameters, they used an ε-insensitive support vector regression model (SVR, Smola and Scholkopf 2004) and compared the results with those of other machine learning (ML) methods. The forecasted values using SVR were found to be more reliable than those of the ANN, and even better than those of the classical statistical models in many cases. Cardenas-Gallo et al. (2017) used an ensemble classifier to estimate track degradation where the track deterioration, regression, and classification were modeled by Gamma process, binary logistic regression, and SVM, respectively. In this case, the regression model was used to compute the probability of warning and action levels from the deterioration data, and the results were imported into the SVM model to predict possible faults in the near future. For this purpose, differences in the measured track irregularities (amplitude), mean tonnage, time interval, and track identification number, together with the regression results mentioned previously, were used as inputs, and the output would be the probability of the action level. 

Meanwhile, Li et al. (2014) applied the SVM to model the failure alarm of the rail car and used the measurement data of the hot box detector (HBD) as well as wheel impact load detector (WILD) to predict the possible failure of the bearing within a certain period of time. The SVM has also been applied to the overhead contact line (OCL, Barmada et al. 2014) to detect arc events and to the railway point systems (Vileiniskis et al. 2015) to predict a possible failure in the system. Since the measurement data of important railway equipment are stored on a daily basis in many cases, the corresponding prediction based on the ANN or SVM has to be updated accordingly and, in this regard, an online SVM can be used to 

predict the remaining useful life (RUL, Fumeo et al. 2015). In addition, a combined model of SVM and ANN was proposed by Tabatabaee et al. (2013) to classify similar characteristics and to predict the performance of the pavement, and SVM classification of fasteners by computer vision technology was proposed by Gibert et al. (2015). 

In summary, application of ANN and SVM models in terms of railway engineering have been reviewed, and special emphasis was placed on the possibility of prediction of TQI by data-driven models. For this, several input parameters, i.e., neurons, of track deterioration have also been investigated and a modified model with refined parameters based on the previous studies will be proposed in the following. 

## Deterioration of Ballasted Track in High Speed Rail Route 

The starting point of ML is to decide the input parameters, i.e., neurons, to model the track degradation realistically. For this, the parameters used in the previous studies of ML were investigated first. Sadeghi and Askarinejad (2007) showed that the track deterioration could be represented by the combined effect of the superstructure, substructure, and track geometry conditions as shown in Kerr (2003). They argued that the effect of load cycles, train speed, and subgrade conditions would be the influential factors in track deterioration. In addition, the initial TQI and ballast index, i.e., the representative values of the aggregate quality and drainage condition, were also the related factors according to their analysis. It is noted that the line classification and corresponding maintenance cost index shown in UIC 714 and 715 (UIC 1992, 2009), respectively, also listed similar influential factors in track deterioration. In addition to the input parameters mentioned before, Guler (2013) added additional geometric parameters such as curvature, gradient, and cross level in the track deterioration model. Furthermore, the rail parameters, e.g., rail type and length and climatic conditions, i.e., land slide, snow, and flood, were also modeled during the ANN training and, as a result, the track deterioration rates were predicted using the field measurement data with the coefficient of determination in the range of 0.73–0.83. 

The number of parameters mentioned previously could be reduced if our interest is confined to a specific high-speed rail route, for which the material properties of rail type, welding, and sleeper are almost the same throughout the total length of the route. In this specific case, the type of subgrade structure, horizontal as well as vertical curvature, and the operational speed will be the main parameters of the track deterioration from the previous studies mentioned previously, and our interest will therefore be concentrated on the influence of these three parameters. Fig. 1 illustrates a typical cross section of the ballasted track constructed in the high-speed rail (HSR) route in Korea. It is noted that the ballasted track has not been used since the second construction stage of the HSR in 2002. The design speed of HSR is 350 km=h and the corresponding minimum radius of the circular curve is 7,000 m. The minimum 

**==> picture [251 x 62] intentionally omitted <==**

Fig. 1. Typical cross section of ballasted track in high-speed rail. 

© ASCE 

04018045-2 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

**==> picture [212 x 113] intentionally omitted <==**

Fig. 2. Deterioration model of ballasted track. 

thickness of the ballast is 350 mm, and a continuous welded rail (CWR) was built from the very beginning of the construction. A prestressed concrete sleeper was used and either e-clip or fast-clip was adopted to fasten the sleeper to the rail. 

In our case, the assumption of the same properties within a specific route is necessary because the maintenance data including TQI values are not fully available. In this regard, Kang (2014), based on the limited information on maintenance history of a high-speed rail, analyzed the maintenance trend of the ballasted track to derive the optimal maintenance technique. The maintenance data used in Kang (2014) will be adjusted to determine the input parameters of the ML process. Because the TQI values of the track segments were not available in our case, the corresponding data were obtained by assuming a deterioration model, and the deterioration rate was subsequently estimated. For this purpose, the linear deterioration model (Lee et al. 2018) shown in Fig. 2 was again used to calculate the TQI. The mean deterioration rate, ro, was assumed to be 0.03 mm per million gross tonnage (MGT) based on the field data from Caetano and Teixeira (2016). In Fig. 2, TO and RT represent tamping only (TO) and renewal and tamping (RT), respectively, and AL and WL mean action level and warning level, respectively. The TQI of the vertical level (VL) can be derived using the following equations: 

**==> picture [181 x 12] intentionally omitted <==**

where 

**==> picture [185 x 12] intentionally omitted <==**

**==> picture [167 x 12] intentionally omitted <==**

and t in Eq. (1) represents the MGT. In Eqs. (2) and (3), β1, β2, and NT represent the deterioration constants and the number of tampings, respectively, and ri is the current deterioration rate. The parameter χ is a multiplier of the mean deterioration rate according to the track conditions and will be elaborated in the following. 

## Influence of Substructure 

The influence of the substructure in track deterioration can be established according to the type of infrastructure, such as a tunnel, embankment, and bridge, as the stiffness of the substructure is closely related to the type of superstructure. In this regard, Kang (2014) summarized the number of tampings for 1 year according to the type of superstructure and, therefore, the result will be used to predict the TQI values in the ML process. Table 1 shows the ratio of the tamping frequency based on tunnel structure and it is clear that the total number of tampings in the bridge are about three times greater than those in the tunnel, mainly because of the temperature change and vibration effects. The effect of subgrade uniformity can 

Table 1. Ratio of tamping frequency according to the type of structure 

|Structure type|Track length ratio|Tamping ratio| |---|---|---| |Tunnel (uniform subgrade property)|1.0|1.0| |Embankment|1.1|2.1| |Bridge|1.7|3.3|



Source: Data from Kang (2014). 

also be verified from Table 1 as the total number of tampings in the embankment is almost twice the sum of those in the tunnel. The tamping ratio can be used as a multiplier of the mean deterioration ratio in Eq. (3) for each segment having a specific type of superstructure. Also shown in Table 1 is the length of each structure and the relative length is calculated based on the length of tunnel. 

## Influence of Curvature Geometry 

The influence of curvature on the tamping frequency is described in Table 2 in which the competition curve represents a combined curve of the plane as well as the vertical curves, and the number of tampings is per unit length. In Table 2, the tamping ratio of each curve type is calculated based on the number of tampings applied to the plane section, and the length ratio is evaluated based on the total length of plane section. As can be expected, the number of tampings in the segments of the competition curve are greater than those of the plane section by 40%. The track deterioration in the segments of the plane and vertical curves are almost the same although the vertical curve is a bit worse than the plane curve in terms of ratio. Detailed data on the number of tampings according to the magnitude of radius were not available and, therefore, the classification presented in Table 2 will be used as a multiplier, χ, during the derivation of TQI for curved segments. It is noted that the maintenance work including tamping is mostly influenced by the vertical impact load from the running train and, therefore, the effect of radius can be ignored when the minimum radius is 7,000 m in high-speed rail. It is also noted that the vertical curve is either concave or convex, and the concave curve is not favorable in terms of maintenance (Kang 2014). For simplicity, during the numerical experiments in the following section, the vertical and competition curve will be merged into one group. 

## Influence of Velocity 

The influence of velocity is visualized by considering the number of tampings in the acceleration and deceleration sections, and Table 3 lists the tamping ratio of each section based on the uniform velocity section, where the velocity, V, is about 300 km=h. In this case, if the train speed is reduced, the deceleration force is applied to the ballasted track and the harmful effect is significant compared to the acceleration case (Kang 2014) by 12%. Meanwhile, the acceleration effect is not significant and the corresponding tamping ratio is about the same as that of constant velocity. Again, the tamping ratio presented in Table 3 will be used as a multiplier of the mean deterioration rate shown in Eq. (3). 

Table 2. Ratio of tamping frequency according to the type of curve 

|Curve type|Track length ratio|Tamping ratio| |---|---|---| |Plane section (without curve)|1.0|1.0| |(uniform loading condition)||| |Plane curve (vertical curve)|0.6 (0.5)|1.2 (1.3)| |Competition curve|0.1|1.4|



Source: Data from Kang (2014). 

© ASCE 

04018045-3 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

EV ¼ E½ðyt − yÞ[2] � ≅ e[T] ðqÞeðqÞ ð5Þ 

Table 3. Ratio of tamping frequency according to the train speed 

|Speed|Track length ratio|Tamping ratio| |---|---|---| |V≈300km=h (uniform velocity)|1.0|1.0| |Acceleration|0.8|0.95| |Deceleration|1.5|1.12|



Source: Data from Kang (2014). 

Thus far, three influential parameters, e.g., subgrade condition, curvature, and velocity, have been introduced from the field maintenance data, and the relative effects of the parameters are modeled by the multiplier to the mean deterioration date. The corresponding networks will be composed of the parameters introduced in the foregoing and the related TQI parameters illustrated in Fig. 2. The importance of the parameters and the number of data set along the maintenance period will be evaluated in the numerical examples in the following section. 

## Prediction of Track Conditions with Machine Learning Process 

A brief introduction of the machine learning theories is made in this section for a comparison of the adopted methods. The methods, based on ANN and SVR, are basically a supervised training process and are nonparametric in nature. In our case, the input data are composed of the track properties from the ERP/EAM and the measurement data including the calculated TQI, while the output is the predicted TQI. 

## Artificial Neural Network Model 

The ANN can be interpreted as a curve-fitting process through training in which multiple input parameters are fed forward to the hidden layers and the trained errors are propagated backwards so that the final errors would be minimized. As seen in Fig. 3, the ANN is composed of input layer, hidden layers of the several neurons, and output layer, and the layers are linked by the connections (Hagan et al. 2012). The hidden layers are made up of several weights, w, and biases, b, so that the input data are connected with these parameters. The transfer or the activation function, f, transforms the summed neurons into the output and its role is similar to the shape functions used in the various numerical analyses. The system equations in a multilayer network can be written as 

**==> picture [183 x 12] intentionally omitted <==**

where k = number of hidden layers in the network; and y[0] ¼ x. The mean square error (MSE) or the performance index for the network, EV, is 

**==> picture [45 x 107] intentionally omitted <==**

**==> picture [180 x 76] intentionally omitted <==**

Fig. 3. ANN data flow diagram. 

© ASCE 

where yt and q = target (measured) value and the iteration number, respectively. The back propagation of the MSE is equivalent to an update of the weights and biases using an approximate steepest descent (gradient) rule (Hagan et al. 2012) 

**==> picture [186 x 26] intentionally omitted <==**

**==> picture [180 x 26] intentionally omitted <==**

where ρ = learning rate. The back propagation algorithm in Eqs. (6) and (7) may have a local minimum if a multilayer network is used, and there are many modified versions to enhance the ANN perfor– mance. The well-known Levenberg Marquardt (LM) algorithm based on Newton’s approximation (Hagan et al. 2012) is widely used and the LM method will be used in the following numerical examples. 

In summary, the prediction of track deterioration in terms of the TQI is possible if the track-related information is used as input and the ANN involving unknown weights as well as biases are used to predict the TQI. Through the minimization of errors, i.e., training, arising from the gap between the target and predicted TQI, the improvement of the TQI prediction is possible. 

## Support Vector Regression Model 

In the beginning, the support vector machine was used for the classification of the binary output and was expanded to the regression of various parameters without introducing any specific statistical model. The main difference between SVR and ANN lies in the usage of the kernel function in the SVR, which is similar to the transfer function in the ANN. In the SVR, the kernel function transforms the complicated relationships among the input data into a simplified linear one by introducing a hyperplane concept. Fig. 4 shows the relationship between input, x, and output, y, and a certain amount of tolerance, ε, so that the regression result will be insensitive to the tube margin ε. That is, we need to find a function fðxÞ so that the predicted value is deviated from the target value, y, at most ε for all 

**==> picture [216 x 180] intentionally omitted <==**

Fig. 4. ε-insensitive SVR with a slack variable ξ. 

04018045-4 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

of the training data (Smola and Scholkopf 2004). In reality, this condition is not easy to fulfill and, therefore, a slack variable, ξ, is introduced and the following quadratic optimization equation shall be solved: 

**==> picture [183 x 29] intentionally omitted <==**

s.t. 

**==> picture [184 x 58] intentionally omitted <==**

where w, C, and n = support vector, regularization parameter, and number of input data, respectively; and ϕðxÞ = special function to transform x into a hyperplane so that a simplified relationship can be established (Chang and Lin 2011). As the optimization equation in Eq. (8) is in the primal form, the following dual problem with the Lagrangian multipliers is easier to solve: 

**==> picture [188 x 66] intentionally omitted <==**

**==> picture [201 x 29] intentionally omitted <==**

where α and η = Lagrangian multipliers, and the following constraints are to be satisfied: 

**==> picture [156 x 12] intentionally omitted <==**

Because the gradient of the Lagrange equation shall be zero, the following approximation function using the Karuth-Kuhn-Tucker condition (Smola and Scholkopf 2004) can be derived: 

**==> picture [191 x 29] intentionally omitted <==**

and 

**==> picture [172 x 29] intentionally omitted <==**

where Kðxi; xÞ = kernel function to be assumed, while ϕðxÞ does not need to be identified during the training process. In many cases, a Gaussian or a radial basis function (RBF) is used as the kernel function, and the same function can also be used in the transfer function in the ANN. Finally, Eq. (14) is compared with the target value, y, in Eq. (9) or (10), and the MSE can be calculated to decide the retraining of the regression model. The optimization of the values in Eq. (12), i.e., C and ε, and in Eq. (14), i.e., the standard deviation in the RBF, can be estimated with various up-to-date methods, and the simplified grid search method proposed in Chang and Lin (2011) can also be applied in our case. 

It is well known that the result using the SVR is stable compared with that of the ANN (Bergmeir et al. 2013). This is because the quadratic optimization scheme is used in SVR and, therefore, the local minimum can be avoided during modeling of the nonlinear 

Table 4. Additional parameters used to generate TQI values 

||Parameter|Value| |---|---|---| ||Million gross tonnage (MGT)/month|2 (4)| ||Standard deviation of longitudinal irregularities|1.9| ||(warning level, mm)<br>Maximum number of tampings to renewal<br>Perturbation parameterκ|5<br>1, 2, 10| ||Initial TQI values, TQIi;o,ro, in Fig.2<br>β1andβ2in Eqs. (2) and (3)|Random variable<br>0.1 and 0.1|



regression. The implementation and verification process of the SVR to model the track deterioration is similar to that in the ANN, although the input data need to be scaled down to reduce the numerical errors during the calculation of the kernel functions (Chang and Lin 2011). 

## Application of Machine Learning Schemes to TQI Prediction 

The influential parameters of the track geometry were introduced in the previous section and, based on these parameters, the data-driven prediction models of the track deterioration were validated using numerical data. As mentioned previously, the measurement data of the high-speed rail are not available at this moment, and artificial data close to the field conditions are generated using the parameters shown in Tables 1–3. In the beginning, a total of 100 segments were produced for each case, and a mean deterioration rate, ro, similar to Caetano and Teixeira (2016) was assigned to every segment. Since the total parameters considered in Tables 1–3 were 3 × 3 × 3 in our case, a total of 2,700 segments having initial values of TQI, TQIi;o, and the number of tampings shown in Fig. 2 were artificially created using a random number generator. From these, the current TQI values were calculated based on the deterioration rate, ri, in Eq. (3), and 27 different tamping ratios in Tables 1–3 were used as multipliers, χ, in Eq. (3) so that the variations of the deterioration rate owing to the influential parameters were obtained. Furthermore, perturbation on the deterioration rate was made by adding a perturbation parameter, κ, shown in Table 4 to the deterioration rate such that the perturbed deterioration rate, riu, has the form of a normal distribution 

**==> picture [159 x 23] intentionally omitted <==**

see Fig. 5 for some of the TQI development according to MGT and κ in Eq. (16). In Fig. 5, the warning level of TQI is 1.9 mm and the number of tampings to renew the track system including ballast is 5 so that, when the tamping is applied to a specific segment for at least 5 times, the track system is renewed. After renewal, TQI is assumed to be the same as the initial TQI value. Table 4 shows the parameters used in the analysis and the numerical values in the parenthesis are for the comparison only. 

Two cases of machine learning schemes were considered to compare the results between the ANN and SVR, obtained by using a commercial mathematical package, MATLAB, Version 2016. In addition, the results using LIBSVM (Chang and Lin 2011) were also studied to check the difference of the optimization algorithms considered in Eq. (12). 

## Case 1: ML Model with Latest Measurement Data Set 

The ANN model with the latest measurement data is illustrated in Fig. 6 and, except for the influential parameters shown in 

04018045-5 J. Transp. Eng., Part A: Syst. 

**==> picture [190 x 12] intentionally omitted <==**

© ASCE 

**==> picture [12 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br> (a)<br>(b)<br>**----- End of picture text -----**<br>


Fig. 5. Generation of TQI data with different MGT and standard deviations: (a) 4 MGT/month and SD of ri ¼ 10; and (b) 2 MGT/month and SD of ri ¼ 2. 

Tables 1–3, MGT, the number of tampings and the initial TQI value after the construction or ballast renewal are added in the training model. In other words, Case 1 is similar to the curve fit in Fig. 2 with the minimum amount of data, and the SVR as well as ANN use the same set of data having 85% of the data to train and the remaining 15% to test. The relationship between prediction and target values can be visualized by the correlation coefficient, R, or by the mean square error (MSE), and the corresponding results are shown in Fig. 7. As can be expected, when the perturbation parameter, κ, of Eq. (16) is increased, the deterioration rate becomes linear and the prediction errors will be decreased accordingly. A similar tendency can be expected when LIBSVM is used, although the prediction errors are slightly increased when κ is small. This is because the optimization scheme used in LIBSVM is different from 

**==> picture [37 x 106] intentionally omitted <==**

**==> picture [52 x 100] intentionally omitted <==**

Fig. 6. Case 1 of ANN model: use of latest data set. 

**==> picture [67 x 131] intentionally omitted <==**

**==> picture [164 x 143] intentionally omitted <==**

Fig. 7. Correlation coefficient, R, and mean square error (MSE) of Case 1 according to the perturbation parameter κ. 

that of MATLAB, and a fine tuning of the grid search method in LIBSVM will decrease the prediction errors. Also noted in Fig. 7 is the MSE or R value of the ANN and SVR models, and the prediction results of the ANN are a little better than those of the SVR, although the difference is negligible. The results are contradictory to the comparison results by Bergmeir et al. (2013) and the main reason for this is the use of the retraining option in the ANN model of MATLAB, which is rather convenient to reiterate compared with the SVR models. 

## Case 2: ML Model with Series of Measurement Data Set 

The ML model with the series of measurement data is next considered and, in this case, the measurement data of TQI and MGT values after the construction or ballast renewal are used. Fig. 8 shows the network model, and the number of data set will be the parameter to be decided through the application of available data from the TMV. During the maintenance work of the high-speed rail, the track inspection is carried out by the TMV every month based on the inspection manual, and the necessary data will therefore be available for each month. Fig. 9 illustrates the R and MSE according to the number of measurement months, as well as κ, and it can be concluded that the total number of measurement data of at least 24 months will provide a stable result. Also shown in the figure is the result of Case 1 with 1 set of data, and it is clear that Case 2, 

**==> picture [38 x 172] intentionally omitted <==**

**==> picture [52 x 166] intentionally omitted <==**

Fig. 8. Case 2 of ANN model: series of measurement data. 

© ASCE 

04018045-6 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

**==> picture [241 x 136] intentionally omitted <==**

Fig. 9. Correlation coefficient, R, and mean square error (MSE) of Case 2 according to the perturbation parameter κ and number of data in month. 

Fig. 10 shows the relationship between the prediction and target values according to the ML schemes and 15% of the data set are again used for testing. The correlation coefficients, R, are almost the same regardless of the ML schemes and, as the testing data set is randomly chosen in MATLAB, R can be changed during the retraining of the data set. 

Thus far, the ANN and SVR of the ML schemes have been applied to model the track deterioration and the results can be directly used to predict the future maintenance work of the ballasted track. The training of the network used the simulation data based on the field conditions, and an additional perturbation term, κ, was also introduced during the estimation of the deterioration rate so that a TQI measurement with noise terms can be modeled with the proposed model. The proposed model is also expected to apply to the general cases of ballasted track because the most influential factors of track deterioration, such as substructure, curvature, and train speed, are evaluated from the field maintenance data. 

with at least 24 points of measurement data, will give better results in our case. Similar results are obtained when either the SVR or LIBSVM model is used. Group 2 of the UIC line classification (UIC 2009) is assumed when calculating the MGT per month. It is noted that, when field data were used in the ANN (Guler 2013), R of the vertical level was about 0.86 and it corresponds to the case of κ ¼ 2 in Fig. 9, although the neurons used in Guler (2013) are different from our case. 

## Conclusions 

Data-driven models of track deterioration have been investigated in this study by using SVR as well as ANN, and the applicability of the ML schemes has been verified with the simulation data, which are close to the field conditions. The estimated TQI data were retrieved considering the influential parameters of the ballasted track, such as type of substructure, track curvature, and velocity 

**==> picture [358 x 355] intentionally omitted <==**

**----- Start of picture text -----**<br> : R=0.9456 : R=0.93047<br>2.5<br>Data Data<br>Fit Fit<br>2.0<br>2.0 Y = T Y = T<br>1.5 1.5<br>1.0 1.0<br>0.5 0.5<br>0.5 1.0 1.5 2.0 2.5 0.5 1.0 1.5 2.0<br>(a) Target (b) Target<br>: R=0.94507 : R=0.93321<br>2.5 2.5<br>Data Data<br>Fit Fit<br>2.0 Y = T 2.0 Y = T<br>1.5 1.5<br>1.0 1.0<br>0.5 0.5<br>0.5 1.0 1.5 2.0 2.5 0.5 1.0 1.5 2.0 2.5<br>(c) Target (d) Target<br>Output=0.87*Target+0.13 Output=0.86*Target+0.14<br>Output=0.87*Target+0.17 Output=0.88*Target+0.16<br>**----- End of picture text -----**<br>


Fig. 10. Relationship of prediction and target value when κ ¼ 10, data set = 24 months, and MGT ¼ 2=mo: (a) ANN training; (b) ANN test; (c) SVC test; and (d) LIBSVM test. 

© ASCE 

04018045-7 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

properties, among others. Additional maintenance parameters, such as number of tampings after ballast renewal, MGT, and initial TQI values were also used in the models. Two case studies having different input parameters were carried out and the following conclusions were made: 


- From the field measurement, the number of tampings in a bridge were found to be more than 3 times higher than those of tunnel structure in a high-speed rail route, whereas the effect of acceleration/deceleration was not significant in terms of ballast tamping. The tamping ratio of a section having a competition curve was 40% higher than that of a plane section, and the overall effect of the influential parameters was included in the estimation of TQI values. 


- A total of 27 cases of influential parameters have been used, and a perturbation parameter was also used during the TQI evaluation to model the field conditions more realistically. 


- Two cases of ML models were considered. Case 1 adopted the latest data on MGT, number of tampings, and initial TQI value after the ballast renewal, whereas Case 2 used the series of data set on MGTand TQI, which are readily available from the TMV. As expected, if the perturbation parameter, κ, is small, the TQI values are perturbed in a large scale and the results of Case 1 are not satisfactory, as shown in Fig. 7. 


- The MSE of Case 1 can be reduced by including a series of data measured on a monthly basis, and when the period of input data was more than 24 months, stable results were obtained. 


- The ANN showed slightly better results than SVR because of the retraining process included in the commercial package, but the difference was negligible and similar results were also obtained when the LIBSVM was used. 


- It is noted that climate conditions such as landslide, snow, and 


- flood considered in Guler (2013) were not included in the proposed models, partly because the HSR structures were relatively new and partly because the track deterioration models based on TQI do not have a direct relationship with weather conditions. Future work will be concentrated on the training of real measurement data from the TMV so that the effect of influential parameters can be verified. In addition, the applicability of the proposed models will also be verified by using TQI data collected from the conventional lines. Furthermore, the online SVM mentioned in literature review in the foregoing can be considered to update the recent measurement data so that training of the data set can be minimized. The prediction results from ML can be used in the DSS within the framework of ERP, and the maintenance schedule can therefore be optimized without sophisticated mathematical modeling processes. 

## Acknowledgments 

This research was funded and supported by the Ministry of Land, Infrastructure and Transport, South Korea, under a grant entitled “Development of the high speed track measurement system for railway maintenance”. The authors are also grateful to Prof. Lin for his helpful suggestion on the LIBSVM. 

## Notation 

The following symbols are used in this paper: 

 - b = bias of ANN; 

 - C = regularization parameter; 

 - EV = mean square error; 

 - f = transfer (activation) function; 


- Kðxi; xÞ = kernel function; 


- R = correlation coefficient; 


- r = deterioration rate of the vertical level; 


- ri = deterioration rate of the vertical level at time span i; 


- ro = initial deterioration rate of the vertical level; 


- TQIo = initial TQI at a segment; 


- TQIvl;o = initial standard deviation of the vertical level after renewal; 


- TQIvl;oðtÞ = initial standard deviation of the vertical level after NT tampings; 


- TQIvlðtÞ = standard deviation of the vertical level at time t; t = time; 


- w = weight of ANN or support vector of SVR; 


- yt = target (measured) value; 


- α, η = Lagrangian multiplier; 


- β1, β2 = deterioration constants; 


- ε = tolerance; 


- κ = perturbation parameter of deterioration rate; 


- ξ = slack variable; 


- ρ = learning rate; 


- ϕðxÞ = transfer function of SVR; and 


- χ = multiplier of the mean deterioration rate. 

## References 


- Barmada, S., M. Raugi, M. Tucci, and F. Romano. 2014. “Arc detection in pantograph-catenary systems by the use of support vector machinesbased classification.” IET Electr. Syst. Transp. 4 (2): 45–52. https://doi .org/10.1049/iet-est.2013.0003. 


- Bergmeir, C., G. Sainz, C. Bertrand, and J. Benitez. 2013. “A study on the use of machine learning methods for incidence prediction in high-speed train tracks.” In Vol. 7906 of Proc., IEA/AIE, LNAI, 674–683. 


- Caetano, L. P., and P. F. Teixeira. 2016. “Predictive maintenance model for ballast tamping.” J. Transp. Eng. 142 (4): 04016006. https://doi.org/10 .1061/(ASCE)TE.1943-5436.0000825. 


- Cardenas-Gallo, I., C. A. Sarmiento, G. A. Morales, and M. A. Bolivar. 2017. “An ensemble classifier to predict track geometry degradation.” Reliab. Eng. Syst. Saf. 161 (May): 53–60. https://doi.org/10.1016/j.ress .2016.12.012. 


- Chang, C.-C., and C.-J. Lin. 2011. “LIBSVM: A library for support vector machines.” ACM Trans. Intell. Syst. Technol. 2 (3): 1–27. https://doi.org /10.1145/1961189.1961199. 


- Fumeo, E., L. Oneto, and D. Anguita. 2015. “Condition based maintenance in railway transportation systems based on big data streaming analysis.” Procedia Comput. Sci. 53: 437–446. https://doi.org/10.1016/j.procs .2015.07.321. 


- Fuqing, Y. 2011. “Failure diagnostics using support vector machine.” Ph.D. thesis, Div. of Operation and Maintenance Engineering, Lulea Univ. of Technology. 


- Gibert, X., V. Patel, and R. Chellappa. 2015. “Robust fastener detection for autonomous visual railway track inspection.” In Proc., IEEE Winter Conf. Applications of Computer Visualization, 694–701. New York: IEEE. 


- Guler, H. 2013. “Prediction of railway track geometry deterioration using artificial neural networks: A case study for Turkish state railways.” Struct. Infrastruct. Eng. 10 (5): 614–626. https://doi.org/10.1080 /15732479.2012.757791. 


- Guler, H. 2016. “Optimisation of railway track maintenance and renewal works by genetic algorithms.” Gradevinar 68 (12): 979–993. https://doi .org/10.14256/JCE.1458.2015. 


- Hagan, M. T., H. B. Demuth, M. H. Beale, and O. De Jesus. 2012. “Neural network design.” Accessed October 9, 2017. http://hagan.okstate.edu /nnd.html. 


- Hu, C., and X. Liu. 2016. “Modeling track geometry degradation using support vector machine technique.” In Proc., Joint Rail Conf. New York: ASME. 

© ASCE 04018045-8 J. Transp. Eng., Part A: Syst. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 


- Jovanovic, S. 2006. “Railway track quality assessment and related decision making.” In Proc., AREMA, 202–230. Louisville, KY. 


- Kang, T. K. 2014. “Optimal maintenance technique of the ballasted track in high-speed railway.” [In Korean.] Ph.D. thesis, Chungnam National Univ. 


- Karlaftis, M., and E. Vlahogianni. 2011. “Statistical methods versus neural networks in transportation research: Differences, similarities and some insights.” Transp. Res. C 19 (3): 387–399. https://doi.org/10.1016/j.trc .2010.10.004. 


- Kerr, A. D. 2003. Fundamentals of railway track engineering. Omaha, NE: Simmons-Boardman Books. 


- Lee, J., I. Choi, I. Kim, and S. Hwang. 2018. “Tamping and renewal optimization of ballasted track using track measurement data and genetic algorithm.” J. Transp. Eng. A. 144 (3): 04017081. https://doi.org/10 .1061/JTEPBS.0000120. 


- Li, D., A. Meddah, K. Hass, and S. Kalay. 2006. “Relating track geometry to vehicle performance using neural network approach.” Proc. Inst. Mech. Eng. F 220 (3): 273–281. https://doi.org/10.1243/09544097JRRT39. 


- Li, H., D. Parikh, Q. He, B. Qian, Z. Li, D. Fang, and A. Hampapur. 2014. “Improving rail network velocity: A machine learning approach to preventive maintenance.” Transp. Res. C 45 (Aug): 17–26. https://doi.org /10.1016/j.trc.2014.04.013. 


- Lovett, A. 2017. “Railroad decision support tools for track maintenance.” Ph.D. thesis, Univ. of Illinois. 


- Sadeghi, J., and H. Askarinejad. 2007. “Influences of track structure, geometry and traffic parameters on railway deterioration.” IJE Trans. B 20 (3): 291–300. 


- Sadeghi, J., and H. Askarinejad. 2012. “Application of neural networks in evaluation of railway track quality condition.” J. Mech. Sci. Tech. 26 (1): 113–122. https://doi.org/10.1007/s12206-011-1016-5. 


- Shafahi, Y., P. Masoudi, and R. Hakhamaneshi. 2008. “Track degradation prediction models, using Markov chain, artificial neural and neuro-fuzzy network.” In Proc., 8th WCRR. Zürich, Switzerland: ITA. 


- Smola, A. J., and B. Scholkopf. 2004. “A tutorial on support vector regression.” Stat. Comput. 14 (3): 199–222. https://doi.org/10.1023/B:STCO .0000035301.49549.88. 


- Sollazzo, G., T. F. Fwa, and G. Bosurgi. 2017. “An ANN model to correlate roughness and structural performance in asphalt pavements.” Constr. Build. Mater. 134 (Mar): 684–693. https://doi.org/10.1016/j.conbuildmat .2016.12.186. 


- Tabatabaee, N., M. Ziyadi, and Y. Shafahi. 2013. “Two-stage support vector classifier and recurrent neural network predictor for pavement performance modeling.” J. Infrastruct. Syst. 19 (3): 266–274. https://doi.org /10.1061/(ASCE)IS.1943-555X.0000132. 


- UIC (Union Internationale des Chemins de Fer). 1992. Factors affecting track maintenance costs and their relative importance. UIC Code 715 R. Paris: UIC. 


- UIC (Union Internationale des Chemins de Fer). 2009. Classification of lines for the purpose of track maintenance. UIC Code 714 R. Paris: UIC. 


- Vileiniskis, M., R. Remenyte-Prescott, and D. Rama. 2015. “A fault detection method for railway point systems.” Proc. Inst. Mech. Eng. F. 230 (3): 852–865. https://doi.org/10.1177/0954409714567487. 


- Woldemariam, W., J. Myrillo-Hoyos, and S. Labi. 2016. “Estimating annual maintenance expenditures for infrastructure: Artificial neural network approach.” J. Infrastruct. Syst. 22 (2): 04015025. https://doi .org/10.1061/(ASCE)IS.1943-555X.0000280. 

J. Transp. Eng., Part A: Systems, 2018, 144(9): 04018045 

© ASCE 

04018045-9 

J. Transp. Eng., Part A: Syst.