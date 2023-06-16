import PostForm from "./PostForm";

const CreatePostForm = ({ threadId, threadSubject }) => {
  const post = {
    subject: '',
    text: '',
  }

  return (
    <PostForm post={post} formType="Create Post">
    </PostForm>
  )
}

export default CreatePostForm;
