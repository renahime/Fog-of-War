import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, Link } from "react-router-dom";
import { signUp } from "../../store/session";
import './SignupPage.css';
function SignUpPage() {

  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    let validationErrors = {}

    if (!email.includes('@') || !email.includes('.')) {
      validationErrors.email = "Oops! You must include a valid email."
    }

    if (password !== confirmPassword) {
      validationErrors.password = "Oops! Your passwords must match!"
    }

    if (Object.values(validationErrors).length) {
      setErrors(validationErrors)
      return
    }

    if (password === confirmPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    } else {
      setErrors(['Confirm Password field must be the same as the Password field']);
    }
  };

  return (
    <div className='main-body'>
      <div className='main-body'>
        <form className='login-form' onSubmit={handleSubmit}>
          <table className='login-table'>
            <tbody>
              <tr>
                <td className='login-title' colSpan={2}>
                  <strong>Register</strong>
                </td>
              </tr>
              {email && (!email.includes('@') || !email.includes('.')) ? <p className='email-error'>Oops! You must type a valid email!</p> : null}
              {(password && confirmPassword) && (password !== confirmPassword) ? <p className="password-error">Oops! You must have matching passwords</p> : null}
              {errors && errors.length ? errors.map((error) => (
                <p className='back-end-error'>{error}</p>
              )) : null}
              {errors && errors.email ? <p className='email-error'>{errors.email}</p> : null}
              {errors && errors.password ? <p className="password-error">{errors.password}</p> : null}
              <div className='space-between-small'> </div>
              <tr >
                <td className='login-row-1'>
                  <strong>Email:</strong>
                </td>
                <td className='login-row-1'>
                  <input
                    className='signup-text-input'
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
                  <strong>Username</strong>
                </td>
                <td className='login-row-2'>
                  <input
                    className='signup-text-input'
                    type="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
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
                    className='signup-text-input'
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </td>
              </tr>
              <div className='space-between'>
              </div>
              <tr >
                <td className='login-row-2'>
                  <strong>Confirm Password</strong>
                </td>
                <td className='login-row-2'>
                  <input
                    className='signup-text-input'
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    required
                  />
                </td>
              </tr>
              <div className='space-between'>
              </div>
              <div className='space-between-small'>
              </div>
            </tbody>
          </table>
          <div className='space-between-small'>
          </div>
          <div>
            <button className='login-button' type="submit">Sign Up!</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default SignUpPage
