
def timify(data):
    from datetime import date
    if str(data)!= '' and len(str(data)) == 10:
        time = date(int(str(data).split('-')[0]),int(str(data).split('-')[1]),int(str(data).split('-')[2]))
        return time
    else:
        return date(2025,1,1)
    
def if_null(data):
    if str(data)!='':
        return data

def save_to_db(source):
    from .models import Client, Application, Credit
    from users.models import User, Filial
    from django.core.exceptions import ObjectDoesNotExist

    data = source
    print(data)
    user = User.objects.get(id=data['user'])

    filial = Filial.objects.get(id=user.filial.id)

    credit, created_credit = Credit.objects.update_or_create(
        id = data['credit_id'],
        defaults = {
            "user" : user,
            "contract_id" : f"F13-{data['credit_id']}",
            "amount" : float(data['amount']),
            "start_date" : timify(data['start_date']),
            "end_date" : timify(data['end_date']),
            "pay_day" : if_null(data['pay_day']),
            "status" : 'Pending',
            "filial" : filial   
        }
    )

    client, created_client = Client.objects.update_or_create(
        passport_pinfl = data['passport_pinfl'],
        defaults={
            # Client's data
            "first_name" : data['first_name'],
            "last_name" : data['last_name'],
            "middle_name" : data['middle_name'],
            "gender" : data['gender'],
            "education" : data['education'],
            "birth_date" : timify(data['birth_date']),
            "client_country" : data['client_country'],
            "client_region" : data['client_region'],
            
            # Passport data
            "passport_type" : 'id',
            "passport_serial_letter" : data['passport_serial_letter'],
            "passport_serial_number" : data['passport_serial_letter'],
            "passport_pinfl" : data['passport_pinfl'],
            "passport_got_date" : timify(data['passport_got_date']),
            "passport_expiry_date" : timify(data['passport_expiry_date']),
            "passport_got_region" : data['passport_got_region'],
            "passport_country" : data['passport_country'],

            # Address data from goverment database
            "base_country" : data['base_country'],
            "base_region" : data['base_region'],
            "base_city" : data['base_city'],
            "base_address" : data['base_address'],

            # Current address data
            "current_country" : data['base_country'],
            "current_region" : data['base_region'],
            "current_city" : data['base_city'],
            "current_address" : data['base_address'],

            # Other data
            "description" : "",
            "filial" : filial,
            }
        )
    new_credit = Credit.objects.get(id=data['credit_id'])
    if new_credit.client is not None:
        new_client = Client.objects.get(passport_pinfl=data['passport_pinfl'])

        return {
            "backend-data-response":{
                    "credit":{
                        "contract_id":new_credit.contract_id,
                        "amount":float(new_credit.amount),
                        "start_date":str(new_credit.start_date),
                        "end_date":str(new_credit.end_date),
                        "pay_day":new_credit.pay_day,
                        "status":new_credit.status,
                        "filial":new_credit.filial.name
                    },
                    "client":{
                        "first_name" : new_client.first_name,
                        "last_name" : new_client.last_name,
                        "middle_name" : new_client.middle_name,
                        "gender" : new_client.gender,
                        "education" : new_client.education,
                        "birth_date" : str(new_client.birth_date),
                        "client_country" : new_client.client_country,
                        "client_region" : new_client.client_region,
                        
                        # Passport data
                        "passport_type" : 'id',
                        "passport_serial_letter" : new_client.passport_serial_letter,
                        "passport_serial_number" : new_client.passport_serial_number,
                        "passport_pinfl" : new_client.passport_pinfl,
                        "passport_got_date" : str(new_client.passport_expiry_date),
                        "passport_expiry_date" : str(new_client.passport_expiry_date),
                        "passport_got_region" : new_client.passport_got_region,
                        "passport_country" : new_client.passport_country,

                        # Address data from goverment database
                        "base_country" : new_client.base_country,
                        "base_region" : new_client.base_region,
                        "base_city" : new_client.base_city,
                        "base_address" : new_client.base_address,

                        # Current address data
                        "current_country" : new_client.base_country,
                        "current_region" : new_client.base_region,
                        "current_city" : new_client.base_city,
                        "current_address" : new_client.base_address,

                        # Other data
                        "description" : "",
                        "filial" : new_client.filial.name,

                    }
                }
            }
    else:
        return {
            "backend-data-response":{
                    "credit":{
                        "contract_id":new_credit.contract_id,
                        "amount":float(new_credit.amount),
                        "start_date":str(new_credit.start_date),
                        "end_date":str(new_credit.end_date),
                        "pay_day":new_credit.pay_day,
                        "status":new_credit.status,
                        "filial":new_credit.filial.name
                    }
            }
        }


        
