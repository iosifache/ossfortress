---
sidebar_position: 2
slug: owasp-threat-dragon
---

## Creating a threat model

1. Access [your local OWASP Threat Dragon user interface](http://localhost:3000) from the browser. If you have issues with the deployment of this container, please use [the publicly available demo instance](https://www.threatdragon.com).
2. Create a new, empty threat model.
3. Fill in the details of the threat model.
4. Create a new STRIDE diagram.
5. Save the details of the threat model and start editing the STRIDE diagram.
6. Use processes, stores, actors, and data flows from the left panel to model the behavior of Ubuntu Portrait. You can use [the architectural diagram](/ubuntu-portrait/architecture) as a starting point.
7. Use the specific elements from the left panel to draw the trust boundaries.
8. For each component of the threat model, identify what actions an attacker can take to damage the security of Ubuntu Portrait.
9. For each identified threat, create a new entry by selecting the affected component and using the bottom-left panel to enter its details.