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
import ThreadForm from "./components/ThreadForm/ThreadForm";
import PostForm from "./components/PostForm/PostForm";

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
            <ThreadForm></ThreadForm>
          </Route>
          <Route exact path='/threads/:category/:threadName'>
            <SingleThread></SingleThread>
          </Route>
          <Route exact path='/threads/:category/:threadId/new'>
            <PostForm></PostForm>
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
