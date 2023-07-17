import React from 'react';
import trail from '../../imgs/trail.png'
import './NotFound.css';


function NotFound() {
  console.log(trail);
  return <div className='not-found-container'>
    <div className='space-between'></div>
    <div className='container-trail'>
      <img className='trail-image' src={trail}></img>
      <img className='trail-image-invert' src={trail}></img>
      <center>
      </center>
    </div>
    <div className='space-between'></div>
    <h2 style={{ textAlign: 'center' }}>Looks like this path leads to nowhere...</h2>
    <div className='space-between'></div>
  </div>
}

export default NotFound
