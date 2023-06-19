import React, { useState } from "react";
import { useModal } from "../../context/Modal";
import { useEffect } from "react"
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux"
import OpenModalButton from '../OpenModalButton';
import { deleteThreadThunk } from "../../store/category";

function DeleteThreadModal({ threadId, category, subcategory, categoryId, subcategoryId }) {
  const { closeModal } = useModal();
  const user = useSelector
  const history = useHistory();
  const dispatch = useDispatch();
  const handleDelete = async (e) => {
    e.preventDefault();
    const deleteThread = await dispatch(deleteThreadThunk(threadId, categoryId, subcategoryId)).then(closeModal())
    if (deleteThread)
      history.push(`/${category}/${subcategory}/threads`, { category: category, subcategory: subcategory, subcategoryId: subcategoryId, categoryId: categoryId })
  }
  return (
    <div className="delete-thread-container">
      <h1>Are you sure?</h1>
      <h6>Once you delete a Thread, you can't undo it!</h6>
      <div className="buttons">
        <button onClick={handleDelete}>Delete</button>
      </div>
    </div>
  )
}
export default DeleteThreadModal;
