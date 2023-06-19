import ThreadForm from "./ThreadForm";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const EditThreadForm = () => {
  const location = useLocation()

  return (
    <>
      <ThreadForm
        thread={location.state.thread}
        category={location.state.category}
        subcategory={location.state.subcategory}
        categoryId={location.state.categoryId}
        subcategoryId={location.state.subcategoryId}
        formType="Update Thread"
      ></ThreadForm>
    </>
  )
}

export default EditThreadForm
