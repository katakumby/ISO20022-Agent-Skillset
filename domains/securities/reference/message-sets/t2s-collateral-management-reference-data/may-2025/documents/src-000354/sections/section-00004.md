---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2 reda.024.001.01 CollateralValueCreationRequestV01

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
2 reda.024.001.01
CollateralValueCreationRequestV01
2.1 MessageDefinition Functionality
The CollateralValueCreationRequest message is sent by the instructing party to the executing party to
request for the creation of a collateral value in the executing system collateral management reference
data.
Usage:
It aims at instructing the creation of a new collateral value with corresponding details.
Processing and confirmation of the collateral value creation request message are provided via a
collateral management status advice.
Outline
The CollateralValueCreationRequestV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CollateralValue
Represents the valuation of securities positions for auto-collateralisation.
C. PartyIdentification
Identifies the party for which the eligible security is defined.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 6 May 2025
```

