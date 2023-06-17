import PostForm from "./PostForm";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const CreatePostForm = () => {
  const location = useLocation()
  const post = {
    subject: '',
    text: '',
  }

  return (
    <PostForm post={post} formType="Create Post" threadId={location.state.id} threadSubject={location.state.subject} category={location.state.category}>
    </PostForm>
  )
}

export default CreatePostForm;
