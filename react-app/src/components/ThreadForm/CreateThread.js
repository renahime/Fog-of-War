import ThreadForm from "./ThreadForm";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const CreateThreadForm = () => {
  const thread = {
    subject: '',
    text: '',
  }
  const location = useLocation()
  return (
    <ThreadForm thread={thread} category={location.state.category} formType="Create Thread">
    </ThreadForm>
  )
}

export default CreateThreadForm;
