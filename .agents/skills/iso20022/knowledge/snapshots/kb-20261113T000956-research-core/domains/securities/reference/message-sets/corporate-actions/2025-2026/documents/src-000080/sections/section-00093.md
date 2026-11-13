---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.19 DateDetails <DtDtls>", "3.4.11.19.1 EarlyResponseDeadline <EarlyRspnDdln>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.19.1 EarlyResponseDeadline <EarlyRspnDdln>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
DateDetails <DtDtls> contains the following CorporateActionDate110 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 148
   CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 148
   ProtectDeadline <PrtctDdln> [0..1] ± 149
   MarketDeadline <MktDdln> [0..1] ± 149
   ResponseDeadline <RspnDdln> [0..1] ± 149
   ExpiryDate <XpryDt> [0..1] ± 150
   SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 150
   DepositoryCoverExpirationDate <DpstryCoverXprtnDt> [0..1] ± 151
   StockLendingDeadline <StockLndgDdln> [0..1] ± 151
   BorrowerStockLendingDeadline
<BrrwrStockLndgDdln>
[0..*]  151
     StockLendingDeadline <StockLndgDdln> [1..1] ± 151
     Borrower <Brrwr> [1..1] ± 152
   EndOfSecuritiesBlockingPeriod
<EndOfSctiesBlckgPrd>
[0..1] ± 152
   DocumentationDeadline <DcmnttnDdln> [0..1] ± 152
3.4.11.19.1  EarlyResponseDeadline <EarlyRspnDdln>
Presence: [0..1]
Definition: Date/time that the account servicer has set as the deadline to respond, with instructions, to
an outstanding event, giving the holder eligibility to incentives.
EarlyResponseDeadline <EarlyRspnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.2  CoverExpirationDeadline <CoverXprtnDdln>
Presence: [0..1]
Definition: Last day a holder can deliver the securities that it had elected on and/or previously protected.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 148 February 2026
```

