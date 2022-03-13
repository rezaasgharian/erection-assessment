from .models import Questionnaire
from rest_framework import serializers


class QuestionnaireSerializer(serializers.ModelSerializer):
    CONFIDENCE_CHOICES = (
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Moderate'),
        (4, 'High'),
        (5, 'Very high'),
    )
    PENETRATION_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    INTERCOURSE_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    COMPLETION_CHOICES = (
        (1, 'Extremely difficult'),
        (2, 'Very difficult'),
        (3, 'Difficult'),
        (4, 'Slightly difficult'),
        (5, 'Not difficult'),
    )
    SATISFACTION_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    confidence = serializers.ChoiceField(choices=CONFIDENCE_CHOICES, write_only=True)
    penetration = serializers.ChoiceField(choices=PENETRATION_CHOICES, write_only=True)
    intercourse = serializers.ChoiceField(choices=INTERCOURSE_CHOICES, write_only=True)
    completion = serializers.ChoiceField(choices=COMPLETION_CHOICES, write_only=True)
    satisfaction = serializers.ChoiceField(choices=SATISFACTION_CHOICES, write_only=True)

    class Meta:
        model = Questionnaire
        fields = (
            'confidence', 'penetration', 'intercourse', 'completion', 'satisfaction', 'score',
        )
        read_only_fields = (
            'created_at',
            'average',
            'score',
        )

    def create(self, validated_data):
        request = self.context['request']
        confidence = int(request.data['confidence'])
        penetration = int(request.data['penetration'])
        intercourse = int(request.data['intercourse'])
        completion = int(request.data['completion'])
        satisfaction = int(request.data['satisfaction'])
        score = confidence + penetration + intercourse + completion + satisfaction
        average = (confidence + penetration + intercourse + completion + satisfaction) / 5

        return Questionnaire.objects.create(
            user_id=request.user.id,
            average=average,
            score=score,
            **validated_data,
        )
