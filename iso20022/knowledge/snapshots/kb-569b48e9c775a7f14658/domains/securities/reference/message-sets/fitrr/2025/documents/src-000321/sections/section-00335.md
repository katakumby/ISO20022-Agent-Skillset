---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.10 InvestmentDecisionPerson <InvstmtDcsnPrsn>", "22.1.13.2.10.2 Algorithm <Algo>"]
file_pages: [389]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.10.2 Algorithm <Algo>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 389 to 389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
Person <Prsn> contains the following elements (see "PersonIdentification12" on page 345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CountryOfBranch <CtryOfBrnch> [1..1] CodeSet C4 346
   Other <Othr> [1..1]  346
     Identification <Id> [1..1] Text 346
     SchemeName <SchmeNm> [0..1]  347
{Or       Code <Cd> [1..1] CodeSet 347
Or}       Proprietary <Prtry> [1..1] Text 347
     Issuer <Issr> [0..1] Text 347
22.1.13.2.10.2  Algorithm <Algo>
Presence: [1..1]
Definition: Identification of an algorithm.
Datatype: "Max50Text" on page 456
22.1.13.2.11  ExecutingPerson <ExctgPrsn>
Presence: [1..1]
Definition: Person or algorithm responsible for the execution of the transaction.
ExecutingPerson <ExctgPrsn> contains one of the following ExecutingParty1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Person <Prsn> [1..1] ± 389
Or   Algorithm <Algo> [1..1] Text 390
Or}   Client <Clnt> [1..1] CodeSet 390
22.1.13.2.11.1  Person <Prsn>
Presence: [1..1]
Definition: Identification of a person.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
389 July 2025
```

