---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.075.001.01"]
---

# 8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
8 reda.075.001.01
EligibleSecuritiesDeletionRequestV01
8.1 MessageDefinition Functionality
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
Approved by the Securities SEG on 17 April 2025. reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 51 May 2025
```

