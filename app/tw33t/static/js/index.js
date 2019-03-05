var app = new Vue({ 
    el: '#app',
    delimiters : ['[[', ']]'],
    data: {
        message: 'Hello Vue!'
    },
    method: {
        imputSearchEventHandle: _.debounce(() => {
            console.log('I get fired every two seconds!')
          }, 2000)
    }
});
