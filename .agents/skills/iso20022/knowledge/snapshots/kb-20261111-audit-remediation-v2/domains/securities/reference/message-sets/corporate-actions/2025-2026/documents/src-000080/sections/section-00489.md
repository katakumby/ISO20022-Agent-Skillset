---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.11 DateDetails <DtDtls>"]
file_pages: [648]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.11 DateDetails <DtDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 648 to 648.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 648

```text
8.4.12.11.11  DateDetails <DtDtls>
Presence: [1..1]
Definition: Provides information about the dates related to a cash movement.
DateDetails <DtDtls> contains the following CorporateActionDate99 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostingDate <PstngDt> [1..1] ± 648
   ValueDate <ValDt> [0..1] Date 648
   ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 648
   EarliestPaymentDate <EarlstPmtDt> [0..1] Date 648
   PaymentDate <PmtDt> [0..1] Date 649
8.4.12.11.11.1  PostingDate <PstngDt>
Presence: [1..1]
Definition: Date/time of the posting (credit or debit) to the account.
PostingDate <PstngDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
8.4.12.11.11.2  ValueDate <ValDt>
Presence: [0..1]
Definition: Date/time when calculating economic benefit for a cash amount.
Datatype: "ISODate" on page 1243
8.4.12.11.11.3  ForeignExchangeRateFixingDate <FXRateFxgDt>
Presence: [0..1]
Definition: Date/time at which a foreign exchange rate will be determined.
ForeignExchangeRateFixingDate <FXRateFxgDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
8.4.12.11.11.4  EarliestPaymentDate <EarlstPmtDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 648 February 2026
```

