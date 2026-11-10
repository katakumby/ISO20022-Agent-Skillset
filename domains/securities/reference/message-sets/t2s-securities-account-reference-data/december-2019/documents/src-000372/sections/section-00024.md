---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["4 reda.020.001.01 SecuritiesAccountStatusAdviceV01"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 4 reda.020.001.01 SecuritiesAccountStatusAdviceV01

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
4 reda.020.001.01
SecuritiesAccountStatusAdviceV01
4.1 MessageDefinition Functionality
The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party
to provide the status of the execution of an creation, modification or deletion of securities account
reference data.
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is succesfully performed, the message includes the related securities account
identification.
Outline
The SecuritiesAccountStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecuritiesAccountStatus
Status of the securities account involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 26 December 2019
```

