REFERENCES

the measurements inherent to these defects. To evaluate our
methods we collect two data sets from different sources and
demonstrate improved performance for predicting flat spot,
shelling and non-roundness.
The methods that were developed for this work are currently being implemented as part of the SBB wayside train
monitoring system. To improve the quality of the training
and test data RFID tags will be deployed to enable perfect
association between defect labels and measurements. Further
future work consists of integrating external features into the
deep learning models, optimizing for precision and predicting
severity scores for the defects. For the prediction of severity
scores we obtained promising preliminary results on regressing
the flat spot length using support vector regression [36] and
the wavelet features.

REFERENCES

[1] R. Müller, D. Leibundgut, B. Stallaert, L. Pesqueux,
and E. A., “Validation of wheel maintenance measures
on the rolling stock for reduced excitation of ground
vibration”, SBB, D2S, Alstom, Trafikverket, Tech. Rep.,
2013.

[2] P. Huber, B. Nélain, and R. Müller, “Rivas–mitigation
measures on vehicles (wp5); experimental analysis of
sbb ground vibration measurements and vehicle data”,
in Noise and vibration mitigation for rail transportation
systems, Springer, 2015, pp. 531–538.

[3] E. Verheijen and F. Elbers, “Future european noise
emission ceilings: Threat or solution? a review based
on swiss and dutch ceilings”, in Noise and Vibration
Mitigation for Rail Transportation Systems, Springer,
2015, pp. 71–78.

[4] Y. Li and S. Pankanti, “Anomalous tie plate detection
for railroad inspection”, in Pattern Recognition (ICPR),
2012 21st International Conference on, IEEE, 2012,
pp. 3017–3020.

[5] Y. Li, H. Trinh, N. Haas, C. Otto, and S. Pankanti, “Rail
component detection, optimization, and assessment for
automatic rail track inspection”, IEEE Transactions
on Intelligent Transportation Systems, vol. 15, no. 2,
pp. 760–770, 2014.

[6] X. Gibert, V. M. Patel, and R. Chellappa, “Deep
multi-task learning for railway track inspection”, ArXiv
preprint arXiv:1509.05267, 2015.

[7] T. Idé, “Formalizing expert knowledge through machine
learning”, in Global Perspectives on Service Science:
Japan, Springer, 2016, pp. 157–175.

[8] N. Nenov, E. Dimitrov, V. Vasilev, and P. Piskulev,
“Sensor system of detecting defects in wheels of railway
vehicles running at operational speed”, in Electronics
Technology (ISSE), 2011 34th International Spring Sem-
inar on, IEEE, 2011, pp. 577–582.

[9] T. K. Ho, S. Liu, Y. Ho, K. Ho, K. Wong, K. Y. Lee,
H. Tarn, and S. Ho, “Signature analysis on wheel-rail
interaction for rail defect detection”, pp. 1–6, 2008.

[10] Y. Jianhai, Q. Zhengding, and C. Boshi, “Application
of wavelet transform to defect detection of wheelflats of
railway wheels”, in Signal Processing, 2002 6th Inter-
national Conference on, IEEE, vol. 1, 2002, pp. 29–32.

[11] W. Badran and U. Nietlispach, “Wayside train monitoring systems: Networking for greater safety”, European
Railway Review, vol. 17, no. 4, pp. 14–21, 2011.

[12] J. C. Nielsen and A. Johansson, “Out-of-round railway
wheels-a literature survey”, Proceedings of the Institu-
tion of Mechanical Engineers, Part F: Journal of Rail
and Rapid Transit, vol. 214, no. 2, pp. 79–91, 2000.

[13] J. Nielsen, “Out-of-round railway wheels”, in
Wheel–Rail Interface Handbook, R. Lewis and
U. Olofsson, Eds., Woodhead Publishing, 2009,
pp. 245–279.

[14] S. Mallat, A wavelet tour of signal processing . Academic press, 1999.

[15] M. Unser and A. Aldroubi, “A review of wavelets in
biomedical applications”, Proceedings of the IEEE, vol.
84, no. 4, pp. 626–638, 1996.

[16] P. Kumar and E. Foufoula-Georgiou, “Wavelet analysis
for geophysical applications”, Reviews of geophysics,
vol. 35, no. 4, pp. 385–412, 1997.

[17] A. Skodras, C. Christopoulos, and T. Ebrahimi, “The
jpeg 2000 still image compression standard”, Signal
Processing Magazine, IEEE, vol. 18, no. 5, pp. 36–58,
2001.

[18] I. Daubechies et al., Ten lectures on wavelets . SIAM,
1992, vol. 61.

[19] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D.
Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich,
“Going deeper with convolutions”, in Computer Vision
and Pattern Recognition (CVPR), 2015.

[20] L. Deng and D. Yu, “Deep learning: Methods and applications”, Foundations and Trends in Signal Processing,
vol. 7, no. 3–4, pp. 197–387, 2014.

[21] A.-r. Mohamed, G. E. Dahl, and G. Hinton, “Acoustic
modeling using deep belief networks”, Audio, Speech,
and Language Processing, IEEE Transactions on, vol.
20, no. 1, pp. 14–22, 2012.

[22] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre,
G. Van Den Driessche, J. Schrittwieser, I. Antonoglou,
V. Panneershelvam, M. Lanctot, et al., “Mastering the
game of go with deep neural networks and tree search”,
Nature, vol. 529, no. 7587, pp. 484–489, 2016.

[23] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with deep convolutional neural networks”, in Advances in neural information processing
systems, 2012, pp. 1097–1105.

[24] Z. Wang and T. Oates, “Encoding time series as images for visual inspection and classification using tiled
convolutional neural networks”, in Workshops at the
Twenty-Ninth AAAI Conference on Artificial Intelli-
gence, 2015.

[25] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep
into rectifiers: Surpassing human-level performance on
imagenet classification”, in Proceedings of the IEEE

International Conference on Computer Vision, 2015,
pp. 1026–1034.

[26] T. G. Dietterich, R. H. Lathrop, and T. Lozano-Pérez,
“Solving the multiple instance problem with axisparallel rectangles”, Artificial intelligence, vol. 89, no.
1, pp. 31–71, 1997.

[27] G. Krummenacher, C. S. Ong, and J. Buhmann, “Ellipsoidal multiple instance learning”, in Proceedings of
the 30th International Conference on Machine Learning
(ICML-13), 2013, pp. 73–81.

[28] C. Cortes and V. Vapnik, “Support-vector networks”,
Machine learning, vol. 20, no. 3, pp. 273–297, 1995.

[29] M. Imani and U. Braga-Neto, “Optimal gene regulatory network inference using the boolean kalman filter
and multiple model adaptive estimation”, in 2015 49th
Asilomar Conference on Signals, Systems and Comput-
ers, IEEE, 2015, pp. 423–427.

[30] P. S. Maybeck and P. D. Hanlon, “Performance enhancement of a multiple model adaptive estimator”, IEEE
Transactions on Aerospace and Electronic Systems, vol.
31, no. 4, pp. 1240–1254, 1995.

[31] C. J. V. Rijsbergen, Information Retrieval, 2nd. Newton,
MA, USA: Butterworth-Heinemann, 1979.

[32] M. Cuturi, “Fast global alignment kernels”, in ICML
2011, 2011.

[33] M. Cuturi, J.-P. Vert, O. Birkenes, and T. Matsui, “A
kernel for time series based on global alignments”, in
ICASSP, vol. 2, 2007.

[34] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever,
and R. Salakhutdinov, “Dropout: A simple way to
prevent neural networks from overfitting”, The Journal
of Machine Learning Research, vol. 15, no. 1, pp. 1929–
1958, 2014.

[35] I. Sutskever, J. Martens, G. Dahl, and G. Hinton,
“On the importance of initialization and momentum
in deep learning”, in Proceedings of the 30th inter-
national conference on machine learning (ICML-13),
2013, pp. 1139–1147.

[36] A. J. Smola and B. Schölkopf, “A tutorial on support
vector regression”, Statistics and computing, vol. 14,
no. 3, pp. 199–222, 2004.

**Gabriel Krummenacher** is a Ph.D. student at the
Institute for Machine Learning at the Department of
Computer Science of ETH Zurich. He is working on
scalable methods for large-scale and robust learning,
on wheel defect detection in a collaboration with
SBB and on sleep stage prediction with deep learning. He received a M.Sc. in computer science from
ETH Zurich in 2011. In February and March 2013
he was an academic guest at the NICTA Bioinformatics group in Melbourne. From September 2008
to February 2009 he did a software engineering
internship in the trading technology team of Axa Rosenberg in San Francisco.
He is interested in solving complex real world problems arising from industry
or the medical domain through machine learning.

12

**Cheng Soon Ong** is a principal researcher at the
Machine Learning Research Group, Data61, CSIRO.
He is also an adjunct associate professor at the
Australian National University, and an honourary
research fellow at the University of Melbourne. His
Ph.D. in Computer Science was completed at the
Australian National University in 2005. He was a
postdoc at the Max Planck Institute of Biological
Cybernetics and the Fredrich Miescher Laboratory
in Tübingen, Germany. From 2008 to 2011, he was
a lecturer in the Department of Computer Science
at ETH Zurich, and he has been with NICTA/Data61 since 2012. interested
in enabling scientific discovery by extending statistical machine learning
methods. In recent years, he has developed new optimization methods for
solving problems such as ranking, feature selection and experimental design,
with the aim of solving scientific questions in collaboration with experts in
other fields.

**Stefan Koller** is head of the Wayside Train Monitoring System department at Swiss Federal Railways
(SBB). He graduated from the Swiss Federal Institute of Technology Zurich (ETH) in Physics with a
Ph.D. He has been working a number of years as
senior scientist in mirco electro mechanical sensor
system (MEMS). After that he has been working a
couple of years as a senior consultant for software
testing. Stefan Koller has been with the Wayside
Train Monitoring Systems department of SBB AG
since 2008. As system engineer for Wayside Train
Monitoring Systems he was responsible for the development and rollout
of SBB’s unique fire and chemicals detection system and the wheel load
checkpoint system.

**Seijin Kobayashi** Seijin Kobayashi is a graduate
student from ETH Zurich and Ecole Polytechnique
in Paris. From September 2015 to March 2016
he worked on his Master Thesis at ETH Zurich
on defect wheel detection and sleep stage staging
using deep learning. He received a M.Sc. in computer science from ETH Zurich in 2016. He is
currently ongoing an internship at Google Zurich.
He is interested in applying deep learning for real
world problems as well as improving artificial neural
network architectures and learning algorithms.

**Joachim M. Buhmann** is professor for Information Science and Engineering at the Computer Science Department of the Swiss Federal Institute of
Technology Zurich (ETH). He received his Ph.D.
degree in theoretical physics from the Technical
University of Munich, Germany, in 1988. He has
held postdoctoral and research faculty positions at
the University of Southern California, Los Angeles,
and the Lawrence Livermore National Laboratory,
Livermore, CA between 1988 and 1992. Until October 2003, he headed the Research Group on Pattern
Recognition, Computer Vision and Bioinformatics in the Computer Science
Department, Rheinische Friedrich-Wilhelms Universität Bonn, Germany. In
October 2003 he joined ETH Zurich. His current research interests cover
machine learning, statistical learning theory and its relations to information
theory as well as applications of machine learning to challenging data analysis
questions. The machine learning applications range from image understanding
and medical image analysis, to signal processing, bioinformatics and computational biology. Special emphasis is devoted to model selection questions for
the analysis of large scale heterogeneous data sets. Dr. Buhmann has served
as an associate editor for IEEE-TNN, IEEETIP and IEEE-TPAMI.