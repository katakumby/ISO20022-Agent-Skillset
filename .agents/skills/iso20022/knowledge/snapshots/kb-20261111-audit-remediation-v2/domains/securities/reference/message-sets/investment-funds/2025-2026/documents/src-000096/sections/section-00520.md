---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.6 RequestedSettlementDate <ReqdSttlmDt>"]
file_pages: [714]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.6 RequestedSettlementDate <ReqdSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 714 to 714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 714

```text
30.4.7.6  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be exchanged at the International Central
Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
30.4.7.7  EffectiveTransferDate <FctvTrfDt>
Presence: [1..1]
Definition: Date and time at which the transfer was executed.
EffectiveTransferDate <FctvTrfDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
30.4.7.8  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities were exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
30.4.7.9  TradeDate <TradDt>
Presence: [0..1]
Definition: Date and time at which the transaction is completed and cleared, that is, securities are
delivered.
TradeDate <TradDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
30.4.7.10  TransferOrderDateForm <TrfOrdrDtForm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 714 May 2026
```

