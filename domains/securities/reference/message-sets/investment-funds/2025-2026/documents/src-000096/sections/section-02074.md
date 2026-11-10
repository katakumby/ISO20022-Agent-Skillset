---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.3 DirectDebitDetails <DrctDbtDtls>", "49.4.5.9.34.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [2910]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2910 to 2910.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2910

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  2910
     Identification <Id> [1..1]  2911
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2911
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2911
Or}       Other <Othr> [1..1] ± 2912
     Name <Nm> [0..1] Text 2912
   Debtor <Dbtr> [0..1] ± 2912
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2912
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 2913
   Creditor <Cdtr> [0..1] ± 2913
   DebtorAgent <DbtrAgt> [1..1]  2913
     Party <Pty> [1..1]  2913
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2914
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2914
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2914
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2915
     LEI <LEI> [0..1] IdentifierSet 2915
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2916
   CreditorAgent <CdtrAgt> [0..1]  2916
     Party <Pty> [1..1]  2916
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2917
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2917
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2917
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2918
     LEI <LEI> [0..1] IdentifierSet 2918
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2919
   RegistrationIdentification <RegnId> [0..1] Text 2919
   MandateIdentification <MndtId> [0..1] Text 2919
49.4.5.9.34.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2910 May 2026
```

