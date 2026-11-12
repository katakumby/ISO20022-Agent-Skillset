---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>", "2.4.2.2 NewCriteria <NewCrit>", "2.4.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.7 SecuritiesAccountServicer <SctiesAcctSvcr>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2.2.2.7 SecuritiesAccountServicer <SctiesAcctSvcr>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
SecuritiesAccountOwner <SctiesAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 64 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 64
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 64
2.4.2.2.2.7  SecuritiesAccountServicer <SctiesAcctSvcr>
Presence: [0..1]
Definition: Party that manages the securities account on behalf of the account owner.
SecuritiesAccountServicer <SctiesAcctSvcr> contains the following elements (see
"PartyIdentification136" on page 62 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 62
   LEI <LEI> [0..1] IdentifierSet 62
2.4.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected account report.
ReturnCriteria <RtrCrit> contains the following CollateralValueReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountOwnerIndicator <CshAcctOwnrInd> [0..1] Indicator 13
   CashAccountServicerIndicator <CshAcctSvcrInd> [0..1] Indicator 14
   SecuritiesAccountOwnerIndicator
<SctiesAcctOwnrInd>
[0..1] Indicator 14
   SecuritiesAccountServicerIndicator
<SctiesAcctSvcrInd>
[0..1] Indicator 14
   TotalCollateralValuationIndicator <TtlCollValtnInd> [0..1] Indicator 14
   SecuritiesAccountIndicator <SctiesAcctInd> [0..1] Indicator 14
   Securities <Scties> [0..1] Indicator 14
2.4.2.2.3.1  CashAccountOwnerIndicator <CshAcctOwnrInd>
Presence: [0..1]
Definition: Indicates whether the cash account owner information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
13 March 2024
```

