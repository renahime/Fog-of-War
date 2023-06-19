import PostForm from "./PostForm";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

const CreatePostForm = () => {
  const location = useLocation()
  const post = {
    subject: '',
    text: '',
  }

  return (
    <PostForm
      post={post} formType="Create Post"
      threadId={location.state.threadId}
      threadSubject={location.state.subject}
      category={location.state.category}
      categoryId={location.state.categoryId}
      subcategory={location.state.subcategory}
      subcategoryId={location.state.subcategoryId}>
    </PostForm>
  )
}

export default CreatePostForm;
