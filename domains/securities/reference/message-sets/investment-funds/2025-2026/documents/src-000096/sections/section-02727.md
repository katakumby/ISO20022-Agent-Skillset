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
file_pages: [3848, 3849]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# Continuation at file page 3848

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3848 to 3849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3848

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 4085
             LEI <LEI> [0..1] IdentifierSet 4085
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4086
             Identification <Id> [1..1]  4086
{Or               IBAN <IBAN> [1..1] IdentifierSet C17 4086
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4087
Or}               Other <Othr> [1..1] ± 4087
             Name <Nm> [0..1] Text 4087
           CreditorAgent <CdtrAgt> [1..1]  4087
             Party <Pty> [1..1]  4088
{Or               NameAndAddress <NmAndAdr> [1..1] ± 4088
Or               BICFI <BICFI> [1..1] IdentifierSet C6 4088
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4089
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 4090
             LEI <LEI> [0..1] IdentifierSet 4090
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  4091
             Identification <Id> [1..1]  4091
{Or               IBAN <IBAN> [1..1] IdentifierSet C17 4091
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4092
Or}               Other <Othr> [1..1] ± 4092
             Name <Nm> [0..1] Text 4092
           Creditor <Cdtr> [0..1] ± 4092
           CreditorAccount <CdtrAcct> [1..1]  4093
             Identification <Id> [1..1]  4093
{Or               IBAN <IBAN> [1..1] IdentifierSet C17 4093
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4094
Or}               Other <Othr> [1..1] ± 4094
             Name <Nm> [0..1] Text 4094
Or         ChequeDetails <ChqDtls> [1..1]  4094
           Number <Nb> [0..1] Text 4095
           PayeeIdentification <PyeeId> [1..1] ± 4095
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3848 May 2026
```

## File page 3849

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DraweeIdentification <DrweeId> [0..1]  4095
             Party <Pty> [1..1]  4096
{Or               NameAndAddress <NmAndAdr> [1..1] ± 4096
Or               BICFI <BICFI> [1..1] IdentifierSet C6 4096
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4097
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 4098
             LEI <LEI> [0..1] IdentifierSet 4098
           DrawerIdentification <DrwrId> [0..1] ± 4099
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  4099
           Number <Nb> [0..1] Text 4099
           PayeeIdentification <PyeeId> [1..1] ± 4099
           DraweeIdentification <DrweeId> [0..1]  4100
             Party <Pty> [1..1]  4100
{Or               NameAndAddress <NmAndAdr> [1..1] ± 4100
Or               BICFI <BICFI> [1..1] IdentifierSet C6 4101
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4101
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 4102
             LEI <LEI> [0..1] IdentifierSet 4102
           DrawerIdentification <DrwrId> [0..1] ± 4103
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 4103
           AccountIdentification <AcctId> [0..1] Text 4103
           Type <Tp> [0..1] ± 4103
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  4104
           Identification <Id> [1..1] Text 4104
           Type <Tp> [0..1] ± 4104
           Name <Nm> [0..1] Text 4104
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4105
   ForeignExchangeDetails <FXDtls> [0..*] ± 4105
   FinancialAdvice <FinAdvc> [0..1] CodeSet 4105
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 4106
   LateReport <LateRpt> [0..1] CodeSet 4106
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3849 May 2026
```

