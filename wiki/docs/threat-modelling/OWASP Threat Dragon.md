---
sidebar_position: 2
slug: owasp-threat-dragon
toc_max_heading_level: 2
---

import Documentation from '@site/src/components/Documentation';
import {WebSetup} from '@site/src/components/Setup';
import {DefaultSolution} from '@site/src/components/Solution';
import {SolutionsNote} from '@site/src/components/BeginnerContent';

<WebSetup software="OWASP Threat Dragon" profile="threat-modelling" link="http://127.0.0.1:8001"/>

<Documentation software="OWASP Threat Dragon" link="https://owasp.org/www-project-threat-dragon/docs-2/"/>

<SolutionsNote/>

## Creating a threat model

1. Access [your local OWASP Threat Dragon user interface](http://localhost:3000) from the browser. If you have issues with the deployment of this container, please use [the publicly available demo instance](https://www.threatdragon.com).
2. Create a new, empty threat model.
3. Fill in the details of the threat model.
4. Create a new STRIDE diagram.
5. Save the details of the threat model and start editing the STRIDE diagram.
6. Use processes, stores, actors, and data flows from the left panel to model the behavior of Sand Castle. You can use [the architectural diagram](/sandcastle#architecture) as a starting point.
7. Use the specific elements from the left panel to draw the trust boundaries.
8. For each component of the threat model, identify what actions an attacker can take to damage the security of Sand Castle.
9. For each identified threat, create a new entry by selecting the affected component and using the bottom-left panel to enter its details.

<DefaultSolution>

Starting from the components illustrated in [the Architecture page](/sandcastle#architecture), OWASP Threat Dragon and the STRIDE model were used to identify threats. They are grouped below by the functionality that enables them.

![Export from OWASP Threat Dragon](/img/threat-model.png)

### Identified threats

:::note

The list of threats is not exhaustive. Please see [the contribution guide](https://github.com/iosifache/ossfortress/blob/main/CONTRIBUTING.md) to propose new threats.

:::

#### Image format conversion

- DoS with large images: An attacker can upload multiple large images, which are heavily processed by the server to obtain the converted image, leading to a denial of service.
- Unrestricted storage location: An attacker can upload its image to an arbitrary location.
- Unrestricted file type upload: An attacker can upload any file type, leading to undefined behaviour.

#### Login

- Brute-forcing: An attacker can brute-force the credentials of the server.
- User enumeration via error codes: An attacker can identify the valid usernames by serving the error codes returned by the website when failing to log in.
- Timing attacks: An attacker is able to observe timing differences when validating credentials.

#### User information retrieval

- Unauthorized access to other information: An attacker can access information about other users on the system.

#### Command-based file explorer

- Arbitrary command execution: An attacker can bypass the allow list and execute any command.
- Access to system files or files of other users: An attacker can use the commands to access files which are owned by the system or other users.
- DoS with resource intensive commands: An attacker can execute commands which consume huge amounts of resources, leading to a denial of service.

#### Archive upload

- Unrestricted storage location: An attacker can upload its archives to an arbitrary location.
- Unrestricted file type upload: An attacker can upload any file type, leading to undefined behaviour.
- DoS with large archives or bombs: An attacker can upload multiple large images or a bomb, which are heavily processed by the server or occupy a huge amount of space, leading to a denial of service.

#### Recovery mode

- Token forging: An attacker can forge a valid recovery token.
- Valid token exfiltration: An attacker can extract a valid token of another user.
- User enumeration via error codes: An attacker can identify the valid usernames by serving the error codes returned by the website when failing to log in.

### Exported threat model

The OWASP Threat Dragon model is available under the repository, in [the `others/threat-model.json` JSON file](https://github.com/iosifache/ossfortress/tree/main/others/threat-model.json).

<div className="yt-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/R99il2vnZMQ?si=CuoAp7zl_GzdPAMj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

</DefaultSolution>

