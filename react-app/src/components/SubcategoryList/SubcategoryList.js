import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';


function SubcategoryList() {
  const sessionUser = useSelector(state => state.session.user);
  let location = useLocation()
  const state = useSelector(state => state.category.categories);
  const category = location.state.category;
  const categoryId = location.state.categoryId;
  const subcategories = state[categoryId].subcategories
  const subcategoriesArr = Object.values(subcategories);

  return (
    <div>
      <div className='main-body'>
        <div className='main-topics-div'>
          <center>
            <table className='main-page-table'>
              <thead>
                <td colSpan={5} className='topic-title'>
                  <strong>Topic</strong>
                </td>
              </thead>
              <tbody>
                <td colSpan={2} className='forum-title'>
                  <strong>Forum</strong>
                </td>
                <td className='threads-title'>
                  <strong>Threads</strong>
                </td>
                <td className='posts-title'>
                  <strong>Posts</strong>
                </td>
                <td className='last-post-title'>
                  <strong>Last Post</strong>
                </td>
              </tbody>
              {
                subcategoriesArr.map((subcategory) => (
                  <>
                    <div className='space-between-homepage'></div>
                    <tr className='home-page-table-row'>
                      <td className='category-name-homepage' colSpan={2}>
                        <NavLink to={{
                          pathname: `/${category}/${subcategory.name}/threads`,
                          state: {
                            category: category,
                            categoryId: location.state.categoryId,
                            subcategory: subcategory.name,
                            subcategoryId: subcategory.id,
                          }
                        }}>
                          <strong>{subcategory.name}</strong>
                        </NavLink>
                      </td>
                      <td className='thread-count-homepage' >
                        <strong >{subcategory.thread_count}</strong>
                      </td>
                      <td className='post-count-homepage'>
                        <strong>0</strong>
                      </td>
                      <td className='last-post-made-homepage'>
                        <center>
                          <strong>
                            (last post here)
                          </strong>
                        </center>
                      </td>
                    </tr>
                    <div className='space-between-homepage'></div>
                  </>
                ))
              }
            </table>
          </center>
        </div>
      </div >
    </div >
  );
}

export default SubcategoryList;
