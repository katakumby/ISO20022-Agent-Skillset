---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.14 Status"]
file_pages: [414]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.14 Status

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 414 to 414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
22.1.14 Status
22.1.14.1  DebtInstrument4
Definition: Specifies the debit instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaturityDate <MtrtyDt> [1..1] Date 414
22.1.14.1.1  MaturityDate <MtrtyDt>
Presence: [1..1]
Definition: Maturity date/time at which an interest bearing financial instrument becomes due, that is
original date of expiry of the reported financial instrument.
Datatype: "ISODate" on page 449
22.1.14.2  DebtInstrument5
Definition: Specifies the debit instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 414
   IssuanceDate <IssncDt> [1..1] Date 414
22.1.14.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of bond type.
Datatype: "BondType1Code" on page 434
CodeName Name Definition
EUSB SovereignBond Bond of type sovereign bond.
OEPB OtherPublicBond Bond of type other public bond.
CVTB ConvertibleBond Bond of type convertible bond.
CRPB CorporateBond Bond of type corporate Bond.
CVDB CoveredBond Bond of type covered Bond.
OTHR Other Other bond type.
22.1.14.2.2  IssuanceDate <IssncDt>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
414 July 2025
```

