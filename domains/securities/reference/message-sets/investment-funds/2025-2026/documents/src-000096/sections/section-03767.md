---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.3 PaymentInstrument17", "66.1.31.3.6 SavingsPlanPaymentInstrument <SvgsPlanPmtInstrm>", "66.1.31.3.6.2 DirectDebitDetails <DrctDbtDtls>"]
file_pages: [5054]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.3.6.2 DirectDebitDetails <DrctDbtDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5054 to 5054.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5054

```text
PaymentCardDetails <PmtCardDtls> contains the following elements (see "PaymentCard29" on
page 5046 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 5046
   Number <Nb> [1..1] Text 5047
   HolderName <HldrNm> [1..1] Text 5047
   StartDate <StartDt> [0..1] YearMonth 5047
   ExpiryDate <XpryDt> [1..1] YearMonth 5047
   CardIssuerName <CardIssrNm> [0..1] Text 5047
   CardIssuerIdentification <CardIssrId> [0..1] ± 5047
   SecurityCode <SctyCd> [0..1] Text 5048
   SequenceNumber <SeqNb> [0..1] Text 5048
66.1.31.3.6.2  DirectDebitDetails <DrctDbtDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by direct debit.
DirectDebitDetails <DrctDbtDtls> contains the following elements (see "DirectDebitMandate7" on
page 4476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1] ± 4477
   Debtor <Dbtr> [0..1] ± 4477
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4477
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 4478
   Creditor <Cdtr> [0..1] ± 4478
   DebtorAgent <DbtrAgt> [1..1] ± 4478
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4478
   CreditorAgent <CdtrAgt> [0..1] ± 4479
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4479
   RegistrationIdentification <RegnId> [0..1] Text 4479
   MandateIdentification <MndtId> [0..1] Text 4480
66.1.31.3.6.3  Cheque <Chq>
Presence: [1..1]
Definition: Indicates whether the payment is done via cheque.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5054 May 2026
```

