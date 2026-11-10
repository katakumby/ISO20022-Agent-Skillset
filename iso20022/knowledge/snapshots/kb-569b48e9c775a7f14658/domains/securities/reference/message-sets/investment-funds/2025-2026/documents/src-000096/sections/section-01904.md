---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.3 DirectDebitDetails <DrctDbtDtls>", "47.4.4.8.20.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [2670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2670 to 2670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2670

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  2670
     Identification <Id> [1..1]  2671
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2671
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2671
Or}       Other <Othr> [1..1] ± 2672
     Name <Nm> [0..1] Text 2672
   Debtor <Dbtr> [0..1] ± 2672
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2672
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 2673
   Creditor <Cdtr> [0..1] ± 2673
   DebtorAgent <DbtrAgt> [1..1]  2673
     Party <Pty> [1..1]  2673
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2674
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2674
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2674
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2675
     LEI <LEI> [0..1] IdentifierSet 2675
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2676
   CreditorAgent <CdtrAgt> [0..1]  2676
     Party <Pty> [1..1]  2676
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2677
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2677
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2677
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2678
     LEI <LEI> [0..1] IdentifierSet 2678
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2679
   RegistrationIdentification <RegnId> [0..1] Text 2679
   MandateIdentification <MndtId> [0..1] Text 2679
47.4.4.8.20.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2670 May 2026
```

