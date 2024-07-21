from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(Form):
    email = StringField(
        'Email Address',
        validators = [
            Email(),
            DataRequired(),
            Length(min=6)
        ]
        )
    submit = SubmitField('Register')
