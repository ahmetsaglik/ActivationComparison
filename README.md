# ActivationComparison
Activation comparison using Python and LSTM

The purpose of this code is to make a comparison between activation functions. For this reason, a simple data set has been prepared. <br>
<br>
Dataset = [10,20,30,40,50,60,70,80,90,100]
<br>

Using this dataset, an LSTM model has been trained and it is aimed to determine the relationships between functions and layer numbers. The functions used are "relu", "sigmoid", "softmax" and "tanh" functions. Trained models were asked to make estimates by giving numbers [110,120,130,140] and the results of the estimates were recorded. Later, these results were transformed into a dataframe and wanted to be analyzed. As a result of the analysis, it was determined that the most suitable function for the sample is the 150-layer "relu" function. It has been found that functions with other irrelevant results are not suitable for this problem. For this reason, it is recommended to check more than one situation for a problem and to choose the most suitable one. Many different factors such as functions, data and established algorithms can produce different results for each problem. The important thing is to understand the problem and to determine the appropriate methods.
<br><br>
## Results <br>
![image](https://user-images.githubusercontent.com/45441084/119277552-16f88980-bc29-11eb-8f34-b5968b5ce0c2.png)
