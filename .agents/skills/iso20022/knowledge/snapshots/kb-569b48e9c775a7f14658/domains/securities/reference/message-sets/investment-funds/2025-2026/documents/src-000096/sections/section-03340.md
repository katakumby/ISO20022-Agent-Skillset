---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.3 ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn>", "66.1.24.4.3.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [4581]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.3.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4581 to 4581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4581

```text
ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn> contains the following
ModificationScope27 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4581
   InvestorProfileValidation <InvstrPrflVldtn> [1..1]  4581
     CertificationIndicator <CertfctnInd> [0..1] Indicator 4582
     ValidatingParty <VldtngPty> [0..1] Text 4582
     CheckingParty <ChckngPty> [0..1] Text 4582
     ResponsibleParty <RspnsblPty> [0..1] Text 4583
     CertificateType <CertTp> [0..1] ± 4583
     CheckingDate <ChckngDt> [0..1] Date 4583
     CheckingFrequency <ChckngFrqcy> [0..1] CodeSet 4583
     NextRevisionDate <NxtRvsnDt> [0..1] Date 4584
     SalaryRange <SlryRg> [0..1] Text 4584
     SourceOfWealth <SrcOfWlth> [0..1] Text 4584
     CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 4584
     RiskLevel <RskLvl> [0..1] ± 4584
     KnowYourCustomerCheckType
<KnowYourCstmrChckTp>
[0..1] ± 4584
     KnowYourCustomerDatabaseCheck
<KnowYourCstmrDBChck>
[0..1] ± 4585
66.1.24.4.3.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied on a set of information.
Datatype: "DataModification2Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
DELT DeleteDataSet Delete an existing set of data.
66.1.24.4.3.2  InvestorProfileValidation <InvstrPrflVldtn>
Presence: [1..1]
Definition: Detailed information about the party profile information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4581 May 2026
```

