---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.18 DateDetails <DtDtls>"]
file_pages: [437]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.18 DateDetails <DtDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 437 to 437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 437

```text
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
7.4.13.18  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action option.
DateDetails <DtDtls> contains the following CorporateActionDate106 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 437
   CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 438
   ProtectDeadline <PrtctDdln> [0..1] ± 438
   MarketDeadline <MktDdln> [0..1] ± 438
   ResponseDeadline <RspnDdln> [0..1] ± 439
   ExpiryDate <XpryDt> [0..1] ± 439
   SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 440
   DepositoryCoverExpirationDate <DpstryCoverXprtnDt> [0..1] ± 440
   StockLendingDeadline <StockLndgDdln> [0..1] ± 440
   BorrowerStockLendingDeadline
<BrrwrStockLndgDdln>
[0..*]  441
     StockLendingDeadline <StockLndgDdln> [1..1] ± 441
     Borrower <Brrwr> [1..1] ± 441
   DocumentationDeadline <DcmnttnDdln> [0..1] ± 441
7.4.13.18.1  EarlyResponseDeadline <EarlyRspnDdln>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 437 February 2026
```

