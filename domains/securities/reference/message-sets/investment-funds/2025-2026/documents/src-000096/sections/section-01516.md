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
file_pages: [2112, 2113, 2114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# Continuation at file page 2112

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2112 to 2114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2112

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Equalisation <Equlstn> [0..1] ± 2257
       CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2257
       TransactionChannelType <TxChanlTp> [0..1] ± 2257
       SignatureType <SgntrTp> [0..1] ± 2258
       OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C39 2258
     BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  2258
       PaymentInstrument <PmtInstrm> [1..1]  2262
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  2266
           Reference <Ref> [0..1] Text 2269
           Debtor <Dbtr> [0..1] ± 2269
           DebtorAccount <DbtrAcct> [0..1]  2269
             Identification <Id> [1..1]  2269
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2270
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2270
Or}               Other <Othr> [1..1] ± 2270
             Name <Nm> [0..1] Text 2271
           DebtorAgent <DbtrAgt> [0..1]  2271
             Party <Pty> [1..1]  2271
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2272
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2272
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2272
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2273
             LEI <LEI> [0..1] IdentifierSet 2273
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  2274
             Identification <Id> [1..1]  2274
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2274
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2275
Or}               Other <Othr> [1..1] ± 2275
             Name <Nm> [0..1] Text 2275
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  2275
             Party <Pty> [1..1]  2276
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2112 May 2026
```

## File page 2113

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2276
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2276
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2277
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2278
             LEI <LEI> [0..1] IdentifierSet 2278
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2279
             Identification <Id> [1..1]  2279
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2279
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2280
Or}               Other <Othr> [1..1] ± 2280
             Name <Nm> [0..1] Text 2280
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  2280
             Party <Pty> [1..1]  2281
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2281
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2281
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2282
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2283
             LEI <LEI> [0..1] IdentifierSet 2283
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2284
             Identification <Id> [1..1]  2284
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2284
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2285
Or}               Other <Othr> [1..1] ± 2285
             Name <Nm> [0..1] Text 2285
           CreditorAgent <CdtrAgt> [1..1]  2285
             Party <Pty> [1..1]  2286
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2286
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2286
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2287
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2288
             LEI <LEI> [0..1] IdentifierSet 2288
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2113 May 2026
```

## File page 2114

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  2289
             Identification <Id> [1..1]  2289
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2289
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2290
Or}               Other <Othr> [1..1] ± 2290
             Name <Nm> [0..1] Text 2290
           Creditor <Cdtr> [0..1] ± 2290
           CreditorAccount <CdtrAcct> [1..1]  2291
             Identification <Id> [1..1]  2291
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 2291
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2292
Or}               Other <Othr> [1..1] ± 2292
             Name <Nm> [0..1] Text 2292
Or         ChequeDetails <ChqDtls> [1..1]  2292
           Number <Nb> [0..1] Text 2293
           PayeeIdentification <PyeeId> [1..1] ± 2293
           DraweeIdentification <DrweeId> [0..1]  2293
             Party <Pty> [1..1]  2294
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2294
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2294
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2295
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2296
             LEI <LEI> [0..1] IdentifierSet 2296
           DrawerIdentification <DrwrId> [0..1] ± 2297
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  2297
           Number <Nb> [0..1] Text 2297
           PayeeIdentification <PyeeId> [1..1] ± 2297
           DraweeIdentification <DrweeId> [0..1]  2298
             Party <Pty> [1..1]  2298
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2298
Or               BICFI <BICFI> [1..1] IdentifierSet C6 2299
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2114 May 2026
```

