import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getThreadThunk } from "../../store/threads";
import ThreadForm from "./ThreadForm";

const EditThreadForm = () => {
  const { threadId } = useParams();
  const thread = useSelector((state) => state.thread.singleThread ? state.thread.singleThread : null);
  const dispatch = useDispatch();
  let [loading, setLoading] = useState(false)

  useEffect(() => {
    dispatch(getThreadThunk(idQuery)).then(() => setLoading(true))
  }, [dispatch, threadId])


  if (!thread) return (<></>)

  return (Object.keys(thread).length > 1 && (
    <>
      <ThreadForm
        thread={thread}
        formType="Update Thread"
      ></ThreadForm>
    </>
  ))
}

export default EditThreadForm
