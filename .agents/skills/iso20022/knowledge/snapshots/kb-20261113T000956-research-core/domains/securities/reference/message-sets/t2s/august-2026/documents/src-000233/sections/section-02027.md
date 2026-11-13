---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01"]
file_pages: [2761]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2761 to 2761.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2761

```text
81 semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
81.1 MessageDefinition Functionality
The SecuritiesTransactionPenaltiesReport V01 message is sent by the Executing/Servicing Party to the
instructing party to inform about the cash penalties:
- Newly computed cash penalties. For example, in case of a CSD, the information shall include the cash
penalties that are either imposed or credited to all of its participants and the CSD itself; in case of a
CSD participant, the information shall include the cash penalties that are either imposed or credited to
the CSD participant itself.
- Modified penalties: to inform about the modifications occurred in existing cash penalties since the
previous reporting.
- Aggregated amounts of cash penalties: to inform about the aggregated amounts of the cash penalties
computed for the business days of a given period, for example the previous month.
Outline
The SecuritiesTransactionPenaltiesReportV01 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. ReportPagination
Provides details on the page number of the report.
Usage: The pagination of the report is only allowed when agreed between the parties.
B. ReportGeneralDetails
Provides general information on the report.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. AccountOwner
Party that legally owns the account.
E. AccountServicer
Party that manages the sub-level account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. Penalty
Claims (penalties) in a currency and of a date reported for a given party.
If there are no penalties in a given currency for a party, this block will not be informed.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2761 August 2026
```

