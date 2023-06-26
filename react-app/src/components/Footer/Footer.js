import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom/cjs/react-router-dom.min';
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
            <i class="fa-brands fa-github fa-2xl fa-pad"></i>
            <i class="fa-brands fa-linkedin fa-2xl fa-pad"></i>
            <i class="fa-brands fa-python fa-2xl fa-pad"></i>
            <i class="fa-brands fa-js fa-2xl fa-pad"></i>
            <i class="fa-brands fa-react fa-2xl fa-pad"></i>
          </p>
          {/* <i class="fa-solid fa-flask fa-2xl"></i>
            <ul className='footer-tags'>
              <li className='footer-list'><i class="fa-brands fa-github fa-2xl"></i></li>
              <li className='footer-list'><i class="fa-brands fa-linkedin fa-2xl"></i></li>
              <li className='footer-list'><i class="fa-brands fa-python fa-2xl"></i></li>
              <li className='footer-list'><i class="fa-brands fa-js fa-2xl"></i></li>
              <li className='footer-list'><i class="fa-brands fa-react fa-2xl"></i></li>
              <li className='footer-list'> <i class="fa-solid fa-flask fa-2xl"></i></li>
            </ul> */}
        </div>
      </div>
    </div>
  )
}

export default Footer
