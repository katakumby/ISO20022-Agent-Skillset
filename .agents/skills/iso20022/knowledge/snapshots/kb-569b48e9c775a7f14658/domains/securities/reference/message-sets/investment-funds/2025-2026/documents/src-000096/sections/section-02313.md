---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.3 DirectDebitDetails <DrctDbtDtls>", "50.4.4.10.1.3.9 CreditorAgentBranch <CdtrAgtBrnch>"]
file_pages: [3230]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.3.9 CreditorAgentBranch <CdtrAgtBrnch>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3230 to 3230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3230

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
50.4.4.10.1.3.9  CreditorAgentBranch <CdtrAgtBrnch>
Presence: [0..1]
Definition: Information identifying a specific branch of a financial institution.
Usage: this component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
CreditorAgentBranch <CdtrAgtBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
50.4.4.10.1.3.10  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Reference assigned to a creditor by its financial institution, or relevant authority, authorising
the creditor to take part in a direct debit scheme.
Datatype: "Max35Text" on page 5403
50.4.4.10.1.3.11  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Reference of the direct debit mandate that has been agreed upon by the debtor and creditor.
Datatype: "Max35Text" on page 5403
50.4.4.10.1.4  ChequeDetails <ChqDtls>
Presence: [1..1]
Definition: Written order on which instructions are given to an account holder (a financial institution) to
pay a stated sum to a named recipient (the payee).
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3230 May 2026
```

