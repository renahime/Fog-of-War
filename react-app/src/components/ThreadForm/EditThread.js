import ThreadForm from "./ThreadForm";
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
