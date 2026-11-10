---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01"]
file_pages: [2389]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.075.001.01"]
---

# 68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2389 to 2389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2389

```text
68 reda.075.001.01
EligibleSecuritiesDeletionRequestV01
68.1 MessageDefinition Functionality
The EligibleSecuritiesDeletionRequest message is exchanged between an instructing party and the
executing party to request for the deletion of an eligible securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the deletion of a existing eligible securities with corresponding details.
Processing and confirmation of the eligible securities deletion request message are provided via a
collateral management status advice.
Outline
The EligibleSecuritiesDeletionRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. EligibleSecurity
Represents securities defined eligible for auto-collateralisation.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities 2389 August 2026
```

