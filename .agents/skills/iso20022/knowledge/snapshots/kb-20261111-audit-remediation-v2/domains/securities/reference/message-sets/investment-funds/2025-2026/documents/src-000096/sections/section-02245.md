---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>", "50.4.4.9.22.1 PaymentInstrument <PmtInstrm>", "50.4.4.9.22.1.3 DirectDebitDetails <DrctDbtDtls>", "50.4.4.9.22.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [3151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3151 to 3151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3151

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  3151
     Identification <Id> [1..1]  3152
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3152
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3152
Or}       Other <Othr> [1..1] ± 3153
     Name <Nm> [0..1] Text 3153
   Debtor <Dbtr> [0..1] ± 3153
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3153
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 3154
   Creditor <Cdtr> [0..1] ± 3154
   DebtorAgent <DbtrAgt> [1..1]  3154
     Party <Pty> [1..1]  3154
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3155
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3155
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3155
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3156
     LEI <LEI> [0..1] IdentifierSet 3156
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3157
   CreditorAgent <CdtrAgt> [0..1]  3157
     Party <Pty> [1..1]  3157
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3158
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3158
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3158
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3159
     LEI <LEI> [0..1] IdentifierSet 3159
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3160
   RegistrationIdentification <RegnId> [0..1] Text 3160
   MandateIdentification <MndtId> [0..1] Text 3160
50.4.4.9.22.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3151 May 2026
```

