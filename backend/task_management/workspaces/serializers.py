from rest_framework import serializers
from workspaces.models import Workspace
from authentication.models import UserProfile

class WorkspaceSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'owner', 'members']

    def get_members(self, obj):
        # Get the user profiles of all members
        member_profiles = UserProfile.objects.filter(user__in=obj.members.all())
        
        # Extract information for each member
        members_data = []
        for profile in member_profiles:
            member_info = {
                'email': profile.user.email,
                'name': profile.name if profile.name else None,
                'nickname': profile.nickname if profile.nickname else None,
            }
            members_data.append(member_info)
        
        return members_data

    def create(self, validated_data):
        # Extract and remove members data from validated data
        members_data = validated_data.pop('members', [])
        # Create workspace instance
        workspace = Workspace.objects.create(**validated_data)
        # Set members for the workspace
        for member_data in members_data:
            workspace.members.add(member_data)
        return workspace
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'nickname']