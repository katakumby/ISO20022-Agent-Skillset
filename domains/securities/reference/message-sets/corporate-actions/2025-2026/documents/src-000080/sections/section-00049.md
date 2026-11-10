---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.9 IntermediateSecurity <IntrmdtScty>", "3.4.9.7 ExpiryDate <XpryDt>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.9.7 ExpiryDate <XpryDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
MarketPrice <MktPric> contains the following elements (see "AmountPrice2" on page 831 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 831
   PriceValue <PricVal> [1..1] Amount C1 831
3.4.9.7  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Date on which an order expires or at which a privilege or offer terminates.
ExpiryDate <XpryDt> contains one of the following elements (see "DateFormat30Choice" on page 842
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.9.8  PostingDate <PstngDt>
Presence: [1..1]
Definition: Date of the posting (credit or debit) to the account.
PostingDate <PstngDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.9.9  TradingPeriod <TradgPrd>
Presence: [0..1]
Definition: Period during which intermediate or outturn securities are tradable in a secondary market.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 90 February 2026
```

