from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TelField,FileField , RadioField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email ,URL

class CompanyAccount(FlaskForm):
    photo = FileField("Upload Logo", validators=[DataRequired()])
    website_link = StringField(" Your Website Link", validators=[DataRequired(),URL()])
    
    company_name = SelectField(
        "Company Name", 
        choices=[("company1", "Company 1"), ("company2", "Company 2")], 
        validators=[DataRequired()]
    )
    
    sector_name = SelectField(
        "Sector", 
        choices=[("tech", "Technology"), ("finance", "Finance"), ("health", "Healthcare")], 
        validators=[DataRequired()]
    )
    
    country_name = SelectField(
        "Country", 
        choices=[("us", "United States"), ("in", "India"), ("uk", "United Kingdom")], 
        validators=[DataRequired()]
    )
    
    city_name = SelectField(
        "City", 
        choices=[("ny", "New York"), ("la", "Los Angeles"), ("ldn", "London")], 
        validators=[DataRequired()]
    )
    
    address = StringField("Address", validators=[DataRequired()])
    
    telephone = SelectField(
        "Telephone Code", 
        choices=[("+1", "+1 USA"), ("+91", "+91 India"), ("+44", "+44 UK")], 
        validators=[DataRequired()]
    )
    
    number = TelField("Phone Number", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    contact = SelectField(
        "Contact Type", 
        choices=[("mr", "MR"), ("MRS", "mrs"), ("MISS", "miss")], 
        validators=[DataRequired()]
    )
    
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    
    company_presentation = StringField("Company's Presentation", validators=[DataRequired()])

class CompanyAccount2(FlaskForm):
    
    position_name = SelectField(
        "Position Name", 
        choices=[("developer", "Developer"), ("designer", "Designer"), ("manager", "Manager")],
        validators=[DataRequired()]
    )
    
    job_offer = StringField("Job Offer", validators=[DataRequired()])
    
    contract_type = SelectField(
        "Contract Type", 
        choices=[("full_time", "Full-Time"), ("part_time", "Part-Time"), ("contract", "Contract")],
        validators=[DataRequired()]
    )
    
    gender_preference = SelectField(
        "Gender Preference", 
        choices=[("male", "Male"), ("female", "Female"), ("any", "Any")],
        validators=[DataRequired()]
    )
    
    age_group = RadioField(
        "Age Group", 
        choices=[("18-25", "18-25"), ("26-35", "26-35"), ("36-45", "36-45"), ("46+", "46 and above")],
        validators=[DataRequired()]
    )
    
    search_contract_type = SelectField(
        "Search Contract Type", 
        choices=[("full_time", "Full-Time"), ("part_time", "Part-Time"), ("contract", "Contract")],
        validators=[DataRequired()]
    )
    
    annual_salary_offered = SelectField(
        "Annual Salary Offered", 
        choices=[("30k", "30k"), ("50k", "50k"), ("70k", "70k"), ("100k", "100k")],
        validators=[DataRequired()]
    )
    
    monthly_salary_offered = SelectField(
        "Monthly Salary Offered", 
        choices=[("2k", "2k"), ("5k", "5k"), ("8k", "8k"), ("10k", "10k")],
        validators=[DataRequired()]
    )
    
    hard_skills = SelectField(
        "Hard Skills", 
        choices=[("python", "Python"), ("java", "Java"), ("javascript", "JavaScript"), ("sql", "SQL")],
        validators=[DataRequired()]
    )
    
    soft_skills = SelectField(
        "Soft Skills", 
        choices=[("communication", "Communication"), ("teamwork", "Teamwork"), ("leadership", "Leadership"), ("problem_solving", "Problem Solving")],
        validators=[DataRequired()]
    )
class CandidateAccount(FlaskForm):
            photo = FileField("Upload Logo", validators=[DataRequired()])
            linkedIn_link = StringField(" Your LinkedIn Link", validators=[DataRequired(),URL()])


            country_name = SelectField(
             "Country", 
            choices=[("select", "Select"),("us", "United States"), ("in", "India"), ("uk", "United Kingdom")], 
            validators=[DataRequired()]
            )  

            city_name = SelectField(
            "City", 
            choices=[("select", "Select"),("ny", "New York"), ("la", "Los Angeles"), ("ldn", "London")], 
            validators=[DataRequired()]
            ) 

            address = StringField("Address", validators=[DataRequired()])

            country_code = SelectField(
            "Country Code", 
            choices=[("select", "Select"),("+1", "+1 USA"), ("+91", "+91 India"), ("+44", "+44 UK")], 
            validators=[DataRequired()]
            )
            number = TelField("Phone Number", validators=[DataRequired()])
            email = StringField("Email", validators=[DataRequired(), Email()])

            first_name = StringField("First Name", validators=[DataRequired()])
            last_name = StringField("Last Name", validators=[DataRequired()])

            candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])

            contract = SelectField(
            "Contract Type", 
            choices=[("select", "Select"),("ft", "Fulltime"), ("pt", "Parttime")], 
            validators=[DataRequired()]
            )

            sector_name = SelectField(
            "Sector", 
            choices=[("select", "Select"),("tech", "Technology"), ("finance", "Finance"), ("health", "Healthcare")], 
            validators=[DataRequired()]
            ) 

            position_name = SelectField(
            "Name Position", 
            choices=[("select", "Select"),("Manager", "Manager"), ("finance", "Financer"), ("developer", "Developer")], 
            validators=[DataRequired()]
            )   

            
            disability = RadioField(
                 "Profile with Disability?", 
                 choices=[("yes", "Yes"), ("no", "No")],validators=[DataRequired()]
            )

            age = StringField("Age",validators=[DataRequired()])

            experience = SelectField(
            "Experience", 
            choices=[("select", "Select"),("0-2", "0-2 years"), ("3+", "3 + years"),], 
            validators=[DataRequired()]
            ) 

            salary = SelectField(
            "Salary Expectation", 
            choices=[("select", "Select"),("$30000-$50000", "$30000-$50000"), ("$70000-$90000", "$70000-$90000"),], 
            validators=[DataRequired()]
            )      

class CandidateAccount2(FlaskForm):
        first_name = StringField("First Name", validators=[DataRequired()])
        last_name = StringField("Last Name", validators=[DataRequired()])
        experience = SelectField(
            "Experience", 
            choices=[("select", "Select"),("0-2", "0-2 years"), ("3+", "3 + years"),], 
            validators=[DataRequired()]
            ) 

            
        salary = SelectField(
        "Salary Expectation", 
        choices=[("select", "Select"),("$30000-$50000", "$30000-$50000"), ("$70000-$90000", "$70000-$90000"),], 
        validators=[DataRequired()]
        )
        first_name = StringField("First Name", validators=[DataRequired()])
        number = TelField("Phone Number", validators=[DataRequired()])
        email = StringField("Email", validators=[DataRequired(), Email()])
        age = StringField("Age",validators=[DataRequired()])
        gender_preference = SelectField(
        "Select Gender", 
        choices=[("select", "Select"),("male", "Male"), ("female", "Female"), ("any", "Any")],
        validators=[DataRequired()]
         )
        salary = SelectField(
        "Salary Expectation", 
        choices=[("select", "Select"),("$30000-$50000", "$30000-$50000"), ("$70000-$90000", "$70000-$90000"),], 
        validators=[DataRequired()]
        )
        #  next section
        disability = RadioField(
        "Profile with Disability?", 
        choices=[("yes", "Yes"), ("no", "No")],validators=[DataRequired()]
        )
        first_name = StringField("First Name", validators=[DataRequired()])
        experience = SelectField(
            "Experience", 
            choices=[("select", "Select"),("0-2", "0-2 years"), ("3+", "3 + years"),], 
            validators=[DataRequired()]
        )

        salary = SelectField(
        "Salary Expectation", 
        choices=[("select", "Select"),("$30000-$50000", "$30000-$50000"), ("$70000-$90000", "$70000-$90000"),], 
        validators=[DataRequired()]
        )

        salary = SelectField(
        "Salary Expectation", 
        choices=[("select", "Select"),("$30000-$50000", "$30000-$50000"), ("$70000-$90000", "$70000-$90000"),], 
        validators=[DataRequired()]
        ) 
        candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])
        candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])
        candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])
       
        # next section


        first_name = StringField("First Name", validators=[DataRequired()])
        first_name = StringField("First Name", validators=[DataRequired()])
        date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
        candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])

         # next section
        first_name = StringField("First Name", validators=[DataRequired()])
        first_name = StringField("First Name", validators=[DataRequired()])
        date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
        
        # next section

        candidate_presentation = TextAreaField("Candidate Presentation", validators=[DataRequired()])




        
                  
