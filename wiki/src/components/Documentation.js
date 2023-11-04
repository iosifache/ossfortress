import React from 'react';

import Admonition from '@theme/Admonition';

export default function Documentation({ software, link }) {
    return (
        <div>
            <Admonition type="info" icon="📚" title={software + " documentation"}>
                The {software} documentation is available <a href={link}>here</a>.
            </Admonition>
        </div>
    );
}