import React from 'react';

import Admonition from '@theme/Admonition';

export default function VulnsTBD({ children }) {
    return (
        <div>
            <Admonition type="success" icon="💎" title={"Vulnerabiltiies to be discovered"}>
                The next vulnerabilities should be discovered in this sections:
                {children}
            </Admonition>
        </div>
    );
}