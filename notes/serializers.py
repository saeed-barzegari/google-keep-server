from rest_framework import serializers

from labels.models import Label
from labels.serializers import LabelSerializer
from notes.models import Note
from django.utils.translation import gettext_lazy as _


class NoteSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)
    label_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'is_deleted', 'is_pinned', 'is_archived', 'color', 'labels', 'label_ids']

    def validate(self, attrs):
        request = self.context.get('request')
        current_user = request.user

        label_ids = attrs.get('label_ids', None)
        if label_ids:
            owner_labels_count = Label.objects.filter(id__in=label_ids, owner=current_user).count()

            if owner_labels_count != len(label_ids):
                raise serializers.ValidationError(
                    {'label_ids': _('You are not allowed to use all the submitted labels. Please only use the labels you own.')},
                    code='NOT_OWNER'
                )

        return attrs

    def create(self, validated_data):
        label_ids = validated_data.pop('label_ids', None)

        note = Note.objects.create(**validated_data)

        if label_ids:
            labels = Label.objects.filter(pk__in=label_ids)
            note.labels.set(labels)

        return note

    def update(self, instance, validated_data):
        label_ids = validated_data.pop('label_ids', None)

        instance = super().update(instance, validated_data)

        if label_ids:
            labels = Label.objects.filter(pk__in=label_ids)
            instance.labels.set(labels)

        return instance

