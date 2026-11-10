---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["8 reda.035.001.01 SecuritiesAccountActivityAdviceV01"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 8 reda.035.001.01 SecuritiesAccountActivityAdviceV01

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
8 reda.035.001.01
SecuritiesAccountActivityAdviceV01
8.1 MessageDefinition Functionality
The SecuritieAccountActivityReport message is sent by the executing party to an instructing party
containing information about changes on securities account reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities account reference
data.
Outline
The SecuritiesAccountActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecuritiesAccountActivity
Activity report of changes occurred for a specific securities account defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities - Securities Account Reference Data 59 December 2019
```

