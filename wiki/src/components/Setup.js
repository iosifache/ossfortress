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

export function WebSetup({ software, profile, link }) {
    return <Setup software={software} profile={profile}>
        Access <a href={link}>this link</a> to interact with the application's web user interface.
    </Setup>
}