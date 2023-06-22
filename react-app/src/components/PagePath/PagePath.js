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
  const location = useLocation();
  let pathArray;
  useEffect(() => {
    pathArray = location.pathname.split('/')

    if (pathArray.length == 2) {
      setCategory(pathArray[1]);
      for(let key in state){
        if(state[key].name == category){
          setCategoryId(key);
        }
      }
      setSubcategory("")
      setSubcategoryId("")
    }

    if (pathArray.length == 4) {
      setCategory(pathArray[1]);
      setSubcategory(pathArray[2]);
      for(let key in state){
        if(state[key].name == category){
          setCategoryId(key);
          for(let subKey in state[key].subcategories){
            if (state[key].subcategories[subKey].name == subcategory){
              setSubcategoryId(subKey)
            }
          }
        }
      }
    }
  }, [location.pathname, pathArray, category, subcategory, categoryId, subcategoryId])
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
              <div className='category-direct' >
                <NavLink
                className='category-direct'
                to={{
                  pathname:`/${category}`,
                  state:{
                    category:category,
                    categoryId:categoryId
                  }
                }}>
                <i class="fa-solid category-arrow fa-chevron-right"></i>
                <h5 style={{ color: 'white' }} className='category-name-path'>{category}</h5>
                </NavLink>
              </div> 
              : null}
            {subcategory ?
                <NavLink className='subcategory-direct' to={{
                                      pathname: `/${category}/${subcategory}/threads`,
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
