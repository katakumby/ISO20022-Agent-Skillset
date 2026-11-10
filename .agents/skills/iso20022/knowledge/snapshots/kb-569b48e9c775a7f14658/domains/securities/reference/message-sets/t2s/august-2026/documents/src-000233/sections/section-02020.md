---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01"]
file_pages: [2748, 2749]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80 semt.040.001.01 SecuritiesAccountPositionResponseV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2748 to 2749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2748

```text
80 semt.040.001.01
SecuritiesAccountPositionResponseV01
80.1 MessageDefinition Functionality
SCOPE
The SecuritiesAccountPositionResponse message is sent by a market infrastructure to an instructing
party to report the securities positions for the given date period as requested in the query, for all
securities across all accounts satisfying the query criteria.
USAGE
The message SecuritiesAccountPositionResponse will provide CSDs and T2S participants with a report
corresponding to the SecuritiesAccountPositionQuery returning balances held in the list of specified
securities accounts within the specified period satisfying the defined selection criteria. The Securities
Account Position Response will provide the following business attributes:
- CSD
- Account owner
- Securities Account Number
- Securities Identifier (e.g. ISIN)
- Date
- The total position
- The blocked position
- The free position
Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero
securities positions in the accounts.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate)
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy)
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2748 August 2026
```

## File page 2749

```text
Outline
The SecuritiesAccountPositionResponseV01 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. ReportGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Central securities depository where the securities accounts are held.
E. Balances
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
F. PartyBaseCurrencyTotalAmounts
Total valuation amounts provided in the base currency of the party.
G. OtherBusinessParties
Other business parties relevant to the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2749 August 2026
```

