---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01", "reda.075.001.01", "reda.077.001.01"]
---

# 1 Message Set Overview

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Collateral Management Reference Data message
set. It includes the new collateral management reference data MessageDefinitions that have been
developed in the scope of the Target2-Securities Business Justification (See BJ#042) and approved by
the Securities SEG on 17 April 2025. 
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
reda.024.001.01
CollateralValueCreationRequestV01
The CollateralValueCreationRequest message is sent
by the instructing party to the executing party to
request for the creation of a collateral value in the
executing system collateral management reference
data.
Usage:
It aims at instructing the creation of a new collateral
value with corresponding details.
Processing and confirmation of the collateral value
creation request message are provided via a collateral
management status advice.
reda.025.001.01
EligibleSecuritiesCreationRequestV01
The EligibleSecuritiesCreationRequest message is
exchanged between an instructing party and the
executing party to request for the creation of an eligible
securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the creation of a new eligible
securities with corresponding details.
Processing and confirmation of the eligible securities
creation request message are provided via a collateral
management status advice.
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
The EligibleCounterpartCSDCreationRequest message
is sent by an instructing party to the executing party to
request for the creation of an eligible counterpart CSD
in the executing system collateral management
reference data.
Usage:
It aims at instructing the creation of a new eligible
counterpart CSD with corresponding details.
Processing and confirmation of the eligible counterpart
CSD creation request message are provided via a
collateral management status advice.
reda.027.001.01
CloseLinkCreationRequestV01
The CloseLinkCreationRequest message is sent by an
instructing party to the executing party to request for
Approved by the Securities SEG on 17 April 2025. Message Set Overview
Target2-Securities - Collateral Management Reference Data 4 May 2025
```

## File page 5

```text
MessageDefinition Definition
the creation of a close link in the executing system
collateral management reference data.
Usage:
It aims at instructing the creation of a new close link
with corresponding details.
Processing and confirmation of the close link creation
request message are provided via a collateral
management status advice.
reda.028.001.01
CollateralDataStatusAdviceV01
The CollateralDataStatusAdvice message is sent by
the executing party to an instructing party (the
requestor) to provide information of a request on
collateral management reference data.
Usage:
It aims at informing about the status of the request.
reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
The EligibleCounterpartCSDStatusAdvice message is
sent by the executing party to an instructing party (the
requestor) to provide information for a request on
eligible counterpart CSD reference data.
Usage:
It aims at informing about the status of the request.
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
The EligibleSecuritiesDeletionRequest message is
exchanged between an instructing party and the
executing party to request for the deletion of an eligible
securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the deletion of a existing eligible
securities with corresponding details.
Processing and confirmation of the eligible securities
deletion request message are provided via a collateral
management status advice.
reda.077.001.01
CloseLinkDeletionRequestV01
The CloseLinkDeletionRequest message is sent by an
instructing party to the executing party to request for
the deletion of a close link in the executing system
collateral management reference data.
Usage:
It aims at instructing the deletion of an existing close
link with corresponding details.
Processing and confirmation of the close link creation
request message are provided via a collateral
management status advice.
Approved by the Securities SEG on 17 April 2025. Message Set Overview
Target2-Securities - Collateral Management Reference Data 5 May 2025
```

