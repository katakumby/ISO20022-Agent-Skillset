---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.21 CashSettlementDetails <CshSttlmDtls>", "44.4.4.9.21.1 PaymentInstrument <PmtInstrm>", "44.4.4.9.21.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [2212, 2213, 2214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.21.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2212 to 2214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2212

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 2247
     Type <Tp> [0..1] ± 2247
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2248
     Identification <Id> [1..1] Text 2248
     Type <Tp> [0..1] ± 2248
     Name <Nm> [0..1] Text 2248
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2249
44.4.4.9.21.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2212 May 2026
```

## File page 2213

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2215
   Debtor <Dbtr> [0..1] ± 2215
   DebtorAccount <DbtrAcct> [0..1]  2215
     Identification <Id> [1..1]  2215
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2216
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2216
Or}       Other <Othr> [1..1] ± 2216
     Name <Nm> [0..1] Text 2217
   DebtorAgent <DbtrAgt> [0..1]  2217
     Party <Pty> [1..1]  2217
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2218
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2218
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2218
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2219
     LEI <LEI> [0..1] IdentifierSet 2219
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2220
     Identification <Id> [1..1]  2220
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2220
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2221
Or}       Other <Othr> [1..1] ± 2221
     Name <Nm> [0..1] Text 2221
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2221
     Party <Pty> [1..1]  2222
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2222
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2222
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2223
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2224
     LEI <LEI> [0..1] IdentifierSet 2224
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2225
     Identification <Id> [1..1]  2225
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2213 May 2026
```

## File page 2214

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2225
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2226
Or}       Other <Othr> [1..1] ± 2226
     Name <Nm> [0..1] Text 2226
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2226
     Party <Pty> [1..1]  2227
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2227
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2227
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2228
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2229
     LEI <LEI> [0..1] IdentifierSet 2229
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2230
     Identification <Id> [1..1]  2230
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2230
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2231
Or}       Other <Othr> [1..1] ± 2231
     Name <Nm> [0..1] Text 2231
   CreditorAgent <CdtrAgt> [1..1]  2231
     Party <Pty> [1..1]  2232
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2232
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2232
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2233
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2234
     LEI <LEI> [0..1] IdentifierSet 2234
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2235
     Identification <Id> [1..1]  2235
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2235
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2236
Or}       Other <Othr> [1..1] ± 2236
     Name <Nm> [0..1] Text 2236
   Creditor <Cdtr> [0..1] ± 2236
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2214 May 2026
```

