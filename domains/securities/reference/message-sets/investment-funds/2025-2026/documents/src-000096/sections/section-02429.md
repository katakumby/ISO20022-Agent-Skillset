---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.3 DirectDebitDetails <DrctDbtDtls>", "52.4.5.10.35.1.3.9 CreditorAgentBranch <CdtrAgtBrnch>"]
file_pages: [3405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.3.9 CreditorAgentBranch <CdtrAgtBrnch>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3405 to 3405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3405

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
52.4.5.10.35.1.3.9  CreditorAgentBranch <CdtrAgtBrnch>
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
52.4.5.10.35.1.3.10  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Reference assigned to a creditor by its financial institution, or relevant authority, authorising
the creditor to take part in a direct debit scheme.
Datatype: "Max35Text" on page 5403
52.4.5.10.35.1.3.11  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Reference of the direct debit mandate that has been agreed upon by the debtor and creditor.
Datatype: "Max35Text" on page 5403
52.4.5.10.35.1.4  ChequeDetails <ChqDtls>
Presence: [1..1]
Definition: Written order on which instructions are given to an account holder (a financial institution) to
pay a stated sum to a named recipient (the payee).
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3405 May 2026
```

