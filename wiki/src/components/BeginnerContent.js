import Cookies from 'js-cookie';
import React, { useEffect, useState } from 'react';

import Admonition from '@theme/Admonition';

export function BeginnerContent({ children, title, note, showNothingOn = "" }) {
    const [mode, setMode] = useState(Cookies.get("wikiMode"));

    useEffect(() => {

    }, [mode]);

    var wikiModeCookie = Cookies.get("wikiMode")
    var wikiMode = wikiModeCookie ? wikiModeCookie : "beginner"

    if (showNothingOn == wikiMode) return "";

    if (wikiMode == "advanced")
        return (
            <div>
                <Admonition type="danger" icon="🔰" title={title}>
                    {note}
                </Admonition>
            </div>
        );

    return <div>{children}</div>;
}

export function BeginnerPage({ children }) {
    return (
        <BeginnerContent title="Beginner page" note="This page is marked as beginner-friendly, but you have the advanced mode enabled. Switch to the beginner mode if you want to see the content of this page.">
            {children}
        </BeginnerContent>
    )
}

export function SolutionsNote({ children }) {
    return (
        <BeginnerContent showNothingOn="beginner" title="Hidden solutions" note="This page also proposes solutions, but you have the advanced mode enabled. Switch to the beginner mode if you want to see the solutions.">
            {children}
        </BeginnerContent>
    )
}
