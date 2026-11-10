---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.25 EffectiveSettlementDate <FctvSttlmDt>"]
file_pages: [1262, 1263, 1264]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.25 EffectiveSettlementDate <FctvSttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1262 to 1264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1262

```text
EffectiveTransferDate <FctvTrfDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
36.4.15.11.25  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities were exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
36.4.15.11.26  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1262 May 2026
```

## File page 1263

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1265
   CreditTransferDetails <CdtTrfDtls> [0..1]  1265
     Debtor <Dbtr> [0..1] ± 1268
     DebtorAccount <DbtrAcct> [0..1]  1268
       Name <Nm> [0..1] Text 1268
       IBAN <IBAN> [0..1] IdentifierSet C28 1268
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1269
       Other <Othr> [0..1] ± 1269
     DebtorAgent <DbtrAgt> [0..1]  1269
       BICFI <BICFI> [0..1] IdentifierSet C9 1270
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1270
       NameAndAddress <NmAndAdr> [0..1] ± 1271
       LEI <LEI> [0..1] IdentifierSet 1271
       ProprietaryIdentification <PrtryId> [0..1] Text 1272
       BranchIdentification <BrnchId> [0..1] ± 1272
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  1272
       Name <Nm> [0..1] Text 1272
       IBAN <IBAN> [0..1] IdentifierSet C28 1272
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1273
       Other <Othr> [0..1] ± 1273
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  1273
       BICFI <BICFI> [0..1] IdentifierSet C9 1274
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1274
       NameAndAddress <NmAndAdr> [0..1] ± 1275
       LEI <LEI> [0..1] IdentifierSet 1275
       ProprietaryIdentification <PrtryId> [0..1] Text 1276
       BranchIdentification <BrnchId> [0..1] ± 1276
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1276
       Name <Nm> [0..1] Text 1276
       IBAN <IBAN> [0..1] IdentifierSet C28 1276
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1263 May 2026
```

## File page 1264

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1277
       Other <Othr> [0..1] ± 1277
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1277
       BICFI <BICFI> [0..1] IdentifierSet C9 1278
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1278
       NameAndAddress <NmAndAdr> [0..1] ± 1279
       LEI <LEI> [0..1] IdentifierSet 1279
       ProprietaryIdentification <PrtryId> [0..1] Text 1280
       BranchIdentification <BrnchId> [0..1] ± 1280
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1280
       Name <Nm> [0..1] Text 1280
       IBAN <IBAN> [0..1] IdentifierSet C28 1280
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1281
       Other <Othr> [0..1] ± 1281
     CreditorAgent <CdtrAgt> [1..1]  1281
       BICFI <BICFI> [0..1] IdentifierSet C9 1282
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1282
       NameAndAddress <NmAndAdr> [0..1] ± 1283
       LEI <LEI> [0..1] IdentifierSet 1283
       ProprietaryIdentification <PrtryId> [0..1] Text 1284
       BranchIdentification <BrnchId> [0..1] ± 1284
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1284
       Name <Nm> [0..1] Text 1284
       IBAN <IBAN> [0..1] IdentifierSet C28 1284
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1285
       Other <Othr> [0..1] ± 1285
     Creditor <Cdtr> [0..1] ± 1285
     CreditorAccount <CdtrAcct> [1..1]  1286
       Name <Nm> [0..1] Text 1286
       IBAN <IBAN> [0..1] IdentifierSet C28 1286
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1287
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1264 May 2026
```

