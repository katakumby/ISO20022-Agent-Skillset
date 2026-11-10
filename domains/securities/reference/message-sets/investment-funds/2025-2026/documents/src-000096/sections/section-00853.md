---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.7 CashAll <CshAll>"]
file_pages: [1180, 1181, 1182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.7 CashAll <CshAll>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1180 to 1182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1180

```text
36.4.15.7  CashAll <CshAll>
Presence: [0..*]
Definition: Specifies whether all assets in the portfolio should be liquidated and transferred as cash.
CashAll <CshAll> contains the following elements (see "CashAll1" on page 4870 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4871
   Currency <Ccy> [0..1] CodeSet C1 4871
36.4.15.8  ResidualCash <RsdlCsh>
Presence: [0..*]
Definition: Specifies how the cash in the account that is awaiting investment is to be dealt with
ResidualCash <RsdlCsh> contains the following elements (see "ResidualCash2" on page 4854 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4854
   Currency <Ccy> [0..1] CodeSet C1 4855
36.4.15.9  TaxDate <TaxDt>
Presence: [0..1]
Definition: Tax date applicable to all the assets.
Datatype: "ISODate" on page 5388
36.4.15.10  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1180 May 2026
```

## File page 1181

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1183
   CreditTransferDetails <CdtTrfDtls> [0..1]  1183
     Debtor <Dbtr> [0..1] ± 1186
     DebtorAccount <DbtrAcct> [0..1]  1186
       Name <Nm> [0..1] Text 1186
       IBAN <IBAN> [0..1] IdentifierSet C28 1186
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1187
       Other <Othr> [0..1] ± 1187
     DebtorAgent <DbtrAgt> [0..1]  1187
       BICFI <BICFI> [0..1] IdentifierSet C9 1188
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1188
       NameAndAddress <NmAndAdr> [0..1] ± 1189
       LEI <LEI> [0..1] IdentifierSet 1189
       ProprietaryIdentification <PrtryId> [0..1] Text 1190
       BranchIdentification <BrnchId> [0..1] ± 1190
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  1190
       Name <Nm> [0..1] Text 1190
       IBAN <IBAN> [0..1] IdentifierSet C28 1190
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1191
       Other <Othr> [0..1] ± 1191
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  1191
       BICFI <BICFI> [0..1] IdentifierSet C9 1192
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1192
       NameAndAddress <NmAndAdr> [0..1] ± 1193
       LEI <LEI> [0..1] IdentifierSet 1193
       ProprietaryIdentification <PrtryId> [0..1] Text 1194
       BranchIdentification <BrnchId> [0..1] ± 1194
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1194
       Name <Nm> [0..1] Text 1194
       IBAN <IBAN> [0..1] IdentifierSet C28 1194
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1181 May 2026
```

## File page 1182

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1195
       Other <Othr> [0..1] ± 1195
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1195
       BICFI <BICFI> [0..1] IdentifierSet C9 1196
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1196
       NameAndAddress <NmAndAdr> [0..1] ± 1197
       LEI <LEI> [0..1] IdentifierSet 1197
       ProprietaryIdentification <PrtryId> [0..1] Text 1198
       BranchIdentification <BrnchId> [0..1] ± 1198
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1198
       Name <Nm> [0..1] Text 1198
       IBAN <IBAN> [0..1] IdentifierSet C28 1198
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1199
       Other <Othr> [0..1] ± 1199
     CreditorAgent <CdtrAgt> [1..1]  1199
       BICFI <BICFI> [0..1] IdentifierSet C9 1200
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1200
       NameAndAddress <NmAndAdr> [0..1] ± 1201
       LEI <LEI> [0..1] IdentifierSet 1201
       ProprietaryIdentification <PrtryId> [0..1] Text 1202
       BranchIdentification <BrnchId> [0..1] ± 1202
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1202
       Name <Nm> [0..1] Text 1202
       IBAN <IBAN> [0..1] IdentifierSet C28 1202
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1203
       Other <Othr> [0..1] ± 1203
     Creditor <Cdtr> [0..1] ± 1203
     CreditorAccount <CdtrAcct> [1..1]  1204
       Name <Nm> [0..1] Text 1204
       IBAN <IBAN> [0..1] IdentifierSet C28 1204
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1205
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1182 May 2026
```

