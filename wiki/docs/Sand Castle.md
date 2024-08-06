---
sidebar_position: 5
slug: sandcastle
---

import {WebSetup} from '@site/src/components/Setup';

<WebSetup software="Sand Castle" profile="sandcastle" link="http://127.0.0.1:8000" credentials="ubuntu:ubuntu"/>

## Description

Sand Castle is a lightweight piece of software that runs on a Debian-based server and allows users to control it through their browsers. Furthermore, it allows anonymous Internet users to profit from a range of free actions, such as changing the format of an image.

## Features

- Logging in with the credentials of the operating system
- Listing details of the user, such as the UID
- Accessing open utilities, which are distributed for free to Internet users
  - Converting the format of an image
- Exploring the file system by running commands from an allow list
- Uploading tar archives to the user's home
- Entering the recovery mode if the credentials were lost

## Architecture

The following C4 diagram shows the application's general architecture:

_![Sand Castle architecture](/img/diagrams/sandcastle.svg)_

## Deployment

It should be deployed on-premise, on each host that wanted to be accessible and (partially) managed via a web interface.

## Demo

:::note

In an August 2024 upgrade, the vulnerable codebase was renamed from **Ubuntu Portrait** to **Sand Castle**. The demos below have not been updated because the old and new features are not substantially different. They will be updated soon.

:::

<div className="yt-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WHi-5XMa2rQ?si=-ypcXb6U1-KECfI9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<br/>

<div className="yt-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/W3CcbnLHf14?si=eTzqxEo9Ub0-vmw3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<br/>

<div className="yt-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/KtqX24IGuRU?si=1lPJEZCUtHc4EZhn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
