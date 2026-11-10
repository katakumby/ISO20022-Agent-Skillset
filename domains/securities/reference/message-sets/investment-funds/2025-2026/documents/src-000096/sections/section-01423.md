---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.32 CashSettlementDetails <CshSttlmDtls>", "43.4.5.9.32.1 PaymentInstrument <PmtInstrm>"]
file_pages: [1996, 1997, 1998, 1999]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.32.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1996 to 1999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1996

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AccountIdentification <AcctId> [0..1] Text 2035
       Type <Tp> [0..1] ± 2035
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  2036
       Identification <Id> [1..1] Text 2036
       Type <Tp> [0..1] ± 2036
       Name <Nm> [0..1] Text 2036
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2037
43.4.5.9.32.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer or
investment account.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1996 May 2026
```

## File page 1997

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument28Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CreditTransferDetails <CdtTrfDtls> [1..1]  2000
     Reference <Ref> [0..1] Text 2003
     Debtor <Dbtr> [0..1] ± 2003
     DebtorAccount <DbtrAcct> [0..1]  2003
       Identification <Id> [1..1]  2003
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2004
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2004
Or}         Other <Othr> [1..1] ± 2004
       Name <Nm> [0..1] Text 2005
     DebtorAgent <DbtrAgt> [0..1]  2005
       Party <Pty> [1..1]  2005
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2006
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2006
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2006
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2007
       LEI <LEI> [0..1] IdentifierSet 2007
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  2008
       Identification <Id> [1..1]  2008
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2008
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2009
Or}         Other <Othr> [1..1] ± 2009
       Name <Nm> [0..1] Text 2009
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  2009
       Party <Pty> [1..1]  2010
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2010
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2010
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2011
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2012
       LEI <LEI> [0..1] IdentifierSet 2012
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1997 May 2026
```

## File page 1998

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2013
       Identification <Id> [1..1]  2013
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2013
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2014
Or}         Other <Othr> [1..1] ± 2014
       Name <Nm> [0..1] Text 2014
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  2014
       Party <Pty> [1..1]  2015
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2015
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2015
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2016
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2017
       LEI <LEI> [0..1] IdentifierSet 2017
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2018
       Identification <Id> [1..1]  2018
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2018
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2019
Or}         Other <Othr> [1..1] ± 2019
       Name <Nm> [0..1] Text 2019
     CreditorAgent <CdtrAgt> [1..1]  2019
       Party <Pty> [1..1]  2020
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2020
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2020
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2021
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2022
       LEI <LEI> [0..1] IdentifierSet 2022
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  2023
       Identification <Id> [1..1]  2023
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2023
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2024
Or}         Other <Othr> [1..1] ± 2024
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1998 May 2026
```

## File page 1999

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [0..1] Text 2024
     Creditor <Cdtr> [0..1] ± 2024
     CreditorAccount <CdtrAcct> [1..1]  2025
       Identification <Id> [1..1]  2025
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2025
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2026
Or}         Other <Othr> [1..1] ± 2026
       Name <Nm> [0..1] Text 2026
Or   ChequeDetails <ChqDtls> [1..1]  2026
     Number <Nb> [0..1] Text 2027
     PayeeIdentification <PyeeId> [1..1] ± 2027
     DraweeIdentification <DrweeId> [0..1]  2027
       Party <Pty> [1..1]  2028
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2028
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2028
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2029
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2030
       LEI <LEI> [0..1] IdentifierSet 2030
     DrawerIdentification <DrwrId> [0..1] ± 2031
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  2031
     Number <Nb> [0..1] Text 2031
     PayeeIdentification <PyeeId> [1..1] ± 2031
     DraweeIdentification <DrweeId> [0..1]  2032
       Party <Pty> [1..1]  2032
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2032
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2033
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2033
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2034
       LEI <LEI> [0..1] IdentifierSet 2034
     DrawerIdentification <DrwrId> [0..1] ± 2035
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 2035
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1999 May 2026
```

