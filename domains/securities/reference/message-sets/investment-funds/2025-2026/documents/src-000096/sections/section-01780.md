---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "46.4.5.12.1 PaymentInstrument <PmtInstrm>", "46.4.5.12.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [2485, 2486, 2487]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.12.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2485 to 2487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2485

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 2520
     Type <Tp> [0..1] ± 2520
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2521
     Identification <Id> [1..1] Text 2521
     Type <Tp> [0..1] ± 2521
     Name <Nm> [0..1] Text 2521
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2522
46.4.5.12.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2485 May 2026
```

## File page 2486

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2488
   Debtor <Dbtr> [0..1] ± 2488
   DebtorAccount <DbtrAcct> [0..1]  2488
     Identification <Id> [1..1]  2488
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2489
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2489
Or}       Other <Othr> [1..1] ± 2489
     Name <Nm> [0..1] Text 2490
   DebtorAgent <DbtrAgt> [0..1]  2490
     Party <Pty> [1..1]  2490
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2491
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2491
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2491
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2492
     LEI <LEI> [0..1] IdentifierSet 2492
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2493
     Identification <Id> [1..1]  2493
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2493
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2494
Or}       Other <Othr> [1..1] ± 2494
     Name <Nm> [0..1] Text 2494
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2494
     Party <Pty> [1..1]  2495
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2495
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2495
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2496
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2497
     LEI <LEI> [0..1] IdentifierSet 2497
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2498
     Identification <Id> [1..1]  2498
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2486 May 2026
```

## File page 2487

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2498
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2499
Or}       Other <Othr> [1..1] ± 2499
     Name <Nm> [0..1] Text 2499
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2499
     Party <Pty> [1..1]  2500
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2500
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2500
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2501
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2502
     LEI <LEI> [0..1] IdentifierSet 2502
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2503
     Identification <Id> [1..1]  2503
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2503
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2504
Or}       Other <Othr> [1..1] ± 2504
     Name <Nm> [0..1] Text 2504
   CreditorAgent <CdtrAgt> [1..1]  2504
     Party <Pty> [1..1]  2505
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2505
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2505
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2506
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2507
     LEI <LEI> [0..1] IdentifierSet 2507
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2508
     Identification <Id> [1..1]  2508
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2508
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2509
Or}       Other <Othr> [1..1] ± 2509
     Name <Nm> [0..1] Text 2509
   Creditor <Cdtr> [0..1] ± 2509
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2487 May 2026
```

