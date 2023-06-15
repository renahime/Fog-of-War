import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const sessionUser = useSelector(state => state.session.user);
	let date = new Date()

	return (
		<div>
			<div className='header-login'>
				<div className='login-register'>
					<Link to='/login'>Login</Link>
					<Link to='/signup'>Register</Link>
				</div>
				<h6 className='date'>{date.toString()}</h6>
			</div>
			<div className='buttons'>
				<i class="fa-solid fa-bars"></i>
			</div>
			<div className='thread-path'>
				<NavLink to="/">
					<i class="fa-solid fa-house"></i>
				</NavLink>
			</div>
		</div>
	);
}

export default Navigation;
