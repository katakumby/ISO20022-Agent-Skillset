---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.26 PaymentDetails <PmtDtls>", "36.4.15.11.26.1 Reference <Ref>"]
file_pages: [1265, 1266, 1267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.26.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1265 to 1267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1265

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Other <Othr> [0..1] ± 1287
36.4.15.11.26.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
36.4.15.11.26.2  CreditTransferDetails <CdtTrfDtls>
Presence: [0..1]
Definition: Payment instrument between a debtor and a creditor that flows through one or more financial
institutions or systems.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1265 May 2026
```

## File page 1266

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1277
     Other <Othr> [0..1] ± 1277
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1266 May 2026
```

## File page 1267

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     Other <Othr> [0..1] ± 1287
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1267 May 2026
```

