import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage/HomePage";
import LoginPage from "./components/LoginPage/LoginPage";
import SignUpPage from "./components/SignUpPage/SignUpPage";
import ThreadList from "./components/ThreadList/ThreadList";
import SingleThread from "./components/SingleThread/SingleThread";
import CreateThreadForm from "./components/ThreadForm/CreateThread";
import CreatePostForm from "./components/PostForm/CreatePost";
import EditThreadForm from "./components/ThreadForm/EditThread"
import EditPostForm from "./components/PostForm/EditPost";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <> <Navigation></Navigation>
      {isLoaded && (
        <Switch>
          <Route exact path="/login" >
            <LoginPage />
          </Route>
          <Route exact path="/signup">
            <SignUpPage />
          </Route>
          <Route exact path="/">
            <HomePage></HomePage>
          </Route>
          <Route exact path='/threads/:category'>
            <ThreadList></ThreadList>
          </Route>
          <Route exact path='/threads/:category/new'>
            <CreateThreadForm></CreateThreadForm>
          </Route>
          <Route exact path='/threads/:category/edit'>
            <EditThreadForm></EditThreadForm>
          </Route>
          <Route exact path='/threads/:category/:threadId'>
            <SingleThread></SingleThread>
          </Route>
          <Route exact path='/threads/:category/:threadId/new'>
            <CreatePostForm></CreatePostForm>
          </Route>
          <Route exact path='/threads/:category/:threadId/edit'>
            <EditPostForm></EditPostForm>
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
