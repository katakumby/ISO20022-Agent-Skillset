---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.3 DirectDebitDetails <DrctDbtDtls>", "50.4.4.10.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [3221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3221 to 3221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3221

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  3221
     Identification <Id> [1..1]  3222
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3222
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3222
Or}       Other <Othr> [1..1] ± 3223
     Name <Nm> [0..1] Text 3223
   Debtor <Dbtr> [0..1] ± 3223
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3223
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 3224
   Creditor <Cdtr> [0..1] ± 3224
   DebtorAgent <DbtrAgt> [1..1]  3224
     Party <Pty> [1..1]  3224
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3225
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3225
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3225
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3226
     LEI <LEI> [0..1] IdentifierSet 3226
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3227
   CreditorAgent <CdtrAgt> [0..1]  3227
     Party <Pty> [1..1]  3227
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3228
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3228
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3228
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3229
     LEI <LEI> [0..1] IdentifierSet 3229
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3230
   RegistrationIdentification <RegnId> [0..1] Text 3230
   MandateIdentification <MndtId> [0..1] Text 3230
50.4.4.10.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3221 May 2026
```

