---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "44.4.4.10.1 PaymentInstrument <PmtInstrm>", "44.4.4.10.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [2266, 2267, 2268]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.10.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2266 to 2268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2266

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 2301
     Type <Tp> [0..1] ± 2301
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2302
     Identification <Id> [1..1] Text 2302
     Type <Tp> [0..1] ± 2302
     Name <Nm> [0..1] Text 2302
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2303
44.4.4.10.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2266 May 2026
```

## File page 2267

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2269
   Debtor <Dbtr> [0..1] ± 2269
   DebtorAccount <DbtrAcct> [0..1]  2269
     Identification <Id> [1..1]  2269
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2270
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2270
Or}       Other <Othr> [1..1] ± 2270
     Name <Nm> [0..1] Text 2271
   DebtorAgent <DbtrAgt> [0..1]  2271
     Party <Pty> [1..1]  2271
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2272
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2272
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2272
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2273
     LEI <LEI> [0..1] IdentifierSet 2273
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2274
     Identification <Id> [1..1]  2274
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2274
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2275
Or}       Other <Othr> [1..1] ± 2275
     Name <Nm> [0..1] Text 2275
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2275
     Party <Pty> [1..1]  2276
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2276
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2276
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2277
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2278
     LEI <LEI> [0..1] IdentifierSet 2278
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2279
     Identification <Id> [1..1]  2279
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2267 May 2026
```

## File page 2268

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2279
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2280
Or}       Other <Othr> [1..1] ± 2280
     Name <Nm> [0..1] Text 2280
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2280
     Party <Pty> [1..1]  2281
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2281
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2281
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2282
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2283
     LEI <LEI> [0..1] IdentifierSet 2283
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2284
     Identification <Id> [1..1]  2284
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2284
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2285
Or}       Other <Othr> [1..1] ± 2285
     Name <Nm> [0..1] Text 2285
   CreditorAgent <CdtrAgt> [1..1]  2285
     Party <Pty> [1..1]  2286
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2286
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2286
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2287
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2288
     LEI <LEI> [0..1] IdentifierSet 2288
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2289
     Identification <Id> [1..1]  2289
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2289
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2290
Or}       Other <Othr> [1..1] ± 2290
     Name <Nm> [0..1] Text 2290
   Creditor <Cdtr> [0..1] ± 2290
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2268 May 2026
```

