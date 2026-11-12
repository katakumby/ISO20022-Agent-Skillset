---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.3 DirectDebitDetails <DrctDbtDtls>", "49.4.5.9.34.1.3.7 DebtorAgentBranch <DbtrAgtBrnch>"]
file_pages: [2916]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.3.7 DebtorAgentBranch <DbtrAgtBrnch>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2916 to 2916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2916

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
49.4.5.9.34.1.3.7  DebtorAgentBranch <DbtrAgtBrnch>
Presence: [0..1]
Definition: Information identifying a specific branch of a financial institution.
Usage: this component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
DebtorAgentBranch <DbtrAgtBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
49.4.5.9.34.1.3.8  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution that receives the payment transaction on behalf of the creditor, or other
nominated party, and credits the account.
CreditorAgent <CdtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2916
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2917
Or     BICFI <BICFI> [1..1] IdentifierSet C7 2917
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2917
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2918
   LEI <LEI> [0..1] IdentifierSet 2918
49.4.5.9.34.1.3.8.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2916 May 2026
```

