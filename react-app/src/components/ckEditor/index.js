import React, { Component } from 'react';
import { CKEditor } from '@ckeditor/ckeditor5-react';
import Editor from 'ckeditor5-custom-build/build/ckeditor';

const CkEditor = ({ setText, text }) => {
  return (
    <div className="App">
      <CKEditor
        editor={Editor}
        data="<p>Hello from CKEditor 5!</p>"
        onReady={editor => {
          console.log('Speak your mind...', editor);
        }}
        onChange={(event, editor) => {
          const data = editor.getData();
          setText(editor.getData());
          console.log(text);
          console.log({ event, editor, data });
        }}
        onBlur={(event, editor) => {
          console.log('Blur.', editor);
        }}
        onFocus={(event, editor) => {
          console.log('Focus.', editor);
        }}
      />
    </div>
  );
}
export default CkEditor;
