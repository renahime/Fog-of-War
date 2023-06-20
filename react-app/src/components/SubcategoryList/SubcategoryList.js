import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';


function SubcategoryList() {
  const sessionUser = useSelector(state => state.session.user);
  let location = useLocation()
  const state = useSelector(state => state.category.categories);
  const subcategories = location.state.subcategories;
  const subcategoriesArr = Object.values(subcategories);
  const category = location.state.category;

  return (
    <div>
      <div className='main-body'>
        <div className='main-topics-div'>
          <div className='header-topic'>
            <h6>Main Topics</h6>
          </div>
          <div className='column-names'>
            <h6>Forum</h6>
            <h6>Threads</h6>
            <h6>Posts</h6>
            <h6>Last Post</h6>
          </div>
          {subcategoriesArr.map((subcategory) => (
            <NavLink to={{
              pathname: `/${category}/${subcategory.name}/threads`,
              state: {
                category: category,
                categoryId: location.state.categoryId,
                subcategory: subcategory.name,
                subcategoryId: subcategory.id,
              }
            }}>
              <div className='category-name'>
                {subcategory.name}
              </div>
            </NavLink>
          ))}
        </div>
      </div>

    </div >
  );
}

export default SubcategoryList;
