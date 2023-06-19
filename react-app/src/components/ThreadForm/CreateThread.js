import ThreadForm from "./ThreadForm";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const CreateThreadForm = () => {
  const thread = {
    subject: '',
    text: '',
  }
  const location = useLocation()
  return (
    <ThreadForm
      thread={thread}
      category={location.state.category}
      subcategory={location.state.subcategory}
      categoryId={location.state.categoryId}
      subcategoryId={location.state.subcategoryId}
      formType="Create Thread">
    </ThreadForm>
  )
}

export default CreateThreadForm;
