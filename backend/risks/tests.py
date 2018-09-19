from django.test import TestCase
from risks.models import Insurer, InsuranceField, InsuranceSchema, InsuranceRecord


class RiskoModelsTestCase(TestCase):
    """
    Come up with a solution that allows insurers to define their own custom data
    model for their risks
    """
    def test_insurance_schema(self):
        """
        Insurers should be able to create their own Insurance/risk types and attach as
        many different fields as they would like.
        """
        jorn_inc = Insurer(name="Jorn Lande Inc.")
        jorn_inc.save()

        # Let's create insurance for a car
        car_schema = InsuranceSchema.objects.create(
            title='Car Insurance',
            description='This is an insurance schema for an automobile',
            insurer=jorn_inc,
        )

        InsuranceField.objects.create(
            title='Premium',
            description='The amount of money charged',
            data_type=InsuranceField.NUMBER,
            schema=car_schema
        )
        InsuranceField.objects.create(
            title='Make',
            description='This is the car make',
            data_type=InsuranceField.ENUM,
            choices=['Ford', 'Honda', 'VW'],
            schema=car_schema
        )
        InsuranceField.objects.create(
            title='Model',
            description='The year of the car',
            data_type=InsuranceField.NUMBER,
            schema=car_schema
        )


        joes_insurance = InsuranceRecord.objects.create(
            schema=car_schema,
            insurer=jorn_inc,
            data={
                'Premium': 123456,
                'Make': 'Ford',
                'Model': 'Focus',
            }
        )

        # check the data was saved.
        self.assertTrue(
            joes_insurance.schema.fields.count(),
            3
        )
        # Just a query test
        q = InsuranceRecord.objects.filter(data__Make='Ford')
        self.assertEqual(len(q), 1)
