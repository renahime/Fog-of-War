import React, { Component } from 'react';
import { CKEditor } from '@ckeditor/ckeditor5-react';
import Editor from 'ckeditor5-custom-build/build/ckeditor';
// import { SimpleUploadAdapter } from '@ckeditor/ckeditor5-upload';



const CkEditor = ({ setText, text }) => {
  return (
    <div className="App">
      <CKEditor
        editor={Editor}
        data={text ? text : "Type your message here"}
        // config={{
        //   plugins: [SimpleUploadAdapter],
        //   simpleUpload: {
        //     // The URL that the images are uploaded to.
        //     uploadUrl: '/path/to/upload',

        //     // Headers sent along with the XMLHttpRequest to the upload server.
        //     headers: {
        //       'X-CSRF-TOKEN': 'CSFR-Token',
        //       Authorization: 'Bearer <JSON Web Token>'
        //     }
        //   }
        // }}
        onReady={editor => {
          console.log('Speak your mind...', editor);
        }}
        onChange={(event, editor) => {
          const data = editor.getData();
          setText(editor.getData());
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
