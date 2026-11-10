---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["40 reda.020.001.01 SecuritiesAccountStatusAdviceV01"]
file_pages: [2118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 40 reda.020.001.01 SecuritiesAccountStatusAdviceV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2118 to 2118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2118

```text
40 reda.020.001.01
SecuritiesAccountStatusAdviceV01
40.1 MessageDefinition Functionality
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2118 August 2026
```

