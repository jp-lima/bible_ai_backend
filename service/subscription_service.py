import mercadopago


sdk = mercadopago.SDK("TEST-3110162942135101-021512-ff7dd5ec81ed5f186bf38e3474ab1be2-1248202234")


def service_create_subscription():
    
    preference_data = {

            "items":[
                {
                    "items":"Alianças",
                    "quantity":1,
                    "unit_price": 0.01

                }
                ],
            "back_urls":{
                     "success": "https://seusite.com/sucesso",
            "failure": "https://seusite.com/erro",
            "pending": "https://seusite.com/pendente"
                    },
                "auto_return":"approved"

            }

    preference = sdk.preference().create(preference_data)

    return preference["response"]["init_point"]  






