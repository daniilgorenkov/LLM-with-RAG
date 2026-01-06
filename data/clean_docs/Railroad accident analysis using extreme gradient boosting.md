# Accident Analysis and Prevention## Railroad accident analysis using extreme gradient boostinga Department of Transportation, Logistics & Finance, College of Business, North Dakota State University, Fargo, ND, 58108, United States
b Upper Great Plains Transportation Institute, North Dakota State University, Fargo, ND, 58108, United StatesRailroads are critical to the economic health of a nation. Unfortunately, railroads lose hundreds of millions of dollars from accidents each year. Trends reveal that derailments consistently account for more than 70 % of the
U.S. railroad industry’s average annual accident cost. Hence, knowledge of explanatory factors that distinguish
derailments from other accident types can inform more cost-effective and impactful railroad risk management strategies. Five feature scoring methods, including ANOVA and Gini, agreed that the top four explanatory factors
in accident type prediction were track class, type of movement authority, excess speed, and territory signali
zation. Among 11 different types of machine learning algorithms, the extreme gradient boosting method was most effective at predicting the accident type with an area under the receiver operating curve (AUC) metric of 89
%. Principle component analysis revealed that relative to other accident types, derailments were more strongly
associated with lower track classes, non-signalized territories, and movement authorizations within restricted limits. On average, derailments occurred at 16 kph below the speed limit for the track class whereas other ac
cident types occurred at 32 kph below the speed limit. Railroads can use the integrated data preparation, ma
chine learning, and feature ranking framework presented to gain additional insights for managing risk, based onfor more than 150 years. Today, U.S. railroads carry approximately onethird of the nation’s exports (ASCE, 2017). Therefore, the safe and
efficient operation of railroads is crucial to the nation’s economic health.
Unfortunately, railroads lose hundreds of millions of dollars from acci
dents each year. Analysis of the Federal Railroad Administration (FRA)
Tolliver, 2020). Hence, the federal government mandated that railroads
accidents caused by human errors (Zhang et al., 2018). With PTC now in
The **goal** of this research is to identify factors associated with theTherefore, the ability to identify and rank features that increase the riskwards the classification accuracy. However, no single type of ML model
dirty data costs the U.S. economy trillion of dollars each year (Ilyas and
Chu, 2019). A survey of data cleaning for ML found that the failure to
(Jesmeen et al., 2018). Although a few approaches to data cleaning are
common, every dataset poses unique challenges (Bridgelall et al., 2018).
Hence, data scientists spend an average of 60 % of their time cleaningR. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126techniques are those that detect and remove outliers and duplicate re
effectively clean all types of datasets. Other techniques that can find data
Custom techniques tend to be heuristic, so they require good familiarity- Visualizing and interpreting the classification power of each attriin relation to the contributions of this research. Section 4 mirrors sub
sections of the methods section to present the results. Section 5 discusses
the significance and interprets the outcome. Section 6 recaps the find(2017) compared the performance of Multinomial Logit (MNL), kNearest Neighbor (kNN), Support Vector Machines (SVM) and Random
had the best and worst performance, respectively, when applied to crash
data from Nebraska, United States. A recent survey of big data analyticsshould be closed to prevent accidents (Soleimani et al., 2019). Wali et al.field (Olson et al., 2017). For example, a performance score consideredby applying various methods to reduce noise, repair data entry errors,
and fill in missing values. The processing layer prepares relevant attri
Hence, there was no entry for the “SIGNAL” field prior to the switchover
date. Similarly, a field indicating the method of operation (“MOPERA”)
form also added a field “SSB1” to indicate if the track was a continuouslyDuplication Attribute contains the same information as (Ilyas and Chu,Redundancy Attribute contains information that is inherent (Liu et al., 2012)Dispersion Attribute has low variance or carries little or (Bridgelall et al.,Duplication 8 with duplicated information (e.g. IMO, IYR, 126 - 8 = 118
Correlated 12 with > 90 % correlation with other attributes 102− 12 = 90irrelevant attributes or features. The classification of those criteria is aR. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 1061262012). A side benefit was that the eliminated records also removed a few
records from 29,297 to 15,087. The statistics shown in the table are the
indicated if the accident was a derailment type or not, and it became thelong tails as outliers or because extreme values provide insufficient exattribute. The proportion transformation retained information about the
within the range. Table 4 chronicles the transformation of attrieliminated post-event attributes such as the number of people injured,
killed, or evacuated. Table 5 chronicles the feature reduction from 401) Packaged similar features of an attribute to simplify the categories.SPDOVR 46 + 1–1 = 46
Temporary geospatial filter flag for county mismatch.fore, data scientists developed a few methods to impute or guess missing
those of their nearest neighbors in feature space . However, the existingwards predicting the target class. Therefore, this research developed a values based on spatial proximity rather than feature space proximity.example, for numerical values such as track density, the method used the
maximum of the aggregated value for a location. The method did not use
bias in the aggregation. A fringe benefit of using the LAP method is thatthe impact of each method. Missing or erroneous geospatial coordinatesR. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126CWR Renamed SSB1 to CWR (continuously welded rail); binarized as “1 [′′] =WEATHER Recoded nominal values in WEATHER as labels {Clear, Cloudy, Rain,
TRKTYP Renamed TYPTRK (track type) and labeled nominal codes as {Main,
VISION Renamed VISIBLTY and replaced nominal codes as descriptive {Dawn,CLASSTRK Renamed TRKCLAS (track class) and cleaned to contain ordinal values{1} → “Freight”, {2, 3, B, C} → “Passenger”, {8, D, E} → “Locomotive”,However, a coarse location such as a large state may introduce bias in
the ML process. Fortunately, the FRA database contains the station name
that is closest to the accident location, so its location can be a surrogatewards the southeast. This skew suggested that there was a lack of res
south and east, respectively. The result was that 21. % of the records
contained the geospatial centroid of each county in the United States. Aordinates in each step of the procedure. The LAP method used all recordsber of features from 25 to 51. Dispersion represents the relative amountvariance in the data. The dispersion measure is the entropy and coeffigeneralization of a model. Outlier data instances are few and different
from the bulk of the dataset (Liu et al., 2012). They could represent noisy
data entries or rare events that can bias the training of an ML model,- One class SVM (OCS) with a radial basis function (RBF) kernel (OCSRBF)forest classifier after removing outliers using each of the four methods,
the LOF algorithm with 20 nearest neighbors and 1% outliers because of
2013). The next subsections describe the different types of models andanalysis. The table provides a brief description of how each algorithm
four broader categories based on their underlying theory of operation:
tree-based methods, statistical models, decision boundaries, and learned
reference. G´eron (2017) discusses both the theory and practical implegradient descent (SGD), and artificial neural network methods (G´eron,R. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126maximize the model generalization on the entire dataset while reducing any tendency towards overfitting or underfitting . Models that have regu
tradeoff between bias and variance, which improves generalization onamong classes in the target attribute. An AUC score of 0. indicates that
whereas a value approaching 1. indicates that the model offers a large
increase in TP rate for a small price of slightly increasing the FP rate.
cation accuracy (CA), precision (Pc), recall (Rc), and F1 scores. Table 12
fiers. However, a high CA score can be misleading if the dataset has high
class imbalanced. For example, a no-skill algorithm applied to a dataset
with only 5% of the instances from one class and the rest from the other
class will appear to have a 95 % accuracy if it picks the dominant class
for every prediction. Stratified sampling of both the training and testingclasses. This section compares five methods that rank features based on
the strength of their association with the classes in the target attribute.Ada Boost (AB) of estimators ( N ), learning rate ( R ), boosting algorithm, andcategorical attributes. D: Tends to overfit, resulting in low predictiveA: Offers the simplicity and intuition of decision trees but with lessA: Method simplicity. D: Sensitive to a skewed class distribution. Theestimators (N), learning rate ( R ), maximum tree depth ( S ), lossApplies Bayes theorem to determine the class probability, given A: Fast and simple method. D: Poor performance when attributes areA: Inherits many of the advantages of linear regression; precisions are
incorrectly classified instances. Model fitting may fail to converge ifR. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126predictions that were imbalance where a nocorrect. skill classifier cancorrelation among rankings indicates that the top-ranking attributes doof feature space, in the order of the data variance (Jolliffe and Cadima,
numerical features in the dataset. Intuitively, the first two principleinstances, as measured by the Euclidean distance. Data clusters tend to
structure in the data. The terminology used in the literature is that each
PC “explains” some proportion of the total variance (information) in the
dataset. Therefore, features that are weak components of most PCs tend
to be associated with noise in the data. Analyst also use PCA to transformrithm, sorted by the AUC metric. The null model is a no-skill model that
predicts the dominant class each time. It provided a baseline to compare
the performance score of skilled classifiers. As expected, the CA score for
ever, the AUC performance of the null classifier was lowest as expected.
the learning rate (L), loss function (LF), regularization (R) parameters,R. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126AUC score for a range of hyperparameter N associated with RF, kNN, and
trees of a RF, the minimum number of samples to retain in the leaves of atheir strength of association with the target class. The rank by each of therelation coefficients listed in Table 16. The correlation ranges from 84.certainty based on the amount of overlap in their class distributions. For example, the class probability was higher for derailment type accidents on class 0, 1, 2, 7, 8, and 9 tracks (Fig. 5a). The distinction is significant
(Fig. 5b). Similarly, the class probability was higher for derailment type
Similarly, the class probability was higher for derailment type accidents
in non-signalized territories (Fig. 5d). The probability difference wasstudent’s t -test shows that the p-value was near zero, which indicated
that the mean difference of 10 mph (16 kph) was statistically significant.viation, respectively. The lighter solid vertical lines indicate the medianaddition PC in their ranked order. This analysis indicated that the first
six PCs explained just over half of the variance in the dataset. Each of the
remaining 45 of 51 total PCs incrementally explain less than 4% of the
variance each, but together account for the remaining half of the varithe top ranking attributes of track class (Fig. 8a), movement authority
(Fig. 8b), and track type (Fig. 8c). Fig. 8d shows the distribution of the
target class in the same PC feature space, where the color shading inbility (Fig. 9a), hour (Fig. 9b), and weather (Fig. 9c). Fig. 9d shows the
distribution of the target class across each cluster. The clusters of the
higher-ranking attributes (Fig. 8) are less distinct than those of the lower
most effective in filling missing values for track density, but that attri
bute ranked low in importance for classification. Although effective, one
those of spatial neighbors rather than guessing values based on the mean,
most frequent, or nearest neighbors in feature space. The geospatial join
method provided the next best alternative to repair erroneous or lowresolution geospatial data. The distinctive southeast skew pattern
theories of decision trees. Using the traditional academic grading system
of nearly 89 % for XGB was associated with a classification accuracy and
excess, and signalized territory (SIG) as the most important features in
ML classifier performance. The interpretation of an attribute rank is itsclass. That is, an exceptionally high overlap of the two class distributions performance. It is rare that any one attribute can completely distinguishcation. Rather, a combination of attributes contributes their ability to
help determine the probability of class membership. Poor classificationwhich accounted for 88 % of the PCs, to explain the remaining half of the
variance in the data set. This outcome indicates that the first six PCs
represented the bulk of the information in the dataset. By extension, the
accumulation of the variance they explained. This result suggests that
just under half of the variance in the dataset lack structure and, therefrom PC1 and PC4 for the top-ranking features of track class, movement authority, and track type. One can visualize the amount of noise by theters. Even though the target class was spread across all clusters (Fig. 8d)
clusters on the left. The bias corresponds to clusters of class 1 tracks
(Fig. 9d) agreed with their low importance ranking. Interestingly, thebutes. The contamination noise in the center column of the cluster grid
(Fig. 9a) suggest similarities in the visibility at dawn and dusk, as ex
pected. Those similarities also corresponded to the separation of “Hour
row of clusters of the cluster grid (Fig. 9c) suggest similarities in weather
conditions like snow, sleet, rain, and fog. Hence, the clustering results
mance more had the situation occurred for the clusters of the highestranking features.structure in the dataset. Hence, the randomized tree-based methods such
noisy neighborhoods in the dataset. On the other hand, kNN seeks localmovement authorizations with restricted limits. Derailments also tended
kph) below the limit. Those findings correspond with the intuition thatated with higher safety risks, which the ML confirmed. Similarly, there is
less guidance for movements in territories without signalization, so the
equipment, signal systems, and infrastructure structures. Losses do not
include costs associated with cleanup, lost freight, societal damages,
fatalities, injuries, and line closures. Nevertheless, financial loss was notR. Bridgelall and D.D. Tolliver Accident Analysis and Prevention 156 (2021) 106126a pre-incident explanatory variable, but any future analysis that uses itmore than a century. Unfortunately, accidents continue to plague their
nated other accident types and resulted in the greatest financial loss.
Therefore, gaining insights into factors that are more strongly associated
with derailments than other accident types can inform more costeffective and impactful risk management strategies.rule-based and statistical methods. However, there are many types of ML
techniques, and no single method works best for all types of datasets.
Therefore, this work applied 11 different types of ML models to a largetrack class, the type of movement authority, the excess speed, and the
presence of signalization in the territory. The feature distribution for
track classes, non-signalized territories, and movement authorizations
with restricted limits. Derailments also tended to occur at 10 mph (16
imputation techniques presented were effective in filling missing values.