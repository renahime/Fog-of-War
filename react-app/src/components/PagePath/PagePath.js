import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom/cjs/react-router-dom.min';
import { Redirect, NavLink, Link } from "react-router-dom";
import { login } from '../../store/session';
import "./PagePath.css";
import tempBanner from '../../imgs/tempwebbanner.png'
import { useLocation } from 'react-router-dom/cjs/react-router-dom.min';

function PagePath() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const state = useSelector((state) => state.category.categories)
  const [threadId, setThreadId] = useState("")
  const [subcategory, setSubcategory] = useState("")
  const [category, setCategory] = useState("")
  const [threadSubject, setSubject] = useState("")
  const location = useLocation();
  let pathArray;
  console.log(location);
  console.log(state);
  useEffect(() => {
    pathArray = location.pathname.split('/')
    if (pathArray.length == 5) {
      setThreadId(pathArray[4]);
      setSubcategory(pathArray[2]);
      setCategory(pathArray[1]);
      for (let key in state) {
        if (state[key].name == category) {
          for (let subKey in state[key].subcategories) {
            if (state[key].subcategories[subKey].name == subcategory) {
              for (let threadKey in state[key].subcategories[subKey].threads) {
                if (threadKey == threadId) {
                  setSubject(state[key].subcategories[subKey].threads[threadKey].subject)
                }
              }
            }
          }
        }
      }
    }

    if (pathArray.length == 2) {
      setCategory(pathArray[1]);
      setThreadId("")
      setSubcategory("")
      setSubject("")
    }

    if (pathArray.length == 4) {
      setCategory(pathArray[1]);
      setSubcategory(pathArray[2]);
      setThreadId("")
      setSubject("")
    }
  }, [location.pathname, pathArray])
  return (
    <div>
      <div className='separate'></div>
      <div className='main-path-body'>
        <div>
          <div className='path-trail'>
            <div className='send-to-home'>
              <NavLink to="/">
                <i class="fa-solid fa-house"></i>
              </NavLink>
            </div>
            {category ?
              <div >
                <i class="fa-solid category-arrow fa-chevron-right"></i>
                <h5 style={{ color: 'white' }} className='category-name-path'>{category}</h5>
                {/* </NavLink> */}
              </div> : null}
            {subcategory ?
              <div>
                <i class={category.includes('Anime') ? "anime-arrow fa-solid subcategory-arrow fa-chevron-right" : "fa-solid subcategory-arrow fa-chevron-right"}></i>
                <h5 style={{ color: 'white' }} className={category.includes('Anime') ? "anime sub-category-name-path" : 'sub-category-name-path'}>{subcategory}</h5>
              </div> : null
            }
          </div>
        </div>
        <div className='separate-image'>
        </div>
        <div>
          <img className='temp-banner' src={tempBanner}></img>
        </div>
        <div className='separate-2'></div>
      </div>
    </div >
  );
}

export default PagePath
