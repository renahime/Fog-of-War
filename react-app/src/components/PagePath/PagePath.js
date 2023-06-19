import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, NavLink } from "react-router-dom";
import { login } from '../../store/session';
import "./PagePath.css";
import tempBanner from '../../imgs/tempwebbanner.png'

function PagePath() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;


  return (
    <div>
      <div className='separateor'></div>
      <div className='main-path-body'>
        <div>
          <div className='path-trail'>
            <div className='send-to-homen'>
              <NavLink to="/">
                <i class="fa-solid fa-house"></i>
              </NavLink>
            </div>
          </div>
        </div>
        <img className='temp-banner' src={tempBanner}></img>
      </div>
    </div>
  );
}

export default PagePath
