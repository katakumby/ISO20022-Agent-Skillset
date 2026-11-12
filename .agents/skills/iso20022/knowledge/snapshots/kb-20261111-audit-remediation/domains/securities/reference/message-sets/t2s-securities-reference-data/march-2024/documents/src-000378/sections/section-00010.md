---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["3 reda.007.001.01 SecurityMaintenanceRequestV01"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 3 reda.007.001.01 SecurityMaintenanceRequestV01

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
3 reda.007.001.01
SecurityMaintenanceRequestV01
3.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityMaintenanceRequest message to an executing/servicing party to
request the maintenance of financial instrument details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security data within the executing/
servicing party system. The instructing party needs this security to be updated at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityMaintenanceRequestV01 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. UpdateType
Request to maintain data's of a security.
C. UpdateReason
Reason for the update of a security.
D. FinancialInstrumentIdentification
Identification of the financial instrument.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 21 March 2024
```

