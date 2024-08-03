import React from 'react';

import { BeginnerContent } from '@site/src/components/BeginnerContent';
import Admonition from '@theme/Admonition';

export default function VulnsTBD({ children }) {
    return (
        <BeginnerContent showNothingOn="advanced">
            <Admonition type="success" icon="💎" title={"Vulnerabiltiies to be discovered"}>
                The next vulnerabilities should be discovered in this sections:
                {children}
            </Admonition>
        </BeginnerContent>
    );
}