---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.16 DateDetails <DtDtls>", "3.4.11.24.16.1 PaymentDate <PmtDt>"]
file_pages: [189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.16.1 PaymentDate <PmtDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 189 to 189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 189

```text
DateDetails <DtDtls> contains the following SecurityDate20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentDate <PmtDt> [1..1] ± 189
   AvailableDate <AvlblDt> [0..1] ± 189
   DividendRankingDate <DvddRnkgDt> [0..1] ± 189
   EarliestPaymentDate <EarlstPmtDt> [0..1] ± 190
   PariPassuDate <PrpssDt> [0..1] ± 190
   LastTradingDate <LastTradgDt> [0..1] ± 190
3.4.11.24.16.1  PaymentDate <PmtDt>
Presence: [1..1]
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
3.4.11.24.16.2  AvailableDate <AvlblDt>
Presence: [0..1]
Definition: Date/time at which securities become available for trading, for example first dealing date.
AvailableDate <AvlblDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.11.24.16.3  DividendRankingDate <DvddRnkgDt>
Presence: [0..1]
Definition: Date/time at which a security will be entitled to a dividend.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 189 February 2026
```

