import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import { grabHours } from '../HomePage/HomePage';
import { getAllCategoriesThunk } from '../../store/category';


function SubcategoryList() {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  let location = useLocation();
  let categoriesState = useSelector(state => state.category.categories);
  const category = location.state.category;
  const categoryId = location.state.categoryId;
  // const subcategories = state[categoryId].subcategories;
  // const subcategoriesArr = Object.values(subcategories);

  const [subcategories, setSubCategories] = useState();
  const [subcategoriesArr, setSubCategoriesArr] = useState();

  useEffect(() => {
    if (!categoriesState)
      dispatch(getAllCategoriesThunk())
  }, [dispatch])

  useEffect(() => {
    if (categoriesState) {
      setSubCategories(categoriesState[categoryId].subcategories);
    }
  }, [categoriesState]);

  useEffect(() => {
    if (subcategories) {
      setSubCategoriesArr(Object.values(subcategories));
    }
  }, [subcategories])


  return (!subcategoriesArr ? <h1>Loading...</h1> :
    <div>
      <div className='main-body'>
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
                    <strong>{subcategory.post_count}</strong>
                  </td>
                  <td className='last-post-made-homepage'>
                    <center>
                      <strong>
                        {subcategory.youngest_post.category ? <NavLink
                          to={{
                            pathname: `/${subcategory.youngest_post.category.name}/${subcategory.youngest_post.subcategory.name}/threads/${subcategory.youngest_post.thread_id}`,
                            state: {
                              category: subcategory.youngest_post.category.name,
                              categoryId: subcategory.youngest_post.category.id,
                              subcategory: subcategory.youngest_post.subcategory.name,
                              subcategoryId: subcategory.youngest_post.subcategory.id,
                              threadId: subcategory.youngest_post.thread_id
                            }
                          }}>
                          <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', gap: '9px', paddingRight: '7px', paddingTop: '7px', paddingBottom: '7px' }}>
                            <strong className='subject-title'>
                              {subcategory.youngest_post.thread_subject ? subcategory.youngest_post.thread_subject : subcategory.youngest_post.subject}
                            </strong>
                            <strong className='time-of-post'>
                              {subcategory.youngest_post ? grabHours(subcategory.youngest_post.created_at) : null}
                            </strong>
                            <strong className='post-author'>
                              By: {subcategory.youngest_post.user ? subcategory.youngest_post.user.username : null}
                            </strong>
                          </div>
                        </NavLink>
                          : null}
                      </strong>
                    </center>
                  </td>
                </tr>
                <div className='space-between-homepage'></div>
              </>
            ))
          }
        </table>
      </div >
    </div >
  );
}

export default SubcategoryList;
