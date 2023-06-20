import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Confirm Password field must be the same as the Password field",
			]);
		}
	};

	return (
		<>
			<div className='main-body'>
				<form className='login-form' onSubmit={handleSubmit}>
					<table className='login-table'>
						<tbody>
							{email && (!email.includes('@') || !email.includes('.')) ? <p className='email-error'>Oops! You must type a valid email!</p> : null}
							{errors && errors.length ? errors.map((error) => (
								<p className='back-end-error'>{error}</p>
							)) : null}
							{errors && errors.email ? <p className='email-error'>{errors.email}</p> : null}
							<tr>
								<td className='login-title' colSpan={2}>
									<strong>Log-In</strong>
								</td>
							</tr>
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

			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<label>
					Email
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					Username
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label>
					Password
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<button type="submit">Sign Up</button>
			</form>
		</>
	);
}

export default SignupFormModal;
