---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.3 DirectDebitDetails <DrctDbtDtls>", "53.4.5.18.1.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [3731]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3731 to 3731.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3731

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  3731
     Identification <Id> [1..1]  3732
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3732
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3732
Or}       Other <Othr> [1..1] ± 3733
     Name <Nm> [0..1] Text 3733
   Debtor <Dbtr> [0..1] ± 3733
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3733
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 3734
   Creditor <Cdtr> [0..1] ± 3734
   DebtorAgent <DbtrAgt> [1..1]  3734
     Party <Pty> [1..1]  3734
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3735
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3735
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3735
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3736
     LEI <LEI> [0..1] IdentifierSet 3736
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3737
   CreditorAgent <CdtrAgt> [0..1]  3737
     Party <Pty> [1..1]  3737
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3738
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3738
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3738
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3739
     LEI <LEI> [0..1] IdentifierSet 3739
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3740
   RegistrationIdentification <RegnId> [0..1] Text 3740
   MandateIdentification <MndtId> [0..1] Text 3740
53.4.5.18.1.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3731 May 2026
```

