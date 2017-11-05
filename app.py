from flask import Flask,render_template,request
from datetime import time
from model import InputForm
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
app=Flask(__name__,template_folder=r'.\template')

def compute(c,btc_converter,btc,inr):
    if(btc==1):
        return (btc,c.convert_to_btc(1,"INR"))
    return (btc_converter.convert_to_btc(inr,"INR"),inr)

@app.route('/',methods=['POST','GET'])
def index():
    c=CurrencyRates()
    btc_converter = BtcConverter()
    price_json=c.get_rates('INR')
    form = InputForm(request.form)
    if(request.method == 'POST' and form.validate()):
        result = compute(c,btc_converter,form.btc.data, form.inr.data)
    else:
        result=None
    prices=[]
    for key,value in price_json.items():
        prices.append((key,value,btc_converter.get_latest_price(key)))
    print('No of Supported Currencies: ',len(price_json),'||||File Type: ',type(price_json))
    legend = 'Temperatures'
    links=['atif','faitma','jabin']
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                        61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                        70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
                 time(hour=11, minute=14, second=30),
                 time(hour=11, minute=14, second=45),
                 time(hour=11, minute=15, second=00),
                 time(hour=11, minute=15, second=15),
                 time(hour=11, minute=15, second=30),
                 time(hour=11, minute=15, second=45),
                 time(hour=11, minute=16, second=00),
                 time(hour=11, minute=16, second=15),
                 time(hour=11, minute=16, second=30),
                 time(hour=11, minute=16, second=45),
                 time(hour=11, minute=17, second=00),
                 time(hour=11, minute=17, second=15),
                 time(hour=11, minute=17, second=30),
                 time(hour=11, minute=17, second=45),
                 time(hour=11, minute=18, second=00),
                 time(hour=11, minute=18, second=15),
                 time(hour=11, minute=18, second=30)]
    return render_template('index.html', values=temperatures, labels=times, legend=legend, links=links, current_prices=prices, form=form, result=result)

@app.route('/about_us')
def about():
    return render_template('about_us.html')

if(__name__=="__main__"):
    app.run(debug=True)
