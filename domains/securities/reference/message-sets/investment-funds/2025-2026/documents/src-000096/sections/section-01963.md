---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "47.4.4.12.1 PaymentInstrument <PmtInstrm>", "47.4.4.12.1.3 DirectDebitDetails <DrctDbtDtls>", "47.4.4.12.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [2740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.12.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2740 to 2740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2740

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  2740
     Identification <Id> [1..1]  2741
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2741
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2741
Or}       Other <Othr> [1..1] ± 2742
     Name <Nm> [0..1] Text 2742
   Debtor <Dbtr> [0..1] ± 2742
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2742
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 2743
   Creditor <Cdtr> [0..1] ± 2743
   DebtorAgent <DbtrAgt> [1..1]  2743
     Party <Pty> [1..1]  2743
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2744
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2744
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2744
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2745
     LEI <LEI> [0..1] IdentifierSet 2745
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2746
   CreditorAgent <CdtrAgt> [0..1]  2746
     Party <Pty> [1..1]  2746
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2747
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2747
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2747
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2748
     LEI <LEI> [0..1] IdentifierSet 2748
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2749
   RegistrationIdentification <RegnId> [0..1] Text 2749
   MandateIdentification <MndtId> [0..1] Text 2749
47.4.4.12.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2740 May 2026
```

