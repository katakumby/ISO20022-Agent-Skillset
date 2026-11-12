---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["5 reda.009.001.01 SecurityActivityAdviceV01"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 5 reda.009.001.01 SecurityActivityAdviceV01

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
5 reda.009.001.01
SecurityActivityAdviceV01
5.1 MessageDefinition Functionality
The SecurityActivityReport message is sent by the executing party to an instructing party containing
information about changes on securities reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities reference data.
Outline
The SecurityActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecurityActivity
Activity report of changes occurred for a financial instrument defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 71 March 2024
```

