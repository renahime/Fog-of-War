import React, { useState } from "react";
import { useModal } from "../../context/Modal";
import { useEffect } from "react"
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux"
import OpenModalButton from '../OpenModalButton';
import { deletePostThunk } from "../../store/threads";

function DeletePostModal({ postId, category, threadId }) {
  const { closeModal } = useModal();
  const history = useHistory();
  const dispatch = useDispatch();
  const handleDelete = async (e) => {
    e.preventDefault();
    const deleteThread = await dispatch(deletePostThunk(postId, threadId)).then(closeModal())
    if (deleteThread) {
      history.push({ pathname: `/threads/${category}/${threadId}`, state: { category: category, id: threadId } })
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
