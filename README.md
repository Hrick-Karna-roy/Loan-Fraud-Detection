# Loan-Fraud-Detection
## The project is of a predictive analysis of Dataset which contains some catagorical and some numerical features of possesion details and personal behaviour of people all over the country and predicting their loan, wether they can be fraud or genuine. ##

                                                              ## PART 1
### 1>.  try out incrementally more complex models which satisfies real world costraint and requirements...


the Dataset contains features like city and state both...
 
 there are total 300 + cities now feature encoding these by one hot encoding is quite useless and doesnot holds much information... and also quite impractical... so on the first step i would like to drop the citi feature and make a model with states as there are only 29 states...
 
 now one hot encodding makes sence with the state but not up to the mark, I can think of a solution for that....
    
    we will think of a new approach...
    
    we will count the frequencies of each state in the dataset and rank them from most to least, and instead of one-hot we will replace the state names with their frequencies in the dataset, that will change it from catagorical to numarical and make our work easy...
    
    ex  suppose west bengal occours 39 times in the whole dataset 
                and Delhi occours 87 times in the dataset
                
                so wherever we find WB we replace by 39 and Delhi by 87
                
    after following this approach we can try to upgrade one more step by making a discission tree with state city and their calss leble and replace all three by  a new numrerical class variable...
    

2>. After doing proper EXPLORATORY DATA ANALYSIS  we came to a conclution that the numerical features on the dataset are not having any proper distribution but they are also not having any outliners in them,but from the coorelation matrix we can find that some features are inter dependent on each other, not very much but to some extent, so if needed we can sometime play with those features... if we need...
   
3>. the model will come under a logestic regression problem... and i think log loss function is quite ok for now... if any change needed we can think into it later...

4>.  after following this approach we can try to upgrade one more step by making a discission tree with      state city and their calss leble and replace all three by  a new numrerical class variable...
      
     there can be some regional clustering to make it more real, suppose if we also do dicession tree then from westbengal Jamtara and Kolkata will come from a same tree node, but these two regions differ a lot on the  basis of their financial reputation and froud cases... so it will make more sence if we can make a proper catgorical selection including a new feature with the region...

    this approach is quite robust in the sence that the datset will hold its information now
    
5>. conclution till now - when there is a lot of unique catagorical  variable encoding in the dataset then most of the time it doesnt make any sence with the real world data, so the model which i stated it will work good for now but we cant say anything until we go through code implementation...

                                                             ## PART 2


The part 1 text contains the EDA done initially before choosing any model and after that, choosing 2 models which seems suitable along with the dataset, I have added a fet new approach in the end, while i was choosing the second model to be Random forest, with 89% score.



Some of them are 1> finding the entropy or the variance of the class lable
                                  which will help me to know how predictive the
                                   model can, because more the entropy less the 
                                   accuracy would be...



                              2> from the corelation matrix it seems like 2 features 
                                   much coreleted with the label, the most corelated is
                                   the experiance
                                ____

conclution – of doc 2

both logestic regression and random forest are giving quite fruteful scores, though random forest is 2% more scorring than logestic model, i may have tried to use other models but it seemed best for me for now,....


in future this type of datasetys can be properly handelled with the process which i have followed, the main part is of data analysis and feature engineering, if one deals properly with it, then the whole pipeline will dafinately give a fruitful reasult, this is the end of second phase for now, it any change is required i will do in future and add something more as required, my next phase will be of deployment, i am thinking of stremlit..

thank you








