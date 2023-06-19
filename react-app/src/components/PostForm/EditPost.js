
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";
import PostForm from "./PostForm";

const EditPostForm = () => {
  const location = useLocation()

  return (
    <>
      <PostForm
        post={location.state.post}
        category={location.state.category}
        threadSubject={location.state.subject}
        threadId={location.state.threadId}
        categoryId={location.state.categoryId}
        subcategory={location.state.subcategory}
        subcategoryId={location.state.subcategoryId}
        formType="Update Post"
      ></PostForm>
    </>
  )
}

export default EditPostForm
