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
file_pages: [2579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# Continuation at file page 2579

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2579 to 2579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2579

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 2689
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2690
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2690
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2690
       ISIN <ISIN> [0..1] IdentifierSet 2692
       OtherIdentification <OthrId> [0..*]  2692
         Identification <Id> [1..1] Text 2692
         Suffix <Sfx> [0..1] Text 2692
         Type <Tp> [1..1]  2692
{Or           Code <Cd> [1..1] CodeSet 2693
Or}           Proprietary <Prtry> [1..1] Text 2694
       Description <Desc> [0..1] Text 2694
     Quantity <Qty> [1..1]  2695
{Or       Quantity <Qty> [1..1] ± C15 2695
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2695
         Quantity <Qty> [1..1] Quantity 2696
         QuantityType <QtyTp> [1..1] Text 2696
         Issuer <Issr> [1..1] Text 2696
         SchemeName <SchmeNm> [0..1] Text 2696
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2696
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 2696
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 2696
   FinancialAdvice <FinAdvc> [0..1] CodeSet 2697
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2697
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2697
   Equalisation <Equlstn> [0..1] ± 2698
   SourceOfCash <SrcOfCsh> [0..*] ± 2698
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2698
   TransactionChannelType <TxChanlTp> [0..1] ± 2699
   SignatureType <SgntrTp> [0..1] ± 2699
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2579 May 2026
```

