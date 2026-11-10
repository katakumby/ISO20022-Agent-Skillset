---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.12 DateDetails <DtDtls>", "3.4.11.25.12.2 ValueDate <ValDt>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.12.2 ValueDate <ValDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
PaymentDate <PmtDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.11.25.12.2  ValueDate <ValDt>
Presence: [0..1]
Definition: Date/time when calculating economic benefit for a cash amount.
ValueDate <ValDt> contains one of the following elements (see "DateFormat57Choice" on page 844
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 845
Or}   DateCode <DtCd> [1..1]  845
{Or     Code <Cd> [1..1] CodeSet 845
Or}     Proprietary <Prtry> [1..1] ± 845
3.4.11.25.12.3  ForeignExchangeRateFixingDate <FXRateFxgDt>
Presence: [0..1]
Definition: Date/time at which a foreign exchange rate will be determined.
ForeignExchangeRateFixingDate <FXRateFxgDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.25.12.4  EarliestPaymentDate <EarlstPmtDt>
Presence: [0..1]
Definition: Date/time on which a payment can be made, for example, if payment date is a non-business
day or to indicate the first payment date of an offer.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 232 February 2026
```

