import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, Link } from "react-router-dom";
import { login } from '../../store/session';
import "./LoginPage.css";

function LoginPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    let validationErrors = {}

    if (!email.includes('@') || !email.includes('.')) {
      validationErrors.email = "Oops! You must include a valid email."
    }

    if (Object.values(validationErrors).length) {
      setErrors(validationErrors)
      return
    }

    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
      console.log(errors);
    }
  };


  return (
    <div className='main-body'>
      <form className='login-form' onSubmit={handleSubmit}>
        <table className='login-table'>
          <tbody>
            <tr>
              <td className='login-title' colSpan={2}>
                <strong>Log-In</strong>
              </td>
            </tr>
            {email && (!email.includes('@') || !email.includes('.')) ? <p className='email-error'>Oops! You must type a valid email!</p> : null}
            {errors && errors.length ? errors.map((error) => (
              <p className='back-end-error'>{error}</p>
            )) : null}
            {errors && errors.email ? <p className='email-error'>{errors.email}</p> : null}
            <div className='space-between-small'> </div>
            <tr >
              <td className='login-row-1'>
                <strong>Email:</strong>
              </td>
              <td className='login-row-1'>
                <input
                  className='login-text-input'
                  type="text"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </td>
            </tr>
            <div className='space-between'>
            </div>
            <tr >
              <td className='login-row-2'>
                <strong>Password</strong>
              </td>
              <td className='login-row-2'>
                <input
                  className='login-text-input'
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </td>
            </tr>
            <div className='space-between'>
            </div>
            <tr className='sign-up' colSpan={2}>
              <Link to='/signup' className="sign-up-link">Don't have an account? Sign up!</Link>
            </tr>
            <div className='space-between-small'>
            </div>
          </tbody>
        </table>
        <div className='space-between-small'>
        </div>
        <div>
          <button className='login-button' type="submit">Log In</button>
        </div>
      </form>
    </div>
  );
}

export default LoginPage
