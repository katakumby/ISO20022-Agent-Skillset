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
file_pages: [2823]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# Continuation at file page 2823

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2823 to 2823.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2823

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2930
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2930
       ISIN <ISIN> [0..1] IdentifierSet 2932
       OtherIdentification <OthrId> [0..*]  2932
         Identification <Id> [1..1] Text 2932
         Suffix <Sfx> [0..1] Text 2932
         Type <Tp> [1..1]  2932
{Or           Code <Cd> [1..1] CodeSet 2933
Or}           Proprietary <Prtry> [1..1] Text 2934
       Description <Desc> [0..1] Text 2934
     Quantity <Qty> [1..1]  2935
{Or       Quantity <Qty> [1..1] ± C16 2935
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2935
         Quantity <Qty> [1..1] Quantity 2936
         QuantityType <QtyTp> [1..1] Text 2936
         Issuer <Issr> [1..1] Text 2936
         SchemeName <SchmeNm> [0..1] Text 2936
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2936
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 2936
   PartialSettlementOfUnits <PrtlSttlmOfUnits> [0..1] Rate 2936
   FinancialAdvice <FinAdvc> [0..1] CodeSet 2937
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2937
   LateReport <LateRpt> [0..1] CodeSet 2937
   PartialSettlementOfCash <PrtlSttlmOfCsh> [0..1] Rate 2937
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2937
   Equalisation <Equlstn> [0..1] ± 2938
   SourceOfCash <SrcOfCsh> [0..*] ± 2938
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2939
   TransactionChannelType <TxChanlTp> [0..1] ± 2939
   SignatureType <SgntrTp> [0..1] ± 2939
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2823 May 2026
```

