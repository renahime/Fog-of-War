import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch, NavLink } from "react-router-dom";
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
import SubcategoryList from "./components/SubcategoryList/SubcategoryList";
import PagePath from "./components/PagePath/PagePath";
import Footer from "./components/Footer/Footer";
import UserProfile from "./components/userProfile/userProfile";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <> <Navigation></Navigation>
      <PagePath></PagePath>
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
          <Route exact path="/profile/:username">
            <UserProfile></UserProfile>
          </Route>
          <Route exact path='/:category'>
            <SubcategoryList></SubcategoryList>
          </Route>
          <Route exact path='/:category/:subcategory/threads'>
            <ThreadList></ThreadList>
          </Route>
          <Route exact path='/:category/:subcategory/threads/new'>
            <CreateThreadForm></CreateThreadForm>
          </Route>
          <Route exact path='/:category/:subcategory/threads/edit'>
            <EditThreadForm></EditThreadForm>
          </Route>
          <Route exact path='/:category/:subcategory/threads/:threadId'>
            <SingleThread></SingleThread>
          </Route>
          <Route exact path='/:category/:subcategory/threads/:threadId/new'>
            <CreatePostForm></CreatePostForm>
          </Route>
          <Route exact path='/:category/:subcategory/threads/:threadId/edit'>
            <EditPostForm></EditPostForm>
          </Route>
        </Switch>
      )}
      <Footer></Footer>
    </>
  );
}

export default App;
