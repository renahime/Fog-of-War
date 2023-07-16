import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { logout } from "../../store/session";
import './Navigation.css';
import logo from '../../imgs/banner.png'
import { useDispatch } from 'react-redux';


function Navigation({ isLoaded }) {
	const user = useSelector(state => state.session.user);
	let date = new Date()
	const dispatch = useDispatch()

	const handleLogout = (e) => {
		e.preventDefault();
		dispatch(logout());
	};

	const handleAlert = (e) => {
		alert("Feature coming soon!")
	}

	return (
		<div className='main-nav-body'>
			<div className='banner'>
				<img src={logo}></img>
			</div>
			<div className='banner-separator'></div>
			<div className='header-login'>
				{user ?
					<div className='logged-in-user-container'>
						<div style={{ gap: '50px', display: 'flex', flexDirection: "row" }}>
							<div className='user-logout-container'>
								<i onClick={handleLogout} class="fa-solid fa-right-from-bracket"></i>
							</div>
							<div className='user-info-container'>
								<h5>Welcome back, {user.username}. You last visited: {user.last_login.slice(0, 16)} </h5>
							</div>
						</div>
						<div className='user-date-container'>
							<h5 className='user-date'>{date.toString()}</h5>
						</div>
					</div> :
					<div className='login-register'>
						<div className='login-container'>
							<Link className='login-link' to='/login'><i class="fa-solid fa-key"></i><h5 className='login-text'>Login</h5></Link>
						</div>
						<div className='signup-container'>
							<Link className='signup-link' to='/signup'><i class="fa-solid fa-right-to-bracket"></i><h5 className='register-text'>Register</h5></Link>
						</div>
						<div className='non-user-date-container'>
							<h5 className='non-user-date'>{date.toString()}</h5>
						</div>
					</div>}
			</div>
			{user ?
				<div className='dropdown-container'>
					<div className='font-buttons'>
						<NavLink to={`/profile/${user.username}`}>
							<i class="fa-solid fa-user"></i>
						</NavLink>
						<NavLink to={`/following/${user.username}`}>
							<i class="fa-solid fa-heart"></i>
						</NavLink>
					</div>
				</div>
				:
				null}
		</div>
	);
}

export default Navigation;
