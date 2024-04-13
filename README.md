# TaskRize

## Description

TaskRize is a robust project management application. Offering a streamlined user experience, TaskRize empowers individuals and teams to efficiently organize tasks, collaborate seamlessly, and enhance productivity. With intuitive features and customizable boards, users can easily visualize workflows, assign tasks, track progress, and prioritize activities. TaskRize facilitates effective project management, fostering teamwork and enabling users to achieve their goals with ease.

🚧 In progress: Continuing development towards MVP milestone. 🚧

## Technologies and Tools
### Frontend

<img src="https://skillicons.dev/icons?i=ts,react,redux,bootstrap" />

### Backend

<img src="https://skillicons.dev/icons?i=python,django" />

## Authentication

TaskRize implements a JWT-based authentication system, providing secure access to authorized users. JSON Web Tokens (JWT) are used to authenticate users and maintain session state across requests. The authentication flow involves the following steps:

- New users can register by providing an email and a password. The password needs to be retyped in order to register.
- Existing users can reset their password if they forgot it. They have to submit their email and they will receive by email a verification code to verify their identity.
- Existing users can login by providing their credentials. Upon successful login, the user receives a JWT token.
- JWT tokens are securely stored on the client-side in http-only cookies and sent with each subsequent request to authenticate the user's identity.
- JWT tokens have an expiration time to enhance security. Users must refresh their tokens periodically to maintain access.
- Users can invalidate their JWT token by logging out, ensuring that unauthorized access is prevented.