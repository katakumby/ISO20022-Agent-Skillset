---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>", "46.4.5.10.33.1 PaymentInstrument <PmtInstrm>", "46.4.5.10.33.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [2421, 2422, 2423]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2421 to 2423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2421

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 2456
     Type <Tp> [0..1] ± 2456
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2457
     Identification <Id> [1..1] Text 2457
     Type <Tp> [0..1] ± 2457
     Name <Nm> [0..1] Text 2457
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2458
46.4.5.10.33.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2421 May 2026
```

## File page 2422

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2424
   Debtor <Dbtr> [0..1] ± 2424
   DebtorAccount <DbtrAcct> [0..1]  2424
     Identification <Id> [1..1]  2424
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2425
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2425
Or}       Other <Othr> [1..1] ± 2425
     Name <Nm> [0..1] Text 2426
   DebtorAgent <DbtrAgt> [0..1]  2426
     Party <Pty> [1..1]  2426
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2427
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2427
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2427
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2428
     LEI <LEI> [0..1] IdentifierSet 2428
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2429
     Identification <Id> [1..1]  2429
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2429
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2430
Or}       Other <Othr> [1..1] ± 2430
     Name <Nm> [0..1] Text 2430
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2430
     Party <Pty> [1..1]  2431
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2431
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2431
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2432
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2433
     LEI <LEI> [0..1] IdentifierSet 2433
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2434
     Identification <Id> [1..1]  2434
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2422 May 2026
```

## File page 2423

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2434
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2435
Or}       Other <Othr> [1..1] ± 2435
     Name <Nm> [0..1] Text 2435
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2435
     Party <Pty> [1..1]  2436
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2436
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2436
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2437
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2438
     LEI <LEI> [0..1] IdentifierSet 2438
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2439
     Identification <Id> [1..1]  2439
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2439
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2440
Or}       Other <Othr> [1..1] ± 2440
     Name <Nm> [0..1] Text 2440
   CreditorAgent <CdtrAgt> [1..1]  2440
     Party <Pty> [1..1]  2441
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2441
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2441
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2442
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2443
     LEI <LEI> [0..1] IdentifierSet 2443
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2444
     Identification <Id> [1..1]  2444
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2444
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2445
Or}       Other <Othr> [1..1] ± 2445
     Name <Nm> [0..1] Text 2445
   Creditor <Cdtr> [0..1] ± 2445
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2423 May 2026
```

