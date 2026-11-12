---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.5 SecuritiesTransactionReport2"]
file_pages: [412]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.5 SecuritiesTransactionReport2

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 412 to 412.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 412

```text
Definition: Date and time of the report originally submitted by the reporting entity when the file is
generated for submission to their reporting authority.
Datatype: "ISODateTime" on page 449
22.1.13.5  SecuritiesTransactionReport2
Definition: Details of the securities transaction report.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 412
   ExecutingParty <ExctgPty> [1..1] IdentifierSet 412
   SubmittingParty <SubmitgPty> [1..1] IdentifierSet 412
   TechnicalAttributes <TechAttrbts> [0..1]  412
     ReceiptDateTime <RctDtTm> [1..1] DateTime 413
     CancellationReason <CxlRsn> [1..1] CodeSet 413
   SupplementaryData <SplmtryData> [0..*] ± C13 413
22.1.13.5.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the transaction.
Datatype: "Max52Text" on page 456
22.1.13.5.2  ExecutingParty <ExctgPty>
Presence: [1..1]
Definition: Identification of the entity executing the transaction.
Usage:
For legal entities, use the legal entity identifier. For non-legal entities, this field shall be populated with
an identifier as specified in the local regulation.
Datatype: "LEIIdentifier" on page 451
22.1.13.5.3  SubmittingParty <SubmitgPty>
Presence: [1..1]
Definition: Entity submitting the transaction report to the competent authority.
Datatype: "LEIIdentifier" on page 451
22.1.13.5.4  TechnicalAttributes <TechAttrbts>
Presence: [0..1]
Definition: Data used for exchanges between national competent authorities, not to be used by
reporting entities.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
412 July 2025
```

