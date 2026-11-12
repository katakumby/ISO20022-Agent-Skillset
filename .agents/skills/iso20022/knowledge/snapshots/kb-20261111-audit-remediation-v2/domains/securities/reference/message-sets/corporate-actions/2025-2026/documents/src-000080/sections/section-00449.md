---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.14 DateDetails <DtDtls>", "8.4.12.10.14.5 EarliestPaymentDate <EarlstPmtDt>"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.14.5 EarliestPaymentDate <EarlstPmtDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
DividendRankingDate <DvddRnkgDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
8.4.12.10.14.5  EarliestPaymentDate <EarlstPmtDt>
Presence: [0..1]
Definition: Date/time at which a payment can be made, for example, if payment date is a non-business
day or to indicate the first payment date of an offer.
EarliestPaymentDate <EarlstPmtDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
8.4.12.10.14.6  PaymentDate <PmtDt>
Presence: [0..1]
Definition: Date/time at which the movement is due to take place (cash and/or securities).
PaymentDate <PmtDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
8.4.12.10.15  RateDetails <RateDtls>
Presence: [0..1]
Definition: Provides information about the rates related to securities movement.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 603 February 2026
```

