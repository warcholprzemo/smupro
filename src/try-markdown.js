import React from 'react';
import './try-markdown.css';
const ReactMarkdown = require('react-markdown');

const global_input = `
# This is header1
### This is header3

*this is italic*

**this is bold **

~~This is Strikethrough~~

1. Ordered list item
2. Ordered list item

* Unordered list item
* Unordered list item
`

export class TryMarkdown extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            foo_input: "# This is a header\n\nAnd this is a paragraph  \nAnd this is another line"
        }
    }

    render(){
        return(
            <div>
                <h1>Try to render Markdown</h1>
                <div className="try-markdown-main">
                    <ReactMarkdown source={global_input} />
                </div>
            </div>
        )
    }
}

