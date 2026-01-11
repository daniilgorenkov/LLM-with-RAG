Accident Analysis and Prevention 156 (2021) 106126 

**==> picture [61 x 67] intentionally omitted <==**

Contents lists available at ScienceDirect Accident Analysis and Prevention journal homepage: www.elsevier.com/locate/aap 

**==> picture [57 x 72] intentionally omitted <==**

## Railroad accident analysis using extreme gradient boosting 

## Raj Bridgelall[a][,] *, Denver D. Tolliver[b ] 

a _Department of Transportation, Logistics & Finance, College of Business, North Dakota State University, Fargo, ND, 58108, United States_ 

b _Upper Great Plains Transportation Institute, North Dakota State University, Fargo, ND, 58108, United States_ 

**==> picture [30 x 30] intentionally omitted <==**

A R T I C L E I N F O A B S T R A C T _Keywords:_ Railroads are critical to the economic health of a nation. Unfortunately, railroads lose hundreds of millions of Data cleaning dollars from accidents each year. Trends reveal that derailments consistently account for more than 70 % of the Feature engineering U.S. railroad industry’s average annual accident cost. Hence, knowledge of explanatory factors that distinguish Financial loss derailments from other accident types can inform more cost-effective and impactful railroad risk management Machine learning strategies. Five feature scoring methods, including ANOVA and Gini, agreed that the top four explanatory factors Principle component analysis Risk management in accident type prediction were track class, type of movement authority, excess speed, and territory signali­ zation. Among 11 different types of machine learning algorithms, the extreme gradient boosting method was most effective at predicting the accident type with an area under the receiver operating curve (AUC) metric of 89 %. Principle component analysis revealed that relative to other accident types, derailments were more strongly associated with lower track classes, non-signalized territories, and movement authorizations within restricted limits. On average, derailments occurred at 16 kph below the speed limit for the track class whereas other ac­ cident types occurred at 32 kph below the speed limit. Railroads can use the integrated data preparation, ma­ chine learning, and feature ranking framework presented to gain additional insights for managing risk, based on their unique operating environments. 

## **1. Introduction** 

U.S. railroads have been an important driver of economic progress for more than 150 years. Today, U.S. railroads carry approximately onethird of the nation’s exports (ASCE, 2017). Therefore, the safe and ’s economic health. efficient operation of railroads is crucial to the nation Unfortunately, railroads lose hundreds of millions of dollars from acci­ dents each year. Analysis of the Federal Railroad Administration (FRA) Rail Equipment Accident database revealed that human-factors was consistently the dominant cause of railroad accidents (Bridgelall and Tolliver, 2020). Hence, the federal government mandated that railroads deploy a positive train control (PTC) system by 2018 to help prevent accidents caused by human errors (Zhang et al., 2018). With PTC now in place, it is important for analysts to study other common causes of accidents. 

The **goal** of this research is to identify factors associated with the most frequent and expensive types of accidents that are not attributable to human error. Data mining of FRA accident records from January 1, 2009, to June 30, 2020, revealed that derailment accidents accounted for 70.9 % of the average annual financial loss (Fig. 1). The trend 

showed that derailment accidents maintained a steady rate each year. Therefore, the ability to identify and rank features that increase the risk of derailments over other accident types can inform more cost-effective and impactful risk management strategies (Ghofrani et al., 2018). 

An **objective** of this research is to build a supervised machine learning (ML) model that can predict derailments from other accident types and to rank the importance of those features that contribute to­ wards the classification accuracy. However, no single type of ML model performs best on all types of datasets (Murphy, 2012). Therefore, another objective is to compare the classification performance of various types of ML models on the same dataset. 

One of the main challenges in data science is to effectively clean datasets before using them to train ML models. Studies estimate that dirty data costs the U.S. economy trillion of dollars each year (Ilyas and Chu, 2019). A survey of data cleaning for ML found that the failure to discover and repair dirty data can weaken data analysis techniques (Jesmeen et al., 2018). Although a few approaches to data cleaning are common, every dataset poses unique challenges (Bridgelall et al., 2018). Hence, data scientists spend an average of 60 % of their time cleaning and organizing data (Ilyas and Chu, 2019). 

* Corresponding author. 

_E-mail addresses:_ raj@bridgelall.com (R. Bridgelall), denver.tolliver@ndsu.edu (D.D. Tolliver). https://doi.org/10.1016/j.aap.2021.106126 Received 23 December 2020; Received in revised form 19 March 2021; Accepted 3 April 2021 

Available online 17 April 2021 

0001-4575/© 2021 Elsevier Ltd. All rights reserved. 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

Although the importance of using clean data is well-known, the research community has paid little attention to the advancement of data cleaning techniques (Rahm and Do, 2000). The most commonly used techniques are those that detect and remove outliers and duplicate re­ cords (Ilyas and Chu, 2019). Even so, those techniques alone cannot effectively clean all types of datasets. Other techniques that can find data entry errors use customized rules to detect violations, for example, house prices exceeding an expected range for a given neighborhood. Custom techniques tend to be heuristic, so they require good familiarity with the data and its meaning. Considering the challenges outlined above, the following are **contributions** of this research: 

modeling to HRGC crash data and found that gate violations were more highly associated with two-quadrant than four-quadrant gates (Liu and Khattak, 2017). Karamati et al. (2020) applied random survival forest to HRGC crash data and found that adding audible alarm devices to crossings that already have gates and flashing lights can decrease crash likelihood by approximately 50 % (Keramati et al., 2020). Soleimani et al. (2019) used extreme gradient boosting to identify HRGCs that should be closed to prevent accidents (Soleimani et al., 2019). Wali et al. (2021) applied text mining to crash narrative data of railroad trespass­ ing incidents and found that confirmed suicide attempts and the use of headphones or cellphones were more likely to result in fatal injuries (Wali et al., 2021). 


- A customized framework to clean a relevant subset of the FRA database and to fill 100 % of missing values for the important at­ tributes (Section 3). 

Only a few studies focused on derailment-type accidents. Liu et al. (2017) found that derailment rates on Class 1 railroad mainlines were lower for signalized tracks with higher FRA track class and higher traffic density (Liu et al., 2017). Wang et al. (2020) found that most derailment type accidents declined with the greatest reductions in broken rails, irregular track geometry, and wheel-related equipment defects (Wang et al., 2020). Iranitalab and Khatta (2020) found that the random forest method of ML outperformed the logistic regression, Naïve Bayes, and support vector machine (SVM) methods in classifying train-level hazmat releases with an AUC score of 87 % (Iranitalab and Khattak, 2020). 


- Interpreting the importance ranking of the feature relevance in predicting accident type (Sections 3.4 and 4.2). 


- Visualizing and interpreting the classification power of each attri­ bute by principle component analysis (PCA) to gain insights about the performance differences among the ML models evaluated (Sec­ tions 3.5 and 4.3). 

The next section (Section 2) reviews related works and their findings in relation to the contributions of this research. Section 4 mirrors sub­ sections of the methods section to present the results. Section 5 discusses 6 the significance and interprets the outcome. Section recaps the find­ ings and concludes with how future research can leverage the methods of this research to further the agenda in accident analysis. 

The survey of Ghofrani (2018) demonstrated that researchers have also used ML methods to analyze other aspects of railroad operations besides safety (Ghofrani et al., 2018). For example, Li et al. (2014) used ML to learn rules from historical and real-time data to predict railroad maintenance needs (Li et al., 2014). Lasisi and Attoh-Okine (2019) proposed a combination of ensemble tree-based ML models to predict rail fatigue defects and achieved an AUC score of 0.783 (Lasisi and Attoh-Okine, 2019). 

## **2. Related works** 

The benchmarking of ML performance is subjective because of its high relevance to the target problem of a particular study in a particular field (Olson et al., 2017). For example, a performance score considered to be “good” in the biotech industry when evaluating vaccine efficacy may be considered “poor” in the automotive industry when evaluating defective unit batches. Subjective performance assessments depend on the level of “acceptable” risk for a given application (Cook, 2007). Therefore, model evaluation often use the fuzzy academic grading sys­ tem to assess and compare performance levels (Echauz and Vachtseva­ nos, 1995). 

Studies that use ML methods to analyze accidents are more common for roadways than for railroads. For example, Iranitalab and Khattak (2017) compared the performance of Multinomial Logit (MNL), k- Nearest Neighbor (kNN), Support Vector Machines (SVM) and Random Forests (RF) in predicting the crash severity of two-vehicle roadway crashes (Iranitalab and Khattak, 2017). They found that kNN and MNL had the best and worst performance, respectively, when applied to crash data from Nebraska, United States. A recent survey of big data analytics applied to railroads found that of 115 journal articles reviewed from 2003 to 2017, only 22 % covered railroad safety whereas 49 % and 29 % covered maintenance and operations, respectively (Ghofrani et al., 2018). This imbalance supports a claim in the introduction that the research community and the railroad industry can benefit from addi­ tional analysis of railroad accident risks. 

## **3. Methodology** 

Fig. 2 shows the methodological framework developed to prepare the data, apply the machine learning methods, rank the features, and to interpret the results. 

Several studies used ML techniques to analyze highway-rail grade crossing (HRGC) accidents. Dabbour et al. (2017) applied ordered regression models to HRGC crash data and found that higher train and vehicle speeds were positively correlated with driver injury severity (Dabbour et al., 2017). Liu and Khattak (2017) applied geospatial 

The input layer gathers the datasets and prepares the combined data by applying various methods to reduce noise, repair data entry errors, and fill in missing values. The processing layer prepares relevant attri­ butes to train and tune the ML models. The processing layer led to the 

**==> picture [313 x 134] intentionally omitted <==**

**Fig. 1.** Annual financial loss reported for different accident types. 

2 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**==> picture [313 x 223] intentionally omitted <==**

**Fig. 2.** The methodological framework. 

discovery of additional errors that made some features irrelevant. In such cases, the framework logic looped back to the data preparation module to address the issue. The model building and validation pro­ cesses also contained a loop that converged after the ML performance stabilized. The final layer ranked the importance of attributes in clas­ sification performance and used PCA to visualize the results for interpretation. 

**Table 1** 

Criteria for Attribute or Feature Elimination. 

||Criteria|Description|Further| |---|---|---|---| ||||Explanation| ||Sparsity|Attribute is missing more than 85 % of the|(Murphy, 2012)| |||values or contain zeros.|| ||Duplication|Attribute contains the same information as|(Ilyas and Chu,| |||other attributes.|2019)| ||Correlated|Attribute is more than 90 % correlated with|(G´eron, 2017)| |||another.|| ||Redundancy|Attribute contains information that is inherent<br>in other attributes.|(Liu et al., 2012)| ||Noise|Attribute is not relevant to the target class.|(Rahm and Do,| ||||2000)| ||Dispersion<br>Combinable|Attribute has low variance or carries little or<br>no information.<br>Attribute that can combine with others<br>without losing information.|(Bridgelall et al.,<br>2018)<br>(Ilyas and Chu,<br>2019)|



## _3.1. Data source_ 

The comprehensive Federal Railroad Administration (FRA) Rail Equipment Accident database provided the main dataset for the analysis (Bridgelall and Tolliver, 2020). Some of the data schema became inconsistent after the FRA changed reporting requirements for a few of the fields starting June 1, 2011 (FRA, 2011). For example, the report added a field to indicate if the accident occurred in a signalized territory. Hence, there was no entry for the “SIGNAL” field prior to the switchover date. Similarly, a field indicating the method of operation (“MOPERA”) replaced the “METHOD” field that encoded similar information. 

**Table 2** 

Chronicle of Dimension Reduction for 29,297 Records. 

Merging 8055 records from 2009 to 2011 with 21,242 records from 2012 to June 2020 produced a total of 29,297 records with 145 attri­ butes. Consequently, 22 % and 79 % of the data was missing in the “MOPERA” and “METHOD” fields, respectively. The accident reporting form also added a field “SSB1” to indicate if the track was a continuously welded (CWR) or other. Hence, the “SSB1” field was mostly empty prior to June 1, 2011. 

||Criteria|Attributes Removed|Count| |---|---|---|---| ||Sparsity|19 with_>_85 % missing data (e.g. DUMMY1-|145 - 19=126| |||DUMMY7).|| ||Duplication|8 with duplicated information (e.g. IMO, IYR,|126 - 8=118| ||Sparsity|MONTH, YEAR).<br>16 with_>_90 % zero-flled (e.g. CABOOSE1,|118−16=102| |||EVACATE, MIDREM1)|| ||Correlated|12 with_>_90 % correlation with other attributes|102−12=90| ||Redundancy|(e.g. PASSINJ, PASSKLD)<br>7 that were redundant with others (e.g. CNTYCD,|90−7=83| |||STATE, COUNTY)|| ||Noise|6 with no relevance to the target (e.g. train|83−6=77| ||Noise<br>Combinable|number, car number)<br>6 with_>_20 % missing or no relevance to the<br>target (e.g. ADJUNCT1, DIV)<br>HUMANS=|77−6=71<br>71–| ||Correlated|(engineers+fremen+conductor+brakemen),<br>drop 4.<br>EQATT (equipment attended) correlates with|4+1=68<br>68–1=67| ||Combinable|HUMANS, drop 1<br>Combine 15 narrative felds into a single feld<br>(NARR), drop original 15.|67–<br>15+1=53| ||Combinable|Fill missing MOPERA (method of operation) data|53–1=52| |||with METHOD, drop 1.||



## _3.2. Data processing_ 

## _3.2.1. Data cleaning_ 

Table 1 describes criteria used to clean the data by eliminating irrelevant attributes or features. The classification of those criteria is a heuristic synthesis by the authors based on a broad understanding from the literature, which the table cites for further explanation. 

Table 2 chronicles each criterion used to reduce the number of fields from 145 to 52. 

## _3.2.2. Data extraction_ 

Passenger trains accounted for a small portion 8.03 % (2354) of accidents. Removing those records enhanced the consistency of the dataset, which is known to improve the ML performance (Murphy, 

3 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

2012 ). A side benefit was that the eliminated records also removed a few attributes that were associated with passenger trains only. Table 3 chronicles the net reduction of attributes from 52 (Table 2) to 50, and records from 29,297 to 15,087. The statistics shown in the table are the number of records (N), number of attributes or variables (V), and “DERAILED” number of metadata fields (M). Adding the target attribute indicated if the accident was a derailment type or not, and it became the label for supervised ML. 

**Table 4** 

Chronicle of the Transformed and Derived Attributes. 

|Attribute|Reduction|Procedure| |---|---|---| |HR24|50–3+1=48|Combined TIMEHR, TIMEMIN, AMPM to 24 -h| |||continuous, then drop old.| |TRK_DEN_LG|48−1+1=48|Log Transform: TRK_DEN, then drop old.| |TRNSPD_LG|48−1+1=48|Log Transform: TRNSPD, then drop old.| |TONS_LG<br>POS_CAR|48−1+1=48<br>48+1−1=48|Log Transform: TONS, then drop old.<br>Rename and recode POSITON1 (position of frst| |||involved car) as the fractional position relative to| |||the number of cars. 0 is front, 1 is back.| |N_CARS|48+1=49|Add N_CARS as the sum of loaded and empty cars.| |CARS_LD|49+1−4=46|Add CARS_LD as proportion of N_CARS loaded.| |||Drop: LOADF1, EMPTYF1, POSITON1, PASSTRN| |CARS_HZMT|46+1−1=46|Add CARS_HZMT as proportion of CARS_LD that| |||carry Hazmat. Drop CARS (number of cars| |||carrying hazmat)| |SPD_OVR|46+1–1=46|Add to capture difference in train speed and speed<br>limit for CLASS_TRK. Dropped feld HIGHSPD.| |Metadata|46−6=40|Converted 6 attributes (REC_ID, SC, STATION,| |||RAILROAD, RR3, IYR) to metadata: 5+6=11.|



## _3.2.3. Attribute transformation_ 

ML algorithms tend to perform poorly on data with attributes that have a highly skewed distribution because the model could treat data in long tails as outliers or because extreme values provide insufficient ex­ amples (Manning and Mullahy, 2001). A shifted natural logarithm LN(1 + _x_ ) reduced the skew and prevented an undefined number if attribute value _x_ is zero. 

Another transformation that can help to reduce the dimension of a dataset is to replace a set of related attributes with proportions of a base attribute. The proportion transformation retained information about the relative relationship among attributes while normalizing the values within the [0,1] range. Table 4 chronicles the transformation of attri­ butes and their effect on reducing the number of attributes from 50 (Table 3) to 40. 

**Table 5** 

Chronicle of the Eliminated Attributes. 

## _3.2.4. Feature selection_ 

|Attribute|Reduction|Process| |---|---|---| |POSCAR<br>LOADED_1|40−1=39<br>39−1=38|Relative position of the frst involved car in the train.<br>Boolean: Is frst involved car loaded? Missing (22 %,| |||6568)| |ACCDMG|38−1=37|Total reported damage in U.S. dollars.| |CASKLD|37−1=36|Total killed for all involved railroads.| |CASINJ|36−1=35|Total injured for all involved railroads.| |CARSHZD|35−1=34|Number of cars that released hazardous materials.| |CARSDMG|34−1=33|Number of cars damaged or derailed.| |POSITON2|33−1=32|Position of car on the train that caused the accident.| |EMPTYF2|32−1=31|Number of empty freight cars that derailed.| |LOADF2|31−1=30|Number of loaded freight cars that derailed.| |HEADEND2|30−1=29|Number of headend locomotives that derailed.| |ACC_TYPE|29−1=28|Type of accident. Missing (0%, 83).| |ACC_CAT|28−1=27|Accident cause category.| |CAUSE|27−1=26|Accident cause code.| |MATCH|26−1=25|Temporary geospatial flter fag for county mismatch.|



Predictive modeling should not contain attributes where values are known only after the outcome. Therefore, the cleaning procedure eliminated _post-event_ attributes such as the number of people injured, killed, or evacuated. Table 5 chronicles the feature reduction from 40 (Table 4) to 25. 


- _3.2.5. Feature engineering_ 

 - The procedures performed the following feature engineering: 


- 1) Packaged similar features of an attribute to simplify the categories. 2) Converted categorical attributes that have some ranking to ordinal attributes. 


- 3) Binarized categorical attributes that contained only two values by replacing one value with zero and the other with one. 


- 4) Replaced nominal values with a single word label to enhance the ease of interpreting trends with more descriptive legends. 

work with missing data, but most cannot (Abidin et al., 2018). There­ fore, data scientists developed a few methods to impute or guess missing values. Common approaches are to replace missing values with the mean, median, most frequent, random, or zero value. More intelligent approaches use tree-based ML techniques to fill missing values with those of their nearest neighbors in _feature space_ . However, the existing methods did not enhance the contribution of the affected attributes to­ wards predicting the target class. Therefore, this research developed a new method, dubbed _local association pivot_ (LAP), to replace missing values based on spatial proximity rather than feature space proximity. The LAP method first creates a pivot table that aggregates non-missing values by a _spatial_ location identifier and by sub-location identifiers if available. The method then merges the pivot table with the dataset by using the main location identifier as the unique merge key. The aggre­ gation method for the pivot depends on the type of missing data. For example, for numerical values such as track density, the method used the maximum of the aggregated value for a location. The method did not use the average value because zero or missing values created an undesirable bias in the aggregation. A fringe benefit of using the LAP method is that it is easy to spot data entry or spelling errors by examining a sorted list of the unique location keys. 

Table 6 summarizes the results of the feature engineering. 

## _3.2.6. Data imputation_ 

A few methods such as decision trees and Bayesian classifiers can 

**Table 3** 

Chronicle of Data Reduction after Data Extraction. 

|Attribute|Statistic|Procedure| |---|---|---| |ACC_CAT|N: 29,297<br>V: 52+1=53|Add accident category based on accident cause<br>code:<br>{Track, Equipment, Human, Signal,| ||M: 5|Miscellaneous}.| ||N: 26,943 (92|Dropped accidents involving passenger type trains| |PASSTRN|%)<br>V: 53−4=49|(PASSTRN=Y).<br>Dropped associated attributes:| ||M: 5|LOADP1, LOADP2, EMPTYP1, EMPTYP2.| ||N: 26,943 (92|| |DERAILED|%)<br>V: 49+1=50|Added“Derailed”as the target attribute.| ||M: 5|| ||N: 25,035|Dropped records where the accident cause was<br>missing, 7% (1908)| ||N: 15,088|Dropped records where human factors were a<br>cause, 39.7 % (9947)| ||N: 15,087|Dropped 1 record with a missing value for<br>WEATHER.|



Table 7 summarizes the results of the imputing missing values and the impact of each method. Missing or erroneous geospatial coordinates are impossible to impute or correct if no other spatial information is available in the dataset. The state or county name provides a coarse 

4 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**Table 6** 

**Table 7** 

Summary of Feature Engineering. 

Summary of Data Imputation. 

|**Table 6**<br>Summary of Feature Engineering.|**Table 7**<br>Summary of Data Imputation.| |---|---| |location identifer that can be helpful for visualizing data on maps.<br>However, a coarse location such as a large state may introduce bias in<br>the ML process. Fortunately, the FRA database contains the station name<br>that is closest to the accident location, so its location can be a surrogate<br>for missing geospatial coordinates.<br>_3.2.7. Geospatial coordinate repair_<br>Aside from missing geospatial coordinates, data entry errors resulted<br>in erroneous or highly skewed geospatial locations.Fig. 3shows the<br>positions of the recorded geospatial coordinates relative to a map of the<br>continental United States. There is an observable systematic skew to­<br>wards the southeast This skew suggested that there was a lack of res­<br>Attribute<br>Procedure<br>CWR<br>Renamed SSB1 to CWR (continuously welded rail); binarized as“1′′ =<br>“CWR”and“0”otherwise.<br>LOADED1<br>Binarized as“1”=“Y”(frst involved car loaded?) and“0”=“N”for<br>non-empty values.<br>WEATHER<br>Recoded nominal values in WEATHER as labels {Clear, Cloudy, Rain,<br>Fog, Sleet, Snow}<br>TRK_TYP<br>Renamed TYPTRK (track type) and labeled nominal codes as {Main,<br>Yard, Siding, Industry}<br>VISION<br>Renamed VISIBLTY and replaced nominal codes as descriptive {Dawn,<br>Day, Dusk, Dark}<br>CLASS_RR<br>Renamed TYPRR (railroad class) and cleaned to contain only values<br>from 1 to 6.<br>CLASS_TRK<br>Renamed TRKCLAS (track class) and cleaned to contain ordinal values<br>from 0 to 9 (X→0)<br>CONSIST<br>Renamed TYPEQ (consist type); repackaged as {freight, passenger,<br>locomotive, cars, work, yard}.<br>{1}→ “Freight”, {2, 3, B, C}→ “Passenger”, {8, D, E}→ “Locomotive”,<br>{5, 6}→ “Cars”, {4, 9, A}→ “Work”, {7}→ “Yard”<br>ACC_TYPE<br>Renamed TYPE (accident type); repackaged as category labels:<br>{1}→ “Derail”, {2, 3, 6}→ “Collide”, {4}→ “Collide (Side)”, {5}→<br>“Collide (Rake)”,<br>{7, 8}→ “RGC”, {9}→ “Obstruct”, {10, 11}→ “Fire”, {12, 13}→<br>“Other”<br>MOVEx<br>Renamed MOPERA; repackaged as labels {signal, control, restrict,<br>blocks, not main}<br>{1, D}→ “Signal”, {2, A, B, C, P}→ “Control”, {3, L, M, I}→<br>“Restrict”,<br>{4, E, F, G, H, J, K}→ “Blocks”, {5, N, O}→ “Not Main”|Attribute<br>Missing<br>Before<br>Missing<br>After<br>Procedure (N=29,297, V=49, M=3)| ||TRK_DEN<br>51 %<br>(15,176)<br>0% (0)<br>Pivot STATION by TRK_TYP, aggregated<br>as maximum TRK_DNSTY (track density).<br>Fill missing data associated with the track<br>type if defned, otherwise use the<br>maximum value.<br>SIG<br>22 %<br>(6473)<br>0%, 0<br>Pivot STATION by TRK_TYP, aggregated<br>as net count SIGNAL (signalized<br>territory). Fill missing data as“1”if net<br>count associated with the track type is<br>greater than 0, otherwise fll with“0”<br>CONSIST<br>39 %<br>(11,537)<br>8%<br>(2605)<br>Layer 1: Fill missing CONSIST with:<br>“Freight”if (LOADF1+EMPTYF1)_>_<br>0 otherwise<br>“Passenger”if (LOADP1+EMPTYP1)_>_<br>0 or PASSTRN is“Y”<br>8%<br>(2605)<br>2% (844)<br>Layer 2: Fill missing CONSIST with:<br>“Freight”if CLASS_RR is“1”(except<br>“Amtrak”) otherwise<br>“Passenger”if RAILROAD (reporting<br>railroad) is“Amtrak”<br>2% (844)<br>1% (377)<br>Layer 3: Fill missing CONSIST with:<br>“Work Train”if TRK_TYP is not“Main”<br>1% (377)<br>0% (0)<br>Layer 4: Fill missing CONSIST with:<br>“Work Train”if TONS (gross tons,<br>excluding locomotives) is 0<br>otherwise fll missing CONSIST with<br>“Freight”if TONS_>_0<br>CWR<br>21 %<br>(6378)<br>0% (0)<br>Fill missing values with“1”if TRK_TYP is<br>“main”and“0”otherwise.<br>MOVEx<br>0% (518)<br>0% (0)<br>Fill missing MOVEx based on SIGNAL or<br>TRK_TYP.<br>PASSTRN<br>6%,<br>(2049)<br>0% (0)<br>Fill missing PASSTRN based on CONSIST.<br>Check original fag for consistency with<br>the type CONSIST and the sum of freight<br>and passenger cars (loaded or empty).<br>Flip the fag accordingly.<br>CLASS_RR<br>0%, (37)<br>0% (0)<br>Fill missing CLASS_RR (railroad class) by<br>internet search:<br>BLF→2, {DD, METC}→3, CN→1<br>TRK_TYP<br>0%, (15)<br>0% (0)<br>Fill missing TRK_TYP (track type) by<br>inference from the metadata.<br>CLASS_TRK<br>0%, (25)<br>0% (0)<br>Fill missing CLASS_TRK (track class) by<br>inference from the metadata.|



Aside from missing geospatial coordinates, data entry errors resulted in erroneous or highly skewed geospatial locations. Fig. 3 shows the positions of the recorded geospatial coordinates relative to a map of the continental United States. There is an observable systematic skew to­ wards the southeast. This skew suggested that there was a lack of res­ olution for those coordinates because in North America, lower resolution latitude and longitude coordinates would bias towards the south and east, respectively. The result was that 21.8 % of the records had erroneous geospatial coordinates because their locations on the map did not match the counties reported for the accidents. 

respectively. 

## _3.2.8. Outlier removal_ 

Sacrificing a few outlier data points to reduce bias can improve the generalization of a model. Outlier data instances are few and different from the bulk of the dataset (Liu et al., 2012). They could represent noisy data entries or rare events that can bias the training of an ML model, resulting in poor predictive performance. The framework used four methods to compare their effect on the model performance: 

The procedure to clean the geospatial coordinates filled missing values in two stages. First, the LAP method averaged the non-missing geospatial coordinates for accidents that occurred on a given track type near a given station. Second, the procedure merged the records ® database that with a map file from the U.S. Census Bureau TIGER contained the geospatial centroid of each county in the United States. A geographic information system (GIS) spatial join method then replaced erroneous geospatial coordinates with the geospatial centroid of the FRA reported county. 


- One class SVM (OCS) with a radial basis function (RBF) kernel (OCSRBF) 


- Covariance estimator (CE) (Rousseeuw and Driessen, 1999) 

Table 8 chronicles the progress of filling missing geospatial co­ ordinates in each step of the procedure. The LAP method used all records prior to data reduction and filled missing values with the mean value of the non-zero latitude and longitude values for that track type near the station, otherwise the method used the maximum value. 


- Local outlier factor (LOF) (Breunig et al., 2000) 


- Isolation forest (IF) (Liu et al., 2012) 

Table 10 summarizes the AUC performance metric for a random forest classifier after removing outliers using each of the four methods, with the various hyperparameter selections shown. All algorithm and parameter selection produced similar performance. The framework used the LOF algorithm with 20 nearest neighbors and 1% outliers because of its slight AUC performance edge. The method removed 126 outliers to result in 15,087–126 = 14,961 records used to train and evaluate the ML models. 

Table 9 summarizes the final set of 25 attributes used to build the ML models. _One-hot-encoding_ the categorical attributes increased the num­ ber of features from 25 to 51. Dispersion represents the relative amount of variability (information) that each attribute contributes to the overall variance in the data. The dispersion measure is the _entropy_ and coeffi­ cient of variation (CV) for categorical and numerical attributes, 

5 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**==> picture [313 x 124] intentionally omitted <==**

**Fig. 3.** Positions of the recorded geospatial coordinates in the FRA database. 

**Table 8** 

**Table 9** 

Chronicle of Geospatial Coordinate Cleaning. 

Summary of the ML Attributes, their Dispersion, and Type. 

|**Table 8**<br>Chronicle of Geospatial Coordinate Cleaning.|**Table 9**<br>Summary of the ML Attributes, their Dispersion, and Type.| |---|---| |_3.3. Machine learning_<br>Many different types of ML models emerged over the years, and each<br>tend to behave differently on different types of datasets (James et al.,<br>2013). The next subsections describe the different types of models and<br>their hyperparameter tuning to optimize performance on the FRA<br>dataset.<br> <br>Attribute<br>Missing<br>Before<br>Missing<br>After<br>Procedure (N=29,297 records)<br>Latitude<br>21 %<br>(6415)<br>2%<br>(817)<br>Treat zero-flled values as missing. Pivot<br>STATION by TRK_TYP, aggregated as the<br>average geospatial coordinate. Fill missing<br>data with the mean value associated with the<br>track type if available, otherwise fll with the<br>maximum value.<br>Longitude<br>21 %<br>(6415)<br>2%<br>(820)<br>Treat zero-flled values as missing. Pivot<br>STATION by TRK_TYP, aggregated as the<br>average geospatial coordinate. Fill missing<br>data with the mean value associated with the<br>track type if available, otherwise fll with the<br>_minimum_value (Longitude is negative in U.<br>S.)<br>REC_ID<br>100 %<br>0% (0)<br>Add a record identifer as the row index.<br>Latitude<br>2% (817)<br>0% (6)<br>Merge the FRA records with the TIGER®<br>county shapefle by the FIPS5 code. Retain<br>the geospatial centroid coordinates for each<br>county. Add the state name abbreviation and<br>fag (MATCH) to the attributes. Add the<br>county name and state name strings to the<br>metadata. Fill missing FRA geospatial<br>coordinates with the county centroid<br>coordinates.<br>Longitude<br>2% (820)<br>0% (6)<br>Latitude<br>0% (6)<br>0% (0)<br>Manually fll missing geospatial coordinates<br>for counties in Alaska and Florida.<br>Longitude<br>0% (6)<br>0% (0)<br>FIPS5<br>0% (4)<br>0% (0)<br>Fill in missing FIPS5 codes for“Baltimore”<br>and“Skagway”stations.<br>LAT<br>0% (0)<br>0% (0)<br>Rename Latitude to LAT and Longitude to<br>LON after the geospatial cleaning procedure.<br>LON<br>0% (0)<br>0% (0)|Attribute<br>Dispersion<br>Type<br>Description (N=15,087, V=25,<br>T=1)| ||DERAILED<br>0.631<br>Categorical<br>Target attribute: 1 if the accident type<br>was derailment.<br>REGION<br>0.400<br>Categorical<br>Cleaned FRA region code for accident<br>location.<br>LAT<br>0.133<br>Continuous<br>Cleaned latitude coordinate<br>LON<br>−0.126<br>Continuous<br>Cleaned longitude coordinate<br>CLASS_RR<br>0.796<br>Ordinal<br>Cleaned railroad class.<br>MONTH<br>0.549<br>Ordinal<br>Incident month.<br>DAY<br>0.561<br>Ordinal<br>Incident day.<br>HR24<br>0.541<br>Continuous<br>Transformed time to fractional 24 -h.<br>TEMP<br>0.391<br>Continuous<br>Temperature (degrees Fahrenheit)<br>VISION<br>1.110<br>Categorical<br>Visibility: {Dawn, Day, Dusk, Dark}<br>WEATHER<br>0.977<br>Categorical<br>Weather: {Clear, Cloudy, Rain, Fog,<br>Sleet, Snow}<br>TRK_TYP<br>1.050<br>Categorical<br>Track Type: {Main, Yard, Siding,<br>Industry}<br>TRK_CL<br>0.753<br>Ordinal<br>Track Class: {X as 0, 1 through 9}<br>CWR<br>0.685<br>Binary<br>1 if the rail type was continuously<br>welded, 0 otherwise.<br>MOVEx<br>1.250<br>Categorical<br>Movement: {Blocks, Control, Signal,<br>Not Main, Restrict}<br>TRK_DEN_LG<br>0.972<br>Continuous<br>log(1+x) of annual track density in<br>millions of gross tons.<br>SIG<br>0.590<br>Binary<br>1 if used signals to control train<br>movements, 0 otherwise.<br>TRNSPD_LG<br>0.589<br>Continuous<br>log(1+x) of train speed in miles per<br>hour (mph).<br>SPD_OVR<br>−1.304<br>Continuous<br>Difference between train speed and<br>limit for track class.<br>CONSIST<br>0.950<br>Categorical<br>Consist: {Freight, Locomotive, Cars,<br>Work, Yard}<br>TONS_LG<br>0.757<br>Continuous<br>log(1+x) of gross tonnage, excluding<br>power units.<br>LOCOS<br>0.704<br>Ordinal<br>Number of headend locomotives.<br>N_CARS<br>0.915<br>Ordinal<br>Total number of cars.<br>CARS_LD<br>0.704<br>Continuous<br>Proportion of the number of cars that<br>were loaded (0–1)<br>CARS_HZMT<br>2.800<br>Continuous<br>Proportion of loaded cars carrying<br>hazardous materials (0–1)<br>HUMANS<br>0.562<br>Continuous<br>Number of humans present on the<br>train.|



## _3.3.1. Supervised classification models_ 

Table 11 summarizes the 11 different types of ML models used in this analysis. The table provides a brief description of how each algorithm works, their most important hyperparameters (HP), their overall ad­ vantages (A) and disadvantages (D). The table groups the models into four broader categories based on their underlying theory of operation: tree-based methods, statistical models, decision boundaries, and learned functions. Numerous excellent books describe the mathematics and theory of operations for each model; they are incorporated here by reference. G´eron (2017) discusses both the theory and practical imple­ mentation of decision tree (DT), random forest (RF), AdaBoost (AB), logistic regression (LR), support vector machine (SVM), stochastic 

gradient descent (SGD), and artificial neural network methods (G´eron, 2017). Jame et al. (2013) discusses both the theory and practical implementation of Naïve Bayes (NB), knearest-neighbors (kNN), and tree-based boosting methods (James et al., 2013). Hastie et al. (2016) provides similar coverage for all the models used in this analysis, including some key ML concepts such as bootstrapping, boosting, bagging, and ensemble learning (Hastie et al., 2016). Murphy (2012) covers the various methods from a more theoretical and probabilistic perspective (Murphy, 2012). 

6 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

(FP) rate as a function of the class membership probability (Fawcett, 2006). Intuitively, AUC measures the power of a model to distinguish among classes in the target attribute. An AUC score of 0.5 indicates that the model has no ability to distinguish among classes of the target whereas a value approaching 1.0 indicates that the model offers a large increase in TP rate for a small price of slightly increasing the FP rate. 

**Table 10** 

Outlier Algorithm Performance Evaluation. 

|Algorithm|Hyperparameters|AUC| |---|---|---| |One class SVM<br>One class SVM<br>One class SVM|Nu: 1%, Kernel Coeffcient: 0.01<br>Nu: 1%, Kernel Coeffcient: 0.1<br>Nu: 10 %, Kernel Coeffcient: 0.01|0.881<br>0.878<br>0.879| |Local Outlier Factor|C: 1%, Neighbors: 10, Euclidean|0.879| |Local Outlier Factor|C: 1%, Neighbors: 20, Euclidean|0.882| |Local Outlier Factor|C: 1%, Neighbors: 50, Euclidean|0.880| |Isolation Forest|C: 0%|0.881| |Isolation Forest|C: 1%|0.880| |Isolation Forest|C: 5%|0.880| |Covariance Estimator|C: 1%|0.817|



The performance evaluation procedure also monitored the classifi­ cation accuracy (CA), precision (Pc), recall (Rc), and F1 scores. Table 12 describes each metric and summarizes their advantages and disadvan­ tages. All performance metric except the AUC was sensitive to class imbalance in the dataset. 

CA is one of the most often cited performance metric for ML classi­ fiers. However, a high CA score can be misleading if the dataset has high class imbalanced. For example, a no-skill algorithm applied to a dataset with only 5% of the instances from one class and the rest from the other class will appear to have a 95 % accuracy if it picks the dominant class for every prediction. Stratified sampling of both the training and testing datasets helps to reduce the imbalance (Krawczyk, 2016). 

## _3.3.2. Hyperparameter tuning_ 

Each model requires that the user select values for key parameters (hyperparameters) that affect their performance. Tuning hyper­ parameters require incremental adjustments while observing a perfor­ mance metric. The optimization loop uses _k-fold cross validation_ to maximize the model _generalization_ on the entire dataset while reducing any tendency towards _overfitting_ or _underfitting_ . Models that have _regu­ larization_ parameters provide a means to balance the unavoidable tradeoff between _bias_ and _variance_ , which improves generalization on unseen data. James et al. (2013) provides an excellent description of the above ML terminologies and concepts, so the book is incorporated here by reference James et al. (2013). The performance evaluation metric used was the area under the curve (AUC) of the receiver operating characteristic (ROC). The AUC trends with hyperparameter value ad­ justments show where each model achieved its best regularized performance. 

## _3.4. Feature ranking_ 

Attributes that contain noisy, irrelevant, or redundant information can diminish the performance of ML methods (Yu and Liu, 2003). Hence, data scientists developed various methods to score features based on the amount of information they contribute towards distinguishing the target classes. This section compares five methods that rank features based on the strength of their association with the classes in the target attribute. Table 13 provides a short description of each method and a reference that provides details about their theory of operations. 

All methods work best with normalized attributes because their magnitudes become comparable. The diversity of methods result in 

The ROC plots the true positive (TP) rate against the false positive 

**Table 11** 

ML Models Compared. 

|Type|Model|Algorithm&Hyperparameters|Advantages and Disadvantages| |---|---|---|---| ||Decision Tree<br>(DT)|Recursive tree node splitting to maximize the purity of sub-trees.<br>HP: Minimum number of instances in leaves (N), and minimum size<br>of subsets (S).|A: Simple to interpret and to visualize. Works with non-numerical<br>categorical attributes. D: Tends to overft, resulting in low predictive<br>power on new data.| ||Random Forest<br>(RF)|Build many full trees for voting. Each tree grows from a<br>bootstrapped dataset and a random subset of attributes. HP:<br>Number of trees (_N_) and minimum size of subsets (S).|A: Offers the simplicity and intuition of decision trees but with less<br>tendency to overft, therefore, improves generalization on unseen<br>data. D: Incomplete trees diminish insights that full trees might<br>otherwise provide.| |**Tree-Based**<br>**Methods**|Ada Boost (AB)<br>Extreme Gradient<br>Boost (XGB)<br>Gradient Boost<br>(GB)|Sequentially build improved shallow trees for voting. HP: Number<br>of estimators (_N_), learning rate (_R_), boosting algorithm, and<br>regression loss function.<br>A highly confgurable version of gradient boosting. HP: Number of<br>estimators (N), learning rate (_R_), maximum tree depth (_S_), loss<br>function.<br>Sequentially build improved models that ft the errors of previous<br>models. HP: Number of estimators (N), learning rate (_R_), maximum<br>tree depth (_S_), loss function.|A: Selects only those features that improve predictive power, hence,<br>reducing the computational burden for datasets with very large<br>dimensionality. Less sensitive to overftting. D: Sensitive to the<br>presence of outliers and data with high incoherence.<br>A: Improved performance over gradient boosting and more effcient.<br>D: Sensitive to hyperparameter selection; requires manual<br>intervention to achieve the best confguration for a given dataset.<br>A: Effcient and good performance on large datasets; inherently<br>supports missing values. D: Sensitive to hyperparameter selection but<br>has fewer to tune than extreme gradient boosting.| |**Statistical**<br>**Models**|_k_-Nearest<br>Neighbors (_k_-NN)<br>Naïve Bayes (NB)|Determine the class of an instance based on the majority class of its<br>k nearest neighbors. HP: Number of neighbors (_k_), distance<br>method.<br>Applies Bayes theorem to determine the class probability, given<br>probabilities of the observations. HP: None|A: Method simplicity. D: Sensitive to a skewed class distribution. The<br>computational intensity grows exponentially with the number of<br>instances and attributes.<br>A: Fast and simple method. D: Poor performance when attributes are<br>not independent.| |**Decision**<br>**Boundaries**<br>**Learned**<br>**Functions**|Logistic<br>Regression (LR)<br>Support Vector<br>Machine (SVM)<br>Stochastic<br>Gradient Descent<br>(SGD)<br>Artifcial Neural<br>Network (ANN)|Establish a decision boundary by using a logistic function to<br>maximally separate classes. HP: Regularization function and<br>strength (C), and probability threshold.<br>Establish a decision boundary by fnding a multidimensional<br>hyperplane to maximally separate classes. HP: Kernel type, cost (C),<br>and regression loss (ε)<br>An optimization technique that fts a linear multivariate function to<br>the data. It works best when all features are scaled. HP: Loss<br>function, learning rate method and parameters.<br>A weighted multilayer linear network that represents a function.<br>HP: Hidden layer neurons (N), solver type, regularization<br>parameter (α), number of iterations (I).|A: Inherits many of the advantages of linear regression; precisions are<br>easy to make. D: Sensitive to noise in the data such as outliers and<br>incorrectly classifed instances. Model ftting may fail to converge if<br>there are many highly correlated features.<br>A: High accuracy with low computational complexity. D: Sensitive to<br>noisy data and multidimensional planes that lack clear boundaries.<br>A: An effcient technique on large datasets.<br>D: Sensitive to feature scaling; many hyperparameters; and the true<br>minima may not be achieved because the gradient is only an<br>approximation.<br>A: Accuracy improves with use and feedback about classifcation<br>accuracy. D: Requires many training examples to improve<br>classifcation accuracy.|



7 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

## _3.5. Principle component analysis_ 

**Table 12** 

Classifier Performance Metric. 

The method of principle component analysis (PCA) creates a set of new orthogonal basis vectors, each maximally spanning the dimensions of feature space, in the order of the data variance (Jolliffe and Cadima, 2016). Each principle component (PC) is a linear combination of all _numerical_ features in the dataset. Intuitively, the first two principle components form a plane in feature space that is _closest_ to all the data instances, as measured by the Euclidean distance. Data clusters tend to form along the directions of maximum variance. Hence, attributes that most influence the formation of data clusters contribute to inherent structure in the data. The terminology used in the literature is that each PC “explains” some proportion of the total variance (information) in the dataset. Therefore, features that are weak components of most PCs tend to be associated with noise in the data. Analyst also use PCA to transform high dimensional data into a lower dimension feature space to enable the visualization of both structure and noise in the dataset (Anowar et al., 2021). 

|**Table 12**<br>Classifer|<br>Performance Metric.||| |---|---|---|---| |Metric|Description|Advantages|Disadvantages| |CA|The proportion of|Simply calculation.|Sensitive to data| ||predictions that were<br>correct.||imbalance where a no-<br>skill classifer can| ||||appear to provide| ||||better performance by| ||||predicting the| ||||dominant class every| ||||time. For example, a<br>no-skill classifer will| ||||score CA at 90 % if the| ||||database labels 90 % of| ||||the accidents as| ||||derailments.| |Pc|The proportion of|Measures the|A bias towards the| ||observations correctly|probability of|majority class can be| ||predicted as positives|mislabeling a|misleading.| ||(TP) to the total|negative sample as|| ||number of|positive.|| ||observations||| ||predicted as positives||| ||(TP+FP).||| |Rc|Measures the|Measures the|A bias towards the| ||proportion of positive|probability of|majority class can be| ||predictions (TP) to the|correctly labeling all|misleading.| ||total number of|the positive|| ||positive observations|observations.|| ||(TP+FN)||| |F1|The harmonic mean of|Measures the|Less bias but as a| ||Pc and Rc, scaled from|balance between|function of Pc and Rc| ||0 to 1.|precision and recall.|will retain some bias.| |AUC|Area under the ROC|Removes biased|More complex| ||curve that plots TP|scores for|calculation than a| ||against FP as a|imbalanced|simple ratio. Requires| ||function of class|datasets.|the class membership| ||membership||probability for every| ||probability.||prediction, which may| ||||not be inherently| ||||available from a model.|



## **4. Results** 

The subsections of this section present the results of applying ma­ chine learning, attribute ranking, and PCA to the cleaned and trans­ formed dataset presented in the previous section. 

## _4.1. Machine learning_ 

Table 14 summarizes the stabilized performance of each ML algo­ rithm, sorted by the AUC metric. The null model is a no-skill model that predicts the dominant class each time. It provided a baseline to compare the performance score of skilled classifiers. As expected, the CA score for the no-skill classifier reflected the class imbalance of 67.42 % for derailment type accidents versus non-derailment type accidents. How­ ever, the AUC performance of the null classifier was lowest as expected. 

Tracking the AUC trend with 10-fold cross validation and stratified sampling produced the optimum hyperparameter values shown in the table. Hyperparameters with common names across some models were the learning rate (L), loss function (LF), regularization (R) parameters, 

**Table 13** 

Feature Ranking by Scoring Methods. 

|some compensating for the weaknesses of the other; therefore, they do<br>not provide identical rankings (Wang et al., 2010). However, a strong<br>correlation among rankings indicates that the top-ranking attributes do<br>contribute most towards ML classifcation performance.<br>Method<br>Description<br>Reference<br>ANOVA<br>Analysis of Variance (ANOVA) measures the<br>difference between average values of a feature in<br>different classes of the target, based on the F<br>distribution.<br>(Agresti,<br>2018)<br>Chi-Squared<br>Measures a dependency or association between<br>the feature and the target class by using a chi-<br>square statistic.<br>(Wang et al.,<br>2010)<br>Information<br>Gain<br>The expected amount of entropy reduction. A<br>decrease in entropy (uncertainty) based on the<br>presence of other features will increase<br>information.<br>(Yu and Liu,<br>2003)<br>Gain Ratio<br>Reduces the bias of Information Gain towards<br>features that have many values by taking the<br>ratio of Information Gain to the intrinsic<br>information (entropy) of the feature.<br>(Quinlan,<br>1986)<br>Gini<br>Decrease<br>A measure of the inequality among values of a<br>frequency distribution based on their statistical<br>dispersion. A value of zero and one represents<br>perfect equality and inequality, respectively, of<br>the distribution of a feature within each target<br>class.<br>(Han et al.,<br>2016)|**Table 14**<br>Model Performance and Optimum Hyperparameter Settings.| |---|---| ||Model<br>AUC<br>CA<br>F1<br>PR<br>RC<br>Optimum<br>Hyperparameters| ||XGB<br>0.888<br>0.828<br>0.875<br>0.859<br>0.892<br>γ:0, Max Depth: 6, Min<br>Child Weight: 1, R:1, w:1,<br>L:0.2,<br>GB<br>0.884<br>0.824<br>0.872<br>0.854<br>0.891<br>LF: LR, Trees (_N_): 100, L:<br>0.2, Min Samples Leaf: 1<br>RF<br>0.882<br>0.821<br>0.817<br>0.817<br>0.821<br>Trees (_N_): 60, Attributes/<br>Split: 5, Min Subset: 5<br>DT<br>0.854<br>0.803<br>0.801<br>0.800<br>0.803<br>Max Depth: 10, Min<br>Samples Leaf (_N_): 90, Min<br>Subset: 5<br>ANN<br>0.838<br>0.786<br>0.785<br>0.784<br>0.786<br>Hidden Nodes: 100,<br>Activation: ReLu, OA:<br>Adam (α:10−4)<br>LR<br>0.832<br>0.783<br>0.777<br>0.777<br>0.783<br>R (L2, C:5)<br>SGD<br>0.828<br>0.783<br>0.776<br>0.776<br>0.783<br>LF: (LR,ε:1), R: E.Net<br>(α:10−5, 0.15), L: IVS<br>(η0:10-2,_t_:0.25)<br>kNN<br>0.803<br>0.765<br>0.759<br>0.758<br>0.764<br>_N_: 30, Distance<br>(Euclidean, Weights:<br>Uniform)<br>NB<br>0.794<br>0.725<br>0.730<br>0.740<br>0.725<br>No parameters to tune<br>ADB<br>0.713<br>0.746<br>0.746<br>0.747<br>0.746<br>Trees (_N_): 50, LF: Linear,<br>OA: SAMME.R, LR: 1.0<br>SVM<br>0.626<br>0.654<br>0.639<br>0.633<br>0.654<br>Kernel: Sigmoid, R (C:0.2,<br>ε:1.0)<br>Null<br>0.500<br>0.674<br>0.543<br>0.455<br>0.674<br>No parameters to tune|



8 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

and optimizer algorithm (OA). To demonstrate the effect of hyperparameter tuning, Fig. 4 plots the AUC score for a range of hyperparameter _N_ associated with RF, kNN, and DT. 

**Table 15** 

Feature Importance Ranking. 

|Feature|ANOVA|χ2|Info. Gain|Gain Ratio|Gini| |---|---|---|---|---|---| |TRK_CL|1|2|4|3|2| |MOVEx=Signal|2|3|3|1|4| |SPD_OVR|3|1|7|11|3| |SIG|4|4|5|2|5| |HUMANS|5|7|6|10|6| |TRK_TYP=Main|6|5|9|6|7| |CWR|7|6|1|8|8| |MOVEx=Not Main|8|11|11|9|11| |LOCOS|9|9|10|12|9| |CONSIST=Cars|10|8|14|4|12| |TRK_TYP=Industry|11|10|12|7|14| |TRK_TYP=Yard|12|16|2|18|16| |TONS_LG|13|14|15|20|17| |CARS_LD|14|18|13|19|13| |CONSIST=Yard|15|15|18|17|19| |N_CARS|16|12|28|16|10| |MOVEx=Restrict|17|17|26|15|20| |LAT|18|20|22|32|22| |TEMP|19|22|24|30|21| |TRK_TYP=Siding|20|21|25|13|24| |VISION=Dark|21|24|21|24|25| |CLASS_RR|22|13|30|14|15| |TRK_DEN_LG|23|19|20|22|18| |REGION=7.0|24|23|19|21|26| |VISION=Day|25|31|29|35|27| |REGION=8.0|26|26|27|23|28| |REGION=6.0|27|27|23|28|29| |REGION=2.0|28|28|33|25|30| |TRNSPD_LG|29|25|37|5|1| |REGION=3.0|30|29|31|31|31|



As noted in Table 14, the hyperparameter _N_ represents the number of trees of a RF, the minimum number of samples to retain in the leaves of a DT, and the number of nearest neighbors for the kNN algorithm. The asymptotic trend was similar for all hyperparameters tuned. 

## _4.2. Feature ranking_ 

Table 15 shows the importance ranking of the first 30 features in their strength of association with the target class. The rank by each of the five scoring methods are correlated as indicated by their pairwise cor­ relation coefficients listed in Table 16. The correlation ranges from 84.2 % for the gini and chi-squared methods to 94.5 % for the ANOVA and chi-squared methods. 

Fig. 5 shows the probability distribution of derailment and nonderailment type accidents for the top two attributes (track class, movement authorization) and the fourth ranking attribute (signalized territory). 

The distributions show that these attributes have some power to separate derailment from non-derailment type accidents, but with un­ certainty based on the amount of overlap in their class distributions. For example, the class probability was higher for derailment type accidents on class 0, 1, 2, 7, 8, and 9 tracks (Fig. 5a). The distinction is significant for class 1 tracks because it has the highest frequency of occurrence (Fig. 5b). Similarly, the class probability was higher for derailment type accidents where movement authority was within restricted limits (restricted) or where movement was not on main tracks (Fig. 5c). Similarly, the class probability was higher for derailment type accidents in non-signalized territories (Fig. 5d). The probability difference was much lower for the lower ranking attributes, but taken together, they improve the ML classification performance. 

**Table 16** 

Correlation of Ranking Methods. 

|Method A|Method B|Correlation| |---|---|---| |ANOVA|Chi-Squared|0.945| |ANOVA|Info. Gain|0.897| |Gain Ratio|Gini|0.843| |Gini|Chi-Squared|0.842|



Fig. 6 is a box plot that shows the distribution and statistics of excess speed for derailment and non-derailment type accidents. 

All accidents tended to occur below the speed limit for the track class on which they operated. However, derailment type accidents tended to occur closer to the speed limit than non-derailment type accidents. A student’s _t_ -test shows that the p-value was near zero, which indicated that the mean difference of 10 mph (16 kph) was statistically significant. The highlighted boxes in the figure indicates the values of the first quartile (25 %) through the third quartile (75 %) of the dataset. The solid vertical and horizontal lines indicate the mean and standard de­ viation, respectively. The lighter solid vertical lines indicate the median values. 

## _4.3. Principle component analysis_ 

Fig. 7 plots the proportion of variance in the data that each PC explained. The top and bottom curves show the cumulative variance and component variance explained, respectively, as a function of each addition PC in their ranked order. This analysis indicated that the first six PCs explained just over half of the variance in the dataset. Each of the remaining 45 of 51 total PCs incrementally explain less than 4% of the variance each, but together account for the remaining half of the vari­ ance explained. 

**==> picture [216 x 165] intentionally omitted <==**

Fig. 8 and 9 are visualizations of the PC clusters that suggest struc­ ture and noise in the dataset. 

Fig. 8 shows that PC1 and PC4 form elongated elliptical clusters for the top ranking attributes of track class (Fig. 8a), movement authority (Fig. 8b), and track type (Fig. 8c). Fig. 8d shows the distribution of the target class in the same PC feature space, where the color shading in­ dicates a bias towards the left clusters with negative PC1 values. 

Fig. 9 shows that PC2 and PC3 form nine distinct clusters for visi­ bility (Fig. 9a), hour (Fig. 9b), and weather (Fig. 9c). Fig. 9d shows the distribution of the target class across each cluster. The clusters of the higher-ranking attributes (Fig. 8) are less distinct than those of the lower ranking attributes (Fig. 9), which is further discussed for interpretation in the next section. 

## **5. Discussion** 

The performance of the top four ML methods reflected the 

**Fig. 4.** AUC score as a function of hyperparameter _N_ . 

9 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**==> picture [433 x 389] intentionally omitted <==**

**==> picture [233 x 13] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig. 5. Class probability for the top two and fourth ranking attributes.<br>**----- End of picture text -----**<br>


**==> picture [217 x 185] intentionally omitted <==**

**==> picture [168 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig. 6. Distribution and statistics for excess speed.<br>**----- End of picture text -----**<br>


**==> picture [217 x 206] intentionally omitted <==**

**==> picture [228 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br> Fig. 7. The proportion of variance in the data that each PC explains.<br>**----- End of picture text -----**<br>


10 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**==> picture [457 x 358] intentionally omitted <==**

**Fig. 8.** Data clusters for attributes with high power to distinguish among the target classes. 

effectiveness of the custom data cleaning procedures, including the LAP technique introduced for imputing missing values. The LAP method was most effective in filling missing values for track density, but that attri­ bute ranked low in importance for classification. Although effective, one limitation of the LAP technique is that it provided a course imputation of the geospatial coordinates, based on an aggregation of entries from other records where a value was present for the track type near that station. However, the LAP method provided a more intelligent and effective scheme to impute missing values such as track density based on those of _spatial_ neighbors rather than guessing values based on the mean, most frequent, or nearest neighbors in feature space. The geospatial join method provided the next best alternative to repair erroneous or lowresolution geospatial data. The distinctive southeast skew pattern revealed those records with low-resolution data entry. 

relative power to separate the distributions of the categories in the target class. That is, an exceptionally high overlap of the two class distributions ranked the attribute exceptionally low in importance towards classifier performance. It is rare that any one attribute can completely distinguish among class members with 100 % accuracy, otherwise there would be no need to use additional attributes as explanatory factors for classifi­ cation. Rather, a combination of attributes contributes their ability to help determine the probability of class membership. Poor classification results with all types of classification models may indicate that all at­ tributes have a high degree of overlap in their class probability distributions. 

The PCA result (Fig. 7) shows that the first 6 PCs explain more than half the variance in the dataset but that it takes the remaining PCs, which accounted for 88 % of the PCs, to explain the remaining half of the variance in the data set. This outcome indicates that the first six PCs represented the bulk of the information in the dataset. By extension, the remaining PCs likely account for noise in the dataset based on the slow accumulation of the variance they explained. This result suggests that just under half of the variance in the dataset lack structure and, there­ fore, constitutes the noise in the dataset. 

The top four algorithms of XGB, GB, RF, and DT were all based on the theories of decision trees. Using the traditional academic grading system for performance, the top four models provided “good” overall perfor­ mance based on an AUC score greater than 85 %. The highest AUC score of nearly 89 % for XGB was associated with a classification accuracy and balanced precision-recall scores (F1) of nearly 83 % and 88 %, respec­ tively. All methods were sensitive to hyperparameter tuning as demonstrated in the performance improvement trends of Fig. 4. The hyperparameter tuning sensitivity cautions against using the default values suggested for each method. 

Fig. 8 further illustrates structure in the dataset by clusters formed from PC1 and PC4 for the top-ranking features of track class, movement authority, and track type. One can visualize the amount of noise by the amount of attribute contamination of clusters and isolation from clus­ ters. Even though the target class was spread across all clusters (Fig. 8d) there was an observable bias of derailment type accidents towards clusters on the left. The bias corresponds to clusters of class 1 tracks (Fig. 8a), movement authorities not on the mainline (Fig. 8b), and non- 

All feature ranking methods and PCA pointed to track class (TRK_CL), signalized movement authority (MOVEx = Signal), speed excess, and signalized territory (SIG) as the most important features in ML classifier performance. The interpretation of an attribute rank is its 

11 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

**==> picture [457 x 366] intentionally omitted <==**

**Fig. 9.** Data clusters for attributes with low power to distinguish among the target classes. 

main track types (Fig. 8c). This result suggests that features that align with the cluster where the derailment class is biased associates more with derailment than non-derailment type accidents. 

attribute similarity. Consequently, noisy neighborhoods can hamper classification performance as evidenced by the low performance rank of kNN. Methods such as SVM and LR seek clear decision boundaries in multidimensional feature space. Hence, the lack of clear hyperplanes between the target classes hampered their performance. In fact, SVM achieved the lowest performance. 

Fig. 9 shows that PC2 and PC3 form clusters for the attributes of visibility (Fig. 9a), hour (Fig. 9b), and weather (Fig. 9c), which are lowranking. The even distribution of each target class across each cluster (Fig. 9d) agreed with their low importance ranking. Interestingly, the level of isolation noise was much lower for those lower-ranking attri­ butes. The contamination noise in the center column of the cluster grid (Fig. 9a) suggest similarities in the visibility at dawn and dusk, as ex­ pected. Those similarities also corresponded to the separation of “Hour 24” (Fig. 9b) where day, night, and visibility transition times corre­ sponded to the expected hour ranges. The contamination in the center row of clusters of the cluster grid (Fig. 9c) suggest similarities in weather conditions like snow, sleet, rain, and fog. Hence, the clustering results were as expected. The low level of isolation noise observed for the clusters of the low-ranking features would have helped the ML perfor­ mance more had the situation occurred for the clusters of the highestranking features. 

Overall, the analysis suggested that derailments were more strongly associated with lower track classes, non-signalized territories, and movement authorizations with restricted limits. Derailments also tended to occur at 10 mph (16 kph) below the speed limit of the track class whereas non-derailment type accidents tended to occur at 20 mph (32 kph) below the limit. Those findings correspond with the intuition that lower-class tracks, which has lower speed limits, and movements with restricted limits are so designated because those operations are associ­ ated with higher safety risks, which the ML confirmed. Similarly, there is less guidance for movements in territories without signalization, so the risk of derailments due to track irregularities or switch problems is higher. However, it may not be wise to go beyond probabilities and statistical associations by assuming general latent reasons for the ML outcome because there are no exclusive distinctions between accident causes for each accident type. 

The above insights about the location of structure and noise in the dataset provided clues to understand the reason for the performance differences of each ML method. Randomized tree-based methods tend to train on various cross-sections of a dataset and use voting to determine the class likelihood. In contrast, the other methods tend to leverage structure in the dataset. Hence, the randomized tree-based methods such as XGB, GB, and RF performed better by discovering patterns across noisy neighborhoods in the dataset. On the other hand, kNN seeks local neighborhoods in feature space to predict class membership based on 

One limitation of the railroad accident database is that it does not necessarily list accidents where the financial loss was below $10,500 because the FRA does not require railroads to report those. A second limitation is that the financial loss includes only the costs of repairing equipment, signal systems, and infrastructure structures. Losses do not include costs associated with cleanup, lost freight, societal damages, fatalities, injuries, and line closures. Nevertheless, financial loss was not 

12 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

a pre-incident explanatory variable, but any future analysis that uses it should be aware of this limitation in the dataset. 

curation, Formal analysis, Writing - original draft. **Denver D. Tolliver:** Supervision, Resources, Funding acquisition, Project administration, Validation, Writing - review & editing. 

## **6. Conclusions** 

## **Declaration of Competing Interest** 

Railroads have been one of the most important modes of transport for more than a century. Unfortunately, accidents continue to plague their operating safety and efficiency. Derailments have consistently domi­ nated other accident types and resulted in the greatest financial loss. Therefore, gaining insights into factors that are more strongly associated with derailments than other accident types can inform more costeffective and impactful risk management strategies. 

The authors report no declarations of interest. 

## **References** 

Abidin, N.Z., Ismail, A.R., Emran, N.A., 2018. Performance analysis of machine learning algorithms for missing value imputation. Int. J. Adv. Comput. Sci. Appl. 9 (6). Agresti, A., 2018. Statistical Methods for the Social Sciences, 5th ed. Pearson, Boston, Massachusetts. p. 608. Anowar, F., Sadaoui, S., Selim, B., 2021. Conceptual and empirical comparison of dimensionality reduction algorithms (PCA, KPCA, LDA, MDS, SVD, LLE, ISOMAP, LE, ICA, t-SNE). Comput. Sci. Rev. 40, 100378. ASCE, 2017. Infrastructure Report Card. American Society of Civil Engineers, Reston, VA. Breunig, M.M., Kriegel, H.-P., Ng, R.T., Sander, J., 2000. LOF: identifying density-based local outliers. Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data. Bridgelall, R., Tolliver, D.D., 2020. Closed form models to assess railroad technology investments. Transp. Plan. Technol. 43 (7), 639–650. Bridgelall, R., Lu, P., Tolliver, D.D., Xu, T., 2018. Mining connected vehicle data for beneficial patterns in Dubai taxi operations. J. Adv. Transp. 2018, 1–8. Cook, N.R., 2007. Use and misuse of the receiver operating characteristic curve in risk prediction. Circulation 115 (7), 928–935. Dabbour, E., Easa, S., Haider, M., 2017. Using fixed-parameter and random-parameter ordered regression models to identify significant factors that affect the severity of drivers’ injuries in vehicle-train collisions. Accid. Anal. Prev. 107, 20–30. Echauz, J., Vachtsevanos, G., 1995. Fuzzy grading system. IEEE Trans. Educ. 38 (2), 158–165. Fawcett, T., 2006. An introduction to ROC analysis. Pattern Recognit. Lett. 27 (8), 861–874. FRA, 2011. Rail Equipment Accident/Incident Data File Structure and Field Input G´eron, A., 2017. Hands-On Machine Learning With Scikit-learn and TensorFlow: Specifications. Federal Railroad Administration (FRA), Washington, D.C. Concepts, Tools, and Techniques to Build Intelligent Systems, 2nd ed. O’Reilly Media, Sebastopol, California. p. 856. Ghofrani, F., He, Q., Goverde, R.M., Liu, X., 2018. Recent applications of big data analytics in railway transportation systems: a survey. Transp. Res. Part C-Emerg. Technol. 90, 226–246. Han, H., Guo, X., Yu, H., 2016. Variable selection using mean decrease accuracy and mean decrease gini based on random Forest. The 7th IEEE International Conference on Software Engineering and Service Science (ICSESS). Hastie, T., Tibshirani, R., Friedman, J., 2016. The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2nd ed. Springer, New York, New York, p. 767. Ilyas, I.F., Chu, X., 2019. Data Cleaning. Association for Computing Machinery and Morgan & Claypool Publishers, New York, NY, p. 282. Iranitalab, A., Khattak, A.J., 2017. Comparison of four statistical and machine learning methods for crash severity prediction. Accid. Anal. Prev. 108, 27–36. Iranitalab, A., Khattak, A.J., 2020. Probabilistic classification of hazardous materials release events in train incidents and cargo tank truck crashes. Reliab. Eng. Syst. Saf. 199, 106914. James, G., Witten, D., Hastie, T., Tibshirani, R., 2013. An Introduction to Statistical Learning With Applications in R, 112. Springer, New York. Jesmeen, M.Z.H., Hossen, J., Sayeed, S., Ho, C., Tawsif, K., Rahman, A., Arif, E., 2018. A survey on cleaning dirty data using machine learning paradigm for big data analytics. Indones. J. Electr. Eng. Comput. Sci. 10 (3), 1234–1243. Jolliffe, I.T., Cadima, J., 2016. Principal component analysis: a review and recent developments. Philos. Trans. Math. Phys. Eng. Sci. 374 (2065), 20150202. Keramati, A., Lu, P., Iranitalab, A., Pan, D., Huang, Y., 2020. A crash severity analysis at highway-rail grade crossings: the random survival forest method. Accid. Anal. Prev. 144, 105683. Krawczyk, B., 2016. Learning from imbalanced data: open challenges and future directions. Prog. Artif. Intell. 5 (4), 221–232. Lasisi, A., Attoh-Okine, N., 2019. Machine learning ensembles and rail defects prediction: multilayer stacking methodology. ASCE. J. Risk Uncertain. Eng. Syst. A. Civ. Eng. 5 (4), 4019016. Li, H., Parikh, D., He, Q., Qian, B., Li, Z., Fang, D., Hampapur, A., 2014. Improving rail network velocity: a machine learning approach to predictive maintenance. Transp. Res. Part C-Emerg. Technol. 45, 17–26. Liu, J., Khattak, A.J., 2017. Gate-violation behavior at highway-rail grade crossings and the consequences: using geo-spatial modeling integrated with path analysis. Accid. Anal. Prev. 109, 99–112. Liu, F.T., Ting, K.M., Zhou, Z.-H., 2012. Isolation-based anomaly detection. ACM Trans. Knowl. Discov. Data 6 (1), 3. Liu, X., Saat, M.R., Barkan, C.P., 2017. Freight-train derailment rates for railroad safety and risk analysis. Accid. Anal. Prev. 98, 1–9. Manning, W.G., Mullahy, J., 2001. Estimating log models: to transform or not to transform? J. Health Econ. 20 (4), 461–494. 

Recent advancements in computing capacity and their cost reduction has enabled machine learning (ML) methods to uncover patterns in large multidimensional datasets that are difficult to analyze with common rule-based and statistical methods. However, there are many types of ML techniques, and no single method works best for all types of datasets. Therefore, this work applied 11 different types of ML models to a large multidimensional dataset of railroad accidents to compare their per­ formance in predicting derailments from other accident types. The extreme gradient boosting (XGB) classifier provided the best predictive performance with an AUC score of 89 %. The model could distinguish accident type with an accuracy of 83 %. Principle component analysis (PCA) revealed that high feature contamination noise and isolation noise would prevent significant further gains in classification accuracy by any algorithm. 

The good ML performance affirmed the relevance and sufficiency of the attributes in their contribution towards distinguishing derailments from other accident types. Hence, knowing the relative importance of those attributes towards classification accuracy can lead to insights for decision-making in railroad risk management. The importance ranking used five different methods that agreed on the ranking with correlations – ranging from 84.2% 94.5%. The ANOVA and chi-squared methods agreed with the highest correlation that the top four attributes were track class, the type of movement authority, the excess speed, and the presence of signalization in the territory. The feature distribution for each target class and the PCA agreed that relative to non-derailment type accidents, derailments were more strongly associated with lower track classes, non-signalized territories, and movement authorizations with restricted limits. Derailments also tended to occur at 10 mph (16 kph) below the speed limit of the track class whereas non-derailment type accidents tended to occur at 20 mph (32 kph) below the limit. 

The good ML performance also suggests that the custom data imputation techniques presented were effective in filling missing values. The data-cleaning framework also demonstrated a spatial join technique that addressed 21.8 % of the geospatial data entry errors. The detailed chronicle of the cleaning procedures will help other researchers save a substantial amount of time in data preparation when using the same dataset. Future work will leverage the framework to examine trends in accidents caused by human error to determine the effectiveness of PTC deployments relative to historic accident rates. 

## **Data availability** 

This paper cited the sources of all the data used, which are currently publicly available. 

## **Funding statement** 

The authors conducted this work with support from North Dakota State University and the Mountain-Plains Consortium, a University Transportation Center funded by the U.S. Department of Transportation. 

## **CRediT authorship contribution statement** 

Murphy, K.P., 2012. Machine Learning : A Probabilistic Perspective. The MIT Press, Cambridge, Massachusetts. 

**Raj Bridgelall:** Conceptualization, Methodology, Software, Data 

13 

_Accident Analysis and Prevention 156 (2021) 106126_ 

_R. Bridgelall and D.D. Tolliver_ 

Olson, R.S., Cava, W.G.L., Orzechowski, P., Urbanowicz, R.J., Moore, J.H., 2017. PMLB: a large benchmark suite for machine learning evaluation and comparison. BioData Min. 10 (1), 1–13. 

heterogeneity-based statistical modeling approach. Accid. Anal. Prev. 150, p. 105835. 

Wang, H., Khoshgoftaar, T.M., Gao, K., 2010. A comparative study of filter-based feature ranking techniques. In: 2010 IEEE International Conference on Information Reuse & Integration. Las Vegas, Nevada. 

Quinlan, J.R., 1986. Induction of decision trees. Mach. Learn. 1 (1), 81–106. 

Rahm, E., Do, H.H., 2000. Data cleaning: problems and current approaches. IEEE Data (base) Eng. Bull. 23, 3–13. 

Wang, B.Z., Barkan, C.P.L., Saat, M.R., 2020. Quantitative analysis of changes in freight train derailment causes and rates. J. Transp. Eng. Part A Syst. 146 (11), p. 4020127. Yu, L., Liu, H., 2003. Feature selection for High-dimensional data: a fast correlationbased filter solution. In: The Twentieth International Conference on Machine Learning (ICML-2003). Washington, D.C.. 

Rousseeuw, P.J., Driessen, K.V., 1999. A fast algorithm for the minimum covariance determinant estimator. Technometrics 41 (3), 212–223. 

Soleimani, S., Mousa, S.R., Codjoe, J., Leitner, M., 2019. A comprehensive railroadhighway grade crossing consolidation model: a machine learning approach. Accid. Anal. Prev. 128, 65–77. 

Zhang, Z., Liu, X., Holt, K., 2018. Positive Train Control (PTC) for railway safety in the United States: policy developments and critical issues. Util. Policy 51 (2018), 33–40. 

Wali, B., Khattak, A.J., Ahmad, N., 2021. Injury severity analysis of pedestrian and bicyclist trespassing crashes at non-crossings: a hybrid predictive text analytics and 

14