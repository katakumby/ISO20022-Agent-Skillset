---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.3 DirectDebitDetails <DrctDbtDtls>", "52.4.5.12.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [3466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3466 to 3466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3466

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  3466
     Identification <Id> [1..1]  3467
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3467
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3467
Or}       Other <Othr> [1..1] ± 3468
     Name <Nm> [0..1] Text 3468
   Debtor <Dbtr> [0..1] ± 3468
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3468
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 3469
   Creditor <Cdtr> [0..1] ± 3469
   DebtorAgent <DbtrAgt> [1..1]  3469
     Party <Pty> [1..1]  3469
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3470
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3470
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3470
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3471
     LEI <LEI> [0..1] IdentifierSet 3471
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3472
   CreditorAgent <CdtrAgt> [0..1]  3472
     Party <Pty> [1..1]  3472
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3473
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3473
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3473
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3474
     LEI <LEI> [0..1] IdentifierSet 3474
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3475
   RegistrationIdentification <RegnId> [0..1] Text 3475
   MandateIdentification <MndtId> [0..1] Text 3475
52.4.5.12.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3466 May 2026
```

