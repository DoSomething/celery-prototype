class MdataMessage():
    """docstring for MdataMessage"""
    def __init__(self,
                 phone,
                 carrier,
                 profile_id,
                 profile_first_name,
                 profile_last_name,
                 profile_email,
                 profile_street1,
                 profile_street2,
                 profile_city,
                 profile_state,
                 profile_postal_code,
                 profile_age,
                 profile_birthdate,
                 profile_birthyear,
                 profile_cause,
                 profile_college_gradyear,
                 profile_ctd_completed,
                 profile_ctd_day1,
                 profile_ctd_day2,
                 profile_ctd_day3,
                 profile_ctd_start,
                 profile_date_of_birth,
                 profile_edutype,
                 profile_gambit_chatbot_response,
                 profile_sfw_day3,
                 profile_source,
                 profile_texting_frequency,
                 args,
                 keyword,
                 timestamp,
                 message_id,
                 mdata_id,
                 mms_image_url,
                 phone_number_without_country_code
        ):
        self.phone = phone
        self.carrier = carrier
        self.profile_id = profile_id
        self.profile_first_name = profile_first_name
        self.profile_last_name = profile_last_name
        self.profile_email = profile_email
        self.profile_street1 = profile_street1
        self.profile_street2 = profile_street2
        self.profile_city = profile_city
        self.profile_state = profile_state
        self.profile_postal_code = profile_postal_code
        self.profile_age = profile_age
        self.profile_birthdate = profile_birthdate
        self.profile_birthyear = profile_birthyear
        self.profile_cause = profile_cause
        self.profile_college_gradyear = profile_college_gradyear
        self.profile_ctd_completed = profile_ctd_completed
        self.profile_ctd_day1 = profile_ctd_day1
        self.profile_ctd_day2 = profile_ctd_day2
        self.profile_ctd_day3 = profile_ctd_day3
        self.profile_ctd_start = profile_ctd_start
        self.profile_date_of_birth = profile_date_of_birth
        self.profile_edutype = profile_edutype
        self.profile_gambit_chatbot_response = profile_gambit_chatbot_response
        self.profile_sfw_day3 = profile_sfw_day3
        self.profile_source = profile_source
        self.profile_texting_frequency = profile_texting_frequency
        self.args = args
        self.keyword = keyword
        self.timestamp = timestamp
        self.message_id = message_id
        self.mdata_id = mdata_id
        self.mms_image_url = mms_image_url
        self.phone_number_without_country_code = phone_number_without_country_code
