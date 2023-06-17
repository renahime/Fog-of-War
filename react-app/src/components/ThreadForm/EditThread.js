import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getThreadThunk } from "../../store/threads";
import ThreadForm from "./ThreadForm";
import { useState } from "react";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const EditThreadForm = () => {
  const location = useLocation()

  return (
    <>
      <ThreadForm
        thread={location.state.thread}
        category={location.state.category}
        formType="Update Thread"
      ></ThreadForm>
    </>
  )
}

export default EditThreadForm
