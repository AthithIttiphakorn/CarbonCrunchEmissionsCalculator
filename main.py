from flask import Flask, render_template, request
from dotenv import load_dotenv #env for env file
#from city import call_city_aqi


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

v_typedict = {
    "car": 0.170,        
    "diesel": 0.173,
    "electric": 0.079,
    "bus": 0.105,
    "trainsel": 0.130,
    "trainelec": 0.045,
    "subway": 0.040,
    "bike": 0.015,
    "walk": 0.008
}

dietdict = {
    "high_meat": 3.3,    
    "medium_meat": 2.5,
    "vegetarian": 1.7,
    "vegan": 1.4
}

        
lifestyledict = {
    "light": 0.4,  
    "average": 1.1,
    "heavy": 1.8
}



@app.route('/display', methods=["GET", "POST"])
def display_footprint():
    recommend = [{"name":"Solar Panels", "image":"https://warmserve-services.co.uk/wp-content/uploads/2024/10/AdobeStock_82260045-1.jpg", "description":"Save on Electricity Bills and guarentee clean energy."}]

    if request.method == "POST":



        city = request.form["city"]
        print(city)
      #  gifty = call_city_aqi(city)
        v_type = request.form["vehicle_type"]
        km_day = int(request.form["km_per_day"])
        flight_km = int(request.form["flights_km"])
        electricity = int(request.form["electricity_kwh"])
        gas = int(request.form["gas_m3"])
        diet = request.form["diet_type"]
        lifestyle = request.form["lifestyle_level"]
 
 
        co2 = (km_day * v_typedict[v_type]  * 365) + lifestyledict[lifestyle] * 365 + dietdict[diet] * 365 + ( 2.015 * gas ) * 12 + 0.16*flight_km + electricity * 12 * 0.233
        print((km_day * v_typedict[v_type]  * 365), lifestyledict[lifestyle] * 365, dietdict[diet] * 365, ( 2.015 * gas ) * 12, 0.16*flight_km, electricity * 12 * 0.233)

        if co2 >= 5000:
            text_color = "red"
            display_solutions = True
        else:
            text_color = "green"

        if diet == "high_meat" or diet == "medium_meat":
           recommend.append( { "name": "Sustainable Meat from trusted sellers",
                              "image": "https://img.freepik.com/free-vector/cooking-ingredients-vector-set-illustration_53876-43781.jpg",
                                "description": "Consider buying meat that has been sustainably farmed to reduce animal suffering, chemicals and greenhouse gas emissions"
                                })
           

        if km_day > 40:
           # print("recommend drive")
            recommend.append( { "name": "Electric Cars",
                               "image":"https://umd-today.transforms.svdcdn.com/production/hero/iStock-1363346936_1920x1080.jpg?w=1920&h=1080&auto=compress%2Cformat&fit=crop&dm=1698266267&s=36719c2651bcd1f031f97f478da4712e",
                               "description":"less co2 from burning"
                               
                               } )

        if electricity > 900 and v_type != "electric":
            #print("recommend electricity")
            recommend.append( { "name": "Save Energy",
                               "image":"https://img.freepik.com/premium-vector/turning-off-switch-energy-saving-save-energy-concept-press-electric-button-vectorxd_506530-4321.jpg",
                               "description":"less co2 from burning"

                                })
        if lifestyle == "heavy":
                #print("recommend shop")
                recommend.append( { "name": "Spend Less, Save more",
                               "image":"https://npr.brightspotcdn.com/dims3/default/strip/false/crop/6000x4000+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F3b%2Fa1%2F72c54a4f46209e83ee4f6eb7b871%2Fnpr-shopping-final.jpg",
                               "description":"Or at least use a reusable bag to reduce plastic waste"

                                })
        if gas > 39 and v_type == "car" or v_type == "diesel":
            recommend.append( {"name":"Best driving practices",
                               "image":"https://res.cloudinary.com/yourmechanic/image/upload/dpr_auto,f_auto,q_auto/v1/article_images/1_Eco_driving_indicator_light",
                               "description": "You can reduce your car gas usage by buying a fuel efficient car, reduce idling, use public transport or walk. Driving at around 80km/h is usually the best speed for fuel consumption. If you drive in a city a lot, consider getting a EV instead."
                               })

    return render_template(
        "display.html",
        emissions = co2,
        text_color = text_color,
        recommendation = recommend
    )


@app.route('/calculate', methods=["GET", "POST"])
def calculate():
    return render_template("calculate.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
