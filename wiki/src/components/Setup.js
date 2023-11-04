import React from 'react';

import Admonition from '@theme/Admonition';

function Setup({ children, software, profile }) {
    return (
        <div>
            <Admonition type="info" icon="⚙️" title={software + " setup"}>
                If you didn't set up the <code>{profile}</code> profile's infrastructure, please do so by running the command <code>docker-compose --profile {profile} up</code>.
                <br /><br />
                {children}
            </Admonition>
        </div>
    );
}

export function CLISetup({ software, profile, container }) {
    return <Setup software={software} profile={profile}>
        Use <code>docker exec --interactive --tty {container} bash</code> to enter the container where the CLI application is contained.
    </Setup>
}

export function WebSetup({ software, profile, link, credentials }) {
    const cred_label = credentials.includes(":") ? "credentials" : "password";

    return <Setup software={software} profile={profile}>
        Access <a href={link}>this link</a> to interact with the application's web user interface.

        {credentials ? <span> Use the <code>{credentials}</code> {cred_label} for login.</span> : ""}
    </Setup>
}