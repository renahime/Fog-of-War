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
  const [subcategory, setSubcategory] = useState("")
  const [category, setCategory] = useState("")
  const [subcategoryId, setSubcategoryId] = useState("")
  const [categoryId, setCategoryId] = useState("")
  const [username, setUsername] = useState("")
  const location = useLocation();
  let pathArray;

  useEffect(() => {
    pathArray = location.pathname.split('/')
    console.log(pathArray)
    setUsername("")
    setCategory("")
    setSubcategory("")
    if (pathArray.length == 2) {
      pathArray[1] ? setCategory("404 :(") : setCategory("")
      setSubcategory("")
      setSubcategoryId("")
    }

    if (pathArray.length == 3) {
      setUsername(pathArray[2])
    }

    if (pathArray.length == 5 || pathArray.length == 6) {
      setCategory(pathArray[2]);
      setSubcategory(pathArray[3]);
      for (let key in state) {
        if (state[key].name == category) {
          setCategoryId(key);
          for (let subKey in state[key].subcategories) {
            if (state[key].subcategories[subKey].name == subcategory) {
              setSubcategoryId(subKey)
            }
          }
        }
      }
    }
  })

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
            {category && !category.includes("404") ?
              <div className='category-direct' >
                <NavLink
                  className='category-direct'
                  to={{
                    pathname: `/category/${category}`,
                    state: {
                      category: category,
                      categoryId: categoryId
                    }
                  }}>
                  <i class="fa-solid category-arrow fa-chevron-right"></i>
                  <h5 style={{ color: 'white' }} className='category-name-path'>{category}</h5>
                </NavLink>
              </div>
              : category && category.includes("404") ? <div className='category-direct' >
                <NavLink
                  className='category-direct'
                  to={{
                    pathname: `/`,
                  }}>
                  <i class="fa-solid category-arrow fa-chevron-right"></i>
                  <h5 style={{ color: 'white' }} className='category-name-path'>{category}</h5>
                </NavLink>
              </div> : null}
            {subcategory ?
              <NavLink className='subcategory-direct' to={{
                pathname: `/category/${category}/${subcategory}/threads`,
                state: {
                  category: category,
                  categoryId: categoryId,
                  subcategory: subcategory,
                  subcategoryId: subcategoryId,
                }
              }}>
                <div className='subcategory-direct'>
                  <i class={category.includes('Anime') ? "anime-arrow fa-solid subcategory-arrow fa-chevron-right" : "fa-solid subcategory-arrow fa-chevron-right"}></i>
                  <h5 style={{ color: 'white' }} className={category.includes('Anime') ? "anime sub-category-name-path" : 'sub-category-name-path'}>{subcategory}</h5>
                </div> </NavLink> : null
            }
            {username ?
              <div>
                <i class="fa-solid category-arrow fa-chevron-right"></i>
                <h5 style={{ color: 'white' }} className='category-name-path'>{username}</h5>
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
