---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.7 CashAll <CshAll>"]
file_pages: [1563, 1564, 1565]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.7 CashAll <CshAll>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1563 to 1565.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1563

```text
40.4.15.7  CashAll <CshAll>
Presence: [0..*]
Definition: Specifies whether all assets in the portfolio should be liquidated and transferred as cash.
CashAll <CshAll> contains the following elements (see "CashAll1" on page 4870 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4871
   Currency <Ccy> [0..1] CodeSet C1 4871
40.4.15.8  ResidualCash <RsdlCsh>
Presence: [0..*]
Definition: Specifies how the cash in the account that is awaiting investment is to be dealt with
ResidualCash <RsdlCsh> contains the following elements (see "ResidualCash2" on page 4854 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4854
   Currency <Ccy> [0..1] CodeSet C1 4855
40.4.15.9  TaxDate <TaxDt>
Presence: [0..1]
Definition: Tax date applicable to all the assets.
Datatype: "ISODate" on page 5388
40.4.15.10  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1563 May 2026
```

## File page 1564

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1566
   CreditTransferDetails <CdtTrfDtls> [0..1]  1566
     Debtor <Dbtr> [0..1] ± 1569
     DebtorAccount <DbtrAcct> [0..1]  1569
       Name <Nm> [0..1] Text 1569
       IBAN <IBAN> [0..1] IdentifierSet C28 1569
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1570
       Other <Othr> [0..1] ± 1570
     DebtorAgent <DbtrAgt> [0..1]  1570
       BICFI <BICFI> [0..1] IdentifierSet C9 1571
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1571
       NameAndAddress <NmAndAdr> [0..1] ± 1572
       LEI <LEI> [0..1] IdentifierSet 1572
       ProprietaryIdentification <PrtryId> [0..1] Text 1573
       BranchIdentification <BrnchId> [0..1] ± 1573
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  1573
       Name <Nm> [0..1] Text 1573
       IBAN <IBAN> [0..1] IdentifierSet C28 1573
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1574
       Other <Othr> [0..1] ± 1574
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  1574
       BICFI <BICFI> [0..1] IdentifierSet C9 1575
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1575
       NameAndAddress <NmAndAdr> [0..1] ± 1576
       LEI <LEI> [0..1] IdentifierSet 1576
       ProprietaryIdentification <PrtryId> [0..1] Text 1577
       BranchIdentification <BrnchId> [0..1] ± 1577
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1577
       Name <Nm> [0..1] Text 1577
       IBAN <IBAN> [0..1] IdentifierSet C28 1577
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1564 May 2026
```

## File page 1565

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1578
       Other <Othr> [0..1] ± 1578
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1578
       BICFI <BICFI> [0..1] IdentifierSet C9 1579
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1579
       NameAndAddress <NmAndAdr> [0..1] ± 1580
       LEI <LEI> [0..1] IdentifierSet 1580
       ProprietaryIdentification <PrtryId> [0..1] Text 1581
       BranchIdentification <BrnchId> [0..1] ± 1581
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1581
       Name <Nm> [0..1] Text 1581
       IBAN <IBAN> [0..1] IdentifierSet C28 1581
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1582
       Other <Othr> [0..1] ± 1582
     CreditorAgent <CdtrAgt> [1..1]  1582
       BICFI <BICFI> [0..1] IdentifierSet C9 1583
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1583
       NameAndAddress <NmAndAdr> [0..1] ± 1584
       LEI <LEI> [0..1] IdentifierSet 1584
       ProprietaryIdentification <PrtryId> [0..1] Text 1585
       BranchIdentification <BrnchId> [0..1] ± 1585
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1585
       Name <Nm> [0..1] Text 1585
       IBAN <IBAN> [0..1] IdentifierSet C28 1585
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1586
       Other <Othr> [0..1] ± 1586
     Creditor <Cdtr> [0..1] ± 1586
     CreditorAccount <CdtrAcct> [1..1]  1587
       Name <Nm> [0..1] Text 1587
       IBAN <IBAN> [0..1] IdentifierSet C28 1587
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1588
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1565 May 2026
```

