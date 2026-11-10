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
file_pages: [3054, 3055]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# Continuation at file page 3054

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3054 to 3055.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3054

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DraweeIdentification <DrweeId> [0..1]  3161
           Party <Pty> [1..1]  3162
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3162
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3162
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3163
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3164
           LEI <LEI> [0..1] IdentifierSet 3164
         DrawerIdentification <DrwrId> [0..1] ± 3165
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  3165
         Number <Nb> [0..1] Text 3165
         PayeeIdentification <PyeeId> [1..1] ± 3165
         DraweeIdentification <DrweeId> [0..1]  3166
           Party <Pty> [1..1]  3166
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3166
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3167
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3167
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3168
           LEI <LEI> [0..1] IdentifierSet 3168
         DrawerIdentification <DrwrId> [0..1] ± 3169
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 3169
         AccountIdentification <AcctId> [0..1] Text 3169
         Type <Tp> [0..1] ± 3169
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  3170
         Identification <Id> [1..1] Text 3170
         Type <Tp> [0..1] ± 3170
         Name <Nm> [0..1] Text 3170
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3171
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3171
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
3171
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3054 May 2026
```

## File page 3055

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ISIN <ISIN> [0..1] IdentifierSet 3173
       OtherIdentification <OthrId> [0..*]  3173
         Identification <Id> [1..1] Text 3173
         Suffix <Sfx> [0..1] Text 3173
         Type <Tp> [1..1]  3173
{Or           Code <Cd> [1..1] CodeSet 3174
Or}           Proprietary <Prtry> [1..1] Text 3175
       Description <Desc> [0..1] Text 3175
     Quantity <Qty> [1..1]  3176
{Or       Quantity <Qty> [1..1] ± C15 3176
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3176
         Quantity <Qty> [1..1] Quantity 3177
         QuantityType <QtyTp> [1..1] Text 3177
         Issuer <Issr> [1..1] Text 3177
         SchemeName <SchmeNm> [0..1] Text 3177
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3177
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3177
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 3177
   FinancialAdvice <FinAdvc> [0..1] CodeSet 3178
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 3178
   RelatedPartyDetails <RltdPtyDtls> [0..10]  C24 3178
     Identification <Id> [1..1] ± 3179
     Account <Acct> [0..1]  3179
       Identification <Id> [1..1] Text 3179
       AccountServicer <AcctSvcr> [0..1] ± 3180
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3180
     Role <Role> [0..1] ± 3180
   Equalisation <Equlstn> [0..1] ± 3180
   SourceOfCash <SrcOfCsh> [0..*] ± 3181
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 3181
   TransactionChannelType <TxChanlTp> [0..1] ± 3181
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3055 May 2026
```

