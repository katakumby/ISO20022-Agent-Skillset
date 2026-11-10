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
file_pages: [3302, 3303]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# Continuation at file page 3302

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3302 to 3303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3302

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           LEI <LEI> [0..1] IdentifierSet 3409
         DrawerIdentification <DrwrId> [0..1] ± 3410
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  3410
         Number <Nb> [0..1] Text 3410
         PayeeIdentification <PyeeId> [1..1] ± 3410
         DraweeIdentification <DrweeId> [0..1]  3411
           Party <Pty> [1..1]  3411
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3411
Or             BICFI <BICFI> [1..1] IdentifierSet C7 3412
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3412
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3413
           LEI <LEI> [0..1] IdentifierSet 3413
         DrawerIdentification <DrwrId> [0..1] ± 3414
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 3414
         AccountIdentification <AcctId> [0..1] Text 3414
         Type <Tp> [0..1] ± 3414
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  3415
         Identification <Id> [1..1] Text 3415
         Type <Tp> [0..1] ± 3415
         Name <Nm> [0..1] Text 3415
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3416
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3416
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C16,
C17,
C24,
C25,
C31
3416
       ISIN <ISIN> [0..1] IdentifierSet 3418
       OtherIdentification <OthrId> [0..*]  3418
         Identification <Id> [1..1] Text 3418
         Suffix <Sfx> [0..1] Text 3418
         Type <Tp> [1..1]  3418
{Or           Code <Cd> [1..1] CodeSet 3419
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3302 May 2026
```

## File page 3303

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 3420
       Description <Desc> [0..1] Text 3420
     Quantity <Qty> [1..1]  3421
{Or       Quantity <Qty> [1..1] ± C18 3421
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3421
         Quantity <Qty> [1..1] Quantity 3422
         QuantityType <QtyTp> [1..1] Text 3422
         Issuer <Issr> [1..1] Text 3422
         SchemeName <SchmeNm> [0..1] Text 3422
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3422
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3422
   PartialSettlementOfUnits <PrtlSttlmOfUnits> [0..1] Rate 3422
   PartialSettlementOfCash <PrtlSttlmOfCsh> [0..1] Rate 3423
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 3423
   FinancialAdvice <FinAdvc> [0..1] CodeSet 3423
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 3423
   LateReport <LateRpt> [0..1] CodeSet 3424
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C27 3424
   Equalisation <Equlstn> [0..1] ± C9, C15,
C20
3424
   SourceOfCash <SrcOfCsh> [0..*] ± 3425
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 3426
   TransactionChannelType <TxChanlTp> [0..1] ± 3426
   SignatureType <SgntrTp> [0..1] ± 3426
   OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C44 3426
Constraints
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Following Must be True
    /PhysicalDeliveryDetails Must be absent
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3303 May 2026
```

