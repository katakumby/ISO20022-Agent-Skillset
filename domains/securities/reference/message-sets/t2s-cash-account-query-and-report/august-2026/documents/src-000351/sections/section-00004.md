---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02"]
file_pages: [4]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2 acmt.025.001.02 AccountQueryListV02

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 4 to 4.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
2 acmt.025.001.02
AccountQueryListV02
2.1 MessageDefinition Functionality
This message is a query message with specification of requested accounts, and requested
characteristics.
Outline
The AccountQueryListV02 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. References
Set of elements for the identification of the message and related references.
B. From
Identifies the business sender of the message, if it is not the account owner or account servicing
financial institution.
C. AccountServicerIdentification
Unique and unambiguous identifier of a financial institution, as assigned under an internationally
recognised or proprietary identification scheme.
.
D. Organisation
Organised structure that is set up for a particular purpose, for example, a business, government
body, department, charity, or financial institution.
E. AccountSearchCriteria
Contains the criteria that must be used to select the requested accounts.
F. AccountReturnCriteria
Contains the characteristics of the selected accounts that must be returned.
G. DigitalSignature
Contains the signature with its components, namely signed info, signature value, key info and the
object.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 4 August 2026
```

