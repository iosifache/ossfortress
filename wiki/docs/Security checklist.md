---
sidebar_position: 14
slug: checklist
---

<!-- Keep this content syced with presentation/project.md. -->

:::note

One-time activities are marked with ☑️, and the recurrent ones with 🔁.

:::

## I. Proactive vulnerability discovery

☑️ Create a threat model. <br/>
☑️ Choose a suite of security tools to scan your codebase. <br/>
☑️ Automate the suite of security tools in local/development environments and CI/CD pipelines, with quality gates. <br/>
☑️ Request the integration of your project with OSS-Fuzz. <br/>
🔁 Periodically check for vulnerabilities in your dependencies. <br/>
🔁 Constantly validate the warnings from your security tooling. <br/>
🔁 Keep the threat model updated.

## II. Secure users

☑️ Design your software to be secure by default. <br/>
☑️ Have security recommendations for users. <br/>
☑️ Create SBOMs.

## III. Established security reporting process

☑️ Have a standardised, documented process for responding to vulnerabilities. <br/>
☑️ Create a security policy with preferred way to contact and report format. <br/>
☑️ Find backup security responders. <br/>
🔁 Be transparent and verbose with the reported vulnerabilities: mention patching commits, attach security tags to issues, and request CVE IDs.
