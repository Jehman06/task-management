import React, { useState } from 'react';
import axios, { AxiosError } from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const SignupPage: React.FC = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    password_confirmation: '',
  });
  const [errorMessage, setErrorMessage] = useState('');

  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (formData.password !== formData.password_confirmation) {
      setErrorMessage("Passwords don't match");
      return;
    }
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/register',
        formData,
      );
      console.log('User registered successfully:', response.data);
      setErrorMessage('');
      navigate('/login');
    } catch (error: any) {
      console.error('Error registering user:', error);
      setErrorMessage(
        (error as AxiosError<any>)?.response?.data?.error ||
          'An error occurred during registration.',
      );
    }
  };

  return (
    <div className="container w-50">
      <h1 className="text-center mt-5 mb-5">Signup</h1>
      <form onSubmit={handleSubmit} className="col-md-6 mx-auto">
        {errorMessage && (
          <div className="p-1 text-danger bg-danger-subtle border border-danger rounded-3 w-100">
            {errorMessage}
          </div>
        )}
        <div className="mb-2">
          <input
            className="form-control"
            id="emailInput"
            type="email"
            name="email"
            placeholder="name@example.com"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-2">
          <input
            className="form-control"
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            aria-describedby="passwordHelpBlock"
            required
          />
        </div>

        <div className="mb-2">
          <input
            className="form-control"
            type="password"
            name="password_confirmation"
            placeholder="Confirm Password"
            value={formData.password_confirmation}
            onChange={handleChange}
            aria-describedby="passwordHelpBlock"
            required
          />
        </div>

        <button type="submit" className="btn btn-primary w-100 mb-1">
          Signup
        </button>
        <Link to="/login">Already have an account? Login</Link>
      </form>
    </div>
  );
};

export default SignupPage;
