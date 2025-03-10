from rest_framework import serializers
from .models import SourceCode, TranslationTask, TranslationResult, Analysis

class SourceCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceCode
        fields = ['id', 'code', 'created_at']

class TranslationTaskSerializer(serializers.ModelSerializer):
    # Embedding the SourceCode details; read-only for now.
    source_code = SourceCodeSerializer(read_only=True)
    
    class Meta:
        model = TranslationTask
        fields = ['id', 'source_code', 'status', 'created_at', 'updated_at']

class TranslationResultSerializer(serializers.ModelSerializer):
    # Embed the associated TranslationTask information
    translation_task = TranslationTaskSerializer(read_only=True)
    
    class Meta:
        model = TranslationResult
        fields = ['id', 'translation_task', 'rust_code', 'compilation_logs', 'created_at']

class AnalysisSerializer(serializers.ModelSerializer):
    # Include translation task details for context
    translation_task = TranslationTaskSerializer(read_only=True)
    
    class Meta:
        model = Analysis
        fields = [
            'id',
            'translation_task',
            'c_execution_time',
            'rust_execution_time',
            'c_memory_usage',
            'rust_memory_usage',
            'result_summary',
            'created_at'
        ]
