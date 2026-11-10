---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.3 DirectDebitDetails <DrctDbtDtls>", "55.4.5.21.1.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [4044]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4044 to 4044.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4044

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  4044
     Identification <Id> [1..1]  4045
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4045
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4045
Or}       Other <Othr> [1..1] ± 4046
     Name <Nm> [0..1] Text 4046
   Debtor <Dbtr> [0..1] ± 4046
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4046
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 4047
   Creditor <Cdtr> [0..1] ± 4047
   DebtorAgent <DbtrAgt> [1..1]  4047
     Party <Pty> [1..1]  4047
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4048
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4048
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4049
     LEI <LEI> [0..1] IdentifierSet 4049
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4050
   CreditorAgent <CdtrAgt> [0..1]  4050
     Party <Pty> [1..1]  4050
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4051
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4051
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4051
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4052
     LEI <LEI> [0..1] IdentifierSet 4052
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4053
   RegistrationIdentification <RegnId> [0..1] Text 4053
   MandateIdentification <MndtId> [0..1] Text 4053
55.4.5.21.1.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4044 May 2026
```

