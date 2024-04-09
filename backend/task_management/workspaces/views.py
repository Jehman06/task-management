from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from workspaces.models import Workspace
from workspaces.serializers import WorkspaceSerializer

# Get the workspaces for the user
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_workspaces(request):
    # Access the authenticated user
    user = request.user
    # Query the database for relevant workspaces
    # Include workspaces where the user is the owner or a member
    workspaces = Workspace.objects.filter(Q(owner=user) | Q(members=user))
    # Serialize the list of workspaces into JSON format, allowing multiple instances
    serializer = WorkspaceSerializer(workspaces, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new workspace
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_workspace(request):
    # Access the authenticated user
    user = request.user
    # Extract the data from the request payload
    data = request.data.copy()  # Create a mutable copy of the data dictionary
    # Extract owner's id
    owner_id = user.id
    # Add the owner's id to the data dictionary
    data['owner'] = owner_id
    # Validate the data using the WorkspaceSerializer
    serializer = WorkspaceSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        # Create a new workspace instance associated with the user
        workspace = serializer.save()
        # Since members is a many-to-many field, set the owner as the initial member
        workspace.members.set([user])
        return Response(WorkspaceSerializer(workspace).data, status=status.HTTP_201_CREATED)
    else:
        print("Validation errors:", serializer.errors)  # Print validation errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Update workspace
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_workspace(request):
    # Retrieve the data from the request
    workspace_id = request.data.get('workspace_id')
    updated_data = request.data.get('updated_data', {})
    if not workspace_id:
        return Response({'error': 'Workspace ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        workspace = Workspace.objects.get(id=workspace_id)
        for key, value in updated_data.items():
            setattr(workspace, key, value)
        # Save the updated workspace
        workspace.save()
        # Serialize and update the workspace
        serializer = WorkspaceSerializer(workspace)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Workspace.DoesNotExist:
        return Response({'error': 'Workspace not found'}, status=status.HTTP_404_NOT_FOUND)
    
# Delete board
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_workspace(request):
    # Retrieve the workspace ID from the request
    workspace_id = request.data.get('workspace_id')
    if not workspace_id:
        return Response({'error': 'Workspace ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        workspace = Workspace.objects.get(id=workspace_id)
        # Delete the workspace
        workspace.delete()
        return Response({'message': 'Workspace deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Workspace.DoesNotExist:
        return Response({'error': 'Workspace not found'}, status=status.HTTP_404_NOT_FOUND)