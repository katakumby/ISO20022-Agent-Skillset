---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["65 reda.049.001.01 AccountLinkCreationRequestV01"]
file_pages: [2369]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 65 reda.049.001.01 AccountLinkCreationRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2369 to 2369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2369

```text
65 reda.049.001.01
AccountLinkCreationRequestV01
65.1 MessageDefinition Functionality
SCOPE:
The AccountLinkCreationRequest message is sent by the instructing party to the executing/servicing
party to request the creation of an account link between a securities account and a cash account in their
system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be set-up at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkCreationRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLink
Defines how the securities account is linked to the cash account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2369 August 2026
```

