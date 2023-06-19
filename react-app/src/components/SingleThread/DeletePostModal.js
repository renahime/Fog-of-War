import React, { useState } from "react";
import { useModal } from "../../context/Modal";
import { useEffect } from "react"
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux"
import OpenModalButton from '../OpenModalButton';
import { deletePostThunk } from "../../store/category";

function DeletePostModal({ postId, category, threadId, subcategory, subcategoryId, categoryId }) {
  const { closeModal } = useModal();
  const history = useHistory();
  const dispatch = useDispatch();
  const handleDelete = async (e) => {
    e.preventDefault();
    const deletePost = await dispatch(deletePostThunk(postId, threadId, categoryId, subcategoryId)).then(closeModal())
    if (deletePost) {
      history.push({ pathname: `/${category}/${subcategory}/threads/${threadId}`, state: { category: category, threadId: threadId, subcategory: subcategory, subcategoryId: subcategoryId, categoryId: categoryId } })
    }
  }
  return (
    <div className="delete-thread-container">
      <h1>Are you sure?</h1>
      <h6>Once you delete a Post, you can't undo it!</h6>
      <div className="buttons">
        <button onClick={handleDelete}>Delete</button>
      </div>
    </div>
  )
}
export default DeletePostModal;
