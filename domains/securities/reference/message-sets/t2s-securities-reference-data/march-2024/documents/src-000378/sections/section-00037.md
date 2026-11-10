---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01"]
file_pages: [77]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6 reda.010.001.01 SecurityQueryV01

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 77 to 77.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
6 reda.010.001.01
SecurityQueryV01
6.1 MessageDefinition Functionality
SCOPE
An instructing party sends a SecurityQuery message to an executing/servicing party to request a report
of financial instrument details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party needs to see data of a security data within the executing/
servicing party system.
Initiator: instructing party.
Outline
The SecurityQueryV01 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. RequestType
Defines the type of action to be performed in the request.
C. SearchCriteria
Defines the criteria to be used to query the securities reference data by the executing system.
D. SmallSetReturnCriteria
Defines the expected securities reference data to be returned.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 77 March 2024
```

