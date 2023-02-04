import pandas as pd 
import numpy as np 
import pickle
import json

class LoanModel():
    def __init__(self,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
        revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid,purpose):
        
        self.int_rate=int_rate
        self.installment=installment
        self.log_annual_inc=log_annual_inc
        self.dti=dti
        self.fico=fico
        self.days_with_cr_line=days_with_cr_line
        self.revol_bal=revol_bal
        self.revol_util=revol_util
        self.inq_last_6mths=inq_last_6mths
        self.delinq_2yrs=delinq_2yrs
        self.pub_rec=pub_rec
        self.not_fully_paid=not_fully_paid
        self.purpose="purpose_"+ purpose
        
    def Load_model(self):


        with open("models/logistic_model1.pkl","rb") as f:
            self.logistic_model=pickle.load(f)


        with open("models/project_data.json","r") as f:
            self.project_data=json.load(f)
    
    def Loan_prediction(self):


        self.Load_model()
        index_value=self.project_data["columns"].index(self.purpose)

        array=np.zeros(len(self.project_data["columns"]))
        array[0]=self.int_rate
        array[1]=self.installment
        array[2]=self.log_annual_inc
        array[3]=self.dti
        array[4]=self.fico
        array[5]=self.days_with_cr_line
        array[6]=self.revol_bal
        array[7]=self.revol_util
        array[8]=self.inq_last_6mths
        array[9]=self.delinq_2yrs
        array[10]=self.pub_rec
        array[11]=self.not_fully_paid
        array[index_value]=1

        prediction=self.logistic_model.predict([array])[0]
        print(prediction)
        if prediction==1:
            return "customer eligible for Loan"
        else:
            return "customer is not eligible for Loan"  
             

if __name__ == "__main__":
    
    int_rate=0.118900
    installment=829.100000
    log_annual_inc=11.350407
    dti=19.480000
    fico=737.000000
    days_with_cr_line=5639.958333
    revol_bal=28854.000000
    revol_util=52.100000
    inq_last_6mths=0.000000
    delinq_2yrs=0.000000
    pub_rec=0.000
    not_fully_paid=0.000000
    purpose="credit_card"

    pred=LoanModel(int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
    revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid,purpose)

    credit_status=pred.Loan_prediction()
    print(credit_status)




       



