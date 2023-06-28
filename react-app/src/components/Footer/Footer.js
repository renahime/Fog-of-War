import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory, Link, Route } from 'react-router-dom/cjs/react-router-dom.min';
import { useLocation } from 'react-router-dom'
import { useState, useEffect, createElement } from 'react';
import rena from '../../imgs/rena.gif'
import './Footer.css'

function Footer() {

  return (
    <div>
      <div className='space-between'></div>
      <center>
        <img src={rena}></img>
      </center>
      <div className='space-between'></div>
      <div className='upper-contents'>
        <div className='upper-container'>
          <p>
            <a href="https://github.com/renahime">
              <i class="fa-brands fa-github fa-2xl fa-pad"></i>
            </a>
            <a href="https://www.linkedin.com/in/lorena-s-a4a106275/">
              <i class="fa-brands fa-linkedin fa-2xl fa-pad"></i>
            </a>
            <i class="fa-brands fa-python fa-2xl fa-pad"></i>
            <i class="fa-brands fa-js fa-2xl fa-pad"></i>
            <i class="fa-brands fa-react fa-2xl fa-pad"></i>
          </p>
          <p style={{ textAlign: 'right', paddingRight: '20px' }}>Created by Rena</p>
        </div>
      </div>
    </div>
  )
}

export default Footer
