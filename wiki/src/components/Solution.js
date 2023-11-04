import React from 'react';

import Admonition from '@theme/Admonition';

export function Solution({ children, pass }) {
    const [inputValue, setInputValue] = React.useState("");
    const [showContent, toggleShowContent] = React.useState(false);

    const onChangeHandler = event => {
        setInputValue(event.target.value);

        if (event.target.value === pass) {
            toggleShowContent(true)
        }
    };

    let content
    if (showContent) {
        content = children;
    }
    else {
        content = <div><p>To display the solution of this task, enter the text <code>{pass}</code> in the field below.</p>
            <input type='text' className='navbar__search-input solution-pass' onChange={onChangeHandler}
                value={inputValue} /></div>
    }

    return (
        <div>
            <Admonition type="warning" icon="🚧" title="Solution">
                {content}
            </Admonition>
        </div>
    );
}

export function DefaultSolution({ children }) {
    return (
        <Solution pass={"i-surrender-to-the-code-security-gods"}>
            {children}
        </Solution>
    )
}