<!-- Keep this content syced with wiki/docs/index.mdx. -->

<p align="center">
    <img src="others/logo.png" height="256" alt="The Open Source Fortress logo"/>
</p>
<h3 align="center">The Open Source Fortress</h3>
<p align="center" float="left">
    <a href="https://github.com/iosifache/ossfortress/packages">
      <img src="https://img.shields.io/badge/Docker_images-GHCR-blue?logo=docker" height="17" alt="Docker image: GHCR"/>
    </a>
    &nbsp; &nbsp;
    <a href="https://ossfortress.io/">
      <img src="https://img.shields.io/badge/Documentation-available-green?logo=docusaurus" height="17" alt="Documentation: available"/>
    </a>
</p>

## Context

Regardless of where it is hosted, a codebase could end up in the hands of malicious actors. Aside from the open source scenario, attackers may utilize sophisticated techniques to access and download it. Okta's 2022 breach, in which the source code of the identity and access management platform was obtained from GitHub, is an example.

With this in mind, developers are advised to take a defensive posture, namely to uncover as many flaws in their code as possible before releasing it to the public.

## The Open Source Fortress

The workshop, named "The Open Source Fortress", provides both theoretical and practical information about **detecting vulnerabilities in codebases**. It explains how each technique works, what open source tools are available, and then provides real examples.

> [!CAUTION]
> If you just want to start solving the workshop without further details, visit [this wiki page with instructions](https://ossfortress.io/guide).

### Sand Castle

The examples imply the discovery of vulnerabilities in a custom, purposefully vulnerable codebase named Sand Castle. It is written in C and Python.

The included techniques are:
- Threat modelling;
- Secret scanning;
- Dependency scanning;
- Linting;
- Code querying;
- Symbolic execution; and
- Fuzzing.

### Wiki

[The wiki](https://ossfortress.io/) includes all the information required to complete the workshop (eventually on your own) and learn more about the provided vulnerable application and analysis infrastructure.

### Repository

[The repository](https://github.com/iosifache/ossfortress) hosts all sources related to The Open Source Fortress, starting from presentations used in talks to source code and Docker images. Its structure is as follows:

```
.
├── sandcastle/            Source code for and Castle
├── tooling/               Docker images for all analysis tooling
├── analysis/              Empty folder that will hold files producedduring the
|                          analysis
├── docker-compose.yaml    Docker intrastructure deploying Sand Castle and the
|                          required analysis tooling
├── wiki/                  Source code of the wiki
├── presentations/         Presentations used when hosting talks and workshops
|                          related to The Open Source Fortress
├── others/                Miscelleneous files, including the logo and diagrams
├── README.md              This page/file
├── CONTRIBUTING.md        Guide on how to contribute to improving this workshop
└── LICENSE                License file
```

## On-site presentations

The Open Source Fortress was hosted multiple times in public setups as:

- Talk, in which the concepts presented in the workshop were summarised and demos showcasing the open-source tools were recorded;
- Workshop, with both theoretical and practical components; and
- CTF challenge, in which the players were required to patch the vulnerabilities included in Sand Castle.

You can use the resources (e.g., slides and recordings) from each as a supplement to the recommended talks and effectively solving the workshop.

| Event                                                                                                           | Showcase date | Showcase form | Duration   | References                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------- | ------------- | ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Opportunity Open Source Conference](https://events.canonical.com/event/89/overview), an OSS-focused conference | August 2024   | Talk          | 40 minutes | [Slides](https://raw.githubusercontent.com/iosifache/ossfortress/main/presentations/oosc-24/export.pdf) and [talk page](https://events.canonical.com/event/89/contributions/476/)                                                                                        |
| [AppSec Village](https://www.appsecvillage.com) at [DEFCON](https://defcon.org), an appsec conference           | August 2024   | Workshop      | 2.5 hours  | [Slides](https://raw.githubusercontent.com/iosifache/ossfortress/main/presentations/defcon-24/export.pdf) and [talk page](https://www.appsecvillage.com/events/dc-2024/the-open-source-fortress-finding-vulnerabilities-in-your-codebase-using-open-source-tools-677630) |
| [SCaLE 21x](https://www.socallinuxexpo.org/scale/21x), an open source community                                 | March 2024    | Talk          | 1 hour     | [Talk page](https://www.socallinuxexpo.org/scale/21x/presentations/open-source-fortress) and [recording](https://www.youtube.com/watch?v=7egfj6voGcI)                                                                                                                    |
| [Ubuntu Summit](https://events.canonical.com/event/31), a community conference                                  | November 2023 | Workshop      | 1.5 hours  | [Slides](https://raw.githubusercontent.com/iosifache/ossfortress/main/presentations/ubuntu-summit-23/export.pdf) and [talk page](https://events.canonical.com/event/31/contributions/219)                                                                                |
| [DefCamp](https://def.camp/speaker), a cybersecurity conference                                                 | November 2023 | Talk          | 30 minutes | [Slides](https://ossfortress.io/defcamp), [talk page](https://def.camp/speaker/george-andrei-iosif-2), and [recording](https://www.youtube.com/watch?v=EqWcojnXrCE)                                                                                                      |
| Canonical lightning talk                                                                                        | November 2023 | Talk          | 5 minutes  | [Slides](https://raw.githubusercontent.com/iosifache/ossfortress/main/presentations/lightning-talk-23/export.pdf)                                                                                                                                                        |
| UbuCTF, a CTF organised by the [Ubuntu Security Team](https://wiki.ubuntu.com/SecurityTeam)                     | November 2023 | CTF challenge | 2 days     | [Podcast mention](https://ubuntusecuritypodcast.org/episode-213/)                                                                                                                                                                                                        |

## Contributing

Please check repo's [`CONTRIBUTING.md`](https://github.com/iosifache/ossfortress/blob/main/CONTRIBUTING.md) for further information on how you can help!

## Acknowledgements

Previous works, such as [Juice Shop](https://owasp.org/www-project-juice-shop), [WebGoat](https://github.com/WebGoat/WebGoat) and [WrongSecrets](https://owasp.org/www-project-juice-shop), inspired this workshop.

This project's logo was created with [Adobe Firefly](https://firefly.adobe.com).
