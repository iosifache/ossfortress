<p align="center">
    <img src="others/logo.png" height="256" alt="The Open Source Fortress logo"/>
</p>
<h2 align="center">The Open Source Fortress</h2>
<p align="center" float="left">
    <a href="https://github.com/iosifache/oss_fortress/packages">
      <img src="https://img.shields.io/badge/Docker_images-GHCR-blue?logo=docker" height="17" alt="Docker image: GHCR"/>
    </a>
    &nbsp; &nbsp;
    <a href="https://ossfortress.io/">
      <img src="https://img.shields.io/badge/Documentation-available-green?logo=docusaurus" height="17" alt="Documentation: available"/>
    </a>
</p>

<!-- Keep this content syced with wiki/docs/index.md. -->

## Context

Regardless of where it is hosted, a codebase could end up in the hands of malicious actors. Aside from the open source scenario, attackers may utilize sophisticated techniques to access and download it. Okta's 2022 breach, in which the source code of the identity and access management platform was obtained from GitHub, is an example.

With this in mind, developers are advised to take a defensive posture, namely to uncover as many flaws in their code as possible before releasing it to the public.

## The Open Source Fortress

The workshop, named The Open Source Fortress, provides both theoretical and practical information about **detecting vulnerabilities in codebases**. It explains how each technique works, what open source tools are available, and then provides real examples.

The examples imply the discovery of vulnerabilities in a custom, purposefully vulnerable codebase named **Sand Castle**. It is written in C and Python.

The **included techniques** are:
- Threat modelling;
- Secret scanning;
- Dependency scanning;
- Linting;
- Code querying;
- Symbolic execution; and
- Fuzzing.

## Wiki

Please visit the [wiki](https://ossfortress.io/) if you want to complete the workshop on your own and learn more about the provided vulnerable application.

## Showcases

<!-- Keep this synced with index.mdx -->

| Event                                                                                       | Showcase date | Showcase form                                                                                         | References                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Ubuntu Summit](https://events.canonical.com/event/31), a community conference              | November 2023 | Entire workshop, with both theoretical and practical components                                       | [Slides](https://raw.githubusercontent.com/iosifache/oss_fortress/main/presentation/ubuntu-summit-23/export.pdf) and [talk page](https://events.canonical.com/event/31/contributions/219) |
| [DefCamp](https://def.camp/speaker), a cybersecurity conference                             | November 2023 | Talk summarizing the concepts presented in the workshop and containing demos of the recommended tools | [Slides](https://ossfortress.io/defcamp) and [talk page](https://def.camp/speaker/george-andrei-iosif-2)                                                                                  |
| Canonical lightning talk                                                                    | November 2023 | 5-minute pitch of the workshop                                                                        | [Slides](https://raw.githubusercontent.com/iosifache/oss_fortress/main/presentation/lightning-talk-23/export.pdf)                                                                         |
| UbuCTF, a CTF organised by the [Ubuntu Security Team](https://wiki.ubuntu.com/SecurityTeam) | November 2023 | CTF challenge in which the players had to patch the vulnerabilities                                   |                                                                                                                                                                                           |

## Contributing

Please check [`CONTRIBUTING.md`](/CONTRIBUTING.md) for further information on how you can help!

## Acknowledgements

Previous works, such as [Juice Shop](https://owasp.org/www-project-juice-shop), [WebGoat](https://github.com/WebGoat/WebGoat) and [WrongSecrets](https://owasp.org/www-project-juice-shop), inspired this workshop.

This project's logo was created with [Adobe Firefly](https://firefly.adobe.com).
