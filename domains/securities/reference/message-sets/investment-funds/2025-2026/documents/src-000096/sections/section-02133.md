---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.3 DirectDebitDetails <DrctDbtDtls>", "49.4.5.13.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [2980]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2980 to 2980.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2980

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  2980
     Identification <Id> [1..1]  2981
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2981
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2981
Or}       Other <Othr> [1..1] ± 2982
     Name <Nm> [0..1] Text 2982
   Debtor <Dbtr> [0..1] ± 2982
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2982
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 2983
   Creditor <Cdtr> [0..1] ± 2983
   DebtorAgent <DbtrAgt> [1..1]  2983
     Party <Pty> [1..1]  2983
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2984
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2984
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2984
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2985
     LEI <LEI> [0..1] IdentifierSet 2985
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2986
   CreditorAgent <CdtrAgt> [0..1]  2986
     Party <Pty> [1..1]  2986
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2987
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2987
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2987
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2988
     LEI <LEI> [0..1] IdentifierSet 2988
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2989
   RegistrationIdentification <RegnId> [0..1] Text 2989
   MandateIdentification <MndtId> [0..1] Text 2989
49.4.5.13.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2980 May 2026
```

