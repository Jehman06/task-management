"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from authentication.views import register_user, login_user, logout_user, reset_password_request, reset_password_confirm, get_profile, update_profile, delete_account, update_user_email, update_user_password, search_profiles
from django.views.generic import RedirectView
from workspaces.views import create_workspace, get_workspaces, update_workspace, delete_workspace, get_workspace_boards, invite_members, accept_invitation, reject_invitation, leave_workspace
from boards.views import get_boards, create_board, update_board, toggle_favorite_board, delete_board, get_board_and_lists
# from lists.views import create_list, update_list, delete_list
# from cards.views import create_card
from notifications.views import send_notification, get_notifications, read_notification
from images.views import create_image, get_sample_images, get_all_images
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Authentication
    path('', RedirectView.as_view(url='/admin/')), # Redirect to the admin page
    path('admin/', admin.site.urls),
    path('api/user/register', register_user, name='register'),
    path('api/user/login', login_user, name='login'),
    path('api/user/logout', logout_user, name='logout'),
    path('api/user/reset-password', reset_password_request, name='reset-password-request'),
    re_path(r'^api/user/reset-password-confirm/(?P<user_id>\d+)/?(?P<reset_code>\w+)?$', reset_password_confirm, name='reset-password-confirm'),
    path('api/user/email-update', update_user_email, name='email-update'),
    path('api/user/password-update', update_user_password, name='password-update'),
    path('api/user/delete', delete_account, name='account-delete'),
    # User
    path('api/user/profile', get_profile, name='user-profile-get'),
    path('api/user/profile/update/<int:pk>/', update_profile, name='user-profile-update'),
    path('api/user/profiles/', search_profiles, name='search-profiles'),
    # Tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Workspaces
    path('api/workspaces/', get_workspaces, name='workspace-list'),
    path('api/workspaces/<int:workspace_id>/boards/', get_workspace_boards, name='workspace-board'),
    path('api/workspaces/create', create_workspace, name='workspace-create'),
    path('api/workspaces/update', update_workspace, name='workspace-update'),
    path('api/workspaces/delete', delete_workspace, name='workspace-delete'),
    path('api/workspaces/leave', leave_workspace, name='workspace-leave'),
    path('api/workspaces/members/invite', invite_members, name='workspace-invite'),
    path('api/workspaces/members/accept-invite', accept_invitation, name='workspace-invite-accept'),
    path('api/workspaces/members/reject-invite', reject_invitation, name='workspace-invite-reject'),
    # Boards
    path('api/boards/', get_boards, name='board-list'),
    path('api/boards/<int:board_id>', get_board_and_lists, name='board-get'),
    path('api/boards/create', create_board, name='board-create'),
    path('api/boards/update', update_board, name='board-update'),
    path('api/boards/toggle-favorite', toggle_favorite_board, name='toggle-favorite-board'),
    path('api/boards/delete', delete_board, name='board-delete'),
    # Lists
    # path('api/lists/create', create_list, name='list-create'),
    # path('api/lists/update/<int:list_id>', update_list, name='list-update'),
    # path('api/lists/delete/<int:list_id>', delete_list, name='list-delete'),
    # Cards
    # path('api/cards/create', create_card, name='card-create'),
    # Notifications
    path('api/notifications', get_notifications, name='notifications'),
    path('api/notifications/send', send_notification, name='notification-send'),
    path('api/notifications/read', read_notification, name='notification-read'),
    # Images
    path('api/images/create', create_image, name='image-create'),
    path('api/images/sample', get_sample_images, name='image-sample'),
    path('api/images/all', get_all_images, name='image-all'),
]