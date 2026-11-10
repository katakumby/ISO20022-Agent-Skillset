---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.4 Message Building Blocks", "24.4.2 CollateralValueQueryDefinition <CollValQryDef>", "24.4.2.2 NewCriteria <NewCrit>", "24.4.2.2.2 SearchCriteria <SchCrit>", "24.4.2.2.2.7 SecuritiesAccountServicer <SctiesAcctSvcr>"]
file_pages: [587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.4.2.2.2.7 SecuritiesAccountServicer <SctiesAcctSvcr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 587 to 587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 587

```text
SecuritiesAccountOwner <SctiesAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
24.4.2.2.2.7  SecuritiesAccountServicer <SctiesAcctSvcr>
Presence: [0..1]
Definition: Party that manages the securities account on behalf of the account owner.
SecuritiesAccountServicer <SctiesAcctSvcr> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
24.4.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected account report.
ReturnCriteria <RtrCrit> contains the following CollateralValueReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountOwnerIndicator <CshAcctOwnrInd> [0..1] Indicator 587
   CashAccountServicerIndicator <CshAcctSvcrInd> [0..1] Indicator 588
   SecuritiesAccountOwnerIndicator
<SctiesAcctOwnrInd>
[0..1] Indicator 588
   SecuritiesAccountServicerIndicator
<SctiesAcctSvcrInd>
[0..1] Indicator 588
   TotalCollateralValuationIndicator <TtlCollValtnInd> [0..1] Indicator 588
   SecuritiesAccountIndicator <SctiesAcctInd> [0..1] Indicator 588
   Securities <Scties> [0..1] Indicator 588
24.4.2.2.3.1  CashAccountOwnerIndicator <CshAcctOwnrInd>
Presence: [0..1]
Definition: Indicates whether the cash account owner information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 587 August 2026
```

