---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.3 DirectDebitDetails <DrctDbtDtls>", "52.4.5.10.35.1.3.1 DebtorAccount <DbtrAcct>"]
file_pages: [3396]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.3.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3396 to 3396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3396

```text
DirectDebitDetails <DrctDbtDtls> contains the following DirectDebitMandate9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1]  3396
     Identification <Id> [1..1]  3397
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3397
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3397
Or}       Other <Othr> [1..1] ± 3398
     Name <Nm> [0..1] Text 3398
   Debtor <Dbtr> [0..1] ± 3398
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3398
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 3399
   Creditor <Cdtr> [0..1] ± 3399
   DebtorAgent <DbtrAgt> [1..1]  3399
     Party <Pty> [1..1]  3399
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3400
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3400
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3400
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3401
     LEI <LEI> [0..1] IdentifierSet 3401
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3402
   CreditorAgent <CdtrAgt> [0..1]  3402
     Party <Pty> [1..1]  3402
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3403
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3403
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3403
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3404
     LEI <LEI> [0..1] IdentifierSet 3404
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3405
   RegistrationIdentification <RegnId> [0..1] Text 3405
   MandateIdentification <MndtId> [0..1] Text 3405
52.4.5.10.35.1.3.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3396 May 2026
```

