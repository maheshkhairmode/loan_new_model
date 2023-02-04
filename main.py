from distutils.command.config import config
from flask import Flask,render_template,request
from models.utils import LoanModel
import config

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/prediction_loan",methods=["POST","GET"])
def Loan_policy():

    if request.method=="POST":

        int_rate=float(request.form.get("int_rate"))
        installment=float(request.form.get("installment"))
        log_annual_inc=float(request.form.get("log_annual_inc"))
        dti=float(request.form.get("dti"))
        fico=float(request.form.get("fico"))
        days_with_cr_line=float(request.form.get("days_with_cr_line"))
        revol_bal=float(request.form.get("revol_bal"))
        revol_util=float(request.form.get("revol_util"))
        inq_last_6mths=float(request.form.get("inq_last_6mths"))
        delinq_2yrs=float(request.form.get("delinq_2yrs"))
        pub_rec=float(request.form.get("pub_rec"))
        not_fully_paid=float(request.form.get("not_fully_paid"))
        purpose=request.form.get("purpose")

        pred=LoanModel(int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
        revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid,purpose)

        credit_status=pred.Loan_prediction()
        print(credit_status)

        return render_template("index.html",prediction=credit_status)

if __name__ == "__main__":

    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)

