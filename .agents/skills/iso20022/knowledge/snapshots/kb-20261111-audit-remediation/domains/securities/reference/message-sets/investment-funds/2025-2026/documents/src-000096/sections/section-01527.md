---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [2148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# Continuation at file page 2148

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2148 to 2148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2148

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Quantity <Qty> [1..1] ± C15 2254
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2254
         Quantity <Qty> [1..1] Quantity 2255
         QuantityType <QtyTp> [1..1] Text 2255
         Issuer <Issr> [1..1] Text 2255
         SchemeName <SchmeNm> [0..1] Text 2255
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2255
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 2255
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 2255
   FinancialAdvice <FinAdvc> [0..1] CodeSet 2256
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2256
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2256
   Equalisation <Equlstn> [0..1] ± 2257
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2257
   TransactionChannelType <TxChanlTp> [0..1] ± 2257
   SignatureType <SgntrTp> [0..1] ± 2258
   OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C39 2258
Constraints
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Following Must be True
    /PhysicalDeliveryDetails Must be absent
• PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'true'
 Or    /PhysicalDeliveryIndicator is equal to value '1'
Following Must be True
    /PhysicalDeliveryDetails Must be present
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in SettlementAmount, if
present.
On Condition
    /RequestedSettlementCurrency is present
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2148 May 2026
```

