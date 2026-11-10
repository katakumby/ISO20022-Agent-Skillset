---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.5 Buyer <Buyr>"]
file_pages: [370]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.5 Buyer <Buyr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 370 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
Definition: Entity submitting the transaction report to the competent authority.
Datatype: "LEIIdentifier" on page 451
22.1.13.2.5  Buyer <Buyr>
Presence: [1..1]
Definition: Identifies the acquirer of the legal title to the financial instrument.
Buyer <Buyr> contains the following elements (see "PartyIdentification79" on page 344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [1..*] ± 344
   DecisionMaker <DcsnMakr> [0..*]  345
{Or     LEI <LEI> [1..1] IdentifierSet 345
Or}     Person <Prsn> [1..1] ± 345
22.1.13.2.6  Seller <Sellr>
Presence: [1..1]
Definition: Identifies the seller of the legal title to the financial instrument.
Seller <Sellr> contains the following elements (see "PartyIdentification79" on page 344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [1..*] ± 344
   DecisionMaker <DcsnMakr> [0..*]  345
{Or     LEI <LEI> [1..1] IdentifierSet 345
Or}     Person <Prsn> [1..1] ± 345
22.1.13.2.7  OrderTransmission <OrdrTrnsmssn>
Presence: [1..1]
Definition: Indication as to whether the transaction results from an order transmitted by the reporting of
a client to a third party.
Usage: Only applicable when the conditions for transmission are not satisfied.
OrderTransmission <OrdrTrnsmssn> contains the following SecuritiesTransactionTransmission2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransmissionIndicator <TrnsmssnInd> [1..1] Indicator 371
   TransmittingBuyer <TrnsmttgBuyr> [0..1] IdentifierSet 371
   TransmittingSeller <TrnsmttgSellr> [0..1] IdentifierSet 371
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
370 July 2025
```

